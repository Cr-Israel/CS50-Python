# def main():
#     # print_column(3)
#     print_row(4)

# # def print_column(height):
# #     for _ in range(height):
# #         print("#")

# def print_row(width):
#     print("?" * width)

# main()


def main():
    print_square(10)


def print_square(size):
    for i in range(size):
        print_row(size)


def print_row(width):
    print("#" * width)


main()
