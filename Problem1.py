import csv
import numpy as np
import pickle
import os
import matplotlib.pyplot as plt
from scipy.stats import chisquare

if os.path.exists("data.txt") == False:
# Count the rows of the csv file
    with open('NYPD_Motor_Vehicle_Collisions.csv', 'r') as csvFile:
        row_count = sum(1 for row in csvFile) - 1
    csvFile.close()

    # Delete the data of 2019
    with open('NYPD_Motor_Vehicle_Collisions.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        mylist = list(reader)
        row = 0

        while row < row_count:
            print(mylist[row][0])
            for col in range(0, 29, 1):
                if mylist[row][col] == '':
                    mylist[row][col] = 'Null'
            if mylist[row][0][-1:] == "9":
                del mylist[row]
                row_count = row_count - 1
            else:
                row = row + 1

        with open("data.txt", "wb") as fp:
            pickle.dump(mylist, fp)
    csvFile.close()

with open("data.txt", "rb") as fp:
     datalist = pickle.load(fp)


# What is the total number of persons injured in the dataset (up to December 31, 2018?)
row_count = len(datalist)
Total_Num_Injured = np.zeros(1)
for row in range(1, row_count, 1):
    if datalist[row][10][0] != 'N':
        Total_Num_Injured = Total_Num_Injured + int(datalist[row][10][0])
print(Total_Num_Injured)

# What proportion of all collisions in 2016 occured in Brooklyn? Only consider entries with a non-null value for BOROUGH.
Brooklyn_Count = np.zeros(1)
Total_Count = np.zeros(1)
for row in range(1, row_count, 1):
    if datalist[row][0][-1:] == "6":
        if datalist[row][2] != 'Null':
            Total_Count = Total_Count + 1
            if datalist[row][2] == 'BROOKLYN':
                Brooklyn_Count = Brooklyn_Count + 1
ratio = Brooklyn_Count/Total_Count
print(ratio)

# What proportion of collisions in 2016 resulted in injury or death of a cyclist?
Cyclist_Count = np.zeros(1)
Total_Count = np.zeros(1)
flag = 0
for row in range(1, row_count, 1):
    if datalist[row][0][-1:] == "6":
        Total_Count = Total_Count + 1
        if datalist[row][14] != 'N' and datalist[row][14] != '0':
            Cyclist_Count = Cyclist_Count + 1
            flag = 1
        if datalist[row][15] != 'N' and datalist[row][15] != '0' and flag == 0:
            Cyclist_Count = Cyclist_Count + 1
ratio = Cyclist_Count/Total_Count
print(ratio)

# For each borough, compute the number of accidents per capita involving alcohol in 2017. Report the highest rate among the 5 boroughs.

Alcohol_Count = np.zeros(5)
Total_Count = [1471160, 2648771, 1664727, 2358582, 479458]
for row in range(1, row_count, 1):
    if datalist[row][0][-1:] == "7":
        if datalist[row][18][0:2] == 'Alc':
            if datalist[row][2] == "BRONX":
                Alcohol_Count[0] = Alcohol_Count[0] + 1
            if datalist[row][2] == "BROOKLYN":
                Alcohol_Count[1] = Alcohol_Count[1] + 1
            if datalist[row][2] == "MANHATTAN":
                Alcohol_Count[2] = Alcohol_Count[2] + 1
            if datalist[row][2] == "QUEENS":
                Alcohol_Count[3] = Alcohol_Count[3] + 1
            if datalist[row][2] == "STATEN":
                Alcohol_Count[4] = Alcohol_Count[4] + 1
ratio = Cyclist_Count/Total_Count
print(ratio)

# Obtain the number of vehicles involved in each collision in 2016. Group the collisions by zip code and compute the sum of all vehicles involved in collisions in each zip code, then report the maximum of these values.

All_Zip_Code = list('')
All_Zip_Count = list('')
for row in range(1, row_count, 1):
    if datalist[row][0][-1:] == "6":
        if datalist[row][3] != 'Null':
            a = int(datalist[row][3])
            if a in All_Zip_Code is True:
                zipcode = All_Zip_Code.index(int(datalist[row][3]))
                for i in range(24, 28, 1):
                    if datalist[row][i] != "Null":
                        All_Zip_Count[zipcode] = All_Zip_Count[zipcode] + 1
            else:
                All_Zip_Code.append(int(datalist[row][3]))
                All_Zip_Count.append(0)
                zipcode = All_Zip_Code.index(int(datalist[row][3]))
                for i in range(24, 28, 1):
                    if datalist[row][i] != "Null":
                        All_Zip_Count[zipcode] = All_Zip_Count[zipcode] + 1
Max_Zip_Count = max(All_Zip_Count)
print(Max_Zip_Count)
All_Zip_Code.clear()

# Consider the total number of collisions each year from 2013-2018. Is there an apparent trend? Fit a linear regression for the number of collisions per year and report its slope.
Year_Count = np.zeros(6)
Year = np.array([2013, 2014, 2015, 2016, 2017, 2018])
for row in range(1, row_count, 1):
    if datalist[row][0][-1:] == "3":
        Year_Count[0] = Year_Count[0] + 1
    if datalist[row][0][-1:] == "4":
        Year_Count[1] = Year_Count[1] + 1
    if datalist[row][0][-1:] == "5":
        Year_Count[2] = Year_Count[2] + 1
    if datalist[row][0][-1:] == "6":
        Year_Count[3] = Year_Count[3] + 1
    if datalist[row][0][-1:] == "7":
        Year_Count[4] = Year_Count[4] + 1
    if datalist[row][0][-1:] == "8":
        Year_Count[5] = Year_Count[5] + 1
print(Year_Count)


def estimate_coef(x, y):
    # number of observations/points
    n = np.size(x)

    # mean of x and y vector
    m_x, m_y = np.mean(x), np.mean(y)

    # calculating cross-deviation and deviation about x
    SS_xy = np.sum(y * x) - n * m_y * m_x
    SS_xx = np.sum(x * x) - n * m_x * m_x

    # calculating regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1 * m_x

    return (b_0, b_1)


def plot_regression_line(x, y, b):
    # plotting the actual points as scatter plot
    plt.scatter(x, y, color="m",
                marker="o", s=30)

    # predicted response vector
    y_pred = b[0] + b[1] * x

    # plotting the regression line
    plt.plot(x, y_pred, color="g")

    # putting labels
    plt.xlabel('x')
    plt.ylabel('y')

    # function to show plot
    plt.show()


b = estimate_coef(Year, Year_Count)
plot_regression_line(Year, Year_Count, b)
print(b[1])

# Do winter driving conditions lead to more multi-car collisions?

Total_Count_2017 = np.zeros(12)
Multi_Count_2017 = np.zeros(12)
Multi_Flag_2017 = 0
for row in range(1, row_count, 1):
    a = int(datalist[row][0][0:2])
    if datalist[row][0][-1:] == "7":
        if datalist[row][0][0] == "0":
            Total_Count_2017[int(datalist[row][0][1])-1] = Total_Count_2017[int(datalist[row][0][1])-1] + 1
        elif datalist[row][0][0] == "1":
            Total_Count_2017[int(datalist[row][0][0:2]) - 1] = Total_Count_2017[int(datalist[row][0][0:2]) - 1] + 1
        for i in range(24, 28, 1):
            if datalist[row][i] != "Null":
                Multi_Flag_2017 = Multi_Flag_2017 + 1
        if Multi_Flag_2017 > 2:
            if datalist[row][0][0] == "0":
                Multi_Count_2017[int(datalist[row][0][1]) - 1] = Multi_Count_2017[int(datalist[row][0][1]) - 1] + 1
            elif datalist[row][0][0] == "1":
                Multi_Count_2017[int(datalist[row][0][0:2]) - 1] = Multi_Count_2017[int(datalist[row][0][0:2]) - 1] + 1
        Multi_Flag_2017 = 0
Corr_Matrix = np.vstack((Total_Count_2017, Multi_Count_2017))
[chistatistics, ptest] = chisquare(Corr_Matrix)

print(Total_Count_2017, Multi_Count_2017, chistatistics[0])

# We can use collision locations to estimate the areas of the zip code regions.

All_Zip_Code = list('')
All_Zip_Collision = list('')
for row in range(1, row_count, 1):
    if datalist[row][0][-1:] == "7":
        if datalist[row][3] != 'Null':
            a = datalist[row][3]
            if a in All_Zip_Code and datalist[row][4] != 'Null' and datalist[row][5] != 'Null':
                zipcode = All_Zip_Code.index(a)
                All_Zip_Collision[zipcode] = All_Zip_Collision[zipcode] + 1
                locals()['All_Zip_Latitude' + str(zipcode)].append(datalist[row][4])
                locals()['All_Zip_Longitude' + str(zipcode)].append(datalist[row][5])
            elif a not in All_Zip_Code and datalist[row][4] != 'Null' and datalist[row][5] != 'Null':
                All_Zip_Code.append(a)
                All_Zip_Collision.append(0)
                zipcode = All_Zip_Code.index(a)
                All_Zip_Collision[zipcode] = All_Zip_Collision[zipcode] + 1
                locals()['All_Zip_Latitude' + str(zipcode)] = []
                locals()['All_Zip_Longitude' + str(zipcode)] = []
                locals()['All_Zip_Latitude' + str(zipcode)].append(datalist[row][4])
                locals()['All_Zip_Longitude' + str(zipcode)].append(datalist[row][5])
Collisions_Per_Square_Kilometer = np.zeros(len(All_Zip_Code))
length = len(All_Zip_Code)-1
for j in range(0, length, 1):
    Latitude = locals()['All_Zip_Latitude' + str(j)]
    Latitude_np = np.array(Latitude).astype('float')
    if len(Latitude) > 1000:
        a = np.std([Latitude_np])
        Latitude_std = np.std([Latitude_np]) * 111.11
        # Detect outlier data points
            # np.median(Latitude_np)
        Longitude = locals()['All_Zip_Longitude' + str(j)]
        Longitude_np = np.array(Longitude).astype('float')
        Longitude_std = np.std([Longitude_np]) * 111.11 * np.cos(np.std([Latitude_np])/180)
        Square = np.pi * Latitude_std * Longitude_std
        Collisions_Per_Square_Kilometer[j] = Latitude_np.shape[0]/Square
Collisions_Per_Square_Kilometer_Max = np.max(Collisions_Per_Square_Kilometer)
print(Collisions_Per_Square_Kilometer_Max)

