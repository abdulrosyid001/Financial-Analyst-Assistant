from fastapi import APIRouter, HTTPException
from ..services.market_service import get_stock_data

router = APIRouter()

@router.get("/market/{ticker}")
async def get_market_data(ticker: str):
    data = get_stock_data(ticker)
    if "error" in data:
        raise HTTPException(status_code=404, detail=data["error"])
    return data