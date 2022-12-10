from utils import read_file

def read_day_input_file(day: int) -> str:
    path = f'day_{day}/input.txt'
    return read_file(path)
