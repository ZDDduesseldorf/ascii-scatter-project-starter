# Praktikum: Vom CSV-Datensatz zum sauberen Python-Projekt

## ASCII Scatter Plot im Terminal
 
**Teamgröße:** 2 Personen  
**Schwerpunkt:** Environment, Dependencies, Projektstruktur, Imports, Git/GitHub-Zusammenarbeit  

> In diesem Praktikum geht es **nicht primär darum, einen schwierigen Plot-Algorithmus zu erfinden**.  
> Die eigentliche Aufgabe ist, aus einer kleinen Programmieridee ein **sauber strukturiertes, reproduzierbares Python-Projekt** zu machen.

---

# 1. Szenario

Ihr bekommt einen kleinen CSV-Datensatz mit drei Spalten:

```csv
type,value1,value2
A,1.2,7.8
B,2.7,5.1
C,4.8,8.4
D,8.2,2.0
```

Die Spalte `type` enthält eine der Kategorien:

```text
A, B, C, D
```

`value1` und `value2` sind numerische Werte.

Eure Aufgabe ist ein kleines Kommandozeilenprogramm, das daraus einen **Scatter Plot direkt im Terminal** erzeugt.

Beispielidee:

```text
ASCII Scatter Plot

  10 |                           C
   9 |
   8 |      A
   7 |
   6 |           B
   5 |
   4 |
   3 |
   2 |                                D
   1 |
   0 +----------------------------------------
      0                                  10

Legend: A  B  C  D
```

