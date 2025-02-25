def main():
    setence = twttr(input("Input: "))
    print(f"Output: {setence}")


# vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
vowels = "aeiouAEIOU"


def twttr(text):
    for vowel in vowels:
        text = text.replace(vowel, "")
    return text


if __name__ == "__main__":
    main()
