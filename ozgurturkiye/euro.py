import json
import os


def manipulate_euro():
    file_path = "kur/data.json"
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            json_data = json.load(f)
            # exchange rate has been increased %5
            euro = float(json_data[3].get('Döviz Satış'))
            euro = euro + ((euro / 100) * 5)
            json_data[3]['Döviz Satış'] = str(euro)
            return json_data[3]
    else:
        return False