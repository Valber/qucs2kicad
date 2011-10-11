# -*- coding: UTF-8 -*-
'''
Здесь описаны функции преобразования компонентов

GPLv2
'''
#15.08.2011 введем коэффициент масштабирования km , на который будут домножаться координаты, т.к. при преобразовании картинка слишком расползается
#походу выгодней действительно использовать 10 т.к индуктивность переноситься 1 к 1 и в случае если использовать другой km квадрат из индуктивностей в qucs
#сломаеться в kiCAD


def resistor(x):
	km=10
	kistr='$Comp\n'
	kistr=kistr+'L '+ 'R' +' '+x[1]+'\n'
	kistr=kistr+'U 1 1 4E44605E\n' #для чего нужна временная метка и как её генерить, пока пробовал выставить одинаковые... никто не ругается
	kistr=kistr+'P '+x[3]+'0 '+x[4]+'0\n' #просто добавляем нули... пока что
	kistr=kistr+'F 0 "'+x[1]+'" V '+str(int(x[3])*km+80)+' '+str(int(x[4])*km)+' 50  0000 C CNN\n'
	kistr=kistr+'F 1 '+x[9]+' '+x[10]+' V '+str(int(x[3])*km)+' '+str(int(x[4])*km)+' 50  0000 C CNN\n'
	kistr=kistr+'\t1    '+str(int(x[3])*km)+' '+str(int(x[4])*km)+'\n'
	if x[8]=='1':
		kistr=kistr+'\t'+'1    0    0    -1   \n' #это повороты и отражения
	elif x[8]=='2':
		kistr=kistr+'\t'+'0    -1   -1   0   \n' #это повороты и отражения
	elif x[8]=='3':
		kistr=kistr+'\t'+'-1   0    0    1   \n' #это повороты и отражения
	else :
		kistr=kistr+'\t'+'0    1    1    0   \n' #это повороты и отражения

	kistr=kistr+'$EndComp\n'
	return kistr

def capsicator(x):
	km=10
	kistr='$Comp\n'
	kistr=kistr+'L '
	if x[14]=='"neutral"':
		kistr=kistr+'C' +' '+x[1]+'\n'
	else:
		kistr=kistr+'CP1' +' '+x[1]+'\n'

	kistr=kistr+'U 1 1 4E44605E\n' #для чего нужна временная метка и как её генерить, пока пробовал выставить одинаковые... никто не ругается
	kistr=kistr+'P '+x[3]+'0 '+x[4]+'0\n' #простой способ *10
	kistr=kistr+'F 0 "'+x[1]+'" V '+str(int(x[3])*km+50)+' '+str(int(x[4])*km+100)+' 50  0000 C CNN\n'
	kistr=kistr+'F 1 '+x[9]+' '+x[10]+' V '+str(int(x[3])*km+50)+' '+str(int(x[4])*km-100)+' 50  0000 C CNN\n'
	kistr=kistr+'\t1    '+str(int(x[3])*km)+' '+str(int(x[4])*km)+'\n'
	if x[8]=='1':
		kistr=kistr+'\t'+'1    0    0    1   \n' #это повороты и отражения
	elif x[8]=='2':
		kistr=kistr+'\t'+'0    1   -1   0   \n' #это повороты и отражения
	elif x[8]=='3':
		kistr=kistr+'\t'+'-1   0    0    -1   \n' #это повороты и отражения
	else :
		kistr=kistr+'\t'+'0    -1    1    0   \n' #это повороты и отражения

	kistr=kistr+'$EndComp\n'
	return kistr

def inductance(x):
	km=10
	kistr='$Comp\n'
	kistr=kistr+'L '+ 'INDUCTOR' +' '+x[1]+'\n'
	kistr=kistr+'U 1 1 4E44605E\n' #для чего нужна временная метка и как её генерить, пока пробовал выставить одинаковые... никто не ругается
	kistr=kistr+'P '+x[3]+'0 '+x[4]+'0\n' #просто добавляем нули... пока что
	kistr=kistr+'F 0 "'+x[1]+'" V '+str(int(x[3])*km-50)+' '+str(int(x[4])*km)+' 40  0000 C CNN\n'
	kistr=kistr+'F 1 '+x[9]+' '+x[10]+' V '+str(int(x[3])*km+100)+' '+str(int(x[4])*km)+' 40  0000 C CNN\n'
	kistr=kistr+'\t1    '+str(int(x[3])*km)+' '+str(int(x[4])*km)+'\n'
	if x[8]=='1':
		kistr=kistr+'\t'+'1    0    0    -1   \n' #это повороты и отражения
	elif x[8]=='2':
		kistr=kistr+'\t'+'0    -1   -1   0   \n' #это повороты и отражения
	elif x[8]=='3':
		kistr=kistr+'\t'+'-1   0    0    1   \n' #это повороты и отражения
	else :
		kistr=kistr+'\t'+'0    1    1    0   \n' #это повороты и отражения

	kistr=kistr+'$EndComp\n'
	return kistr

