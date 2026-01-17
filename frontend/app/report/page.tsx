'use client';

import { useState } from 'react';

export default function ReportPage() {
  const [insights, setInsights] = useState('');

  const generateReport = async () => {
    // Trigger download
    const link = document.createElement('a');
    link.href = 'http://localhost:8000/report';
    link.download = 'portfolio_report.pdf';
    link.click();
  };

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4">Generate Report</h1>
      <button onClick={generateReport} className="bg-purple-500 text-white px-4 py-2">Download PDF Report</button>
    </div>
  );
}