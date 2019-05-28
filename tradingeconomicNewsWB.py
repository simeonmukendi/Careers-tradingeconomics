# -*- coding: utf-8 -*-
"""
Created on Wed May 22 12:07:59 2019

@author: User
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import tradingeconomics as te
from IPython.display import display, HTML

te.login()
import json
import html
te.login()
#To get the latest news.

te.getNews(output_type = None)

#To get several countries and indicators.

te.getNews(country =[ 'united states','China'],indicator=['Imports','Exports'])
#It is possible to limit the amount of news by a start index and a limited number of news to get.


te.getNews(country ='united states',indicator='Imports',start=10,limit=5)
#To get the latest articles by several countries and indicators and also with a start index and limit size.
te.getArticles(country =[ 'united states','Portugal'],indicator=['Imports','Interest rate'],start=10,lim=5)
#To get the latest articles by country and within a specific date.
te.getArticles(country = 'united states',initDate='2018-10-10',endDate='2018-10-15')
#To get the latest articles by Id.
te.getArticleId(id = '26902')
#With no category specified, a list of categories will be provided.
te.getWBCategories(category=None)
#To get World Bank data by category.
te.getWBCategories(category = 'Demographics')
#To get World Bank data by category, and page number.
te.getWBCategories(category = 'Demographics',page_number=2)
#To get World Bank data by indicator (series_code).

te.getWBIndicator(series_code = 'usa.fr.inr.rinr')
#To get World Bank data by URL.
te.getWBIndicator(url = '/united-states/real-interest-rate-percent-wb-data.html')
#To get World Bank data by country and page number.
te.getWBCountry(country = 'Portugal',page_number = 3)
#To get Comtrade categories.
te.getCmtCategories(category = None)
#To get Comtrade by country.
te.getCmtCountry(country = 'China')
#o get Comtrade by several countries.
te.getCmtCountry(country = ['China', 'united states', 'japan'])
#To get Comtrade by countries and page number.
te.getCmtCountry(country =['China','Portugal'],page_number=3)
#To get Comtrade by country and page number.
te.getCmtCountry(country ='China', page_number=3)
#To get Comtrade between two countries and page number.
te.getCmtTwoCountries(country1 ='portugal',country2 ='spain', page_number=3)
#To get Comtrade historical data by specific symbol.
te.getCmtHistorical(symbol = 'PRTESP24031')
#To get Federal Reserve snapshots by symbol.

te.getFedRSnaps(symbol = 'AGEXMAK2A647NCEN')
#To get Federal Reserve snapshots by url.

te.getFedRSnaps(url = 'united states''/united-states/white-to-non-white-racial-dissimilarity-index-for-benton-county-ar-fed-data.html')  
#To get Federal Reserve snapshots by country.

te.getFedRSnaps(country = 'united states')   

#To get Federal Reserve snapshots by state.

te.getFedRSnaps(state = 'tennessee')  
#To get Federal Reserve snapshots by county or state and page number.

te.getFedRSnaps(state ='tennesse',page_number = 1)
#To get Federal Reserve snapshots on Pike County, AR.

te.getFedRCounty(output_type = None) 
#To get Federal Reserve historical data by more than one symbol.
te.getFedRHistorical(symbol = [ 'racedisparity005007', '2020ratio002013'] )
#To get Federal Reserve historical data by symbol.

te.getFedRHistorical(symbol = 'racedisparity005007')
#To get Federal Reserve states and counties.
#With no county specified, a list of all states will be provided.

te.getFedRStates(county = 'arkansas')
display(HTML(' <span style="color:green"><h1 style="text-align:center">China and Japan Unemployment Rate and Balance of Trade</h1> </span>  '))

df = te.getCalendarData(country = ['united states', 'china'],  initDate = '2017-01-01', endDate = '2018-01-01', output_type= 'df' )
display(HTML(df.to_html()))
