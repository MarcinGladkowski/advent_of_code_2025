def load_data(file: str) -> list[str]:
    with open(file) as f:
        return list(map(lambda x: x.replace("\n", ""), f.readlines()))