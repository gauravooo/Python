# Python program that accepts a number as a command-line argument and outputs the current value of that many bitcoins in USD. The program should use the requests library to fetch the current price of bitcoin from the CoinCap API, and then calculate and display the total value in USD. If the user does not provide a command-line argument, or if the argument is not a valid number, the program should exit with an appropriate error message. Additionally, if there is an issue with the API request (e.g., network error), the program should catch the exception and print "Server busy".
import sys
import requests
import json

try:
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    if (sys.argv[1]).replace(".", "").isnumeric():
        value = float(sys.argv[1])
        response = requests.get(
            "https://rest.coincap.io/v3/assets/bitcoin?apiKey=75439ee8949e78f763c76dba7d6473312ede8c44bbb177a644897f3dcc1d22f8"
        )
        j = response.json()
        price = float(j["data"]["priceUsd"])
        result = value * price
        print(f"${result:,.4f}")
    else:
        sys.exit("Command-line argument is not a number")

except requests.RequestException:
    print("Server busy")
