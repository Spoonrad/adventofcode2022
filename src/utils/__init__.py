from pathlib import Path

def read_day_input_file(day: int) -> str:

    path = str(Path().resolve().parent) + f'/day_{day}/input.txt'
    return read_file(path)

def read_file(path: str) -> str:
    with open(path, encoding='utf-8') as file:
        text = file.read()
    return text

###

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

