#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math 
import matplotlib.pyplot as plt
import collections

#funktion zum plotten von punkten im format [x,y, farbe]

def plotting(clustered_data):
	min_x=""
	max_x=""
	min_y=""
	max_y=""

	for j in clustered_data:
		color=j[2][0]
		plt.plot(j[0], j[1], color+'o' )

		if clustered_data.index(j)==0:
			min_x=j[0]
			max_x=j[0]
			min_y=j[1]
			max_y=j[1]
		else:
			if (j[0]<min_x): min_x=j[0]
			if (j[0]>max_x): max_x=j[0]
			if (j[1]<min_y): min_y=j[1]
			if (j[1]>max_y): max_y=j[1]

	diff_y=float(max_y)-float(min_y)
	plt.ylim( (min_y-1.1*diff_y, max_y+1.1*diff_y) )

	diff_x=float(max_x)-float(min_x)
	plt.xlim( (min_x-1.1*diff_x, max_x+1.1*diff_x) )
	
	plt.show()
	plt.savefig('k-nearest-neighbours')


def get_distances(i):

	#liste mit Distanzen zu punkt i
	dist=list()

	ld_index=0
	max_val=0

	# iterieren durch labled data
	for ld in labled_data:
		
		this_dist=float()
		for  n in range (0, len(i) ): 
			this_dist+=math.pow(i[n]-ld[n], 2)
		this_dist_square=math.sqrt(this_dist)
		if this_dist> max_val: max_val=this_dist

		dist.append([this_dist, ld_index ])
		ld_index+=1
	return dist, max_val

#computing k nearest neighbours for i
#returns list of indexes in labled_data of nearest neighbours
def find_k_nearest (max_val, dist):
		
	nearest=list()
	for ii in range(0,k):
		small_val=max_val
		small_ldindex= -1

		for j in range (0, len(dist)):

			if ((dist[j][0]<small_val)or (small_ldindex==-1)) and (dist[j][1] not in nearest):
				small_val=dist[j][0]
				small_ldindex=dist[j][1]

		nearest.append(small_ldindex)
	return nearest

#zählen der häufigkeit von den lables der k nearest neighbours
#gibt häufigstes lable zurück
def counting_lables(nearest):

	lables=list()
	for l in nearest:
		lables.append(labled_data[l][-1])

	counter=collections.Counter(lables)
	most_common_lable=counter.most_common(3)[0][0]
	return most_common_lable


#algorithmus führt k nearest neighbours durch
def k_nearest_neighbours(labled_data,data, k):
	
	#liste in die alle gelableten punkte eingefügt werden
	output=list()

	#iterieren durch punkte die gelabled werden müssen
	for i in data:

		#berechnet liste mit distanzen zu punkt i und den maximal wert in der liste
		dist, max_val=get_distances(i)

		#finden der k nächsten nachbarn, gibt diese als liste zurück
		nearest=find_k_nearest(max_val, dist)


		lable=counting_lables(nearest)

		output.append([i[0],i[1],lable])

	print output
	plotting(output)



labled_data=[[1,2, 'green'],[5,2, 'green'], [5,1, 'green'], [1,10,'red'], [1,20,'red'], [1,11,'red']] #traindata mit lables

data=[[1,1], [6,2], [2,11], [1,2], [5,1], [3,10], [1,30], [1,20]] #input data fürs clustern

k=3

k_nearest_neighbours(labled_data, data,k)