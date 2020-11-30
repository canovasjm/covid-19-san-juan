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

# %% target website
url = "https://sisanjuan.gob.ar/modulo-coronavirus"

# make GET request
html = requests.get(url).content

# create scrapy selector
sel = Selector(text = html)
print("The number of elements in the HTML is: ", len(sel.xpath('//*')))

# from the selector, extract categories and cases
categories = sel.css('.g-table-title h4 ::text').extract()
cases = sel.css('div.g-table-price ::text').extract()
date = [str(datetime.date.today() - datetime.timedelta(days = 1))] * 6
# date = [str(datetime.date.today())] * 6


# %% create daily dataframe
# tall format
df_tall = pd.DataFrame({'date': date, 'cases': cases, 'categories': categories})
df_tall.head()

# wide format
df_wide = df_tall.pivot(index = 'date', columns = 'categories', values = 'cases').reset_index()
df_wide.head()

# %% update and save to csv
# read file with data from past days
df_historical = pd.read_csv('data/covid-san-juan.csv')

# append today's data
df_historical = df_historical.append(df_wide).sort_values(by = 'date', ascending = False)

# save updated file 
df_historical.to_csv('data/covid-san-juan.csv', index = False)
