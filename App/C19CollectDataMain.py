#!/usr/bin/env python3
#
# CovidDataMain.py
#
# Prepare the data from Github and produce the csv files for other apps
#

from datetime import datetime
from dateutil.relativedelta import relativedelta
from dateutil import parser
from geopy.geocoders import Nominatim
import os
import logging
import numpy as np
import pandas as pd

import C19CollectDataGlobalTimeSeries as gts
import C19CollectDataGlobalRollup as gpr
import C19CollectDataUSStates as uss
import C19CollectDataWriteIndexCsv as wcs

# ----------------------------------------------------------------------------
# Constants
# ----------------------------------------------------------------------------

BASE_DIRECTORY  = '/Users/paulhart/GitHubWork/BC-Covid-19-Data/'
CSV_URL         = 'https://raw.githubusercontent.com/CSSEGISandData/'
#                  https://raw.githubusercontent.com/CSSEGISandData/
#                                      COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv
#                  https://raw.githubusercontent.com/CSSEGISandData/
#                                      COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv
CSV_DIRECTORY    = BASE_DIRECTORY + 'CSV_Files'

# CONFIRMED_GLOBAL = BASE_DIRECTORY + 'COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
# CONFIRMED_US     = BASE_DIRECTORY + 'COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv'
# DEATHS_GLOBAL    = BASE_DIRECTORY + 'COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
# DEATHS_US        = BASE_DIRECTORY + 'COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv'

CONFIRMED_GLOBAL = CSV_URL + 'COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
CONFIRMED_US     = CSV_URL + 'COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv'
DEATHS_GLOBAL    = CSV_URL + 'COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
DEATHS_US        = CSV_URL + 'COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv'

WORLD_POP        = BASE_DIRECTORY + 'WorldPop.csv'



# ----------------------------------------------------------------------------
# Global Variables
# ----------------------------------------------------------------------------

global global_keys
global global_new_keys
#global file_index_entry
#global file_index

class file_index_entry():
    combined_key = ''
    file_name = ''
    country = ''
    province = ''
    latitude = ''
    longitude = ''
    population = ''

    def __init__(self, combined_key, file_name, country, province, latitude, longitude, population):
        self.combined_key = combined_key
        self.file_name = file_name
        self.country = country
        self.province = province
        self.latitude = latitude
        self.longitude = longitude
        self.population = population

file_index = []

dfPopulations = pd.read_csv(WORLD_POP)

# ----------------------------------------------------------------------------
# Prepare dataframe
# ----------------------------------------------------------------------------

def process_dataframe():
    ''' Processing global and US state data'''

    dfGlobal = gts.processGlobalDataframe()
    gpr.processProvinceRollup(dfGlobal)
    uss.processUSDataframe()
    wcs.writeWriteIndexCsv()

# ----------------------------------------------------------------------------
# Entry point
# ----------------------------------------------------------------------------

def main():
    df = process_dataframe()

if __name__ == '__main__':
    main()
