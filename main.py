import requests
from datetime import datetime
'''
USD — United States Dollar (доллар США);
EUR — Euro (евро);
RUB — Russian Ruble (российский рубль);
GBP — Great Britain Pound (фунт стерлингов Великобритании);
JPY — Japanese Yen (японская иена);
CNY — Chinese Yuan (китайский юань);
CAD — Canadian Dollar (канадский доллар);
AUD — Australian Dollar (австралийский доллар);
CHF — Swiss Franc (швейцарский франк);
UAH — Ukrainian Hryvnia (украинская гривна).'''





''' Получает курс обмена через API'''


def get_exchange_rate(base_currency, target_currency):
    url = f"https://open.er-api.com/v6/latest/{base_currency}"
    # url = "https://open.er-api.com/v6/latest/USD"
    response = requests.get(url)
    data = response.json()
    if data["result"] == "success":
        rate_ = data["rates"].get(target_currency)
        if rate_:
            date_string = 'Wed, 27 May 2026 00:02:31 +0000'
            last_updated = datetime.strptime(date_string, '%a, %d %b %Y %H:%M:%S %z')
            return rate_, last_updated
        else:
            raise ValueError(f"Валюта {target_currency} не найдена")

    else:
        raise Exception(f"Ошибка API: {data['error-type']}")



'''Конвертирует сумму из одной валюты в другую'''

def convert_currency(amount, base_currency, target_currency):
    rate_, last_updated = get_exchange_rate(base_currency, target_currency)
    converted_amount = amount * rate_
    return converted_amount, rate_, last_updated

if __name__ == "__main__":
    try:
        amount_ = float(input("Введите сумму:\n"))
        base_curr = input("Введите исходную валюту (например, USD): ").upper()
        target_curr = input("Введите целевую валюту (например, EUR): ").upper()

        result, rate, updated = convert_currency(amount_, base_curr, target_curr)

        print(f"\nРезультат конвертации:")
        print(f"{amount_} {base_curr} = {result:.2f} {target_curr}")
        print(f"Курс: 1 {base_curr} = {rate:.2f} {target_curr}")
        print(f"Данные обновлены: {updated.strftime('%Y-%m-%d %H:%M:%S')}")

    except ValueError as e:
        print(f"Ошибка ввода: {e}")

print(f"Точные время и дата на данный момент {datetime.now()}")