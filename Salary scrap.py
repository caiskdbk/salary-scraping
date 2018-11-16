import re
import pandas as pd
import numpy as np
import requests
import bs4 as bs
from lxml import html

def SalarySinglePage(base_url, pagenumber):
    res = requests.get(base_url % pagenumber)

    #Parse the response HTML using BeautifulSoup
    soup = bs.BeautifulSoup(res.text, "lxml")

    #Find the salary table and store it as a pandas series
    table = soup.find_all('table')[1]

    #RegEx Pattern: start with $, then with at least 1 digit, then with a comma, and then with at least 1 digit
    pattern = re.compile('\$\d+,\d+')
    salary = pd.Series(pattern.findall(table.get_text()))

    return salary


def academia():
    base_url = "http://data.richmond.com/salaries/2016/state/university-of-virginia?page=%s"

    #Get max page number
    res = requests.get(base_url % 1)
    soup = bs.BeautifulSoup(res.text, "lxml")
    #Regex pattern: number with at least three digits
    pattern = re.compile('\d{3,}')
    page = int(pattern.findall(str(soup.find_all('b')[2]))[0])+1

    #Get first page of salary data to initialize the data series
    salary = SalarySinglePage(base_url, 1)
    
    #Get the rest of salary data
    for i in range(2,page):
        temp = SalarySinglePage(base_url, i)
        salary = salary.append(temp, ignore_index=True)

    #Get stats on the website
    table = soup.find_all('table')[0]
    table = pd.read_html(str(table), index_col=0)[0]

    #Make sure the number of observations extracted matches the number on the website
    N = int(table.loc['Employees'][1])
    if len(salary) == N:
        print ("Successfully extracted all the salary data")

        #Remove the dollar sign
        salary = salary.str.replace('$','')
        salary = salary.str.replace(',','')
        salary = salary.astype(int)
        
        #Make sure the summary stats for data extracted matches summary stats on the website
        print ("Some Stats from extracted data: \n")
        print (salary.describe())
        print ("Some Stats on the website: \n")
        print (table)

        #Write the extracted data as csv file
        salary.to_csv('.\RawData\salary.csv', index = False)

def medcenter():
    base_url = "http://data.richmond.com/salaries/2016/state/university-of-virginia-medical-center?page=%s"

    #Get max page number
    res = requests.get(base_url % 1)
    soup = bs.BeautifulSoup(res.text, "lxml")
    #Regex pattern: number with at least three digits
    pattern = re.compile('\d{3,}')
    page = int(pattern.findall(str(soup.find_all('b')[2]))[0])+1

    #Get first page of salary data to initialize the data series
    salary = SalarySinglePage(base_url, 1)
    
    
    
    #Get the rest of salary data
    for i in range(2,page):
        temp = SalarySinglePage(base_url, i)
        salary = salary.append(temp, ignore_index=True)

    #Get stats on the website
    table = soup.find_all('table')[0]
    table = pd.read_html(str(table), index_col=0)[0]

    #Make sure the number of observations extracted matches the number on the website
    N = int(table.loc['Employees'][1])
    if len(salary) == N:
        print ("Successfully extracted all the salary data")

        #Remove the dollar sign
        salary = salary.str.replace('$','')
        salary = salary.str.replace(',','')
        salary = salary.astype(int)
        
        #Make sure the summary stats for data extracted matches summary stats on the website
        print ("Some Stats from extracted data: \n")
        print (salary.describe())
        print ("Some Stats on the website: \n")
        print (table)

        #Write the extracted data as csv file
        salary.to_csv('.\RawData\salary_med_center.csv', index = False)
    

if __name__ == '__main__':
    #Comment out one of the functions below to just scrap for one division instead. 
    academia()
    medcenter()
