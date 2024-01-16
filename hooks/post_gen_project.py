#!/usr/bin/env python
from pathlib import Path

PROJECT_DIRECTORY = Path.cwd()


def rm_tree(pth: Path):
    pth = pth if isinstance(pth, Path) else Path(pth)
    if not pth.exists():
        return
    for child in pth.glob("*"):
        if child.is_file():
            child.unlink()
        else:
            rm_tree(child)
    pth.rmdir()


def remove_file(filepath: Path | str):
    filepath = PROJECT_DIRECTORY / Path(filepath)
    if filepath.exists():
        if filepath.is_dir():
            rm_tree(filepath)
        else:
            filepath.unlink(missing_ok=True)


if __name__ == "__main__":
    if "{{ cookiecutter.add_gh_workflow }}" != "y":
        remove_file(".github")
    elif "{{ cookiecutter.gh_workflow_publish_to_pypi }}" != "y":
        remove_file(".github/workflows/publish-pypi.yaml")
