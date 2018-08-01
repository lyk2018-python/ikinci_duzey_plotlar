import matplotlib
import matplotlib.pyplot as plt
import requests
import bs4
import lxml


base_url="https://weather.com/tr-TR/kisisel/saatlik/l/Bolu+T%C3%BCrki%CC%87ye+TUXX0032:1:TU"

bolu_response=requests.get(base_url)
bolu_soup=bs4.BeautifulSoup(bolu_response.text, "lxml")
sicaklik=[]
saat=[]
for satir in bolu_soup.find("table").find_all("tr"):
    sutunlar=[]
    for sutun in satir.find_all("td"):
        sutunlar.append(sutun.text)

    if sutunlar:
        sicaklik.append(int(sutunlar[3].replace("°", "")))
        saat.append(sutunlar[1])

figure, ax1 = plt.subplots()
ax1.plot(saat, sicaklik)
ax1.set_ylabel("Sıcaklık")
ax1.set_xlabel("Saatler")
ax1.tick_params(labelrotation=90)
plt.show()
