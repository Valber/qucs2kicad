# -*- coding: UTF-8 -*-
#Зададим словарь?
import string
import component

qu=open('./simple.sch','r')
ki=open('./sample.sch','w')
wr=open('./wires','w')

#Поехали!
ki.write('EESchema Schematic File Version 2  date Вск 07 Авг 2011 00:36:35\nLIBS:power\nLIBS:device\nLIBS:transistors\nLIBS:conn\nLIBS:linear\nLIBS:regul\nLIBS:74xx\nLIBS:cmos4000\nLIBS:adc-dac\nLIBS:memory\nLIBS:xilinx\nLIBS:special\nLIBS:microcontrollers\nLIBS:dsp\nLIBS:microchip\nLIBS:analog_switches\nLIBS:motorola\nLIBS:texas\nLIBS:intel\nLIBS:audio\nLIBS:interface\nLIBS:digital-audio\nLIBS:philips\nLIBS:display\nLIBS:cypress\nLIBS:siliconi\nLIBS:opto\nLIBS:atmel\nLIBS:contrib\nLIBS:valves\nEELAYER 43  0\nEELAYER END\n$Descr A4 11700 8267\nencoding utf-8\nSheet 1 1\nTitle ""\nDate "9 aug 2011"\nRev ""\nComp ""\nComment1 ""\nComment2 ""\nComment3 ""\nComment4 ""\n$EndDescr\n')	#это все пока не разбираем

#15.08.2011 Структура QUCS файла отличается от kiCAD порядком появления соединений wires в qucs они следуют после компонентов, в kicad до, необходим буффер
#15.08.2011 Да вроде все читается и в обратном порядке(kiCAD поменял порядок wire и component), введу буфер для сохранения всех wire и дальнейшего
#уменьшения их количества после преобразования.

