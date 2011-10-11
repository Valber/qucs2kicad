EESchema Schematic File Version 2  date Вск 07 Авг 2011 00:36:35
LIBS:power
LIBS:device
LIBS:transistors
LIBS:conn
LIBS:linear
LIBS:regul
LIBS:74xx
LIBS:cmos4000
LIBS:adc-dac
LIBS:memory
LIBS:xilinx
LIBS:special
LIBS:microcontrollers
LIBS:dsp
LIBS:microchip
LIBS:analog_switches
LIBS:motorola
LIBS:texas
LIBS:intel
LIBS:audio
LIBS:interface
LIBS:digital-audio
LIBS:philips
LIBS:display
LIBS:cypress
LIBS:siliconi
LIBS:opto
LIBS:atmel
LIBS:contrib
LIBS:valves
EELAYER 43  0
EELAYER END
$Descr A4 11700 8267
encoding utf-8
Sheet 1 1
Title ""
Date "9 aug 2011"
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L R R1
U 1 1 4E44605E
P 3800 4700
F 0 "R1" V 3880 4700 50  0000 C CNN
F 1 "50 Ohm" V 3800 4700 50  0000 C CNN
	1    3800 4700
	1    0    0    -1   
$EndComp
$Comp
L DIODE D1
U 1 1 4E44605E
P 3800 6400
F 0 "D1" H 3800 6500 40  0000 C CNN
F 1 "normal" H 3800 6300 40  0000 C CNN
	1    3800 6400
	0    -1   -1   0   
$EndComp
$Comp
L R R2
U 1 1 4E44605E
P 5200 4700
F 0 "R2" V 5280 4700 50  0000 C CNN
F 1 "50 Ohm" V 5200 4700 50  0000 C CNN
	1    5200 4700
	1    0    0    -1   
$EndComp
$Comp
L GND PWR?
U 1 1 4E44605E
P 5200 7100
F 0 ""#PWR?" H 5200 7100 30  0000 C CNN
F 1 "GND" H 5200 7030 30  0000 C CNN
	1    5200 7100
	1   0    0    -1   
$EndComp
$Comp
L NPN Q1
U 1 1 4E44605E
P 5200 5800
F 0 "Q1" H 5100 5650 50  0000 R CNN
F 1 "npn" H 5100 5950 50  0000 R CNN
	1    5100 5800
	1   0    0    -1   
$EndComp
$Comp
L CP1 C1
U 1 1 4E44605E
P 2500 6400
F 0 "C1" V 2550 6500 50  0000 C CNN
F 1 "1 pF" V 2550 6300 50  0000 C CNN
	1    2500 6400
	-1   0    0    -1   
$EndComp
$Comp
L GND PWR?
U 1 1 4E44605E
P 2500 7100
F 0 ""#PWR?" H 2500 7100 30  0000 C CNN
F 1 "GND" H 2500 7030 30  0000 C CNN
	1    2500 7100
	1   0    0    -1   
$EndComp
$Comp
L INDUCTOR L1
U 1 1 4E44605E
P 6400 4700
F 0 "L1" V 6350 4700 40  0000 C CNN
F 1 "1 nH" V 6500 4700 40  0000 C CNN
	1    6400 4700
	1    0    0    -1   
$EndComp
$Comp
L C C2
U 1 1 4E44605E
P 7200 4700
F 0 "C2" V 7250 4800 50  0000 C CNN
F 1 "1 pF" V 7250 4600 50  0000 C CNN
	1    7200 4700
	1    0    0    1   
$EndComp
Wire Wire Line
	3800 4950 3800 5000
Wire Wire Line
	3800 4450 3800 4400
Wire Wire Line
	3800 6600 3800 6700
Wire Wire Line
	3800 6200 3800 6100
Wire Wire Line
	5200 4950 5200 5000
Wire Wire Line
	5200 4450 5200 4400
Wire Wire Line
	5200 6000 5200 6100
Wire Wire Line
	5200 5600 5200 5500
Wire Wire Line
	2500 6600 2500 6700
Wire Wire Line
	2500 6200 2500 6100
Wire Wire Line
	7200 4900 7200 5000
Wire Wire Line
	7200 4500 7200 4400
Wire Wire Line
	2500 6700 3800 6700
Wire Wire Line
	2500 6700 2500 7100
Wire Wire Line
	2500 6100 3800 6100
Wire Wire Line
	3800 5000 3800 5800
Wire Wire Line
	3800 5800 3800 6100
Wire Wire Line
	3800 5800 4900 5800
Wire Wire Line
	3800 4400 5200 4400
Wire Wire Line
	5200 5000 5200 5500
Wire Wire Line
	5200 6100 5200 7100
Wire Wire Line
	5200 4400 6400 4400
Wire Wire Line
	6400 4400 7200 4400
Wire Wire Line
	6400 5000 7200 5000
Wire Wire Line
	5200 5000 6400 5000
$EndSCHEMATC