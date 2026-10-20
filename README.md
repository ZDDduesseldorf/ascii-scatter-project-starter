# Praktikum: Vom CSV-Datensatz zum sauberen Python-Projekt

## ASCII Scatter Plot im Terminal

**Teamgröße:** 2 Personen  
**Werkzeuge:** VS Code, Git/GitHub, `uv`, Python, `rich`  
**Schwerpunkt:** Environment, Dependencies, `pyproject.toml`, `.gitignore`, `src`-Layout, Packages/Module, relative Imports und Team-Workflow

> **Wichtig:** In diesem Praktikum geht es **nicht primär darum, einen schwierigen Plot-Algorithmus zu erfinden**. Die eigentliche Aufgabe ist, aus einer kleinen Programmieridee ein **sauber strukturiertes, reproduzierbares Python-Projekt** zu machen.

---

# Szenario

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

# Was heute gelernt werden soll

Am Ende sollt ihr erklären können:

- warum jedes Projekt ein eigenes Environment haben sollte,
- was `.venv` enthält und warum es **nicht** ins Repository gehört,
- welche Rolle `pyproject.toml` spielt,
- warum `uv.lock` committed wird,
- warum wir unseren Python-Code unter `src/` organisieren,
- was ein Python-Package ist,
- wozu `__init__.py` dient,
- wie Module innerhalb eines Packages voneinander importieren,
- warum wir das Programm mit `python -m ...` ausführen,
- wie zwei Personen über Branches, Commits, Push/Pull und Pull Requests zusammenarbeiten,
- wie VS Code euch beim Git-Workflow unterstützt, ohne dass Git dadurch „verschwindet“.

Die bereitgestellte GitHub Action prüft automatisch einen großen Teil dieser Punkte.

> Die CI ist heute nur euer **automatischer Projekt-Checker**. Wie GitHub Actions intern funktioniert, behandeln wir erst später.

---

# Starter-Repository

Ihr startet von einem bereitgestellten Repository.

Es enthält bereits:

```text
ascii-scatter-project-starter/
├── .ci/
│   └── check_project.py
├── .github/
│   └── workflows/
│       └── project-check.yml
├── data/
│   └── points.csv
├── resources/
│   ├── README_HINTS.md
│   └── VSCode_Git_Workflow.md
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

**Die Dateien unter `.ci/` und `.github/` sollen nicht verändert werden.**

---

# Zielstruktur

Am Ende soll euer Repository ungefähr so aussehen:

```text
ascii-scatter-project/
├── .ci/
│   └── check_project.py
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
│   ├── HINTS.md
│   └── VSCode_Git_Workflow.md
└── src/
    └── ascii_plotter/
        ├── __init__.py
        ├── io.py
        ├── plot.py
        └── cli.py
