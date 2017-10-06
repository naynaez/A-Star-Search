from heapq import *

costPath = [
		{4:90,},  #0
		{3:120,10:146,8:138}, #1
		{6:86}, #2
		{1:120,5:75}, #3
		{0:90,7:85,8:101,13:211}, #4
		{3:75,9:70}, #5
		{2:86,7:98}, #6
		{4:85,6:98,12:142}, #7
		{1:138,4:101,10:97}, #8
		{5:70,11:111}, #9
		{1:146,8:97,14:80}, #10
		{9:111,15:118}, #11
		{7:142,16:92}, #12
		{4:211,14:99}, #13
		{10:80,13:99,15:140,19:151}, #14
		{11:118,14:140,17:75}, #15
		{12:92,18:87}, #16
		{15:75,19:71}, #17
		{16:87}, #18
		{14:151,17:71}, #19

	]

def printHeap(h):
	for i in range(len(h)):
		print(heappop(h))


def A_starSearch(heuristic,start,end):
	checkPass =  [False] * 20
	resultPath = []

	startNode = start
	endNode = end
	h = []	

	resultPath = None

	valueF = 0 + heuristic[startNode][endNode]
	heappush(h, (valueF,startNode,0,[] )) # valueF, indexNode, cost, path
	while True:		
		print("-------------------------")
		printHeap(list(h))
		valueF, currentNode, cost ,path = heappop(h)
		checkPass[currentNode] = True
		# print(path)
		path.append(currentNode)
		print("Choose -> node:"+str(currentNode)+" ValueF :"+str(valueF)+" cost :"+str(cost)+" heu :"+str(heuristic[currentNode][endNode]))	

		if currentNode == endNode:
			print("endd")
			print(path)
			resultPath = list(path)
			break

		for key,value in costPath[currentNode].items():

			if checkPass[key] == False:			
				newCost = cost + value
				newValueF = newCost + heuristic[key][endNode]
				heappush(h, (newValueF, key, newCost, list(path)))

	return resultPath



