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
P 3800 3800
F 0 "R1" V 3880 3800 50  0000 C CNN
F 1 "50 Ohm" V 3800 3800 50  0000 C CNN
	1    3800 3800
	0    1    1    0   
$EndComp
$Comp
L C C1
U 1 1 4E44605E
P 3700 2900
F 0 "C1" V 3750 3000 50  0000 C CNN
F 1 "1 pF" V 3750 2800 50  0000 C CNN
	1    3700 2900
	0    -1    1    0   
$EndComp
$Comp
L INDUCTOR L1
U 1 1 4E44605E
P 3800 1800
F 0 "L1" V 3750 1800 40  0000 C CNN
F 1 "1 nH" V 3900 1800 40  0000 C CNN
	1    3800 1800
	0    1    1    0   
$EndComp
$Comp
L GND PWR?
U 1 1 4E44605E
P 4600 3800
F 0 ""#PWR?" H 4600 3800 30  0000 C CNN
F 1 "GND" H 4600 3730 30  0000 C CNN
	1    4600 3800
	1   0    0    -1   
$EndComp
Wire Wire Line
	4050 3800 4100 3800
Wire Wire Line
	3550 3800 3500 3800
Wire Wire Line
	3900 2900 4000 2900
Wire Wire Line
	3500 2900 3400 2900
Wire Wire Line
	3200 1800 3500 1800
Wire Wire Line
	3200 1800 3200 2900
Wire Wire Line
	3200 2900 3400 2900
Wire Wire Line
	3200 3800 3500 3800
Wire Wire Line
	3200 2900 3200 3800
Wire Wire Line
	4100 3800 4600 3800
Wire Wire Line
	4600 1800 4600 2900
Wire Wire Line
	4100 1800 4600 1800
Wire Wire Line
	4600 2900 4600 3800
Wire Wire Line
	4000 2900 4600 2900
$EndSCHEMATC