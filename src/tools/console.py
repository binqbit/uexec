
import shutil

columns, _ = shutil.get_terminal_size((80, 24))
columns -= 1
empty_line = " " * columns
one_line = "-" * columns
two_line = "=" * columns

def get_columns():
    return columns

def clear_line():
    print(empty_line, end="\r")

def print_one_line():
    print(one_line)

def print_two_line():
    print(two_line)