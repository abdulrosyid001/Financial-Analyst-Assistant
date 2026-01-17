export interface Portfolio {
  id: number;
  ticker: string;
  quantity: number;
  buy_price: number;
  sector?: string;
}

export interface MarketData {
  ticker: string;
  data: any[];
}

export interface AnalysisResult {
  value: any;
  returns: any;
  optimization: any;
  ai_risk_explanation: string;
}

export interface ChatResponse {
  response: string;
}