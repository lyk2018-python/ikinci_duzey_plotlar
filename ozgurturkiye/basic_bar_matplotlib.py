import numpy as np
import matplotlib
import requests

matplotlib.use('Cairo')
# matplotlib.use('Qt5Agg')
# matplotlib.rcParams['backend.qt5'] = 'PySide2'

import matplotlib.pyplot as plt  # noqa: E402


data = requests.get("http://127.0.0.1:5000/start_parse").json()

doviz_types = []
doviz_rates = []

for sozluk in data:
    doviz_types.append(sozluk.get("Döviz Cinsi"))
    if sozluk.get("Döviz Satış") != "":
        doviz_rates.append(float(sozluk.get("Döviz Satış")))
    else:
        doviz_rates.append(0)

doviz_types = doviz_types[:19]
doviz_rates = doviz_rates[:19]

objects = doviz_types
y_pos = np.arange(len(objects))
performance = doviz_rates


plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects, rotation=90)
plt.ylabel('TL - Turkish Lira')
plt.title('Exchange Rates for Turkish Lira')


plt.show()
plt.savefig("resim1.png")