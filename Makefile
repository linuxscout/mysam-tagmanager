.PHONY: help install develop clean lint format test coverage build publish

PYTHON := python3
PIP := pip

help:
	@echo "Available commands:"
	@echo "  make install     - Install package"
	@echo "  make develop     - Install package in editable mode"
	@echo "  make clean       - Remove build and cache files"
	@echo "  make lint        - Run linter (ruff)"
	@echo "  make format      - Auto-format code (black)"
	@echo "  make test        - Run tests with pytest"
	@echo "  make coverage    - Run tests with coverage report"
	@echo "  make build       - Build distribution packages"
	@echo "  make upload     - Upload distribution to PyPI"

install:
	$(PIP) install .

develop:
	$(PIP) install -e .[dev]

clean:
	rm -rf build/ dist/ *.egg-info
	find . -name "__pycache__" -exec rm -rf {} +
	find . -name "*.pyc" -delete

lint:
	ruff check .

format:
	black .

test:
	pytest -v

coverage:
	pytest --cov=mysam --cov-report=term-missing

build:
	$(PYTHON) -m build
wheel:
	sudo python3 setup.py bdist_wheel

# Publish to github
publish:
	git push origin master 

upload:
	echo "use twine upload dist/mysam-tagmanager-0.1.tar.gz"
	
tagsetdoc:
	mv doc/tagset.md doc/tagset.md.bak
	python3 tests/makedoc.py > doc/tagset.md
doc:
	epydoc -v --config epydoc.conf

examples:
	$(PYTHON) tests/examples/test_tagconfig.py
	$(PYTHON) tests/examples/test_tagcoder.py
	$(PYTHON) tests/examples/test_taginflector.py