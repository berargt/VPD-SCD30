#!/usr/bin/python3

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

# Create some mock data
#t = np.arange(0.01, 10.0, 0.01)
#data1 = np.exp(t)
#data2 = np.sin(2 * np.pi * t)

fig, ax2 = plt.subplots()

color = 'tab:red'
#ax1.set_xlabel('time (s)')
#ax1.set_ylabel('VPD CO2 °C RH', color=color)

data['CO2'] = data['CO2']/100
RH_saved = data['RH']
data['RH'] = data['RH']/10

print("%RH median:", RH_saved.median())
print("°F max:", (data['°C'].max()*9/5+32))
print("°F min:", (data['°C'].min()*9/5+32))
print("%RH max:", (RH_saved.max()*9/5+32))
print("%RH min:", (RH_saved.min()*9/5+32))

color = 'tab:purple'
ax2.plot(data['Date'], data['Status'], color=color)
ax2.set_ylabel('Status', color=color)  # we already handled the x-label with ax1
ax2.tick_params(axis='y', labelcolor=color)

ax1 = ax2.twinx()  # instantiate a second axes that shares the same x-axis

ax1.tick_params(axis='y', labelcolor=color)

ax1.plot_date(data['Date'],data['°C'],marker='None',linestyle='solid')
ax1.plot_date(data['Date'],data['VPD'],marker='None',linestyle='solid')
ax1.plot_date(data['Date'],data['CO2'],marker='None',linestyle='solid')
ax1.plot_date(data['Date'],data['RH'],marker='None',linestyle='solid')
ax1.legend(['°C', 'VPD (kPa)', 'CO2/100', 'RH/10'])


plt.gcf().autofmt_xdate()
date_format = mpl_dates.DateFormatter('%d/%m/%Y %H:%M:%S')
plt.gca().xaxis.set_major_formatter(date_format)
plt.grid(which='both', axis='both')

plt.title('Vapor Pressure Deficit')
plt.xlabel('Date')
#plt.ylabel(["VPD, CO2/100, °C"])
#fig.tight_layout()  # otherwise the right y-label is slightly clipped

plt.savefig("VPD.png")
plt.ion
plt.show()
