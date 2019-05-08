import csv
import pickle

with open('HistoricalQuotes.csv') as csv_file:
    # Google
    reader = csv.reader(csv_file, delimiter=',')
    row_count = 800
    mylist_Google = list(reader)[200:row_count]
    with open("data1.txt", "wb") as fp:
        pickle.dump(mylist_Google, fp)

with open('HistoricalQuotes1.csv') as csv_file:
    # Goldman Sachs
    reader = csv.reader(csv_file, delimiter=',')
    row_count = 800
    mylist_GS = list(reader)[200:row_count]
    with open("data2.txt", "wb") as fp:
        pickle.dump(mylist_GS, fp)


with open('HistoricalQuotes2.csv') as csv_file:
    # Comcast
    reader = csv.reader(csv_file, delimiter=',')
    row_count = 800
    mylist_CMCSA = list(reader)[200:row_count]
    with open("data3.txt", "wb") as fp:
        pickle.dump(mylist_CMCSA, fp)

with open('HistoricalQuotes3.csv') as csv_file:
    # Comcast
    reader = csv.reader(csv_file, delimiter=',')
    row_count = 800
    mylist_KO = list(reader)[200:row_count]
    with open("data4.txt", "wb") as fp:
        pickle.dump(mylist_KO, fp)








