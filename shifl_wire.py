#!/usr/bin/python
# -*- coding: UTF-8 -*-
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

#Функция для уменьшения количества проводников при конвертации форматов
import string

def shifl (wire,n,wirs):
	out=[]
	chng=0
	pnt=wire[n]
	rang=0
	conn=0
	#~ print "########################################"
	#~ print "wire"
	#~ print wire
	#~ print "point"
	#~ print wire(n)
	#~ print "wires"
	#~ print wirs
	for j in wirs:
		if (pnt==j[0]) or (pnt==j[1]):
			#~ rang=rang+1
			if (j[0][0]==wire[1][0] and j[0][0]==wire[0][0] and j[1][0]==wire[0][0] and j[1][0]==wire[1][0]) or (j[0][1]==wire[1][1] and j[0][1]==wire[0][1] and j[1][1]==wire[0][1] and j[1][1]==wire[1][1])and (chng==0):
				if wire[1]==j[1]:
					wire=[wire[0],j[0]]
				elif wire[1]==j[0]:	
					wire=[wire[0],j[1]]
				elif wire[0]==j[1]:	
					wire=[wire[1],j[0]]
				elif wire[0]==j[0]:	
					wire=[wire[1],j[1]]
				wirs.remove(j)
				chng=1
			
			
	out.append(chng)
	out.append(wire)
	out.append(wirs)
	return out

#271.9 мбайт,79.7
#берем первый проводник первую точку смотрим оставшиеся проводники используя счетчик совпадений
#если совпадений нет или у нас ситуация --УГОЛ ,то не делаем ничего в случае --ПРЯМОЙ производим видоизменение
#проводника и досчитываем оставшиеся проводники , если тройник или четверник добавляеться запись connection~
#далее если было произведено объединение начинаем с объединенного проводника с новой точки
#если не было объединений то проверяем другую точку проводника.	

def wirecomp(address_file_wire):
	wirefile=address_file_wire
	outfile=address_file_wire
	f=open(wirefile,'r')
	A=[]
	S=f.readline()
	while S!='':
		S=string.strip(S)
		coord=string.split(S)
		if coord!=['Wire', 'Wire', 'Line']:
			A.append([coord[:2],coord[2:]])
		S=f.readline()
	f.close()
	print "###############################################################"
	Pts=[]
	C=[]
	for i in A:
		C.append(i[0])
		C.append(i[1])
	for i in C:
		a=C.count(i)
		if a>2:
			Pts.append(i)
		for j in range(a):
			C.remove(i)
	a=0
	while (a<(len(A)-1)):
		ind=0
		i=A[a]
		while(ind!=2):
			p=i[ind]
			ost=A[:a]
			C=shifl(i,ind,A[(a+1):])
			if C[0]==0:
				ind=ind+1
			i=C[1]
			ost.append(C[1])
			ost=ost+C[2]
			A=ost
		a=a+1
	
	#этот кусок записывает преобразованную информацию
	out=open(outfile,'w')
	print "Number wires ",len(A)," Node number " ,len(Pts)
	for i in A:
		out.write("Wire Wire Line\n")
		str="\t"+i[0][0]+" "+i[0][1]+" "+i[1][0]+" "+i[1][1]+"\n"
		out.write(str)
	for i in Pts:
		str="Connection ~ "+i[0]+" "+i[1]+"\n"
		out.write(str)
	out.close()
	
	print "######################################################"
	print A
