def load_data(file: str) -> list[str]:
    with open(file) as f:
        return list(map(lambda x: x.replace("\n", ""), f.readlines()))
    
def list_transformer(row: list[str]) -> list[list[str]]:
    return [[x for x in item] for item in row]


