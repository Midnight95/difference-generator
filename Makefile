install:
	python3 -m poetry install

build:
	python3 -m poetry build

publish:
	python3 -m poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

gendiff:
	python3 -m poetry run gendiff

test:
	python3 -m poetry run pytest

test-coverage:
	python3 -m poetry run coverage run -m pytest && python3 -m poetry run coverage report  # если что не бейте

lint:
	python3 -m poetry run flake8 gendiff