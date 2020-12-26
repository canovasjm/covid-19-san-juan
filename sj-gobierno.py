#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 00:59:25 2020

@author: jm
"""
# %% required libraries
from scrapy import Selector
import requests
import pandas as pd
import datetime
import os
import smtplib
from email.message import EmailMessage

# %% target website
url = "https://sisanjuan.gob.ar/modulo-coronavirus"

# make GET request
html = requests.get(url).content

# create scrapy selector
sel = Selector(text = html)
print("The number of elements in the HTML is: ", len(sel.xpath('//*')))

# from the selector, extract categories
categories = sel.css('.g-table-title h4 ::text').extract()

# from the selector, extract cases
cases = sel.css('div.g-table-price ::text').extract()
cases = [i.replace(".", "") for i in cases]
cases = [int(i) for i in cases]

# create date column    
date = [str(datetime.date.today() - datetime.timedelta(days = 1))] * 6
# date = [str(datetime.date.today())] * 6

# %% create daily dataframe
# long format
df_long = pd.DataFrame({'date': date, 'cases': cases, 'categories': categories})
df_long.head()

# wide format
df_wide = df_long.pivot(index = 'date', columns = 'categories', values = 'cases').reset_index()
df_wide.head()

# %% read file with data from past days
df_historical = pd.read_csv('data/covid-san-juan.csv')

# %% get the latest value of 'Total confirmados' as a pandas series to use isin()
last_total_confirmados = pd.Series(df_wide.loc[0, 'Total confirmados'])
# type(last_total_confirmados)
# type(last_total_confirmados.isin(df_historical['Total confirmados']))

# %% check we are not inserting a duplicate
# check if the source dashboard has been updated. If yes, update and save to csv 
# if not, send me an email
if (last_total_confirmados.isin(df_historical['Total confirmados']).bool() == True):
    
    # get email and password from environment variables
    EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
    EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
    EMAIL_RECIPIENT = os.environ.get('EMAIL_RECIPIENT')
    
    # set up email content
    msg = EmailMessage()
    msg['Subject'] = 'GitHub Actions: covid-19-san-juan'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_RECIPIENT
    msg.set_content('Numero de "Total confirmados" igual al dia anterior. El dashboard no esta actualizado.')
    
    # send email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
        
else:
    # append today's data 
    df_historical = df_historical.append(df_wide).sort_values(by = 'date', ascending = False)

    # save updated file 
    df_historical.to_csv('data/covid-san-juan.csv', index = False)