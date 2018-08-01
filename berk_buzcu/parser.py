import requests
import bs4
import matplotlib.pyplot as pyplot

labelsnsizes = {}

for i in range(0, 20):
    request = requests.get('https://stackoverflow.com/questions?page={}&sort=newest'.format(i))
    request_soup = bs4.BeautifulSoup(request.text, features="html.parser")
    for question in request_soup.find_all("div", {"class": "question-summary"}):
        for tag in question.find_all("a", {"class": "post-tag"}):
            try:
                labelsnsizes['{}'.format(tag.text)] += 1
            except KeyError:
                labelsnsizes['{}'.format(tag.text)] = 0

plotted = pyplot.pie([float(v) for v in labelsnsizes.values() if v > 5],
                     labels=[k for k in labelsnsizes if labelsnsizes[k] > 5],
                     autopct=None)
pyplot.show()
