"""Makefile for common tasks
"""

.PHONY: help install dev test lint format build clean

help:
	@echo "Electrical AI Engineering Suite - Development Commands"
	@echo ""
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  help          - Show this help message"
	@echo "  install       - Install all dependencies"
	@echo "  dev           - Start development server"
	@echo "  test          - Run all tests"
	@echo "  lint          - Run linters"
	@echo "  format        - Format code"
	@echo "  build         - Build for production"
	@echo "  clean         - Clean up temporary files"

install:
	docker-compose build

dev:
	docker-compose up

test:
	docker-compose exec backend python -m pytest tests/ -v

lint:
	docker-compose exec backend flake8 .
	docker-compose exec backend black --check .

format:
	docker-compose exec backend black .
	docker-compose exec backend isort .

build:
	docker-compose build --no-cache

clean:
	docker-compose down -v
	rm -rf backend/__pycache__
	rm -rf frontend/.next
	rm -rf frontend/node_modules