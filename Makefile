up:
	uvicorn app:app --reload

.PHONY: migrate-revision
migrate-revision:
	alembic revision --autogenerate -m $(name)

.PHONY: migrate-up
migrate-up:
	alembic upgrade $(rev)