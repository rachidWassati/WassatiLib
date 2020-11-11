from datetime import datetime
import os
import pandas as pd 
import csv

# Function to get the current date
def getCurrentDate(listData):
    currentDate = ""
    listData = [element.lower() for element in listData]

    if 'month' in listData:
        currentMonth = str(datetime.now().month)
    else:
        currentMonth = ''

    if 'year' in listData:
        currentYear = str(datetime.now().year)
    else:
        currentYear = ''

    if 'day' in listData:
        currentDay = str(datetime.now().day)
    else:
        currentDay = ''

    currentDate = currentYear + currentMonth + currentDay

    return currentDate

# This function will write into csv format the main and related themes' url
def writeToCsv(path_file, dico, list_columns):
    with open(path_file, 'a') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=list_columns)
        writer.writerow(dico)

# Function to drop duplicates
def cleanDf(path_file, columns):
    df = pd.read_csv(path_file)
    df = df.drop_duplicates(subset=columns)
    df.to_csv(path_file, index=False)

# Function to initiate an empty csv file
def initiateCsvFile(csvFilePath, list_columns):
    if not os.path.isfile(csvFilePath):
        df = pd.DataFrame(columns=list_columns)
        df.to_csv(csvFilePath, index=False)

def diffList(list1, list2):
    return list(set(list1).symmetric_difference(set(list2)))