import numpy as np
import numpy
import cv2
import math
import csv
from prettytable import PrettyTable
import csv


def getCoordinate(img):
    ret,thresh = cv2.threshold(gray,127,255,1)
    _ , contours,h = cv2.findContours(thresh,1,2)
    cityCoord = []  # index is city number in map , value is [x,y] ( upper-left is (0,0) )
    num = 0
    for cnt in contours:    ## find city coordinates
        approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
        cv2.drawContours(img,[cnt],0,(0,0,255),-1)
        cv2.putText(img,str(num),(approx[0][0][0] + 18,approx[0][0][1] + 18),1, 2,(0,0,0),2,cv2.LINE_AA)
        cityCoord.append(approx[0][0])
        num = num + 1
    return (cityCoord , img)

def getHeuristic(coord):
    heuristic = [[0 for x in range(20)] for y in range(20)]
    for i in range(20):         ### find heuristicTable
        for j in range(20):
            dist = int(math.hypot(coord[i][0] - coord[j][0], coord[i][1] - coord[j][1]))
                    # ( x1 - x2 , y1 - y2 )
            heuristic[i][j] = int(dist/2)
    return heuristic # heuristic[start city num][destination city num] = distance (pixels)

def printHeuristicTable(heuristic):
    ht = PrettyTable()   ## print table to console with PrettyTable format
    ht.field_names = range(0,20)
    for row in heuristic:
        ht.add_row(row)
    print(ht)

cityName = ['Giurgiu','Craiova','Eforie','Drobeta','Bucharest',
            'Mehadia','Hirsova','Urziceni','Pitesti','Lugoj',
            'Rimnicu Vilcea','Timisoara','Vaslui','Fagaras','Sibiu',
            'Arad','Iasi','Zerind','Neamt','Oradea','None','']
gray = cv2.imread('map-cen.png',0)
citycoord , img = getCoordinate(gray)
heuristic = getHeuristic(citycoord)
printHeuristicTable(heuristic)
print(citycoord)
#numArray = numpy.asarray( heuristic )
#numpy.savetxt("table2.csv", numArray, delimiter=",")


#cv2.imshow('Romania map with label',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
