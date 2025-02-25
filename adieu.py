import inflect

p = inflect.engine()

names = []

try:
    while True:
        entry = input("Name: ")
        names.append(entry)
except EOFError:
    print("\nAdieu, adieu, to", p.join(names))
