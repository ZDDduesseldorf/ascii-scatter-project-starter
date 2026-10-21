from rich.console import Console
from rich.text import Text


STYLES = {
    "A": "bold cyan",
    "B": "bold magenta",
    "C": "bold green",
    "D": "bold yellow",
}

console = Console()

points = [
    ("A", 1.2, 7.8),
    ("B", 2.7, 5.1),
    ("C", 4.8, 8.4),
    ("D", 8.2, 2.0),
]

def scale(value, minimum, maximum, size):
    if maximum == minimum:
        return 0

    relative = (value - minimum) / (maximum - minimum)
    return round(relative * (size - 1))


def render_scatter(points, width=40, height=15):
    grid = [["   " for _ in range(width)] for _ in range(height)]

    min_x = min(point[1] for point in points)
    min_y = min(point[2] for point in points)

    max_x = max(point[1] for point in points)
    max_y = max(point[2] for point in points)

    line = Text()

    for p in points:
        label, x, y = p

        x_pos = scale(x, min_x, max_x, width)
        y_pos = scale(y, min_y, max_y, height)

        row = height - 1 - y_pos

        grid[row][x_pos] = label

    max_char_row = len(str(len(grid)))

    for i, row in enumerate(grid):
        line.append(f"{len(grid) - i:>{max_char_row}}|")
        for symbol in row:
            if symbol in STYLES:
                line.append(symbol, style=STYLES[symbol])
            else:
                line.append(symbol)

        line.append("\n")
    line.append("0 +" + round(max_y) * "-" * 5)
    line.append("\n")
    line.append("   0\n")
    line.append("Legend: A B C D")
    console.print(line, )


if __name__ == "__main__":
    render_scatter(points, 10, 10)
