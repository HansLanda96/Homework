def key_value_connect(key: tuple, value: tuple) -> dict:
    dictionary = {k: item for k, item in zip(key, value)}
    return dictionary


def main():
    coins = ("Bitcoin", "Ether", "Ripple", "Litecoin", "Polygon", "Polkadot")
    codes = ("BTC", "ETH", "XRP", "LTC", "MATIC", "DOT")
    print(key_value_connect(coins, codes))


if __name__ == "__main__":
    main()