```

Je nach installierter `uv`-Version können außerdem automatisch Dateien wie
`.python-version` und `src/ascii_plotter/py.typed` entstehen. Diese sind in Ordnung und müssen nicht entfernt werden.

Optional später:

```text
tests/
```

Das kommt allerdings erst in der nächsten Veranstaltung.

---

# Git-Regel für dieses Praktikum

Ihr arbeitet **zu zweit an einem gemeinsamen Remote-Repository**.

Beide Personen müssen:

- das Repository selbst lokal in VS Code klonen,
- mindestens einen eigenen Branch erstellen,
- eigene Python-Code-Commits erzeugen,
- den eigenen Branch pushen,
- mindestens einmal Änderungen vom Remote holen,
- mindestens einen Pull Request erstellen oder reviewen.

Am Ende müssen im Git-Verlauf **Beiträge von beiden Personen** sichtbar sein.

> Ab dieser Veranstaltung verwenden wir für den normalen Git-Alltag primär die **Source-Control-Oberfläche von VS Code**. Die Git-Kommandos stehen weiterhin als Hinweise dabei, weil VS Code intern genau diese Git-Operationen ausführt und die Kommandozeile für Diagnose und Verständnis weiterhin wichtig ist.

---

# Ablaufplan

| Phase |      Aufgabe                                        |
| ----: | --------------------------------------------------- |
|     A | Repository klonen und in VS Code öffnen             |
|     B | Projektstruktur + `uv` + `.gitignore` aufsetzen     |
|     C | Schnittstellen festlegen und Arbeit aufteilen       |
|     D | Parallel: CSV-Import und Plot-Rendering             |
|     E | Pull Requests, Review und Integration               |
|     F | CLI verbinden, CI grün bekommen, Abschlusskontrolle |

---

# Phase A – Team-Repository in VS Code öffnen

## 0. Auf EIN gemeinsames Remote Repository einigen!

Gemeinsames Team-Repository erstellen
Ihr arbeitet zu zweit, benötigt aber ein gemeinsames Remote-Repository, auf das beide schreiben können.

Person A
1. Öffnet das bereitgestellte Starter-Repository auf GitHub.
2. Klickt auf Fork und erstellt einen Fork im eigenen GitHub-Account.
3. Öffnet im neuen Fork Settings → Collaborators → Add people.
4. Fügt Person B über den GitHub-Benutzernamen als Collaborator hinzu.
Person B
5. Akzeptiert die GitHub-Einladung.
Danach verwenden beide Personen den Fork von Person A als gemeinsames Team-Repository.

Beide öffnen in VS Code:

Command Palette → Git: Clone

und klonen dieselbe URL, zum Beispiel:
```bash
https://github.com/alice/ascii-scatter-project-starter.git
```

Danach öffnen beide den geklonten Ordner in VS Code.

Kontrolliert gemeinsam auf GitHub, dass ihr wirklich im selben Fork arbeitet.

Ab jetzt gilt:
gemeinsamer Fork auf GitHub = Remote-Repository des Teams
eigener Rechner            = eigener lokaler Clone

Beide arbeiten lokal in ihrem eigenen Clone. Änderungen werden erst durch Commit + Push zum gemeinsamen GitHub-Repository übertragen. Änderungen der anderen Person erscheinen erst nach Pull im eigenen lokalen Clone.


## 1. Beide Personen klonen das Repository

Beide Teammitglieder arbeiten auf ihrem **eigenen Rechner / in ihrem eigenen lokalen Clone**.

### In VS Code

1. VS Code öffnen.
2. `Ctrl+Shift+P` unter Windows/Linux bzw. `Cmd+Shift+P` unter macOS drücken.
3. **Git: Clone** auswählen.
4. Die URL eures gemeinsamen Team-Repositories einfügen.
5. Einen lokalen Zielordner auswählen.
6. Nach dem Clone **Open** / **Open Repository** wählen.
7. Unten links kontrollieren, dass ihr auf Branch `main` seid.

Öffnet anschließend das integrierte Terminal über:

**Terminal → New Terminal**

Ein sinnvoller Kontrollbefehl ist:

```bash
git status
```

> **Terminal-Hinweis:** Das Klonen ginge auch mit `git clone <URL>`. Ab jetzt arbeiten wir aber primär über VS Code Source Control.

### Optional: Python-Extension

Falls ihr die Python-Extension für VS Code installiert habt, könnt ihr später den Interpreter eures `.venv` auswählen:

1. `Ctrl/Cmd+Shift+P`
2. **Python: Select Interpreter**
3. Interpreter aus `.venv` auswählen

---

# Phase B – Projektstruktur aufsetzen

## 2. Setup-Branch anlegen

**Person A** übernimmt zunächst den Setup-Branch. Person B schaut mit und kontrolliert die entstehenden Dateien.

### In VS Code

1. Unten links auf den aktuellen Branchnamen `main` klicken.
2. **Create new branch...** auswählen.
3. Branch nennen:

```text
setup/python-project
```

Alternativ über die Command Palette:

**Git: Create Branch**

> Terminal-Hinweis: `git switch -c setup/python-project`

---

## 3. uv-Projekt initialisieren

Im integrierten VS-Code-Terminal:

```bash
uv init --lib --name ascii-plotter
```

Kontrolliert anschließend im Explorer links die neu erzeugte Struktur.

Insbesondere sollte ein Package unter

```text
src/ascii_plotter/
```

entstanden sein.

Öffnet gemeinsam `pyproject.toml` und schaut euch die wichtigsten Einträge an.

---

## 4. Environment erzeugen

Im VS-Code-Terminal:

```bash
uv venv
```

Danach sollte im Projektordner entstehen:

```text
.venv/
```

Frage:

> Ist `.venv` Quellcode? Sollte dieser Ordner wirklich über Git mit anderen geteilt werden?

Falls ihr die Python-Extension nutzt, könnt ihr jetzt den Interpreter aus `.venv` auswählen.

---

## 5. Dependency hinzufügen

```bash
uv add rich
```

Kontrolliert danach:

- Was hat sich in `pyproject.toml` verändert?
- Ist `uv.lock` entstanden?
- Welche Dateien zeigt VS Code unter **Source Control → Changes** an?

Prüft außerdem:

```bash
uv run python -c "import rich; print('rich import works')"
```

---

## 6. `.gitignore`

Kontrolliert oder erstellt `.gitignore`.

Mindestens:

```gitignore
.venv/
__pycache__/
.pytest_cache/
.ruff_cache/
.DS_Store
```

### Kontrolle in VS Code

Öffnet links **Source Control** (`Ctrl/Cmd+Shift+G`).

Unter **Changes** darf `.venv/` **nicht** auftauchen.

Optional könnt ihr im Terminal zusätzlich kontrollieren:

```bash
git check-ignore -v .venv/
```

Frage:

> Warum committen wir `uv.lock`, aber nicht `.venv/`?

---

## 7. Setup über VS Code committen und pushen

Jetzt wird nicht primär über `git add` und `git commit` gearbeitet, sondern über VS Code.

### Source Control

1. Links **Source Control** öffnen (`Ctrl/Cmd+Shift+G`).
2. Unter **Changes** jede Datei kurz ansehen.
3. Eine Datei anklicken, um den Diff zu sehen.
4. Prüfen: `.venv` darf nicht auftauchen.
5. Mit dem `+` neben einer Datei die gewünschten Änderungen **stagen**.
6. Alternativ `+` neben **Changes**, um alle sinnvollen Änderungen zu stagen.
7. Oben Commit-Nachricht eingeben:

```text
Set up uv Python project
```

8. **Commit** klicken.
9. Danach **Publish Branch** bzw. **Push** klicken.

> Terminal-Hinweis: Dies entspricht ungefähr `git add ...`, `git commit -m "Set up uv Python project"` und `git push -u origin setup/python-project`.

---

## 8. Setup-Pull-Request

Auf GitHub im Browser:

1. Repository öffnen.
2. **Compare & pull request** auswählen.
3. Kontrollieren:
   - Base: `main`
   - Compare: `setup/python-project`
4. Pull Request erstellen.

### Person B reviewt

Person B prüft insbesondere:

- existiert `.gitignore`?
- ist `.venv/` ignoriert?
- existiert `pyproject.toml`?
- ist `rich` als Dependency vorhanden?
- existiert `uv.lock`?
- existiert `src/ascii_plotter/__init__.py`?

Danach Setup-PR mergen.

---

## 9. Beide lokalen Clones synchronisieren

Ein Merge auf GitHub verändert euren lokalen Clone **nicht automatisch**.

Deshalb jetzt bei **beiden Personen**:

### In VS Code

1. Unten links auf den Branchnamen klicken.
2. `main` auswählen.
3. Source Control öffnen.
4. `...` → **Pull** auswählen.

Je nach VS-Code-Version kann auch **Sync Changes** angeboten werden.

> Terminal-Hinweis: `git switch main` und anschließend `git pull`.

Das ist wichtig: Euer lokales Repository kennt den gemergten Setup-Code erst nach dem Pull.

Optional zur Kontrolle:

```bash
git log --oneline --graph --all
```

---

# Phase C – Erst Schnittstellen festlegen

## 10. Bevor ihr parallel arbeitet

Bevor Person A und Person B unterschiedliche Branches öffnen, einigt ihr euch kurz auf die Funktionen, die später miteinander verbunden werden.

### CSV-Seite

```python
def load_points(path):
    ...
