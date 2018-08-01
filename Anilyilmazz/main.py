import matplotlib
import csv
import operator

matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt

citys = []
salarys = []


def city_salary_average(city):
    total = 0
    sequence = 0

    if city[0] not in ["i", "İ"]:
        city = city.upper()[0] + city[1:]
    else:
        city = 'İ' + city[1:]

    with open("yazilimci-maaslari.csv") as csvfile:
        reader = csv.reader(csvfile)

        for item in (reader):

            if str(city) in item:
                sequence = sequence + 1
                total = total + int(item[5].split(" ")[0].replace(".", ""))

                try:
                    total = total + int(item[5].split(" ")[3].replace(".", ""))
                except ValueError:
                    total = 2000 + total
    return int((total / sequence) / 2)


with open("yazilimci-maaslari.csv") as csvfile:
    reader = csv.reader(csvfile)
    for item in (reader):
        if item[4] not in citys:
            citys.append(item[4])

for item in citys:
    salarys.append(city_salary_average(item))

dictionary = dict(zip(citys, salarys))
sorted_list = sorted(dictionary.items(), key=operator.itemgetter(1))
sorted_dict = {}

for i in range(0, len(sorted_list)):
    sorted_dict[sorted_list[i][0]] = sorted_list[i][1]

plt.bar(range(len(sorted_dict)), sorted_dict.values(), align='center')
plt.xticks(range(len(sorted_dict)), sorted_dict.keys(), rotation=90)
plt.title("Şehirlere Göre Ortalama Maaş")
plt.show()
