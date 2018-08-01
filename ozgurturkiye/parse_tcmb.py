import requests
from bs4 import BeautifulSoup
import json


def get_tcmb_exchange_rates():
    base_url = "http://www.tcmb.gov.tr/kurlar/today.xml"
    try:
        html = requests.get(base_url)
    except:
        print("Connection error", "|", base_url)
        raise
    else:
        print("Succesfully connected")

    soup = BeautifulSoup(html.text, "lxml")

    all_exchange_data = []
    for link in soup.find_all('currency'):
        all_exchange_data.append({
                        "Döviz Kodu": link.get('currencycode'),
                        "Birim": link.unit.text,
                        "Döviz Cinsi": link.isim.text,
                        "Döviz Alış": link.forexbuying.text,
                        "Döviz Satış":link.forexselling.text,
                        "Efektif Alış":link.banknoteselling.text,
                        })

    # save data.json file as a json
    json_path = "kur/data.json"
    with open(json_path, "w") as f:
        json.dump(all_exchange_data, f, ensure_ascii=False)

    # Return data as json
    return all_exchange_data
