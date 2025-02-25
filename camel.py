def main():
    camel_case = input("camelCase: ").strip()
    snake_case = add_spaces(camel_case).lower().replace(" ", "_")
    print(f"snake_case: {snake_case}")


def add_spaces(text):
    new_text = ""
    for char in text:
        if char.isupper() and new_text:
            new_text += " "
        new_text += char
    return new_text


if __name__ == "__main__":
    main()
