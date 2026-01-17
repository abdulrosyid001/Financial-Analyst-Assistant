'use client';

import { useState, useEffect } from 'react';
import { api } from '../../services/api';
import { Portfolio } from '../../types';

export default function PortfolioPage() {
  const [portfolios, setPortfolios] = useState<Portfolio[]>([]);
  const [form, setForm] = useState({ ticker: '', quantity: '', buy_price: '', sector: '' });

  useEffect(() => {
    loadPortfolios();
  }, []);

  const loadPortfolios = async () => {
    const data = await api.getPortfolios();
    setPortfolios(data);
  };

  const handleSubmit = async (e: any) => {
    e.preventDefault();
    await api.addPortfolio({
      ticker: form.ticker,
      quantity: parseFloat(form.quantity),
      buy_price: parseFloat(form.buy_price),
      sector: form.sector || undefined,
    });
    setForm({ ticker: '', quantity: '', buy_price: '', sector: '' });
    loadPortfolios();
  };

  const handleDelete = async (id: number) => {
    await api.deletePortfolio(id);
    loadPortfolios();
  };

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Portfolio Management</h1>
      <form onSubmit={handleSubmit} className="mb-8">
        <input
          type="text"
          placeholder="Ticker"
          value={form.ticker}
          onChange={(e) => setForm({ ...form, ticker: e.target.value })}
          className="border p-2 mr-2"
          required
        />
        <input
          type="number"
          placeholder="Quantity"
          value={form.quantity}
          onChange={(e) => setForm({ ...form, quantity: e.target.value })}
          className="border p-2 mr-2"
          required
        />
        <input
          type="number"
          placeholder="Buy Price"
          value={form.buy_price}
          onChange={(e) => setForm({ ...form, buy_price: e.target.value })}
          className="border p-2 mr-2"
          required
        />
        <input
          type="text"
          placeholder="Sector"
          value={form.sector}
          onChange={(e) => setForm({ ...form, sector: e.target.value })}
          className="border p-2 mr-2"
        />
        <button type="submit" className="bg-blue-500 text-white px-4 py-2">Add</button>
      </form>
      <ul>
        {portfolios.map((p) => (
          <li key={p.id} className="flex justify-between items-center border-b py-2">
            <span>{p.ticker} - {p.quantity} @ ${p.buy_price} ({p.sector})</span>
            <button onClick={() => handleDelete(p.id)} className="bg-red-500 text-white px-2 py-1">Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}