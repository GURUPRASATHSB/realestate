# 🏠 EstateHub AI – Agentic Multi-Agent Real Estate Assistant

EstateHub AI is a demo/mock **agentic AI real-estate assistant** that coordinates property discovery, area insights, site-visit scheduling and affordability estimation.

> **Important:** Demo mode uses mock property data. It does not claim real-time listings, ownership, title status, approvals, market prices or confirmed visits.

## Features
- Property Search Agent
- Area Insights Agent
- Site Visit Agent
- Affordability Agent
- Validation Agent
- Orchestrator Agent
- LangGraph workflow
- Pydantic schemas
- FastAPI backend
- Streamlit UI
- PostgreSQL/Supabase + SQLAlchemy
- SQLite fallback for local demo
- Mock provider architecture
- Pytest tests

## Architecture
```mermaid
flowchart TD
    U[User] --> O[Orchestrator]
    O --> P[Property Search Agent]
    P --> A[Area Insights Agent]
    A --> V[Site Visit Agent]
    V --> L[Affordability Agent]
    L --> X[Validation Agent]
    X --> F[Final Property Plan]
    P --> PT[Property Search Tool]
    A --> AT[Area Tool]
    V --> VT[Visit Tool]
    L --> LT[Loan Tool]
    PT --> RP[Mock Real Estate Provider]
    AT --> RP
    VT --> RP
```

## Folder Structure
```text
estatehub-ai/
├── app/
│   ├── tools/
│   │   ├── property_search_tool.py
│   │   ├── area_tool.py
│   │   ├── visit_tool.py
│   │   └── loan_tool.py
│   ├── agents.py
│   ├── config.py
│   ├── db.py
│   ├── idempotency.py
│   ├── memory.py
│   ├── providers.py
│   ├── runner.py
│   └── worker.py
├── schema/
├── api/
├── frontend/
├── scripts/
├── tests/
├── database/
│   └── supabase_schema.sql
├── README.md
├── PROJECT_BRIEF.md
├── requirements.txt
├── pytest.ini
├── .env.example
├── .gitignore
└── estatehub_server.py
```

## Tech Stack
Python 3.11+, LangGraph, Pydantic, FastAPI, PostgreSQL/Supabase, SQLAlchemy, python-dotenv, pytest and Streamlit.

## Installation
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
# source .venv/bin/activate
pip install -r requirements.txt
```

## Environment
Copy `.env.example` to `.env`.

### Supabase database setup
1. Create a project at Supabase.
2. Open **SQL Editor** and run `database/supabase_schema.sql`.
3. Open **Connect** in Supabase and copy the PostgreSQL connection string.
4. Put it in `.env` as `DATABASE_URL` using the SQLAlchemy form `postgresql+psycopg2://...`.
5. Never commit `.env` or expose the database password.

Example:
```text
MOCK_MODE=true
DATABASE_URL=postgresql+psycopg2://postgres.PROJECT_REF:PASSWORD@HOST:5432/postgres
SUPABASE_URL=https://YOUR_PROJECT_REF.supabase.co
SUPABASE_ANON_KEY=YOUR_SUPABASE_ANON_KEY
```

The included SQL creates `properties`, `clients`, `property_inquiries`, `property_visits` and `search_history` and inserts demo property records.

## Run Backend
```bash
python estatehub_server.py
```
Open `http://127.0.0.1:8000/docs`.

## Run Streamlit
```bash
streamlit run frontend/real_estate_dashboard.py
```

## Run Tests
```bash
pytest
```

## Example Request
```json
{
  "client_name":"Demo Client",
  "location":"Chennai",
  "property_type":"Apartment",
  "purpose":"Purchase",
  "budget":8000000,
  "bedrooms":2,
  "min_area_sqft":1000,
  "amenities":["Parking","Gym"]
}
```

## API
- `GET /health`
- `POST /properties/plan`

## Mock Mode
**Demo mode uses mock real-estate data. Real listing availability, ownership, title, approvals, current prices and financing terms require appropriate external providers and independent verification.**

## Future Improvements
Real listing APIs, maps, mortgage APIs, property document verification, CRM, saved searches, alerts, secure authentication and multilingual support.
