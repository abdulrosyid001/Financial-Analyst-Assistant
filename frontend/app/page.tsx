import Link from 'next/link'

export default function Home() {
  return (
    <div className="min-h-screen flex items-center justify-center">
      <div className="text-center">
        <h1 className="text-4xl font-bold mb-8">AI Financial Analyst Assistant</h1>
        <div className="space-x-4">
          <Link href="/portfolio" className="bg-blue-500 text-white px-4 py-2 rounded">Portfolio Management</Link>
          <Link href="/chat" className="bg-green-500 text-white px-4 py-2 rounded">AI Chat</Link>
          <Link href="/report" className="bg-purple-500 text-white px-4 py-2 rounded">Generate Report</Link>
        </div>
      </div>
    </div>
  )
}