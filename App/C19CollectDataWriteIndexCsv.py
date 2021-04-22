#!/usr/bin/env python3
#
# C19CollectDataWriteCsv
#
# Prepare the data from Github and produce the csv files for other apps
#

import csv
from datetime import datetime
from dateutil.relativedelta import relativedelta
from dateutil import parser
from geopy.geocoders import Nominatim
import os
import logging
import numpy as np
import pandas as pd
import streamlit as st

import C19CollectDataMain as cd

def writeWriteIndexCsv():


    logging.info('Processing Index')

    index_file_name = cd.CSV_DIRECTORY + '/Index.csv'

    for entry in cd.file_index:
        entry.display_key = entry.country
        if entry.province != "":
            entry.display_key += f", {entry.province}"

    cd.file_index.sort(key=lambda x: x.display_key, reverse=False)

    with open(index_file_name, mode='w') as index_csv_file:
        index_csv_writer = csv.writer(index_csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        index_csv_writer.writerow(['display_key', 'combined_key', 'file_name', 'country', 'province','latitude','longitude','population'])    
        for entry in cd.file_index:
            index_csv_writer.writerow([entry.display_key, entry.combined_key, entry.file_name, entry.country, entry.province, entry.latitude, entry.longitude, entry.population])