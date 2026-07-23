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

# The allspice tests (and the full run) need a local Hub at :3000 and a .token; generator doesn't.
# Run tests: `just test` (all), `just test generator`, `just test allspice`.
test package="":
    #!/usr/bin/env bash
    case "{{package}}" in
        generator) uv run pytest packages/open-api-generator/tests ;;
        allspice)  uv run pytest packages/allspice/tests ;;
        "")        uv run pytest ;;
        *)         echo "unknown package '{{package}}' (use: generator, allspice)" >&2; exit 2 ;;
    esac

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

# Generate the client from a Hub: `just generate local` or `just generate prod`
generate target:
    #!/usr/bin/env bash
    case "{{target}}" in
        local) uv run python -m open_api_generator http://localhost:3000 ;;
        prod)  uv run python -m open_api_generator https://hub.allspice.io/ ;;
        *)     echo "unknown target '{{target}}' (use: local, prod)" >&2; exit 2 ;;
    esac
