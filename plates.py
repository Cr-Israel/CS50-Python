def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not (2 <= len(s) <= 6):
        return False

    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    num_started = False
    for i in range(len(s)):
        if s[i].isdigit():
            if not num_started:
                if s[i] == "0":
                    return False
                num_started = True
        elif num_started:
            return False

    if not s.isalnum():
        return False

    return True


if __name__ == "__main__":
    main()
