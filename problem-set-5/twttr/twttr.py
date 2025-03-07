def main():
    setence = shorten(input("Input: ").strip())
    print(f"Output: {setence}")


def shorten(word):
    vowels = "aeiouAEIOU"
    for vowel in vowels:
        word = word.replace(vowel, "")
    return word


if __name__ == "__main__":
    main()
