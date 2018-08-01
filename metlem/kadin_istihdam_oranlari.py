import pandas
import matplotlib

matplotlib.use('Cairo')

import matplotlib.pyplot as plt
veri = pandas.read_csv('kadin_istihdam.csv')

v1 = veri["yil"]
v2 = veri["tarim"]
v3 = veri["sanayi"]
v4 = veri["hizmet"]


plt.suptitle("Türkiye'de Yıllara Göre Kadın İstihdam Oranları")
ax = plt.subplot2grid((2, 2), (0, 0))
ax.plot(v1, v2,color="b",label = "Tarım")
ax.legend()
plt.xlabel('Yıllar')
plt.ylabel('İstihdam Oranları % ')


ax1 = plt.subplot2grid((2, 2), (0, 1))
ax1.plot(v1, v3, color="g",label = "Sanayi")
ax1.legend()
plt.xlabel('Yıllar')
plt.ylabel('İstihdam Oranları % ')

ax2 = plt.subplot2grid((2, 2), (1,0), colspan=2)
ax2.plot(v1, v4, color = "orange",label = "Hizmet")
ax2.legend()
plt.xlabel('Yıllar')
plt.ylabel('İstihdam Oranları % ')

plt.show()
plt.savefig("plot.png")
