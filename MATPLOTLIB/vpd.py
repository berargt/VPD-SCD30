#!/usr/bin/python

import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from matplotlib import dates as mpl_dates
import pandas as pd
import csv

#plt.style.use('seaborn')
#plt.style.use("fivethirtyeight")
plt.xkcd()

#Date,Status,CO2,°C,RH,DP,VPAct,VPSat,VPD
data = pd.read_csv('VPD.csv')
data['Date'] = pd.to_datetime(data['Date'])
data.sort_values('Date', inplace=True)

plt.figure(figsize=(18, 9))

data['CO2'] = data['CO2']/100
data['RH'] = data['RH']/10

plt.plot_date(data['Date'],data['Status'],marker='None',linestyle='solid')
plt.plot_date(data['Date'],data['VPD'],marker='None',linestyle='solid')
plt.plot_date(data['Date'],data['CO2'],marker='None',linestyle='solid')
plt.plot_date(data['Date'],data['°C'],marker='None',linestyle='solid')
plt.plot_date(data['Date'],data['RH'],marker='None',linestyle='solid')

plt.gcf().autofmt_xdate()
date_format = mpl_dates.DateFormatter('%d/%m/%Y %H:%M:%S')
plt.gca().xaxis.set_major_formatter(date_format)
plt.grid(which='both', axis='both')

#plt.tight_layout()

plt.title('Vapor Pressure Deficit')
plt.xlabel('Date')
#plt.ylabel(["VPD, CO2/100, °C"])
plt.legend(['VPD (kPa)', 'CO2/100', '°C', 'RH/10'])

plt.savefig("VPD.png")
plt.show()
