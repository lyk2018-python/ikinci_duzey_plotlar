import json
import os
import dolar


def get_generic(exchange_code='USD'):
    file_path = "kur/data.json"
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            json_data = json.load(f)
            # exchange rate has been increased %5
            for exchange in json_data:
                if exchange.get('Döviz Kodu') == exchange_code:
                    new_exchange_rate = float(exchange.get('Döviz Satış'))
                    new_exchange_rate += ((new_exchange_rate / 100) * 5)
                    exchange['Döviz Satış'] = str(new_exchange_rate)

                    return exchange

            # if there is no exchange code match default USD return
            return dolar.manipulate_dolar()
    else:
        return False
