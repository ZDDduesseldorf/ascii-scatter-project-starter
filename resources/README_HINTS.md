# Hints for the ASCII scatter project

Use this file only when you need a small push. The main goal of the exercise is
project structure, environments, dependencies, imports, and Git collaboration.

## 1. Suggested target structure

```text
.
|-- .gitignore
|-- pyproject.toml
|-- uv.lock
|-- data/
|   `-- points.csv
`-- src/
    `-- ascii_plotter/
        |-- __init__.py
        |-- io.py
        |-- plot.py
        `-- cli.py
```

## 2. Create the uv project

From the repository root:

```bash
uv init --lib --name ascii-plotter
uv venv
uv add rich
```

Check the environment:

```bash
uv run python -c "import rich; print('rich import works')"
```

## 3. Minimal .gitignore

```gitignore
.venv/
__pycache__/
*.py[cod]
.pytest_cache/
.ruff_cache/
.DS_Store
```

## 4. CSV loader

A possible starting point for `src/ascii_plotter/io.py`:

```python
import csv
import os


def load_points(csv_path):
    if not os.path.isfile(csv_path):
        raise FileNotFoundError(csv_path)

    points = []

    with open(csv_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            point_type = row["type"]
            x = float(row["value1"])
            y = float(row["value2"])
            points.append(... add own code ...)

    return points
```

## 5. Scale coordinates to the terminal grid

```python
def scale(value, minimum, maximum, size):
    if maximum == minimum:
        return 0

    relative = (value - minimum) / (maximum - minimum)
    return ... add own code ...
```

Remember: row 0 is at the TOP of the terminal, so the y coordinate must be
flipped when writing into the grid.

## 6. Rich basics

```python
from rich.console import Console
from rich.text import Text

STYLES = {
    "A": "bold cyan",
    "B": "bold magenta",
    "C": "bold green",
    "D": "bold yellow",
}

console = Console()
line = Text()
line.append("A", style=STYLES["A"])
console.print(line)
```

## 7. CLI with os.path

```python
import os
import sys

from .io import load_points
from .plot import render_scatter


def main():
    if len(sys.argv) != 2:
        print("Usage: python -m ascii_plotter.cli <csv-file>")
        raise SystemExit(1)

    csv_path = os.path.abspath(sys.argv[1])

    if not os.path.isfile(csv_path):
        print(f"File not found: {csv_path}")
        raise SystemExit(1)

    ... add own code ... --> load points and render points
```

Run from the repository root:

```bash
uv run python -m ascii_plotter.cli data/points.csv
```
