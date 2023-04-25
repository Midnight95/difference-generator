
build:
	poetry build

publish:
	poetry publish

install:
	poetry install

gendiff:
	poetry run gendiff

test:
	poetry run pytest

lint:
	poetry run flake8 gendiff