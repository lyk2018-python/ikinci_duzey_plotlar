import statistics

import matplotlib
import requests

matplotlib.use('Qt5Agg')
matplotlib.rcParams['backend.qt5'] = 'PySide2'
import matplotlib.pyplot as plt  # noqa: E402


data = requests.get("https://www.doviz.com/api/v1/currencies/all/latest").json()[0:10]

buying = []
selling = []
change_rate = []
full_name = []
full_name_idx = []

for i, d in enumerate(data):
    full_name_idx.append(i)
    full_name.append(d["full_name"])
    buying.append(d["buying"])
    selling.append(d["selling"])
    change_rate.append(d["change_rate"])

avg_exchange = statistics.mean(change_rate)

figure, ax1 = plt.subplots()
ax2 = ax1.twinx()

p0 = ax1.plot(full_name_idx, [avg_exchange for i in full_name], '--', color='lightgray')
p1 = ax1.bar([i + 0.3 for i in full_name_idx], buying, 0.25)
p2 = ax1.bar([i + 0.6 for i in full_name_idx], selling, 0.25)
p3 = ax2.plot(full_name, change_rate)

plt.legend((p0[0], p1[0], p2[0], p3[0]),
           ('Average', 'Buying', 'Selling', 'Change Rate'))
ax1.set_ylabel("Exchange Rate")
ax2.set_ylabel("‰")
plt.xticks(rotation=45)
plt.show()
