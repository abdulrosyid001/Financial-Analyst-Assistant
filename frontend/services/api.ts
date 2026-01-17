const API_BASE = 'http://localhost:8000';

export const api = {
  getMarketData: async (ticker: string) => {
    const res = await fetch(`${API_BASE}/market/${ticker}`);
    return res.json();
  },
  getPortfolios: async () => {
    const res = await fetch(`${API_BASE}/portfolio`);
    return res.json();
  },
  addPortfolio: async (data: any) => {
    const res = await fetch(`${API_BASE}/portfolio`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data),
    });
    return res.json();
  },
  deletePortfolio: async (id: number) => {
    await fetch(`${API_BASE}/portfolio/${id}`, { method: 'DELETE' });
  },
  analyzePortfolio: async () => {
    const res = await fetch(`${API_BASE}/analyze/portfolio`, { method: 'POST' });
    return res.json();
  },
  chat: async (query: string) => {
    const res = await fetch(`${API_BASE}/chat`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ query }),
    });
    return res.json();
  },
};