name = input("What's your name? ")

match name:
    case "Harry" | "Ron" | "Hermione":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")

# _ é para qualquer entrada que não esteja dentro dos cases, seria o "padrão"
