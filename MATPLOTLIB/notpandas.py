#!/usr/bin/python

import pandas as pd
import numpy as np
import datetime
import random

a1 = pd.to_datetime([
    '6/1/2020 10:56',
    '6-2-2020',
    datetime.datetime(2020, 6,3),
    np.datetime64('2020-06-04'),
    np.datetime64('2020-06-05')])

print (a1)
