def main():
    get_input()


def get_input():
    entri = input()
    return set_lowercase(entri)


def set_lowercase(entri):
    entri_lower = entri.lower()
    print(entri_lower)


main()
