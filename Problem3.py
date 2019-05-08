import csv
import pickle
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.optimize import curve_fit

with open("data1.txt", "rb") as fp:
    datalist_GOOG = pickle.load(fp)
    for j in range(0, len(datalist_GOOG), 1):
        datalist_GOOG[j][0] = datalist_GOOG[j][0].replace('/', '-')
with open("data2.txt", "rb") as fp:
    datalist_GS = pickle.load(fp)
    for j in range(0, len(datalist_GOOG), 1):
        datalist_GS[j][0] = datalist_GS[j][0].replace('/', '-')
with open("data3.txt", "rb") as fp:
    datalist_CMCSA = pickle.load(fp)
    for j in range(0, len(datalist_GOOG), 1):
        datalist_CMCSA[j][0] = datalist_CMCSA[j][0].replace('/', '-')
with open("data4.txt", "rb") as fp:
    datalist_KO = pickle.load(fp)
    for j in range(0, len(datalist_GOOG), 1):
        datalist_KO[j][0] = datalist_KO[j][0].replace('/', '-')

with open('temp_datalab_records_linkedin_company.csv') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    mylist = list(reader)
    list_GOOG = list('')
    list_GS = list('')
    list_CMCSA = list('')
    list_KO = list('')
    row_count = len(mylist)
    for row in range(0, row_count, 1):
        if mylist[row][2] == 'Google':
            for row_stock in range(0, len(datalist_GOOG), 1):
                if datalist_GOOG[row_stock][0] == mylist[row][1]:
                    data_extend = datalist_GOOG[row_stock] + mylist[row][3:4] + mylist[row][4:5]
                    list_GOOG.append(data_extend)
        if mylist[row][2] == 'Goldman Sachs':
            for row_stock in range(0, len(datalist_GS), 1):
                if datalist_GS[row_stock][0] == mylist[row][1]:
                    data_extend = datalist_GS[row_stock] + mylist[row][3:4] + mylist[row][4:5]
                    list_GS.append(data_extend)
        if mylist[row][2] == 'Comcast':
            for row_stock in range(0, len(datalist_CMCSA), 1):
                if datalist_CMCSA[row_stock][0] == mylist[row][1]:
                    data_extend = datalist_CMCSA[row_stock] + mylist[row][3:4] + mylist[row][4:5]
                    list_CMCSA.append(data_extend)
        if mylist[row][2] == 'The Coca-Cola Company':
            for row_stock in range(0, len(datalist_KO), 1):
                if datalist_KO[row_stock][0] == mylist[row][1]:
                    data_extend = datalist_KO[row_stock] + mylist[row][3:4] + mylist[row][4:5]
                    list_KO.append(data_extend)
GOOG = np.asarray(list_GOOG)[:, 1:].astype('float')
GS = np.asarray(list_GS)[:, 1:].astype('float')
CMCSA = np.asarray(list_CMCSA)[:, 1:].astype('float')
KO = np.asarray(list_KO)[:, 1:].astype('float')

[Pearson_GOOG_SE, _] = stats.pearsonr(GOOG[:, 0], GOOG[:, 6])
[Pearson_GS_SE, _] = stats.pearsonr(GS[:, 0], GS[:, 6])
[Pearson_CMCSA_SE, _] = stats.pearsonr(CMCSA[:, 0], CMCSA[:, 6])
[Pearson_KO_SE, _] = stats.pearsonr(KO[:, 0], KO[:, 6])

[Pearson_GOOG_SF, _] = stats.pearsonr(GOOG[:, 0], GOOG[:, 5])
[Pearson_GS_SF, _] = stats.pearsonr(GS[:, 0], GS[:, 5])
[Pearson_CMCSA_SF, _] = stats.pearsonr(CMCSA[:, 0], CMCSA[:, 5])
[Pearson_KO_SF, _] = stats.pearsonr(KO[:, 0], KO[:, 5])

Pearson_SE = [Pearson_GOOG_SE, Pearson_GS_SE, Pearson_CMCSA_SE, Pearson_KO_SE]
Pearson_SF = [Pearson_GOOG_SF, Pearson_GS_SF, Pearson_CMCSA_SF, Pearson_KO_SF]

# Analyze the relationship between the number of Linkedin Employees/Followers and the stock price.
plt.figure(1)
name_list = ['Google', 'Goldman Sachs', 'Comcast', 'Coca Cola']
num_list = Pearson_SE
num_list1 = Pearson_SF
x = list(range(len(num_list)))
total_width, n = 0.8, 2
width = total_width / n

plt.bar(x, num_list, width=width, label='Pearson coefficient between number of Linkedin Employees and stock open price', tick_label=name_list, fc='r')
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, num_list1, width=width, label='Pearson coefficient between number of Linkedin followers and stock open price', fc='g')
plt.legend()
plt.show()

# Use the stock price to predict the number of Followers on Linkedin of the four companies. The data used for estimation is obtained at 05/04/2019


def func(x, a, b, c, d):
    return a * x ** 3 + b * x ** 2 + c * x + d

plt.figure(2)
popt, pcov = curve_fit(func, GOOG[:, 0], GOOG[:, 6])
plt.subplot(2, 2, 1)
plt.grid()
plt.plot(GOOG[:, 0], func(GOOG[:, 0], *popt), 'r-')
plt.plot(1189.55, func(1189.55, *popt), 'bo')
plt.plot(1189.55, 108388, 'go')
plt.xlabel('Stock price')
plt.ylabel('Number of employees')
plt.title('Google')
popt, pcov = curve_fit(func, GS[:, 0], GS[:, 6])
plt.subplot(2, 2, 2)
plt.grid()
plt.plot(GS[:, 0], func(GS[:, 0], *popt), 'r-')
plt.plot(207.52, func(207.52, *popt), 'bo')
plt.plot(207.52, 55370, 'go')
plt.xlabel('Stock price')
plt.ylabel('Number of employees')
plt.title('Goldman Sachs')
popt, pcov = curve_fit(func, CMCSA[:, 0], CMCSA[:, 6])
plt.subplot(2, 2, 3)
plt.grid()
plt.plot(CMCSA[:, 0], func(CMCSA[:, 0], *popt), 'r-')
plt.plot(43.29, func(43.29, *popt), 'bo')
plt.plot(43.29, 73407, 'go')
plt.xlabel('Stock price')
plt.ylabel('Number of employees')
plt.title('Comcast')
popt, pcov = curve_fit(func, KO[:, 0], KO[:, 6])
plt.subplot(2, 2, 4)
plt.grid()
plt.plot(KO[:, 0], func(KO[:, 0], *popt), 'r-')
plt.plot(48.72, func(48.72, *popt), 'bo')
plt.plot(48.72, 63183, 'go')
plt.xlabel('Stock price')
plt.ylabel('Number of employees')
plt.title('Coca Cola')

plt.show()







