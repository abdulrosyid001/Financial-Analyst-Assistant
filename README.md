# AI Financial Analyst Assistant

A complete, production-ready AI-powered financial analysis tool that runs entirely locally without any paid services.

## Overview

This project provides:
- Real-time and historical stock data ingestion via Yahoo Finance
- Portfolio management with SQLite database
- Financial analytics (returns, volatility, optimization)
- AI-driven insights using DSPy and open-source LLMs
- Natural language query interface
- PDF report generation

## Architecture

```
Frontend (Next.js) <-> Backend (FastAPI)
       |                    |
       v                    v
   User Interface      API Endpoints
                          |
                          v
                    DSPy Modules
                          |
                          v
                 Local LLM (Hugging Face)
                          |
                          v
                 Data Services (yfinance, SQLite)
```

## Tech Stack

- **Frontend**: Next.js (App Router), TypeScript, Tailwind CSS
- **Backend**: FastAPI, Python
- **Database**: SQLite with SQLAlchemy ORM
- **AI**: DSPy, Hugging Face Transformers
- **Data**: yfinance, pandas, numpy
- **PDF**: reportlab

## Installation

### Prerequisites
- Python 3.8+
- Node.js 18+
- At least 16GB RAM (for LLM inference)
- GPU recommended for faster inference

### Backend Setup
1. Navigate to backend directory:
   ```bash
   cd backend
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Copy environment file:
   ```bash
   cp ../.env.example ../.env
   ```

4. The LLM model will be downloaded automatically on first run.

### Frontend Setup
1. Navigate to frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

## Running the Application

### Start Backend
```bash
cd backend
uvicorn main:app --reload
```
Backend will run on http://localhost:8000

### Start Frontend
```bash
cd frontend
npm run dev
```
Frontend will run on http://localhost:3000

## Usage

1. Open the frontend in your browser.
2. Manage your portfolio by adding/removing stocks.
3. Ask questions to the AI chat (e.g., "Is my portfolio too risky?").
4. Generate PDF reports with AI insights.

## API Endpoints

- `GET /market/{ticker}`: Get stock data
- `GET /portfolio`: List portfolios
- `POST /portfolio`: Add portfolio
- `DELETE /portfolio/{id}`: Delete portfolio
- `POST /analyze/portfolio`: Analyze portfolio
- `POST /chat`: AI chat query

## Hardware Requirements

- CPU: Multi-core processor
- RAM: 16GB minimum, 32GB recommended
- Storage: 10GB for models and data
- GPU: Optional, but speeds up LLM inference significantly

## Notes

- The system uses open-source models and runs locally.
- Internet connection required only for fetching stock data from Yahoo Finance.
- First run may take time to download the LLM model.