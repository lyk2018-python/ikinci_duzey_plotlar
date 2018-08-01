import requests
import matplotlib.pyplot as plt
from bs4 import *
import string


def steaminfo():
    url = "https://steamdb.info/"

    r = requests.get(url)
    soup = BeautifulSoup(r.content, "lxml")

    liste = []


    for i in soup.find_all("td", attrs={"class": "text-center"}):
        mytexts = i.text
        new_str = mytexts.replace(",", "")

        if new_str.isdigit():
            liste.append(int(new_str))

    return liste

plt.plot(steaminfo())
plt.ylabel("Current player")
plt.show()

