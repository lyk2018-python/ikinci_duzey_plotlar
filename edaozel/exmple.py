import matplotlib
import pandas as pd
matplotlib.use('Cairo')
import matplotlib.pyplot as plt



xls = pd.read_excel('ekonomik.xls', skiprows=5)
xls.plot()
plt.show()
plt.savefig('python.png')
