def main():
    get_input()


def get_input():
    entri = input()
    entri_split = entri.split()
    set_str(entri_split)


def set_str(entri_split):
    entri_splited = "...".join(entri_split)
    print(entri_splited)


main()