def diode(x):
	km=10
	kistr='$Comp\n'
	kistr=kistr+'L '
	if x[-2]=='"Zener"':
		kistr=kistr+'DIODE' +' '+x[1]+'\n'
	elif x[-2]=='"Schottky"':
		kistr=kistr+'DIODESCH' +' '+x[1]+'\n'
#	elif x[-2]=='"Varactor"':
#		kistr=kistr+'VARICAP' +' '+x[1]+'\n'
	else:
		kistr=kistr+'DIODE' +' '+x[1]+'\n'

	kistr=kistr+'U 1 1 4E44605E\n' #для чего нужна временная метка и как её генерить, пока пробовал выставить одинаковые... никто не ругается
	kistr=kistr+'P '+x[3]+'0 '+x[4]+'0\n' #просто добавляем нули... пока что
	kistr=kistr+'F 0 "'+x[1]+'" H '+str(int(x[3])*km)+' '+str(int(x[4])*km+100)+' 40  0000 C CNN\n' 
	kistr=kistr+'F 1 '+x[-2]+' H '+str(int(x[3])*km)+' '+str(int(x[4])*km-100)+' 40  0000 C CNN\n' #Здесь нечего писать
	kistr=kistr+'\t1    '+str(int(x[3])*km)+' '+str(int(x[4])*km)+'\n'
	if x[8]=='1':
		kistr=kistr+'\t'+'0    1    1    0   \n' #это повороты и отражения
	elif x[8]=='2':
		kistr=kistr+'\t'+'1    0    0    -1   \n' #это повороты и отражения
	elif x[8]=='3':
		kistr=kistr+'\t'+'0    -1   -1   0   \n' #это повороты и отражения
	else :
		kistr=kistr+'\t'+'-1   0    0    1   \n' #это повороты и отражения

	kistr=kistr+'$EndComp\n'
	return kistr

def transistor(x):
	km=10
	kistr='$Comp\n'
	kistr=kistr+'L '
	if x[9]=='"npn"':
		kistr=kistr+'NPN' +' '+'Q'+x[1][1:]+'\n'
	else:
		kistr=kistr+'PNP' +' '+'Q'+x[1][1:]+'\n'
	if x[8]=='0':
		x0=str(int(x[3])*km-100)
		y0=str(int(x[4])*km)
	elif x[8]=='1':
		x0=str(int(x[3])*km)
		y0=str(int(x[4])*km+100)
	elif x[8]=='2':
		x0=str(int(x[3])*km+100)
		y0=str(int(x[4])*km)
	else	:
		x0=str(int(x[3])*km)
		y0=str(int(x[4])*km-100)
	kistr=kistr+'U 1 1 4E44605E\n' #для чего нужна временная метка и как её генерить, пока пробовал выставить одинаковые... никто не ругается
	kistr=kistr+'P '+x[3]+'0 '+x[4]+'0\n' #просто добавляем нули... пока что
	kistr=kistr+'F 0 "'+'Q'+x[1][1:]+'" H '+x0+' '+str(int(y0)-150)+' 50  0000 R CNN\n' 
	kistr=kistr+'F 1 '+x[9]+' H '+x0+' '+str(int(y0)+150)+' 50  0000 R CNN\n' 
	kistr=kistr+'\t1    '+x0+' '+y0+'\n'
	if x[8]=='1':
		kistr=kistr+'\t'+'0    -1    -1    0   \n' #это повороты и отражения
	elif x[8]=='2':
		kistr=kistr+'\t'+'-1    0    0    1   \n' #это повороты и отражения
	elif x[8]=='3':
		kistr=kistr+'\t'+'0    1   1   0   \n' #это повороты и отражения
	else :
		kistr=kistr+'\t'+'1   0    0    -1   \n' #это повороты и отражения

	kistr=kistr+'$EndComp\n'
	return kistr

def gnd(x):
	km=10
	kistr='$Comp\n'
	kistr=kistr+'L '+ 'GND' +' '+'PWR?'+'\n'
	kistr=kistr+'U 1 1 4E44605E\n' #для чего нужна временная метка и как её генерить, пока пробовал выставить одинаковые... никто не ругается
	kistr=kistr+'P '+x[3]+'0 '+x[4]+'0\n' #просто добавляем нули... пока что
	kistr=kistr+'F 0 "'+'"#PWR?"'+' H '+str(int(x[3])*km)+' '+str(int(x[4])*km)+' 30  0000 C CNN\n'
	kistr=kistr+'F 1 '+'"GND"'+' H '+str(int(x[3])*km)+' '+str(int(x[4])*km-70)+' 30  0000 C CNN\n'
	kistr=kistr+'\t1    '+str(int(x[3])*km)+' '+str(int(x[4])*km)+'\n'
	if x[8]=='1':
		kistr=kistr+'\t'+'0    -1    -1    0   \n' #это повороты и отражения
	elif x[8]=='2':
		kistr=kistr+'\t'+'-1    0    0    1   \n' #это повороты и отражения
	elif x[8]=='3':
		kistr=kistr+'\t'+'0    1   1   0   \n' #это повороты и отражения
	else :
		kistr=kistr+'\t'+'1   0    0    -1   \n' #это повороты и отражения
	kistr=kistr+'$EndComp\n'
	return kistr
