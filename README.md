# Ledgerly

Personal-finance API for tracking transactions, category spending, and monthly budgeting insights.

## Why it stands out

- Clean FastAPI routing and Pydantic validation
- Deterministic spending analytics endpoint
- Containerized local deployment
- Focused tests and practical README documentation

## Start

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Visit `/docs` to explore the API. Create transactions at `POST /transactions`; review a monthly category breakdown at `GET /analytics/monthly`.

## License

MIT
