import requests
import json
import csv
from argparse import ArgumentParser
from datetime import datetime as dt, timedelta as td
from tabulate import tabulate


def date_now():
    return dt.now().strftime('%Y-%m-%d')


def args_parser():
    parser = ArgumentParser(description="Online currency exchange")
    parser.add_argument('-from', '--from_currency', default="USD",
                        help='Currency to be converted. Default - USD.')
    parser.add_argument('-to', '--to_currency', default="UAH",
                        help='In this currency default currency "-from" convert. Default - UAH.')
    parser.add_argument('-sd', '--start_date', default=date_now(),
                        help="Date in format YYYY-MM-DD. Default - today's date")
    parser.add_argument('-a', '--amount', default=100, type=float,
                        help="Amount of money to exchange. Default - 100")
    parser.add_argument('-sf', '--save_file', action='store_true',
                        help='If args is called will save output in file. Default - console output')
    return parser.parse_args()


def file_name(curr_from: str, curr_to: str, amount: float) -> str:
    return f'{date_now()} {curr_from} {curr_to} {amount}.txt'.replace(" ", "-")


def save_json(name: str, currency: dict):
    with open(name, 'w') as f:
        json.dump(currency, f)


def response_json(url: str, values=()) -> json:
    return requests.get(url,  params=values).json()


def load_json(name: str):
    with open(name, 'r') as f:
        return json.load(f)


def symbols_json() -> dict:
    currency = {'symbols': []}
    currency_json = load_json('symbols.json')
    for cur in currency_json['symbols']:
        currency['symbols'].append(cur)
    return currency


def currency_checker(currencies: dict, default: str, currency: str) -> str:
    currency = currency.upper()
    for cur in currencies['symbols']:
        if currency == cur:
            return currency
    return default


def dates_list(date: str) -> list:
    result = []
    today = dt.now()
    date_inp = dt(*[int(d) for d in date.split("-")])
    if date_inp < today:
        while date_inp <= today:
            result.append(date_inp.strftime('%Y-%m-%d'))
            date_inp += td(days=1)
    else:
        result.append(date_now())
    return result


def tab_rows(cur_from: str, cur_to: str, amount: float, date: str) -> list:
    params = {'from': cur_from, 'to': cur_to, 'amount': amount, 'date': date}
    response = response_json('https://api.exchangerate.host/convert', params)
    return [date, cur_from, cur_to, amount, response['info']['rate'], response['result']]


def table(cur_from: str, cur_to: str, amount: float, date: list) -> list:
    result = [['DATE', '   FROM', '   TO', '   AMOUNT', '   RATE', '   RESULT']]
    for dates in date:
        result.append(tab_rows(cur_from, cur_to, amount, dates))
    return result


def save_txt(name: str, tabl: list):
    with open(name, 'w') as f:
        file = csv.writer(f, delimiter='\t')
        for rows in tabl:
            file.writerow(rows)


def main():
    params = args_parser()
    dates = dates_list(params.start_date)
    currencies_list = symbols_json()
    params.from_currency = currency_checker(
        currency=params.from_currency,
        currencies=currencies_list,
        default="USD"
    )
    params.to_currency = currency_checker(
        currency=params.to_currency,
        currencies=currencies_list,
        default="UAH"
    )
    array = table(
        date=dates,
        cur_from=params.from_currency,
        cur_to=params.to_currency,
        amount=params.amount
    )
    if params.save_file:
        name = file_name(params.from_currency, params.to_currency, params.amount)
        save_txt(name, array)
    else:
        print(tabulate(array, tablefmt='github'))


if __name__ == '__main__':
    main()
