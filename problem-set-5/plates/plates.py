def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not (2 <= len(s) <= 6):
        return False

    if not s[:2].isalpha():
        return False

    num_started = False
    for char in s:
        if char.isdigit():
            if not num_started:
                if char == "0":
                    return False
                num_started = True
        elif num_started:
            return False

    return s.isalnum()


if __name__ == "__main__":
    main()
