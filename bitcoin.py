import requests

import sys


def main():
    amount = get_argument()

    try:
        response = requests.get("https://api.coincap.io/v2/assets/bitcoin")
    except requests.RequestException:
        sys.exit("Error in API request")

    data = response.json()

    try:
        price_usd = float(data["data"]["priceUsd"])
    except (KeyError, ValueError):
        sys.exit("Error")

    usd_value = amount * price_usd
    print(f"${usd_value:,.4f}")


def get_argument():
    if len(sys.argv) != 2:
        sys.exit("Missing comand-line argument")

    try:
        value = float(sys.argv[1])
    except ValueError:
        sys.exit("Comand-line argument is not a number")

    return value


if __name__ == "__main__":
    main()
