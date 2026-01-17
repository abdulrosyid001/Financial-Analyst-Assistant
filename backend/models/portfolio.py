from sqlalchemy import Column, Integer, String, Float
from ..utils.database import Base

class Portfolio(Base):
    __tablename__ = "portfolios"

    id = Column(Integer, primary_key=True, index=True)
    ticker = Column(String, index=True)
    quantity = Column(Float)
    buy_price = Column(Float)
    sector = Column(String, nullable=True)