from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..utils.database import get_db
from ..schemas.portfolio import PortfolioCreate, Portfolio
from ..services.portfolio_service import get_portfolios, create_portfolio, delete_portfolio

router = APIRouter()

@router.get("/portfolio", response_model=list[Portfolio])
async def read_portfolios(db: Session = Depends(get_db)):
    return get_portfolios(db)

@router.post("/portfolio", response_model=Portfolio)
async def add_portfolio(portfolio: PortfolioCreate, db: Session = Depends(get_db)):
    return create_portfolio(db, portfolio)

@router.delete("/portfolio/{portfolio_id}")
async def remove_portfolio(portfolio_id: int, db: Session = Depends(get_db)):
    success = delete_portfolio(db, portfolio_id)
    if not success:
        raise HTTPException(status_code=404, detail="Portfolio not found")
    return {"message": "Deleted"}