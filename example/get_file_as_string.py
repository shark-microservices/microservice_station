#!/usr/bin/env python
# Copyright (c) 2022 SMHI, Swedish Meteorological and Hydrological Institute.
# License: MIT License (see LICENSE.txt or http://opensource.org/licenses/mit).
"""
Created on 2022-03-11 14:51

@author: johannes
"""
import requests
from io import StringIO
import pandas as pd
import time

if __name__ == '__main__':
    url = r'http://127.0.0.1:8010/file'
    start_time = time.time()
    response = requests.request("GET", url)
    print("Timeit:--%.5f sec" % (time.time() - start_time))
    start_time = time.time()
    # Store string data in a pandas Dataframe.
    df = pd.read_csv(
        StringIO(response.text),
        sep='\t',
        header=0,
        encoding='cp1252',
        dtype=str,
        keep_default_na=False,
    )
    print("Timeit:--%.5f sec" % (time.time() - start_time))
