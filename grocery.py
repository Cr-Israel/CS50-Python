def main():
    grocery_list = {}

    while True:
        try:
            item = input().strip().upper()
            if item:
                grocery_list[item] = grocery_list.get(item, 0) + 1
        except EOFError:
            print()
            break

    for item in sorted(grocery_list):
        print(f"{grocery_list[item]} {item}")


if __name__ == "__main__":
    main()
