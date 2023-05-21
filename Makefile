install:
	poetry install

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

test-coverage:


lint:
	poetry run flake8 gendiff