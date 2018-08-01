import requests
import matplotlib
from bs4 import BeautifulSoup
matplotlib.use('Qt5Agg')
matplotlib.rcParams['backend.qt5'] = 'PySide2'
import matplotlib.pyplot as plt # noqa: E402
import numpy as np

r = requests.get("http://www.muhasebefinans.net/yillar-itibariyle-asgari-ucret-kac-dolar/")
soup = BeautifulSoup(r.content, "lxml")
gelen_veri = soup.find("tbody",attrs={"class":"row-hover"}).find_all("tr")
#print(gelen_veri)

dolarim = []
asgarim = []
yilim = []
for veri in gelen_veri[:-1]:
    yil = veri.find("td", attrs={"class":"column-1"}).text
    asgari = veri.find("td", attrs={"class": "column-2"}).text
    dolar = veri.find("td", attrs={"class": "column-3"}).text

    if(int(yil)<2005):
        asgari = float(asgari[:-8])
        dolar = float(dolar[:-7].replace(".",""))/1000
        dolarim.append(dolar)
        asgarim.append(asgari)
        yilim.append(yil)
    else:
        asgari = float(asgari.replace(",","").replace(".",""))/100
        dolar = float(dolar.replace(",", ""))/100
        dolarim.append(dolar)
        asgarim.append(asgari)
        yilim.append(yil)
    print("{}    {}    {}".format(yil, asgari, dolar))

for idx, val in enumerate(dolarim):
    if idx > 0:
        dolarim[idx - 1] = ((val - dolarim[idx - 1]) / dolarim[idx - 1]) * 100
dolarim[-1] = 0
print(dolarim)
for idx, val in enumerate(asgarim):
    if idx>0:
        asgarim[idx-1]=((val-asgarim[idx-1])/asgarim[idx-1])*100
asgarim[-1]=0
print(asgarim)

x = np.array(yilim)
y = np.array(asgarim)
z = np.array(dolarim)

fig, ax = matplotlib.pyplot.subplots()
#p0 = ax1.plot(x, y, color='lightgray')
ax.plot(x, y, color='red')
ax.plot(x, z, color='blue')
ax.set_xlabel('Seneler')
ax.set_ylabel('Asgari Ücret')
ax.set_title('Dolar-Asgari Ücret Grafiği')
ax.grid()
matplotlib.pyplot.savefig("test.png")
matplotlib.pyplot.show()
