# i = 0
# while i < 3:
#     print("meow")
#     i += 1

# num = [0, 1, 2]

# for i in num:
#     print("meow")

# for i in range(3):
#     print("meow")

# for _ in range(3):
#     print("meow")

# print("meow\n" * 3, end="")


# while True:
#     n = int(input("What's n? "))
#     if n > 0:
#         break

# for _ in range(n):
#     print("meow")


def main():
    meow(get_number())


def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 1:
            return n


def meow(n):
    for _ in range(n):
        print("meow")


main()
