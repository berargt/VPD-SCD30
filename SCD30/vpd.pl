#!/usr/bin/perl

use strict;
use warnings;

my $timedate;
my $CO2;
my $temp;
my $rh;
my $tdew;
my $X; # intermediate variable dewpoint calc
my $vp_act;
my $vp_sat;
my $stage = "";
my $vpd;


printf("Date,Status,CO2,°C,RH,DP,VPAct,VPSat,VPD\n");

while (<STDIN>) {

	($timedate, $CO2, $temp, $rh) = split(',', $_);
	chomp $rh;
#	printf("%0.2f ", $temp);
	$temp	= ($temp - 32)*5/9;
	$X = log($rh/100)+((17.269*$temp)/(237.3+$temp));
	$tdew = (237.3*$X)/(17.269-$X);
	$vp_act = 6.11*10**(7.5*$tdew/(237.3+$tdew));
	$vp_act = $vp_act;
	$vp_sat = 6.11*10**(7.5*$temp/(237.3+$temp));
	$vp_sat = $vp_sat;
	$vpd = ($vp_sat - $vp_act);

	# https://growingmarijuanaperfectly.com/2020/07/17/understanding-vapor-pressure-deficit-the-weird-humidity-puzzle-in-marijuana-growing/ 
	if ($vpd < 4.5) {
		$stage = "LO";
	}
	elsif ($vpd > 13.7) {
		$stage = "HI"
	}
	elsif ($vpd>=4.5 && $vpd<=7.4) {
		$stage = "Prop"; 
	}
	elsif ($vpd> 7.4 && $vpd<=10.6) {
		$stage = "Early"; # Flower
	}
	elsif ($vpd>10.6 && $vpd<=13.7) {
		$stage = "Mid/Late"; # Flower
	}
		
	printf("%s,%s,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f,%.2f\n", $timedate, $stage, $CO2, $temp, $rh, $tdew, $vp_act, $vp_sat, $vpd);
}
