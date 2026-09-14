# Finance Dashboard

## Architecture (Tech Stack)

[ Amex Alerts Inbox ] 
        │
        ▼ (Email / Webhook)
┌─────────────────────────┐          ┌──────────────────────────┐
│  FastAPI Backend        │◄────────►│  Supabase (PostgreSQL)   │
│  (Hosted on Render)     │          │  (Cloud Database)        │
└─────────────────────────┘          └──────────────────────────┘
        ▲
        │ (API Requests / JSON data)
┌─────────────────────────┐
│  Frontend Dashboard     │
│  (Hosted on Vercel)     │
└─────────────────────────┘
      ▲             ▲
      │ (You)       │ (Partner)


## TODO

[] implement ML to identify transactions and assign them to a category

### Project Progress Tracker
Step 1: Set up project workspace & local database 
Step 2: Add Python/FastAPI to Docker & connect to the database 
Step 3: Write database models (users, categories, budgets, transactions)
Step 4: Build the API endpoints for managing data
Step 5: Connect frontend (Vercel) to the backend
Step 6: Set up Amex email ingestion / automation