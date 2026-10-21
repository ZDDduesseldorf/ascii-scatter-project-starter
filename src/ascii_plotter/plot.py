from rich.console import Console
from rich.text import Text

points = [
    ("A", 1.2, 7.8),
    ("B", 2.7, 5.1),
    ("C", 4.8, 8.4),
    ("D", 8.2, 2.0),
]

STYLES = {
    "A": "bold cyan",
    "B": "bold magenta",
    "C": "bold green",
    "D": "bold yellow",
}

def render_scatter(point, width=40, height=15):
    console = Console()
    min_x = min_y = 0
    max_x = width
    max_y = height

    grid = [
    [" " for _ in range(width)]
    for _ in range(height)
    ]

    for i in point:
      point_type, x, y, = i
      x_pos = scale(x, min_x, max_x, width)
      y_pos = scale(y, min_y, max_y, height)

      row = height - 1 - y_pos

      grid[row][x_pos] = point_type

      line = Text()
    #print(grid)

    for row in grid:
        line.append('|')
        for symbol in row:
          
          if symbol in STYLES:
                  line.append((symbol), style=STYLES[symbol])
          else:
                  line.append(symbol)
        line.append('\n')
    line.append('-' * width)

    console.print(line)


def scale(value, minimum, maximum, size):
    if maximum == minimum:
        return 0

    relative = (value - minimum) / (maximum - minimum)
    return round(relative * (size - 1))

if __name__ == "__main__":
    render_scatter(points)