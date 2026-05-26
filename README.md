# lux_template

[![codecov](https://codecov.io/gh/LiTTY-FYDP/lux-template/branch/main/graph/badge.svg?token=lux-template_token_here)](https://codecov.io/gh/LiTTY-FYDP/lux-template)
[![CI](https://github.com/LiTTY-FYDP/lux-template/actions/workflows/main.yml/badge.svg)](https://github.com/LiTTY-FYDP/lux-template/actions/workflows/main.yml)

Awesome lux_template created by LiTTY-FYDP.

## Requirements

Use [mise](https://mise.jdx.dev/) for local tools. The project pins Python 3.14.5 and uv in `mise.toml`, and mise creates the project virtual environment at `~/.virtualenvs/lux-template`.

```bash
mise install
mise run install
```

## Install it from PyPI

```bash
pip install lux_template
```

## Usage

```py
from lux_template import NAME

print(NAME)
```

```bash
python -m lux_template
lux_template
```

## Development

```bash
mise run fmt
mise run lint
mise run typecheck
mise run test
mise run build
```

Read [CONTRIBUTING.md](CONTRIBUTING.md) for the full contribution workflow.
