const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

export async function getTransactions() {
  const res = await fetch(`${API_URL}/transactions/`);
  if (!res.ok) throw new Error('Failed to fetch transactions');
  return res.json();
}