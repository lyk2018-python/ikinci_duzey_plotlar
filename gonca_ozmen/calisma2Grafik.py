
import matplotlib

import numpy as np

matplotlib.use("Cairo")
import matplotlib.pyplot as plt
plt.rcdefaults()
objects = (2004,2005,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017)
y_pos = np.arange(len(objects))
kkullanim = [0,87.8,88.7,90.6,90.7,92.3,94.0,93.5,92.0,94.4,95.2,95.9,97.2]
sint_erisim=[0,80.4,85.4,89.2,88.8,90.9,92.4,92.5,90.8,89.9,92.5,93.7,95.9]
sweb_var=[0, 48.2, 63.1, 62.4, 58.7, 52.5, 55.4, 58.0, 53.8, 56.6, 65.5, 66.0, 72.9]
#plt.bar(y_pos, performance, align='center', alpha=0.5)
#plt.bar(y_pos,sint_erisim)

bKullanim= [23.6, 22.9, 33.4, 38.0, 40.1, 43.2, 46.4, 48.7, 49.9, 53.5, 54.8, 54.9, 56.6]
bKullanim_male= [31.1, 30.0, 42.7, 47.8, 50.5, 53.4, 56.1, 59.0, 60.2, 62.7, 64.0, 64.1, 65.7]
bKullanim_female=[16.2, 15.9,23.7, 28.5, 30.0, 33.2, 36.9, 38.5, 39.8, 44.3, 45.6, 45.9, 47.7]
intKullanim=[18.8, 17.6, 30.1, 35.9, 38.1, 41.6,45.0, 47.4, 48.9, 53.8, 55.9, 61.2,66.8]
intKul_male=[25.7, 24.0, 39.2, 45.4, 48.6, 51.8, 54.9, 58.1, 59.3, 63.5, 65.8, 70.5, 75.1]
intKul_female=[12.1, 11.1, 20.7, 26.6, 28.0, 31.7, 35.3, 37.0, 38.7, 44.1, 46.1, 51.9, 58.7]
intKullanim=[18.8, 17.6, 30.1, 35.9, 38.1, 41.6,45.0, 47.4, 48.9, 53.8, 55.9, 61.2,66.8]


internetErisim=[7.0, 8.7, 19.7, 25.4, 30.0, 41.6, 42.9, 47.2, 49.1, 60.2, 69.5, 76.3, 80.7]

eni= 0.35



figure, ax1 = plt.subplots()


opacity = 0.4
error_config = {'ecolor': '0.3'}

rects1 = ax1.bar(y_pos, kkullanim, eni,
                alpha=opacity, color='red',
                error_kw=error_config, label="Kurumsal Kullanim")



rects2 = ax1.bar(y_pos+eni, sint_erisim, eni,
                alpha=opacity, color='blue',
                error_kw=error_config,
                label='Kurumsal erişim')

c3=ax1.plot(y_pos,sweb_var,label="Kurumsal Web Sayfası")
#p3=ax2.plot(y_pos,sweb_var)plt.savefig("grafik_Bilgi2.png")

ax1.set_xlabel('Yıllar')
ax1.set_ylabel('%')
ax1.set_title('Yıllara Göre Kurumsal Bilgisayar Kullanımı')
ax1.set_xticks(y_pos + eni/ 2)
ax1.set_xticklabels(objects)
ax1.legend()
plt.xticks(rotation=90)

# figure.tight_layout()
plt.show()

plt.savefig("grafik_Bilgi3.png")



# plt.legend((kkullanim,sint_erisim[1]),('Kullanim', 'Erisim'))

# plt.xticks(y_pos , objects)
# # plt.legend(loc='best')
# plt.xticks(rotation=90)
# plt.show()









#
# yils= [2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017]
# bkul_m = np.array(bKullanim_male)
# bkul_f = np.array(bKullanim_female)
# intK_m = np.array(intKul_male)
# intK_f=np.array(intKul_female)
# ind = np.arange(len(yils))
#
# plt.bar(ind, bKullanim_male, width=0.8, label='Bay',  bottom=bkul_f)
# plt.bar(ind, bKullanim_female, width=0.8, label='Bayan')
# #plt.bar(ind, intKul_female, width=0.8, label='Web', color='#CD853F')
#
# plt.xticks(ind, yils)
# plt.ylabel("Kullanim")
# plt.xlabel("Yillar")
# plt.legend(loc="upper right")
# plt.title("TUIK Bilgi Toplumu istatistik 2004-2017")
#
# plt.show()


