def main():
    getInput()


def getInput():
    text = input("Digite um texto: ")
    converted_text = convert(text)
    print(converted_text)


def convert(text):
    return text.replace(":)", "🙂").replace(":(", "🙁")


main()
