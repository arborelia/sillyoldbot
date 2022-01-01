from pathlib import Path

BASE_PATH = Path(__file__).absolute().parent.parent


def data_path(filename):
    return BASE_PATH / "data" / filename
