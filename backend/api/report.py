from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from ..utils.database import get_db
from ..services.portfolio_service import get_portfolios
from ..services.analysis_service import calculate_portfolio_value
from ..services.pdf_service import generate_pdf_report
from ..dspy.analyst import explain_risk

router = APIRouter()

@router.get("/report")
async def generate_report(db: Session = Depends(get_db)):
    portfolios = get_portfolios(db)
    if not portfolios:
        raise HTTPException(status_code=400, detail="No portfolios found")
    
    value = calculate_portfolio_value(portfolios)
    analytics_str = str(value)
    insights = explain_risk(analytics_str)
    
    filename = generate_pdf_report(portfolios, {"value": value}, insights)
    return FileResponse(filename, media_type='application/pdf', filename='portfolio_report.pdf')