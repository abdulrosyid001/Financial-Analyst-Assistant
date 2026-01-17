from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..utils.database import get_db
from ..services.portfolio_service import get_portfolios
from ..services.analysis_service import calculate_portfolio_value, calculate_returns, optimize_portfolio
from ..dspy.analyst import explain_risk

router = APIRouter()

@router.post("/analyze/portfolio")
async def analyze_portfolio(db: Session = Depends(get_db)):
    portfolios = get_portfolios(db)
    value = calculate_portfolio_value(portfolios)
    returns = calculate_returns(portfolios)
    optimization = optimize_portfolio(portfolios)
    
    # AI explanation
    analytics_str = f"Value: {value}, Returns: {returns}"
    risk_exp = explain_risk(analytics_str)
    
    return {
        "value": value,
        "returns": returns,
        "optimization": optimization,
        "ai_risk_explanation": risk_exp
    }