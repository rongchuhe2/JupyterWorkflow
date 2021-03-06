import os
import requests

import pandas as pd

FREMONT_URL = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'

def get_fremont_data(filename='Fremont.csv', url=FREMONT_URL,
                     force_download=False):
    """ Download and Cache the Fremont Data

    Parameters
    -------------
    filename : string (optional)
         location to save the data
    url : string (optional)
         web location of the data
    force_download : bool (optional)
         if true, force redownload of data

    Returns
    =====
    data : pandas.DataFrame
            The fremont bridge data
    """
    if force_download or not os.path.exists(filename):
        response = requests.get(URL)
        with open('Fremont.csv', 'wb') as f:
            f.write(response.content)

    data = pd.read_csv('Fremont.csv', index_col='Date')
    try:
        data.index = pd.to_datetime(data.index, format='%m/%d/%Y %H:%M:%S %p')
    except TypeError:
        data.index = pd.to_datetime(data.index)            
    # data = pd.read_csv('Fremont.csv', index_col='Date', parse_dates=True)
    data.columns = ['West', 'East']
    data['Total'] = data['West'] + data['East']
    return data
