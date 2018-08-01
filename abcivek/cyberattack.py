import requests
import bs4

base_url = "https://www.hackmageddon.com/2018-master-table/"
main_response = requests.get(base_url)
main_soup = bs4.BeautifulSoup(main_response.text, "html.parser")
title = main_soup.find_all("td", class_="column-6")
words = []

for i in title:
    words.append(i.text)

unique_words = []
for i in words:
    if i not in unique_words:
        unique_words.append(i)

unique_words.remove('>1')
unique_words.remove('')

latest = []
for i in unique_words:
    how_many = words.count(i)
    latest.append([i, how_many])

total = 0
for j in latest:
    total = total + int(j[1])

attack_mean = total / len(unique_words)

for k in latest:
    if int(k[1]) > attack_mean:
        attack_vectors = [k[0] for k in latest]
        attack_numbers = [k[1] for k in latest]

attack_percentage = []
for i in attack_numbers:
    attack_percentage.append((int(i) / total) * 100)

import matplotlib

matplotlib.use('Qt5Agg')
matplotlib.rcParams['backend.qt5'] = 'PySide2'
# matplotlib.use('Cairo')

import matplotlib.pyplot as plt

figure, ax = plt.subplots()
ax.legend(title="Cyber Attack Vektors in 2018")
plt.pie(attack_percentage, labels=attack_vectors, autopct='%1.1f%%')
plt.show()
#plt.savefig("python.png", dpi=600)
