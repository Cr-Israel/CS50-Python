import sys

for arg in sys.argv[1:]:
    try:
        lines = open(arg, "r").readlines()
        print(lines)
    except FileNotFoundError:
        raise FileNotFoundError("File does not exist")
