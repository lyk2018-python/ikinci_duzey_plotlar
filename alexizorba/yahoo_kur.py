import matplotlib
matplotlib.use('Qt5Agg')
matplotlib.rcParams['backend.qt5'] = 'PySide2'
import matplotlib.pyplot as plt
import json
import requests

url="https://www.doviz.com/api/v1/currencies/all/latest"
response=requests.get(url).json()

#with open('latest.json') as data_file:
#    data = json.load(data_file)

birimler=[]
degerler=[]
for item,aa in enumerate(response):
    birimler.append(aa["code"])
    degerler.append(aa["buying"])



plt.bar(birimler, degerler)  #çizgi Grafiği
# plt.bar(birimler, degerler)   # bar grafiği

plt.ylabel('Birimler')
plt.xlabel('Oran')
plt.xticks(rotation=90)
plt.show()