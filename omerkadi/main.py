import xlrd
import matplotlib
import numpy


matplotlib.use("Cairo")
import matplotlib.pyplot as plt  # noqa: E402

datas = xlrd.open_workbook("5592599359848417021..xls")
worksheet = datas.sheet_by_name('Sheet1')

ihracat = []
ithalat = []
karsilama_orani = []
yillar = []
for i in range(21, 218, 14):
    ihracat.append(worksheet.cell(i, 2).value/1000000)
    ithalat.append(worksheet.cell(i, 5).value/1000000)
    karsilama_orani.append(worksheet.cell(i, 13).value)
    yil = worksheet.cell(i-12, 0).value
    if type(yil) is float:
        yillar.append(int(yil))
    else:
        yillar.append(int(yil[:4]))

ind = numpy.arange(15)
width = 0.35

figure, ax1 = plt.subplots()
ax2 = ax1.twinx()

p0 = ax1.bar(ind, ihracat, width)
p1 = ax1.bar(ind + width, ithalat, width)
p2 = ax2.plot(ind + width / 2, karsilama_orani, "g")
ax1.set_xticks(ind + width / 2)
ax1.set_xticklabels(yillar)

plt.legend((p0[0], p1[0], p2[0]), ("İhracat", "İthalat", "Karşılama Oranı"))

ax1.set_ylabel("Milyar Dolar")
ax1.set_xlabel("Yıllar")
ax2.set_ylabel("%")
ax1.tick_params(labelrotation=45)

plt.show()
plt.savefig("Itahlat_Ihtacat.png")
