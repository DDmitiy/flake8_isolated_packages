PYTHONPATH = PYTHONPATH=./
TEST = $(PYTHONPATH) pytest --verbosity=2 --showlocals --strict-markers $(arg) -k "$(k)"
PYLINT_CODE = flake8_isolated_packages.py tests
MYPY_CODE = $(PYLINT_CODE)
CODE = $(PYLINT_CODE)

.PHONY: test lint format check

test:
	$(TEST) --cov

lint:
	flake8 --jobs 1 --statistics --show-source $(CODE)
	pylint --jobs 1 --rcfile=pyproject.toml $(PYLINT_CODE)
	mypy $(MYPY_CODE)
	black --target-version py38 --skip-string-normalization --check $(CODE)
	pytest --dead-fixtures --dup-fixtures

format:
	autoflake --recursive --in-place --remove-all-unused-imports $(CODE)
	isort $(CODE)
	black --target-version py38 --skip-string-normalization $(CODE)
	unify --in-place --recursive $(CODE)

check: format lint test
