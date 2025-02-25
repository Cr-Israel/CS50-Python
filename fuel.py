def get_fraction():
    while True:
        try:
            fraction = input("Fraction: ")
            x, y = fraction.split("/")
            x, y = int(x), int(y)
            if y == 0:
                raise ZeroDivisionError
            if x > y:
                raise ValueError
            return x / y
        except (ValueError, ZeroDivisionError):
            pass


def main():
    fraction = get_fraction()
    percentage = round(fraction * 100)

    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")


if __name__ == "__main__":
    main()
