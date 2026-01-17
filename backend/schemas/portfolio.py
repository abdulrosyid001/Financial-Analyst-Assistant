from pydantic import BaseModel
from typing import Optional

class PortfolioBase(BaseModel):
    ticker: str
    quantity: float
    buy_price: float
    sector: Optional[str] = None

class PortfolioCreate(PortfolioBase):
    pass

class Portfolio(PortfolioBase):
    id: int

    class Config:
        from_attributes = True