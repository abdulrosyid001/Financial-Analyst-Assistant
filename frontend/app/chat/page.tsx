'use client';

import { useState } from 'react';
import { api } from '../../services/api';

export default function ChatPage() {
  const [query, setQuery] = useState('');
  const [response, setResponse] = useState('');

  const handleSubmit = async (e: any) => {
    e.preventDefault();
    const res = await api.chat(query);
    setResponse(res.response);
  };

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">AI Chat</h1>
      <form onSubmit={handleSubmit} className="mb-4">
        <input
          type="text"
          placeholder="Ask a question..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          className="border p-2 w-full"
          required
        />
        <button type="submit" className="bg-green-500 text-white px-4 py-2 mt-2">Ask</button>
      </form>
      {response && (
        <div className="border p-4 bg-white">
          <p>{response}</p>
        </div>
      )}
    </div>
  );
}