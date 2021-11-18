#!/usr/bin/bash

./GenPltData.sh
./GenMatrixData.sh

cp Matrix_Data.csv ../MATPLOTLIB/VPD_MATRIX_PLOT/
cp VPD.csv ../MATPLOTLIB/
