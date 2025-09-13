# Architecture Overview

## System Architecture
```
Frontend (React/Vite) → Backend API (FastAPI) → Database (PostgreSQL)
```

## Backend Components
- **FastAPI**: REST API server
- **SQLAlchemy**: ORM for database operations
- **Alembic**: Database migrations
- **PostgreSQL**: Primary data storage

## Frontend Components  
- **React**: UI framework
- **TypeScript**: Type safety
- **Vite**: Build tool and dev server
- **Axios**: HTTP client for API calls

## Key Services
- Policy analysis engine
- Risk assessment module
- Document processing pipeline
- Comparison and recommendation system

## Data Flow
1. User uploads policy documents
2. Backend processes and analyzes documents
3. Analysis results stored in database
4. Frontend displays insights and recommendations