'client' // If using Next.js App Router, ensure this is a client component for state

import { useState, useEffect } from 'react';
import { getTransactions } from '@/lib/api'; // Adjust path if needed

interface Transaction {
  id: number;
  title: string;
  amount: number;
  category: string;
  date: string;
}

export default function Dashboard() {
  const [transactions, setTransactions] = useState<Transaction[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  // Form state
  const [title, setTitle] = useState('');
  const [amount, setAmount] = useState('');
  const [category, setCategory] = useState('');

  const fetchTransactions = async () => {
    try {
      setLoading(true);
      const data = await getTransactions();
      setTransactions(data);
    } catch (err: any) {
      setError(err.message || 'Failed to load transactions');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchTransactions();
  }, []);

  const handleCreate = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!title || !amount || !category) return;

    try {
      const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';
      const res = await fetch(`${API_URL}/transactions/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ title, amount: parseFloat(amount), category }),
      });

      if (!res.ok) throw new Error('Failed to create transaction');

      // Reset form and reload list
      setTitle('');
      setAmount('');
      setCategory('');
      fetchTransactions();
    } catch (err: any) {
      alert(err.message);
    }
  };

  return (
    <main style={{ maxWidth: '800px', margin: '40px auto', padding: '0 20px', fontFamily: 'sans-serif' }}>
      <h1>Finance Dashboard</h1>

      {/* Add Transaction Form */}
      <section style={{ background: '#f9f9f9', padding: '20px', borderRadius: '8px', marginBottom: '30px' }}>
        <h3>Add Transaction</h3>
        <form onSubmit={handleCreate} style={{ display: 'flex', gap: '10px', flexWrap: 'wrap' }}>
          <input
            type="text"
            placeholder="Title (e.g. Groceries)"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            required
            style={{ padding: '8px', flex: 1 }}
          />
          <input
            type="number"
            step="0.01"
            placeholder="Amount"
            value={amount}
            onChange={(e) => setAmount(e.target.value)}
            required
            style={{ padding: '8px', width: '100px' }}
          />
          <input
            type="text"
            placeholder="Category"
            value={category}
            onChange={(e) => setCategory(e.target.value)}
            required
            style={{ padding: '8px', width: '120px' }}
          />
          <button type="submit" style={{ padding: '8px 16px', background: '#0070f3', color: '#fff', border: 'none', borderRadius: '4px', cursor: 'pointer' }}>
            Add
          </button>
        </form>
      </section>

      {/* Transaction List */}
      <section>
        <h3>Transactions</h3>
        {loading && <p>Loading...</p>}
        {error && <p style={{ color: 'red' }}>{error}</p>}
        {!loading && !error && transactions.length === 0 && <p>No transactions found.</p>}
        
        <ul style={{ listStyle: 'none', padding: 0 }}>
          {transactions.map((tx) => (
            <li key={tx.id} style={{ display: 'flex', justifyContent: 'space-between', padding: '12px', borderBottom: '1px solid #eaeaea' }}>
              <div>
                <strong>{tx.title}</strong> <span style={{ color: '#666', fontSize: '0.9em' }}>({tx.category})</span>
              </div>
              <div style={{ fontWeight: 'bold', color: tx.amount < 0 ? 'red' : 'green' }}>
                ${tx.amount.toFixed(2)}
              </div>
            </li>
          ))}
        </ul>
      </section>
    </main>
  );
}