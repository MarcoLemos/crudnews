POETRY = poetry run
.PHONY: install shell run format test sec docs img imgm imgd imgs img


install:
	@poetry install
shell:
	@poetry shell
format:
	@${POETRY} isort .
	@${POETRY} blue .
test:
	@${POETRY} pytest
cover:
	@${POETRY} pytest --cov=.
sec:
	@${POETRY} pip-audit
docs:
	@${POETRY} mkdocs serve
imgup:
	docker-compose --env-file .env up -d
imgm:
	docker-compose --env-file .env up -d mongo
img:
	docker-compose --env-file .env start
imgs:
	docker-compose --env-file .env stop
imgd:
	docker-compose --env-file .env down