```

Rückgabe zum Beispiel:

```python
[
    ("A", 1.2, 7.8),
    ("B", 2.7, 5.1),
    ...
]
```

### Plot-Seite

```python
def render_scatter(points, width=40, height=15):
    ...
```

Damit kann Person B den Plot bereits mit selbst erzeugten Beispieldaten entwickeln, ohne darauf warten zu müssen, dass `io.py` fertig ist.

> **Software-Engineering-Idee:** Eine vereinbarte Schnittstelle ermöglicht parallele Arbeit.

---

# Phase D – Parallele Arbeit

# 11. Person A: CSV-Import

## Eigenen Branch erstellen

### In VS Code

1. Prüfen, dass ihr auf aktuellem `main` seid.
2. Unten links auf `main` klicken.
3. **Create new branch...**
4. Branch nennen:

```text
feature/csv-loader
```

> Terminal-Hinweis: `git switch -c feature/csv-loader`

### Datei

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

## Hilfscode für CSV

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

### Kurze lokale Kontrolle

Ihr könnt vorübergehend im VS-Code-Terminal ausprobieren:

```bash
uv run python -c "from ascii_plotter.io import load_points; print(load_points('data/points.csv')[:3])"
```

## Commit + Push über VS Code

1. Source Control öffnen.
2. `io.py` anklicken und Diff ansehen.
3. `io.py` stagen.
4. Commit-Nachricht:

```text
Add CSV point loader
```

5. **Commit**.
6. **Publish Branch** / **Push**.

> Terminal-Hinweis: `git add src/ascii_plotter/io.py`, `git commit -m "Add CSV point loader"`, `git push -u origin feature/csv-loader`.

---

# 12. Person B: ASCII Scatter Plot

## Eigenen Branch erstellen

### In VS Code

1. Prüfen, dass ihr auf aktuellem `main` seid.
2. Unten links auf `main` klicken.
3. **Create new branch...**
4. Branch nennen:

```text
feature/ascii-plot
```

> Terminal-Hinweis: `git switch -c feature/ascii-plot`

### Datei

```text
src/ascii_plotter/plot.py
```

Implementiert:

```python
def render_scatter(points, width=40, height=15):
    ...
