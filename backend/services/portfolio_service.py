from sqlalchemy.orm import Session
from ..models.portfolio import Portfolio
from ..schemas.portfolio import PortfolioCreate, Portfolio
from typing import List

def get_portfolios(db: Session) -> List[Portfolio]:
    return db.query(Portfolio).all()

def create_portfolio(db: Session, portfolio: PortfolioCreate) -> Portfolio:
    db_portfolio = Portfolio(**portfolio.dict())
    db.add(db_portfolio)
    db.commit()
    db.refresh(db_portfolio)
    return db_portfolio

def delete_portfolio(db: Session, portfolio_id: int) -> bool:
    portfolio = db.query(Portfolio).filter(Portfolio.id == portfolio_id).first()
    if portfolio:
        db.delete(portfolio)
        db.commit()
        return True
    return False