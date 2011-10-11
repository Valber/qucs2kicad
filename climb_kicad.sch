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
L R R2
U 1 1 4E44605E
P 2800 2400
F 0 "R2" V 2880 2400 50  0000 C CNN
F 1 "50 Ohm" V 2800 2400 50  0000 C CNN
	1    2800 2400
	0    1    1    0   
$EndComp
$Comp
L C C1
U 1 1 4E44605E
P 4500 1700
F 0 "C1" V 4550 1800 50  0000 C CNN
F 1 "1 pF" V 4550 1600 50  0000 C CNN
	1    4500 1700
	0    -1    1    0   
$EndComp
$Comp
L R R1
U 1 1 4E44605E
P 2800 900
F 0 "R1" V 2880 900 50  0000 C CNN
F 1 "50 Ohm" V 2800 900 50  0000 C CNN
	1    2800 900
	0    1    1    0   
$EndComp
Wire Wire Line
	3050 2400 3600 2400
Wire Wire Line
	2550 2400 2100 2400
Wire Wire Line
	4700 1700 5600 1700
Wire Wire Line
	4300 1700 3600 1700
Wire Wire Line
	3050 900 3600 900
Wire Wire Line
	2550 900 2100 900
Wire Wire Line
	2100 900 2100 2400
Wire Wire Line
	3600 900 3600 2400
Wire Wire Line
	5600 1700 5600 3300
Wire Wire Line
	600 3300 5600 3300
Wire Wire Line
	600 1700 600 3300
Wire Wire Line
	600 1700 2100 1700
Wire Wire Line
	2100 3300 2100 4600
Wire Wire Line
	2100 4600 2500 4600
Wire Wire Line
	2500 4200 2500 4600
Wire Wire Line
	2500 4200 4200 4200
Wire Wire Line
	4200 3300 4200 4200
Connection ~ 2100 1700
Connection ~ 3600 1700
Connection ~ 2100 3300
Connection ~ 4200 3300
$EndSCHEMATC