```

Ihr müsst **nicht** alles selbst erfinden.

Zum Entwickeln könnt ihr zunächst feste Beispieldaten benutzen:

```python
points = [
    ("A", 1.2, 7.8),
    ("B", 2.7, 5.1),
    ("C", 4.8, 8.4),
    ("D", 8.2, 2.0),
]
```

Damit seid ihr unabhängig vom CSV-Loader von Person A.

---

# 13. Koordinaten auf Terminalgröße skalieren

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

# 14. Grid erzeugen

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

Falls zwei Punkte zufällig auf dieselbe Terminalposition fallen, dürft ihr z. B. `*` verwenden.

---

# 15. Farben mit Rich

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

## Commit + Push über VS Code

1. Source Control öffnen.
2. `plot.py` anklicken und Diff ansehen.
3. Datei stagen.
4. Commit-Nachricht:

```text
Add terminal scatter renderer
```

5. **Commit**.
6. **Publish Branch** / **Push**.

> Terminal-Hinweis: `git add src/ascii_plotter/plot.py`, `git commit -m "Add terminal scatter renderer"`, `git push -u origin feature/ascii-plot`.

---

# Phase E – Pull Requests und Integration

## 16. Beide erstellen einen Pull Request

Auf GitHub sollten jetzt mindestens existieren:

```text
PR 1: feature/csv-loader
PR 2: feature/ascii-plot
```

Jede Person:

1. eigenen Branch pushen,
2. GitHub im Browser öffnen,
3. **Compare & pull request**,
4. Zielbranch `main` kontrollieren,
5. PR erstellen.

---

## 17. Gegenseitiges Review

Reviewt den PR der jeweils anderen Person.

Kurze Review-Fragen:

- Sind Funktions- und Variablennamen verständlich?
- Liegt der Code im richtigen Modul?
- Gibt es offensichtliche unnötige Duplikation?
- Importiert das Modul nur Dinge, die es wirklich benötigt?
- Ist der Code ohne großen Kontext nachvollziehbar?
- Entspricht die Funktion der vereinbarten Schnittstelle?

Merge zunächst **einen** der beiden PRs.

---

## 18. Nach einem Merge: lokalen Stand aktualisieren

Jetzt existiert auf GitHub Code, den die andere Person lokal noch nicht hat.

### In VS Code

1. Auf `main` wechseln.
2. Source Control → `...` → **Pull**.
3. Kontrollieren, dass die Datei des Partners / der Partnerin jetzt im Explorer sichtbar ist.

> Terminal-Hinweis: `git switch main` + `git pull`.

### Eigenen Feature-Branch aktualisieren

Falls euer eigener PR noch offen ist:

1. wieder auf den eigenen Feature-Branch wechseln,
2. `Ctrl/Cmd+Shift+P`,
3. **Git: Merge Branch...** auswählen,
4. `main` auswählen,
5. eventuelle Konflikte in VS Code lösen,
6. falls nötig Merge-Commit erstellen,
7. **Push** / **Sync Changes**.

> Terminal-Hinweis: Auf dem Feature-Branch wäre die entsprechende Operation `git merge main`.

Damit wird euer offener Pull Request aktualisiert.

Danach zweiten PR mergen.

---

# Phase F – Module miteinander verbinden

## 19. Nach beiden Merges synchronisieren

Bei beiden Personen:

1. auf `main` wechseln,
2. **Pull**.

Jetzt sollten sowohl

```text
io.py
```

als auch

```text
plot.py
```

lokal vorhanden sein.

---

## 20. Integrationsbranch `feature/cli`

Eine Person übernimmt den kleinen Integrationsbranch. Sinnvoll ist hier die Person, die bisher weniger Integrationsarbeit hatte.

### In VS Code

1. auf aktuellem `main` sein,
2. Branch-Menü unten links,
3. **Create new branch...**,
4. Name:

```text
feature/cli
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

