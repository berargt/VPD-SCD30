#!/usr/bin/python3

import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from matplotlib import dates as mpl_dates
import pandas as pd
import csv

plt.xkcd()

#Date,Status,CO2,°C,RH,DP,VPAct,VPSat,VPD
data = pd.read_csv('DHT.csv')
data['Date'] = pd.to_datetime(data['Date'])
data.sort_values('Date', inplace=True)

# Create some mock data
#t = np.arange(0.01, 10.0, 0.01)
#data1 = np.exp(t)
#data2 = np.sin(2 * np.pi * t)

fig, ax1 = plt.subplots()

color = 'tab:red'
#ax1.set_xlabel('time (s)')
#ax1.set_ylabel('VPD CO2 °C RH', color=color)

#data['CO2'] = data['CO2']/100
#data['RH'] = data['RH']/10

print(data['RH'].mean())
print(data['°F'].max()*9/5+32)
print(data['°F'].min()*9/5+32)

ax1.plot_date(data['Date'],data['°F'],marker='None',linestyle='solid')
ax1.plot_date(data['Date'],data['RH'],marker='None',linestyle='solid')
ax1.legend(['°F', 'RH'])

ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

#color = 'tab:purple'
#ax2.set_ylabel('Status', color=color)  # we already handled the x-label with ax1
#ax2.plot(data['Date'], data['Status'], color=color)
#ax2.tick_params(axis='y', labelcolor=color)

plt.gcf().autofmt_xdate()
date_format = mpl_dates.DateFormatter('%d/%m/%Y %H:%M:%S')
plt.gca().xaxis.set_major_formatter(date_format)
plt.grid(which='both', axis='both')

plt.title('°F & %RH')
plt.xlabel('Date')
#plt.ylabel(["VPD, CO2/100, °C"])
#fig.tight_layout()  # otherwise the right y-label is slightly clipped

plt.savefig("DHT.png")
plt.ion
plt.show()
