# Setup development environment
setup:
	curl -sSL https://install.python-poetry.org | python3 -
	poetry install

# Run setup script
run-setup: setup
	poetry run python setup_project.py

# Run tests
test:
	pytest tests/

# Clean up temporary files
clean:
	rm -rf __pycache__
	rm -rf some_temporary_files

.PHONY: setup run-setup test clean
