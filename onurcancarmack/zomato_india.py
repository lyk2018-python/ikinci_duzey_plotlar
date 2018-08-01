import statistics
import matplotlib
import csv

matplotlib.use('Qt5Agg')
matplotlib.rcParams['backend.qt5'] = 'PySide2'
import matplotlib.pyplot as plt  # noqa: E402

data=[]
names = [1,2,3,4,5]
prices = [1,2,3,4,5]
votes = [1,2,3,4,5]

with open('zomato.txt', 'r') as file:
    for row in file.readlines():
        data.append(row.strip().split(sep=','))

# print(data)
figure, ax1 = plt.subplots()
p1 = ax1.bar(names, prices)
p2 = ax1.bar(names, votes, bottom= prices)


plt.show()
