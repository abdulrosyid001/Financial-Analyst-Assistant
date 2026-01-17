from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .utils.database import engine, Base
from .api import market, portfolio, analyze, chat, report

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Financial Analyst Assistant", version="1.0.0")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(market.router)
app.include_router(portfolio.router)
app.include_router(analyze.router)
app.include_router(chat.router)
app.include_router(report.router)

@app.get("/")
async def root():
    return {"message": "AI Financial Analyst Assistant API"}