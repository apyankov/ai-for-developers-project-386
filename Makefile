POETRY = $(shell command -v poetry 2>/dev/null || echo ~/.local/bin/poetry)

.PHONY: dev dev-backend dev-frontend build test lint generate

dev:
	docker compose up --build

dev-backend:
	cd backend && $(POETRY) run uvicorn app.main:app --reload --port 8000

dev-frontend:
	cd frontend && npm run dev

generate:
	cd typespec && npm run compile

test:
	cd backend && $(POETRY) run pytest -v

lint:
	cd backend && $(POETRY) run ruff check .
	cd frontend && npm run lint
