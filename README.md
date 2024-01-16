# CookieCutter Python Poetry

# Features

- [x] Use `poetry` as package manager
- [x] Integrated with `pre-commit` configuration
- [x] Integrated with `github workflow` configuration
- [x] For Python ^3.12

# Usage

**You should install cookiecutter first by `pip install cookiecutter`**

```bash
cookiecutter gh:iiicebearrr/cookiecutter-pypackage-poetry
```

then, cd to your app and init your project:

```bash
git init
poetry env use {YOUR PYTHON EXECUTABLE}
source {YOUR POETRY VENV PATH}/bin/activate
poetry install
```