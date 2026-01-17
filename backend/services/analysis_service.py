import pandas as pd
import numpy as np
from typing import Dict, Any, List
from .market_service import get_current_price
from ..models.portfolio import Portfolio
from sqlalchemy.orm import Session

def calculate_portfolio_value(portfolios: List[Portfolio]) -> Dict[str, Any]:
    """
    Calculate total portfolio value, asset allocation, etc.
    """
    total_value = 0.0
    allocations = {}
    for p in portfolios:
        current_price = get_current_price(p.ticker)
        value = p.quantity * current_price
        total_value += value
        allocations[p.ticker] = value
    
    # Percentages
    for ticker in allocations:
        allocations[ticker] = (allocations[ticker] / total_value) * 100 if total_value > 0 else 0
    
    return {
        "total_value": total_value,
        "allocations": allocations
    }

def calculate_returns(portfolios: List[Portfolio]) -> Dict[str, Any]:
    """
    Calculate daily returns, volatility, etc.
    Simplified: use historical data for one year.
    """
    # For simplicity, fetch data for each ticker and compute
    volatilities = {}
    for p in portfolios:
        # Fetch 1y data
        import yfinance as yf
        hist = yf.Ticker(p.ticker).history(period="1y")
        if not hist.empty:
            returns = hist['Close'].pct_change().dropna()
            vol = returns.std() * np.sqrt(252)  # Annualized volatility
            volatilities[p.ticker] = vol
        else:
            volatilities[p.ticker] = 0.0
    
    return {"volatilities": volatilities}

def optimize_portfolio(portfolios: List[Portfolio]) -> Dict[str, Any]:
    """
    Simple portfolio optimization: equal weight.
    """
    n = len(portfolios)
    if n == 0:
        return {}
    weights = {p.ticker: 1/n for p in portfolios}
    return {"suggested_weights": weights}