install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

gendiff:
	poetry run gendiff

test:
	poetry run pytest

test-coverage:
	poetry run coverage run -m pytest && poetry run coverage report  # если что не бейте

lint:
	poetry run flake8 gendiff