# 21. Programm ausführen

Vom Repository-Root im VS-Code-Terminal:

```bash
uv run python -m ascii_plotter.cli data/points.csv
```

Nicht bevorzugt:

```bash
python src/ascii_plotter/cli.py
```

Warum?

Bei relativen Imports verliert Python bei direkter Dateiausführung leicht den Package-Kontext.

Das `-m` bedeutet vereinfacht:

> Starte dieses Modul **als Teil des Packages**.

---

# 22. CLI committen und PR erstellen

### In VS Code

1. Source Control öffnen.
2. Diff von `cli.py` ansehen.
3. Datei stagen.
4. Commit-Nachricht:

```text
Connect loader and scatter plot CLI
```

5. **Commit**.
6. **Publish Branch** / **Push**.

Danach auf GitHub:

1. Pull Request erstellen,
2. andere Person reviewt,
3. PR mergen.

> Terminal-Hinweis: Entspricht `git add ...`, `git commit ...`, `git push -u origin feature/cli`.

---

# 23. Finalen Stand lokal holen

Nach dem letzten Merge bei **beiden Personen**:

1. auf `main` wechseln,
2. **Pull**.

Dann lokal ausführen:

```bash
uv run python -m ascii_plotter.cli data/points.csv
```

Beide lokalen Clones sollten jetzt denselben Programmstand besitzen.

---

# 24. CI kontrollieren

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

1. Fehlermeldung auf GitHub lesen.
2. Lokal in VS Code korrigieren.
3. Source Control öffnen und Diff ansehen.
4. Änderung stagen.
5. Commit erstellen.
6. Pushen.
7. CI erneut beobachten.

Ihr müsst die Workflow-Datei **nicht** verändern.

---

# Was tun bei einem Merge Conflict?

