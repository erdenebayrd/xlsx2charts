# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands
- **Backend (Python/FastAPI)**:
  - Run: `poetry run uvicorn backend.main:app --reload`
  - Test: `poetry run pytest backend/tests/`
  - Single test: `poetry run pytest backend/tests/test_file.py::test_name`

- **Frontend (React)**:
  - Run: `cd frontend && npm start`
  - Build: `cd frontend && npm run build`
  - Test: `cd frontend && npm test`
  - Single test: `cd frontend && npm test -- -t "test name"`

- **Docker**:
  - Start all: `docker-compose up`
  - Build: `docker-compose build`

## Code Style
- **Python**: PEP 8, type hints, docstrings for public functions
- **JavaScript**: ESLint with React App defaults, Tailwind CSS for styling
- **Imports**: Group standard library, third-party, local imports with blank lines
- **Error handling**: Use try/except in Python, try/catch in JS with meaningful messages
- **Naming**: snake_case for Python, camelCase for JavaScript