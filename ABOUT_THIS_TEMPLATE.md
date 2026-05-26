# About this template

This template provides a small, modern Python project structure with low runtime dependency pressure and strict development checks.

## Structure

```text
├── Containerfile            # Container image for the project
├── CONTRIBUTING.md          # Contributor workflow
├── docs                     # Documentation site
├── .github                  # GitHub metadata and workflows
├── .gitignore               # Local and generated files to ignore
├── HISTORY.md               # Project changelog
├── LICENSE                  # Project license
├── MANIFEST.in              # Source distribution file manifest
├── mise.toml                # Python, uv, virtual environment, and tasks
├── mkdocs.yml               # MkDocs configuration
├── pyproject.toml           # Packaging and tool configuration
├── lux_template             # Main Python package
│   ├── base.py              # Core package module
│   ├── __init__.py          # Public package interface
│   ├── __main__.py          # Module execution entry point
│   └── VERSION              # Static package version
├── README.md                # Project overview
└── tests                    # Unit tests
    ├── conftest.py          # Pytest fixtures
    ├── __init__.py          # Test package marker
    └── test_base.py         # Base tests
```

## Tooling decisions

### Why pyproject.toml?

`pyproject.toml` is the modern home for Python package metadata and tool configuration. This template uses setuptools through PEP 517/518 build metadata, keeps the package version in `lux_template/VERSION`, and configures pytest, coverage, Ruff, and ty in one place.

### Why mise?

mise pins Python 3.14.5 and uv for the project, creates the virtual environment, and replaces ad hoc shell targets with discoverable tasks.

```bash
mise install
mise run install
mise run check
```

### Why Ruff and ty?

Ruff replaces the older Black, isort, and Flake8 stack with one formatter and linter. ty provides fast type checking. Both are configured with strict defaults so new projects start from a high signal baseline.

### Why keep VERSION as a file?

The package version is readable without importing the package. That keeps release automation and external packaging simple while still letting setuptools read the version dynamically during builds.

### Why keep MANIFEST.in?

The manifest keeps source distributions explicit for downstream packagers that run tests, inspect the changelog, or rebuild container images from the source release.

### Why no pre-commit by default?

The default workflow stays centered on mise tasks to keep setup small. Projects that want pre-commit can add it later and delegate hooks to the same Ruff, ty, and pytest commands.
