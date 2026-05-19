UV ?= uv
APP ?= app.main:app
HOST ?= 0.0.0.0
PORT ?= 8005

.PHONY: help dev run

help:
	@echo "Available targets:"
	@echo "  make dev                 Start the app with reload"
	@echo "  make run                 Start the app without reload"
	@echo ""
	@echo "You can override variables like:"
	@echo "  make dev PORT=8000 HOST=127.0.0.1"

dev:
	$(UV) run uvicorn $(APP) --host $(HOST) --port $(PORT) --reload

run:
	$(UV) run uvicorn $(APP) --host $(HOST) --port $(PORT)