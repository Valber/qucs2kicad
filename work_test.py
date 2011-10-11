#!/usr/bin/python
# -*- coding: UTF-8 -*-
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
	#~ print n
	#~ print "wires"
	#~ print wirs
	for j in wirs:
		if (pnt==j[0]) or (pnt==j[1]):
				if (j[0][0]==wire[1][0] and j[0][0]==wire[0][0] and j[1][0]==wire[0][0] and j[1][0]==wire[1][0]) or (j[0][1]==wire[1][1] and j[0][1]==wire[0][1] and j[1][1]==wire[0][1] and j[1][1]==wire[1][1]):
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
				else:
					rang=rang+1
					if rang>=2:
						conn=1
	out.append(chng)
	out.append(wire)
	out.append(conn)
	out.append(wirs)
	return out
	
#Примерчик
A=[[[5,7],[7,7]],[[7,7],[7,6]],[[7,6],[9,6]],[[9,6],[10,6]],[[10,6],[12,6]],[[12,6],[12,8]],[[12,6],[12,4]],[[12,6],[14,6]]]
Pts=[]
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
		if C[2]==1:
			Pts.append(p)
		i=C[1]
		ost.append(C[1])
		ost=ost+C[3]
		#print ost
		A=ost
		#~ print "Out"
		#~ print A
	a=a+1
print A
print Pts