#Считаем файл, обратите внимание на знаки переноса строки... в автоматически созданном файле нет \n в конце файла
S=qu.readline()
print S
while S!='</Paintings>\n':
	#print S
	if S=='<Components>\n':
		S=qu.readline()
		while S!='</Components>\n':
			#Действия по преобразованию			
			s=string.strip(S)	#избавляемся от пробелов до и после
			s=s[1:-1]			
			rs=string.split(s)	#Возможно ошибка в которой у списка сбивается нумерации из-за обработки надписей вроде "5 kOhm" и "5 k Ohm"
			print rs
			if rs[0]=='R':				
				letter=component.resistor(rs) #Выполняем функцию выполняем функцию преобразования
				ki.write(letter)
				if (rs[8]=='0') or (rs[8]=='2'): #По габаритам корректно преобразуется только индуктивность, остальным дописываем хвостики
					letter='Wire Wire Line\n'
					letter=letter+'\t'+str(int(rs[3])*10+250)+' '+str(int(rs[4])*10)+' '
					letter=letter+str(int(rs[3])*10+300)+' '+str(int(rs[4])*10)+'\n'
					letter=letter+'Wire Wire Line\n'
					letter=letter+'\t'+str(int(rs[3])*10-250)+' '+str(int(rs[4])*10)+' '
					letter=letter+str(int(rs[3])*10-300)+' '+str(int(rs[4])*10)+'\n'
				else:
					letter='Wire Wire Line\n'
					letter=letter+'\t'+str(int(rs[3])*10)+' '+str(int(rs[4])*10+250)+' '
					letter=letter+str(int(rs[3])*10)+' '+str(int(rs[4])*10+300)+'\n'
					letter=letter+'Wire Wire Line\n'
					letter=letter+'\t'+str(int(rs[3])*10)+' '+str(int(rs[4])*10-250)+' '
					letter=letter+str(int(rs[3])*10)+' '+str(int(rs[4])*10-300)+'\n'
				wr.write(letter)		
			elif rs[0]=='C':
				letter=component.capsicator(rs)
				ki.write(letter)
				if (rs[8]=='0') or (rs[8]=='2'): #По габаритам корректно преобразуется только индуктивность, остальным дописываем хвостики
					letter='Wire Wire Line\n'
					letter=letter+'\t'+str(int(rs[3])*10+200)+' '+str(int(rs[4])*10)+' '
					letter=letter+str(int(rs[3])*10+300)+' '+str(int(rs[4])*10)+'\n'
					letter=letter+'Wire Wire Line\n'
					letter=letter+'\t'+str(int(rs[3])*10-200)+' '+str(int(rs[4])*10)+' '
					letter=letter+str(int(rs[3])*10-300)+' '+str(int(rs[4])*10)+'\n'
				else:
					letter='Wire Wire Line\n'
					letter=letter+'\t'+str(int(rs[3])*10)+' '+str(int(rs[4])*10+200)+' '
					letter=letter+str(int(rs[3])*10)+' '+str(int(rs[4])*10+300)+'\n'
					letter=letter+'Wire Wire Line\n'
					letter=letter+'\t'+str(int(rs[3])*10)+' '+str(int(rs[4])*10-200)+' '
					letter=letter+str(int(rs[3])*10)+' '+str(int(rs[4])*10-300)+'\n'
				wr.write(letter)
			elif rs[0]=='L':
				letter=component.inductance(rs)
				ki.write(letter)
			elif rs[0]=='Diode':
				letter=component.diode(rs)
				ki.write(letter)				
				if (rs[8]=='0') or (rs[8]=='2'):
					letter='Wire Wire Line\n'
					letter=letter+'\t'+str(int(rs[3])*10+200)+' '+str(int(rs[4])*10)+' '
					letter=letter+str(int(rs[3])*10+300)+' '+str(int(rs[4])*10)+'\n'
					letter=letter+'Wire Wire Line\n'
					letter=letter+'\t'+str(int(rs[3])*10-200)+' '+str(int(rs[4])*10)+' '
					letter=letter+str(int(rs[3])*10-300)+' '+str(int(rs[4])*10)+'\n'
				else:
					letter='Wire Wire Line\n'
					letter=letter+'\t'+str(int(rs[3])*10)+' '+str(int(rs[4])*10+200)+' '
					letter=letter+str(int(rs[3])*10)+' '+str(int(rs[4])*10+300)+'\n'
					letter=letter+'Wire Wire Line\n'
					letter=letter+'\t'+str(int(rs[3])*10)+' '+str(int(rs[4])*10-200)+' '
					letter=letter+str(int(rs[3])*10)+' '+str(int(rs[4])*10-300)+'\n'
				wr.write(letter)
			elif rs[0]=='_BJT':
				letter=component.transistor(rs)
				ki.write(letter)
				if (rs[8]=='1') or (rs[8]=='3'): 
					letter='Wire Wire Line\n'
					letter=letter+'\t'+str(int(rs[3])*10+200)+' '+str(int(rs[4])*10)+' '
					letter=letter+str(int(rs[3])*10+300)+' '+str(int(rs[4])*10)+'\n'
					letter=letter+'Wire Wire Line\n'
					letter=letter+'\t'+str(int(rs[3])*10-200)+' '+str(int(rs[4])*10)+' '
					letter=letter+str(int(rs[3])*10-300)+' '+str(int(rs[4])*10)+'\n'
				else:
					letter='Wire Wire Line\n'
					letter=letter+'\t'+str(int(rs[3])*10)+' '+str(int(rs[4])*10+200)+' '
					letter=letter+str(int(rs[3])*10)+' '+str(int(rs[4])*10+300)+'\n'
					letter=letter+'Wire Wire Line\n'
					letter=letter+'\t'+str(int(rs[3])*10)+' '+str(int(rs[4])*10-200)+' '
					letter=letter+str(int(rs[3])*10)+' '+str(int(rs[4])*10-300)+'\n'
				wr.write(letter)
			elif rs[0]=='GND':
				letter=component.gnd(rs)
				ki.write(letter)
			S=qu.readline()
	
	if S=='<Wires>\n':
		S=qu.readline()
		while S!='</Wires>\n':
			#Действия по преобразованию соединений
			s=string.strip(S)	#избавляемся от пробелов до и после
			s=s[1:-1]			
			rs=string.split(s)	#Возможно ошибка в которой у списка сбивается нумерации из-за обработки надписей вроде "5 kOhm" и "5 k Ohm"
			print rs
			letter='Wire Wire Line\n'
			letter=letter+'\t'+str(int(rs[0])*10)+' '+str(int(rs[1])*10)+' '+str(int(rs[2])*10)+' '+str(int(rs[3])*10)+'\n'
			wr.write(letter)
			#if rs[0]=='R':
			S=qu.readline()
	S=qu.readline()
else:
	print S	#вот тут мы и будем сливать буфер!
	wr.close()
	wr=open('./wires','r')
	S=wr.readline()
	while S!='':
		ki.write(S)
		S=wr.readline()

ki.write('$EndSCHEMATC')

qu.close()
ki.close()
