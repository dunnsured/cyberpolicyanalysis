# Cyber Insurance Analyzer

A comprehensive tool for analyzing and evaluating cyber insurance policies to help organizations make informed decisions about their cybersecurity coverage.

## Project Structure

```
cyber-insurance-analyzer/
├── .bmad-core/           # (Will be added in Step 2)
├── backend/              # FastAPI backend
│   ├── app/
│   │   ├── main.py      # FastAPI application
│   │   ├── models/      # Database models
│   │   ├── routers/     # API routes
│   │   ├── services/    # Business logic
│   │   └── core/        # Core utilities
│   ├── requirements.txt
│   └── .env.example
├── frontend/             # React frontend
│   ├── src/
│   ├── package.json
│   └── vite.config.js
├── docs/
│   ├── prd.md           # Product Requirements Document
│   └── architecture.md  # Architecture overview
├── docker-compose.yml
└── README.md
```

## Quick Start

1. Clone the repository
2. Copy `.env.example` to `.env` in the backend directory and configure
3. Run with Docker Compose:
   ```bash
   docker-compose up --build
   ```

## Development

### Backend
- FastAPI server runs on http://localhost:8000
- API documentation available at http://localhost:8000/docs

### Frontend  
- React development server runs on http://localhost:3000
- Built with Vite for fast development

### Database
- PostgreSQL database runs on localhost:5432
- Use Alembic for database migrations

## Features

- Policy document analysis and comparison
- Risk assessment integration
- Coverage gap identification  
- Premium optimization recommendations
- Compliance requirement mapping