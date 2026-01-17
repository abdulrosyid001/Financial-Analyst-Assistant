from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from ..utils.database import get_db
from ..services.portfolio_service import get_portfolios
from ..services.analysis_service import calculate_portfolio_value, calculate_returns
from ..dspy.analyst import analyze_market, recommend_investment

class ChatRequest(BaseModel):
    query: str

router = APIRouter()

@router.post("/chat")
async def chat_with_ai(request: ChatRequest, db: Session = Depends(get_db)):
    query = request.query.lower()
    portfolios = get_portfolios(db)
    
    if "risky" in query or "risk" in query:
        returns = calculate_returns(portfolios)
        analytics_str = str(returns)
        from ..dspy.analyst import explain_risk
        response = explain_risk(analytics_str)
    elif "volatility" in query:
        returns = calculate_returns(portfolios)
        max_vol = max(returns["volatilities"], key=returns["volatilities"].get)
        response = f"The stock contributing most to volatility is {max_vol}."
    elif "market" in query:
        # Simplified: assume some market data
        market_data = "Market is stable."  # In real, fetch indices
        response = analyze_market(market_data)
    elif "recommend" in query:
        portfolio_str = str([p.ticker for p in portfolios])
        response = recommend_investment(portfolio_str)
    else:
        response = "I'm sorry, I didn't understand the query."
    
    return {"response": response}