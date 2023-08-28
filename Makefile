up:
	poetry run uvicorn app:app --reload --port 8000

.PHONY: migrate-revision
migrate-revision:
	alembic revision --autogenerate -m $(name)

.PHONY: migrate-up
migrate-up:
	alembic upgrade $(rev)