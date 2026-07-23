# Install dependencies and set up the project
sync:
    uv sync --all-packages --dev

# Update all dependency versions, then sync
update:
    uv lock --upgrade
    uv sync --all-packages --dev

# Lint and auto-format
lint:
    uv run ruff check --fix
    uv run ruff format

# Type-check
typecheck:
    uv run pyright

# Run the test suite (needs a local AllSpice Hub at :3000 and a .token)
test:
    uv run pytest

# Lint, type-check, and test
check: lint typecheck test

# Re-record the VCR cassettes against a live Hub
record:
    uv run pytest --record-mode=rewrite

# Update syrupy snapshots
snapshot-update:
    uv run pytest --snapshot-update

# Build the py-allspice wheel + sdist
build:
    uv build --package py-allspice

# Generate API docs with pdoc
docs:
    uv run pdoc --output-dir docs/ allspice
