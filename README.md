# Phonebook Backend (FastAPI)

A simple backend service built with **FastAPI**, **SQLAlchemy**, and **PostgreSQL**.

## Tech Stack
- FastAPI
- SQLAlchemy ORM
- PostgreSQL
- psycopg (Postgres driver)
- Uvicorn

## Features
- Health check endpoint
- Create users
- SQLAlchemy models & schemas
- Dependency-injected DB sessions

## Setup (Local)
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
