import yfinance as yf
import pandas as pd
from typing import Dict, Any

def get_stock_data(ticker: str, period: str = "1y") -> Dict[str, Any]:
    """
    Fetch historical stock data for a given ticker.
    Returns OHLCV data as dict.
    """
    stock = yf.Ticker(ticker)
    hist = stock.history(period=period)
    if hist.empty:
        return {"error": "No data found"}
    
    # Convert to dict
    data = hist.reset_index().to_dict(orient='records')
    return {"ticker": ticker, "data": data}

def get_current_price(ticker: str) -> float:
    """
    Get current price of a stock.
    """
    stock = yf.Ticker(ticker)
    info = stock.info
    return info.get('currentPrice', 0.0)