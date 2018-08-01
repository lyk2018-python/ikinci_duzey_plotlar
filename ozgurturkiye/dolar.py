import json
import os
import save_dolar_to_database


def manipulate_dolar():
    file_path = "kur/data.json"
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            json_data = json.load(f)
            # exchange rate has been increased %5
            dolar = float(json_data[0].get('Döviz Satış'))
            dolar = dolar + ((dolar / 100) * 5)
            json_data[0]['Döviz Satış'] = str(dolar)

            # send database data to save
            save_dolar_to_database.dolar_write(json_data[0])
            return json_data[0]
    else:
        return False
