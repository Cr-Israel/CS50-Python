def main():
    file_name = input("File name: ").strip().lower()

    if file_name.endswith(".gif"):
        print("image/gif")
    elif file_name.endswith(".jpg"):
        print("image/jpeg")
    elif file_name.endswith(".jpeg"):
        print("image/jpeg")
    elif file_name.endswith(".png"):
        print("image/png")
    elif file_name.endswith(".pdf"):
        print("image/pdf")
    elif file_name.endswith(".txt"):
        print("image/text")
    elif file_name.endswith(".zip"):
        print("image/zip")
    else:
        print("application/octet-stream")


if __name__ == "__main__":
    main()