Die Punkte sollen mit [`rich`](https://rich.readthedocs.io/) farbig dargestellt werden.

---

# 2. Was hier bewertet / automatisch geprüft wird

Am Ende soll euer Repository insbesondere zeigen:

- ein eigenes `uv`-Projekt,
- eine lokale `.venv`,
- eine sinnvolle `.gitignore`,
- ein `pyproject.toml`,
- ein committed `uv.lock`,
- `rich` als deklarierte Abhängigkeit,
- eine `src/`-Projektstruktur,
- ein richtiges Python-Package mit `__init__.py`,
- mehrere Module mit Imports untereinander,
- ein ausführbares Gesamtprogramm,
- Git-Commits **von beiden Teammitgliedern**,
- Arbeit über Branches, Push/Pull und Pull Requests.

Die bereitgestellte GitHub Action gibt euch automatisch Feedback zu einem großen Teil dieser Punkte.

> Die CI ist heute nur euer **automatischer Projekt-Checker**. Wie GitHub Actions intern funktioniert, behandeln wir erst später.

---

# 3. Starter-Repository

Ihr startet von einem bereitgestellten Repository.

Es enthält bereits:

```text
ascii-scatter-starter/
├── .github/
│   └── workflows/
│       └── project-check.yml
├── data/
│   └── points.csv
├── resources/
│   └── README_HINTS.md
└── README.md
```

Es enthält absichtlich **noch nicht**:

```text
pyproject.toml
uv.lock
.gitignore
src/
```

Diese Projektstruktur erstellt ihr selbst.

**Die Dateien unter `.github/` sollen nicht verändert werden.**

---

# 4. Zielstruktur

Am Ende soll euer Repository ungefähr so aussehen:

```text
ascii-scatter-project/
├── .github/
│   └── workflows/
│       └── project-check.yml
├── .gitignore
├── README.md
├── pyproject.toml
├── uv.lock
├── data/
│   └── points.csv
├── resources/
│   └── README_HINTS.md
└── src/
    └── ascii_plotter/
        ├── __init__.py
        ├── io.py
        ├── plot.py
        └── cli.py
```

Je nach installierter `uv`-Version koennen ausserdem automatisch Dateien wie
`.python-version` und `src/ascii_plotter/py.typed` entstehen. Diese sind in Ordnung
und muessen nicht entfernt werden.

Optional später:

```text
tests/
```

Das kommt allerdings erst in der nächsten Veranstaltung.

---

# 5. Git-Regel für dieses Praktikum

Ihr arbeitet **zu zweit an einem gemeinsamen Remote-Repository**.

Beide Personen müssen:

- das Repository selbst lokal klonen,
- mindestens einen eigenen Branch erstellen,
- eigene Python-Code-Commits erzeugen,
- den Branch pushen,
- mindestens einmal neue Änderungen vom Remote holen,
- mindestens einen Pull Request erstellen oder reviewen.

Am Ende müssen also im Git-Verlauf **Beiträge von beiden Personen** sichtbar sein.

---

# 6. Ablaufplan

| Phase | Aufgabe |
|---:|---|
| 1 | Repository gemeinsam einrichten und lokal klonen |
| 2 | Projektstruktur + `uv` + `.gitignore` aufsetzen |
| 3 | Parallel: CSV-Import und Plot-Rendering |
| 4 | Pull Requests, Review, Merge, `git pull` |
| 5 | Module verbinden und Programm ausführen |
| 6 | CI grün bekommen + Repository kontrollieren |

---

# Phase A – Gemeinsames Repository vorbereiten

## 7. Beide Personen klonen das Repository

Beide Teammitglieder arbeiten auf ihrem **eigenen Rechner / in ihrem eigenen lokalen Clone**.

```bash
git clone <URL-DES-TEAM-REPOSITORIES>
cd <repository>
```

Überprüfen:

```bash
git status
git remote -v
```

Beide Personen sollten dasselbe `origin` sehen.

---

# Phase B – Projektstruktur aufsetzen

## 8. Setup-Branch

Eine Person übernimmt zunächst den Driver, die andere Person schaut mit und kontrolliert.

```bash
git switch -c setup/python-project
```

Initialisiert im vorhandenen Repository ein `uv`-Projekt.

Empfehlung:

```bash
uv init --lib --name ascii-plotter
```

Damit soll direkt ein Package unter

```text
src/ascii_plotter/
```

entstehen. Kontrolliert die erzeugte Struktur und öffnet anschließend kurz `pyproject.toml`.

## 8.1 Environment erzeugen

```bash
uv venv
```

## 8.2 Dependency hinzufügen

```bash
uv add rich
```

Prüft:

```bash
uv run python -c "import rich; print('rich import works')"
```

## 8.3 `.gitignore`

Mindestens:

```gitignore
.venv/
__pycache__/
*.py[cod]
.pytest_cache/
.ruff_cache/
.DS_Store
```

Kontrolle:

```bash
git status
```

**Die `.venv/` darf nicht als untracked content erscheinen.**

Optional:

```bash
git check-ignore -v .venv/
```

## 8.4 Setup committen

```bash
git add .
git commit -m "Set up uv project structure"
git push -u origin setup/python-project
```

Erstellt einen Pull Request.

Die zweite Person reviewt kurz:

- existiert `.gitignore`?
- ist `.venv/` ignoriert?
- existiert `pyproject.toml`?
- ist `rich` dort als Dependency vorhanden?
- existiert `uv.lock`?
- existiert `src/ascii_plotter/__init__.py`?

Danach Setup-PR mergen.

---

# 9. Beide synchronisieren ihren lokalen Stand

Jetzt **beide Personen**:

```bash
git switch main
git pull
```

Das ist wichtig: Euer lokales Repository kennt den gemergten Setup-Code erst nach dem Pull.

Optional prüfen:

```bash
git log --oneline --graph --all
```

---

# Phase C – Arbeit aufteilen

Jetzt arbeitet ihr parallel.

## Person A: CSV-Import

Branch:

```bash
git switch -c feature/csv-loader
```

Datei:

```text
src/ascii_plotter/io.py
```

Implementiert:

```python
def load_points(path):
    ...
```

Die Funktion soll die CSV-Datei lesen und die Daten in einer einfachen Python-Struktur zurückgeben.

Eine mögliche Struktur ist:

```python
[
    ("A", 1.2, 7.8),
    ("B", 2.7, 5.1),
    ...
]
```

### Hilfscode für CSV

Ihr dürft die Standardbibliothek `csv` verwenden:

```python
import csv


def load_points(path):
    points = []

    with open(path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            point_type = row["type"]
            x = float(row["value1"])
            y = float(row["value2"])
            points.append((point_type, x, y))

    return points
```

Ihr dürft diesen Code übernehmen und sinnvoll verbessern.

Mindestens prüfen:

- Kategorien A–D funktionieren,
- `value1` und `value2` werden zu Zahlen,
- mehrere Zeilen werden eingelesen.

Commit + Push:

```bash
git add src/ascii_plotter/io.py
git commit -m "Add CSV point loader"
git push -u origin feature/csv-loader
```

---

# Person B: ASCII Plot

Branch:

```bash
git switch -c feature/ascii-plot
```

Datei:

```text
src/ascii_plotter/plot.py
```

Implementiert:

```python
def render_scatter(points, width=40, height=15):
    ...
```

Ihr müsst **nicht** alles selbst erfinden.

## 10. Koordinaten auf Terminalgröße skalieren

Hilfsfunktion:

```python
def scale(value, minimum, maximum, size):
    if maximum == minimum:
        return 0

    relative = (value - minimum) / (maximum - minimum)
    return round(relative * (size - 1))
```

Beispiel:

```text
Originalwerte x: 1.2 ... 9.8

werden abgebildet auf:

Terminalspalten: 0 ... 39
```

Für y gilt dasselbe.

Achtung: Terminalzeilen laufen von **oben nach unten**. Für einen klassischen Plot muss die y-Position deshalb beim Rendern umgedreht werden.

---

# 11. Grid erzeugen

Eine einfache Darstellung:

```python
grid = [
    [" " for _ in range(width)]
    for _ in range(height)
]
```

Dann für jeden Datenpunkt:

```python
x_pos = scale(x, min_x, max_x, width)
y_pos = scale(y, min_y, max_y, height)

row = height - 1 - y_pos

grid[row][x_pos] = point_type
```

---

# 12. Farben mit Rich

Ihr könnt beispielsweise verwenden:

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
```

Eine Zeile des Plots kann als `Text` aufgebaut werden:

```python
line = Text()

for symbol in row:
    if symbol in STYLES:
        line.append(symbol, style=STYLES[symbol])
    else:
        line.append(symbol)

console.print(line)
```

Rich kann Strings und `Text`-Objekte farbig im Terminal ausgeben.

Commit + Push:

```bash
git add src/ascii_plotter/plot.py
git commit -m "Add terminal scatter renderer"
git push -u origin feature/ascii-plot
```

---

# Phase D – Pull Requests und Integration

## 13. Beide erstellen einen Pull Request

Es sollten jetzt mindestens existieren:

```text
PR 1: feature/csv-loader
PR 2: feature/ascii-plot
```

Reviewt gegenseitig den PR der anderen Person.

Kurze Review-Fragen:

- Sind Funktions- und Variablennamen verständlich?
- Liegt der Code im richtigen Modul?
- Gibt es offensichtliche unnötige Duplikation?
- Importiert das Modul nur Dinge, die es wirklich benötigt?
- Ist der Code ohne großen Kontext nachvollziehbar?

Merge zunächst **einen** der beiden PRs.

---

# 14. Nach einem Merge: lokalen Stand aktualisieren

Die andere Person sollte jetzt erleben, dass auf GitHub Änderungen existieren, die im eigenen Clone noch fehlen.

```bash
git switch main
git pull
```

Zurück zum eigenen Branch:

```bash
git switch feature/ascii-plot
```

bzw.:

```bash
git switch feature/csv-loader
```

Den aktuellen `main` integrieren:

```bash
git merge main
```

Danach:

```bash
git push
```

Damit wird der Pull Request aktualisiert.

Jetzt zweiten PR mergen.

---

# Phase E – Module miteinander verbinden

## 15. `cli.py`

Nach beiden Merges:

```bash
git switch main
git pull
```

Erstellt einen letzten kleinen Integrationsbranch:

```bash
git switch -c feature/cli
```

Datei:

```text
src/ascii_plotter/cli.py
```

Minimalvariante:

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

    points = load_points(csv_path)
    render_scatter(points)


if __name__ == "__main__":
    main()
```

Hier sind besonders wichtig:

```python
from .io import load_points
from .plot import render_scatter
```

Das sind **relative Imports innerhalb eures Packages**.

---

# 16. Programm ausführen

Vom Repository-Root:

```bash
uv run python -m ascii_plotter.cli data/points.csv
```

Nicht bevorzugt:

```bash
python src/ascii_plotter/cli.py
```

Bei relativen Imports verliert Python bei direkter Dateiausführung leicht den Package-Kontext.

---

# 17. Commit und letzter PR

Die Person, die den Integrationsbranch erstellt, committed `cli.py`.

Die andere Person reviewt den PR.

```bash
git add src/ascii_plotter/cli.py
git commit -m "Connect loader and scatter plot CLI"
git push -u origin feature/cli
```

Danach PR → Review → Merge.

---

# 18. CI kontrollieren

Auf GitHub sollte die bereitgestellte Action automatisch laufen.

Sie gibt Feedback zu Punkten wie:

```text
✅ pyproject.toml exists
✅ uv.lock exists
✅ rich declared as dependency
✅ .gitignore exists
✅ .venv is ignored
✅ src/ascii_plotter/__init__.py exists
✅ expected modules exist
✅ project can be synchronized with uv
✅ ascii_plotter can be imported
✅ CLI can process the provided CSV file
✅ commits from at least two contributors exist
```

Wenn etwas rot ist:

1. Fehlermeldung lesen.
2. Lokal korrigieren.
3. Commit erstellen.
4. Pushen.
5. CI erneut beobachten.

Ihr müsst die Workflow-Datei **nicht** verändern.

---

# 19. Definition of Done

Euer Praktikum ist abgeschlossen, wenn:

- [ ] beide Teammitglieder lokal am Projekt gearbeitet haben,
- [ ] beide Teammitglieder eigene Python-Code-Commits haben,
- [ ] Branches und Pull Requests verwendet wurden,
- [ ] mindestens einmal `git pull` benutzt wurde, um Änderungen des Partners zu holen,
- [ ] `.venv/` lokal existieren darf, aber nicht von Git getrackt wird,
- [ ] `pyproject.toml` vorhanden ist,
- [ ] `rich` als Dependency eingetragen ist,
- [ ] `uv.lock` committed ist,
- [ ] `src/ascii_plotter/__init__.py` existiert,
- [ ] `io.py`, `plot.py` und `cli.py` existieren,
- [ ] relative Imports zwischen den Modulen verwendet werden,
- [ ] `uv run python -m ascii_plotter.cli data/points.csv` funktioniert,
- [ ] die GitHub-CI grün ist.

---

# 20. Wenn ihr früher fertig seid

## Bonus A – schönere Legende

Gebt mit Rich eine farbige Legende aus:

```text
A = cyan
B = magenta
C = green
D = yellow
```

## Bonus B – Achsen

Ergänzt einfache x-/y-Achsen oder Min-/Max-Werte.

## Bonus C – CLI Entry Point

Recherchiert `[project.scripts]` in `pyproject.toml` und richtet ein Kommando ein, sodass anschließend z. B. funktioniert:

```bash
uv run ascii-scatter data/points.csv
```

## Bonus D – mehrere Datensätze

Legt eine zweite CSV-Datei an und prüft, ob euer Programm ohne Codeänderung damit funktioniert.

---

# 21. Abschlussfragen

Besprecht kurz im Zweierteam:

1. Welche Dateien eures Projekts sind **lokal**, welche gehören ins Repository?
2. Warum committen wir `uv.lock`, aber nicht `.venv/`?
3. Welche Aufgabe hat `pyproject.toml`?
4. Wozu dient `__init__.py`?
5. Warum teilen wir `io.py`, `plot.py` und `cli.py` auf?
6. Was bedeutet der Punkt in `from .io import load_points`?
7. Was musste passieren, damit der Code eures Partners auf eurem Rechner auftauchte?

