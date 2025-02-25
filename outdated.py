def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    while True:
        try:
            date = input("Date: ").strip()

            if "/" in date:
                month, day, year = date.split("/")

            elif "," in date:
                month_name, rest = date.split(" ", 1)
                day, year = rest.split(", ")
                month = str(months.index(month_name) + 1)
            else:
                continue
            month, day, year = int(month), int(day), int(year)

            if 1 <= month <= 12 and 1 <= day <= 31:
                print(f"{year:04}-{month:02}-{day:02}")
                break
        except (ValueError, IndexError):
            continue


if __name__ == "__main__":
    main()
