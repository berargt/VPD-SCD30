# VPD-SCD30
Vapor Pressure Deficit is acquired from an SCD30 CO2 Sensor

The driver was cloned from here;

https://github.com/berargt/VPD-SCD30.git


I have this history from making the driver work;

removed that damn '-l' from pigpiod launch

  973  sudo gvim /lib/systemd/system/pigpiod.service
  974  ps auxw  | grep pig
  975  sudo systemctl stop pigpiod
  976  sytemctl daemon-reload
  977  sudo systemctl daemon-reload
  978  sudo systemctl stop pigpiod
  979  sudo systemctl restart pigpiod
  980  ps auxw  | grep pig
  981  ll
  982  ./scd30-once.py 
  983  sps auxw | system
  984  ps auxw | grep system
  985  ps auxw | grep scd
  986  gvim README.md 
  987  cat /run/sensors/*
  988  ll /run/
  989  ps axuw | grep scd
  990  ll
  991  sudo systemctl enable scd30.service
  992  sudo systemctl restart scd30
  993  sudo systemctl status scd30
  994  ll /run/sensors/scd30/last 
  995  tail -f  /run/sensors/scd30/last 

Directories;

MATPLOTLIB - Plot the data
   root directory contains files that plots all the data. It generates the
   VPD ranges and also plots them

SCD30 - Collect the data











