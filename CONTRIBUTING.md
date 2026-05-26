# How to develop on this project

lux_template welcomes contributions from the community.

## Set up your fork

On GitHub, click `Fork`, then clone your fork and enter the project directory.

```bash
git clone git@github.com:YOUR_GIT_USERNAME/lux-template.git
cd lux-template
git remote add upstream https://github.com/LiTTY-FYDP/lux-template
```

## Set up the toolchain

This project uses mise for Python, uv, the virtual environment, and common tasks.

```bash
mise install
mise run install
```

The pinned runtime is Python 3.14.5. The virtual environment is created at `~/.virtualenvs/lux-template`.

## Work on changes

```bash
git checkout -b my_contribution
mise run fmt
mise run lint
mise run typecheck
mise run test
mise run docs
```

Coverage is expected to stay at 100%.

## Commit your changes

This project uses [conventional commit messages](https://www.conventionalcommits.org/en/v1.0.0/).

Example: `fix(package): update pyproject metadata`

## Mise tasks

```bash
mise tasks
mise run install
mise run fmt
mise run lint
mise run typecheck
mise run test
mise run check
mise run clean
mise run docs
mise run build
mise run release
mise run init
```

## Making a release

This project uses semantic versioning and tags releases with `X.Y.Z`. When a tag is pushed, GitHub Actions creates a GitHub release and publishes to PyPI.

Configure a `PYPI_API_TOKEN` secret in the repository settings, then run:

```bash
mise run release
```
