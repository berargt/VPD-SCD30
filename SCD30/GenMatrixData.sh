echo "Date,CO2,°F,RH" > Matrix_Data.csv
tail -n 43200 CO2.dat >> Matrix_Data.csv
