"""Dundie core module"""


def load(filepath):
    """Loads data from filepath and insert it into a database."""
    try:
        with open(filepath) as file_:
            for line in file_:
                print(line)
    except FileNotFoundError:
        print(
            f'It was not possible to locate the file "{filepath}". '
            f"Check the file path or the permissions over the file."
        )
