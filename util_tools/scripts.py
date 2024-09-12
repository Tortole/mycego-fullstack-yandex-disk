"""
Project scripts for run through Poetry
"""

import sys
import subprocess
from pathlib import Path


def manager() -> None:
    subprocess.run(["poetry", "run", "python", "manage.py", *sys.argv[1:]], check=False)


def tailwind() -> None:
    subprocess.run(
        [
            "npx",
            "tailwindcss",
            "-i",
            str(Path("apps/static/base/css/input.css")),
            "-o",
            str(Path("apps/static/base/css/out.css")),
            *sys.argv[1:],
        ],
        shell=True,
        check=False,
    )


def full_migrate() -> None:
    subprocess.run(
        ["poetry", "run", "python", "manage.py", "makemigrations"], check=False
    )
    subprocess.run(["poetry", "run", "python", "manage.py", "migrate"], check=False)


def flake8() -> None:
    subprocess.run(["poetry", "run", "flake8", "."], check=False)


def black() -> None:
    subprocess.run(["poetry", "run", "black", "."], check=False)
    flake8()


def export_requirements() -> None:
    subprocess.run(
        [
            "poetry",
            "export",
            "-f",
            "requirements.txt",
            "-o",
            "requirements.txt",
            "--without-hashes",
        ],
        check=False,
    )
