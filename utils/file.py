from pathlib import Path


def get_path(path):
    return (
        Path(__file__)
        .parent.parent.joinpath(path)
        .absolute()
        .__str__()
    )