Falls ihr beide dieselbe Datei verändert habt, kann VS Code einen Merge Conflict anzeigen.

Dann:

1. Source Control öffnen.
2. Unter **Merge Changes** die Konfliktdatei auswählen.
3. Den Merge Editor verwenden.
4. Bewusst entscheiden, welche Änderungen erhalten bleiben sollen.
5. Datei speichern.
6. Datei stagen.
7. Merge-Commit abschließen.

Mögliche Optionen heißen je nach VS-Code-Version zum Beispiel:

- **Accept Current**
- **Accept Incoming**
- **Accept Both**

Nicht einfach blind auf **Accept Both** klicken.

Kontrolliert im Zweifel zusätzlich:

```bash
git status
```

---

# Definition of Done

Euer Praktikum ist abgeschlossen, wenn:

- [ ] beide Teammitglieder das Repository selbst lokal in VS Code geklont haben,
- [ ] beide Teammitglieder eigene Python-Code-Commits haben,
- [ ] beide mindestens einen eigenen Branch verwendet haben,
- [ ] Pull Requests und Reviews verwendet wurden,
- [ ] mindestens einmal Änderungen über **Pull** / **Sync** vom Remote geholt wurden,
- [ ] `.venv/` lokal existieren darf, aber nicht von Git getrackt wird,
- [ ] `pyproject.toml` vorhanden ist,
- [ ] `rich` als Dependency eingetragen ist,
- [ ] `uv.lock` committed ist,
- [ ] `src/ascii_plotter/__init__.py` existiert,
- [ ] `io.py`, `plot.py` und `cli.py` existieren,
- [ ] relative Imports zwischen den Modulen verwendet werden,
- [ ] `uv run python -m ascii_plotter.cli data/points.csv` funktioniert,
- [ ] beide lokalen Clones nach einem finalen Pull auf demselben Stand sind,
- [ ] die GitHub-CI grün ist.

---

# Wenn ihr früher fertig seid

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

## Bonus C – Kollisionen

Falls zwei Punkte auf derselben Terminalzelle landen, zeigt statt eines Typs z. B. `*` an.

## Bonus D – CLI Entry Point

Recherchiert `[project.scripts]` in `pyproject.toml` und richtet ein Kommando ein, sodass anschließend z. B. funktioniert:

```bash
uv run ascii-scatter data/points.csv
```

## Bonus E – mehrere Datensätze

Legt eine zweite CSV-Datei an und prüft, ob euer Programm ohne Codeänderung damit funktioniert.

---

# Abschlussfragen

Besprecht kurz im Zweierteam:

1. Welche Dateien eures Projekts sind **lokal**, welche gehören ins Repository?
2. Warum committen wir `uv.lock`, aber nicht `.venv/`?
3. Welche Aufgabe hat `pyproject.toml`?
4. Wozu dient `__init__.py`?
5. Warum teilen wir `io.py`, `plot.py` und `cli.py` auf?
6. Was bedeutet der Punkt in `from .io import load_points`?
7. Warum starten wir das Programm mit `python -m ascii_plotter.cli`?
8. Was musste passieren, damit der Code eures Partners auf eurem Rechner auftauchte?
9. Was passiert technisch, wenn ihr in VS Code auf **Commit**, **Push** oder **Pull** klickt?
10. Warum sollte man auch bei einer GUI weiterhin ungefähr wissen, welche Git-Operation gerade durchgeführt wird?

---

# VS-Code-Git-Kurzroutine

Für dieses und die kommenden Praktika könnt ihr euch diese Routine merken:

```text
Branch erstellen
    ↓
Dateien bearbeiten
    ↓
Diff in Source Control ansehen
    ↓
Stage
    ↓
Commit
    ↓
Push / Publish Branch
    ↓
Pull Request + Review
    ↓
Merge auf GitHub
    ↓
main lokal aktualisieren (Pull)
```

Eine kompakte VS-Code-Git-Anleitung findet ihr zusätzlich unter:

```text
resources/VSCode_Git_Workflow.md
```