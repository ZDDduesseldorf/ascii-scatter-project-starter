import csv


def load_points(path):
    points = []

    with open(path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        muss_column = ["type", "value1", "value2"]


        for row in reader:
            #row = {'typewww': 'A', 'value1': '1.2', 'value2': '7.8'}
            if list(row.keys()) != muss_column:
                raise ValueError(f"Die CSV-Datei muss enthalten: {muss_column}")
            point_type = row["type"]
            x = float(row["value1"])
            y = float(row["value2"])
            points.append((point_type, x, y))

    return points