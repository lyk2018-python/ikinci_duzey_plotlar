import bs4
import matplotlib
import requests
import lxml
matplotlib.use('Cairo')
#matplotlib.rcParams['backend.qt5']='PySide2'
import matplotlib.pyplot as plt
import numpy as np


base_url="http://www.aracmetre.com/satis-raporlari/marka/mitsubishi/"

response=requests.get(base_url)


icerik=response.content

soup=bs4.BeautifulSoup(icerik,"lxml")

liste=[]
modeller=[]
satis=[]
ilk_veri=soup.find("tbody")


for i in ilk_veri.find_all("td"):

    liste.append(i.text)


for i in range(0,len(liste),2):

    satis.append((liste[i+1]))



for i in range(0, len(liste),2):

    modeller.append((liste[i]))


satis_2=[]
for a in satis:
    a=float(a)
    satis_2.append(a)


y_pos=np.arange(len(modeller))

plt.bar(y_pos,satis_2,align="center",alpha=0.5)
plt.xticks(y_pos,modeller)
plt.ylabel("Satış")
plt.show()

plt.savefig("mitsubishi.png")

