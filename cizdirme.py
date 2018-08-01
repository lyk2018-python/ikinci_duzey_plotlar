import matplotlib.pyplot as plt

x = []
y = []
z = []
k = []

infile = open("cicek.txt", "r")
for line in infile.readline():
    temp = infile.readline()
    value = temp.split(",")
    x.append(float(value[0]))
    y.append(float(value[1]))
    z.append(float(value[2]))
    k.append(float(value[3]))

aa = []
for i in range(0,28):
    aa.append(i)

figure, ax1 = plt.subplots()

ax1 = plt.subplot2grid((2, 1), (0, 0))
p1 = ax1.bar([i for i in aa], x, 0.2)
p2 = ax1.bar([i + 0.3 for i in aa], y, 0.2)

y_max = max(y)
y_index_max = y.index(y_max)
y_min = min(y)
y_index_min = y.index(y_min)
x_max = max(x)
x_index_max = x.index(x_max)
x_min = min(x)
x_index_min = x.index(x_min)

plt.plot(y_index_max-1, y[y_index_max] ,'x')
plt.plot(y_index_min-1 ,y[y_index_min] ,'x')

plt.plot(x_index_max-1, x[x_index_max] ,'o')
plt.plot(x_index_min-1 ,x[x_index_min] ,'bo')

plt.title('Muhteşem çiçek')
plt.legend((p1[0], p2[0]),
           ('Çanak Uzunluk', 'Çanak Genişlik', 'Numero'))

ax2= plt.subplot2grid((2, 1), (1,0))
p3 = ax2.bar([i + 0.3 for i in aa], z, 0.2)
p4 = ax2.bar([i + 0.6 for i in aa], k, 0.2)

plt.title('Çanak Çömlek patladı')
plt.legend((p3[0], p4[0]),
           ('Petal Uzunluk', 'Petal Genişlik', 'Numero'))

plt.show()