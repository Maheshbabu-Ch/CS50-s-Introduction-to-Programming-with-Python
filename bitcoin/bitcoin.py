import requests
import sys
try:
    if len(sys.argv) < 1:
        sys.exit("Missing command-line argument")
    def is_float(s):
        return s.count(".") == 1 and s.replace(".","").isdigit() or s.isdigit()
    if not is_float(sys.argv[1]):
        sys.exit("Command-line argument is not a number")
    n = float(sys.argv[1])
    # n = 1
    d = requests.get(" https://api.coindesk.com/v1/bpi/currentprice.json")
    c = d.json()["bpi"]["USD"]['rate_float']
    # print(is_float("1.5"))
    print(f"${c*n:,.4f}")
    # print(f"${amount:,.4f}")
except requests.RequestException:
    ...
