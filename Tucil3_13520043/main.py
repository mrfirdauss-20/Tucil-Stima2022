
import numpy as np
from Node import Node
from PrioQueue import PrioQueue
import time

finalMat = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])

print("+================================+")
print("|| Welcome to 15th Puzzle Solver||")
print("+================================+")
print()


final = Node(0,[],finalMat)
print("========================================================")
fileName = input("\tMasukkan Nama File Data Puzzle: ")
print("========================================================")
f = open(fileName, "r")
arr = []
txt= f.readlines()
for i in txt:
    arr+=[i.split(" ")]
arr=[[int(j.replace('\n','')) for j in i]for i in arr]
f.close()

npArr = np.array(arr)

print()
print("Puzzle Awal:\n",npArr)
print()
puzzleAwal = Node(0,[],npArr)
print("Nilai Kurang (i) dari Puzzle adalah: ")
puzzleAwal.printKurangI()
print()
x,y= np.where(npArr == 16)
print("Nilai \Sigma kurang (i) + X = {}".format(puzzleAwal.countCost()+((x[0]+y[0])%2)))

startTime = time.time()
if((puzzleAwal.countCost()+x[0]+y[0])%2!=0):
    print("Persoalan tidak dapat diselesaikan :\"(")
else:
    prio = PrioQueue()
    prio.append(puzzleAwal)
    arr ={}
    arr[np.array_str(puzzleAwal.getMat())]=True
    while(not final.isEqualWith(prio.getHead()) and prio.getLen()>0):
        temp = prio.pop()
        y,x=np.where(temp.getMat()==16)
        if(y[0]>0):
            node3 = Node(temp.getDepth()+1,temp.getPrevMove(),temp.getMat())
            node3.move("up")
            if(not (np.array_str(node3.getMat()) in arr)):
                prio.append(node3)
                arr[np.array_str(node3.getMat())]=True
        if (x[0]>0):
            node2 = Node(temp.getDepth()+1,temp.getPrevMove(),temp.getMat())
            node2.move("left")
            if(not (np.array_str(node2.getMat()) in arr)):
                prio.append(node2)
                arr[np.array_str(node2.getMat())]=True
        if(y[0]<3):
            node1 = Node(temp.getDepth()+1,temp.getPrevMove(),temp.getMat())
            node1.move("down")
            if(not (np.array_str(node1.getMat()) in arr)):
                prio.append(node1)
                arr[np.array_str(node1.getMat())]=True
        if(x[0]<3):
            node4 = Node(temp.getDepth()+1,temp.getPrevMove(),temp.getMat())
            node4.move("right")
            if(not (np.array_str(node4.getMat()) in arr)):
                prio.append(node4)
                arr[np.array_str(node4.getMat())]=True
        
    end = time.time()
    count=0
    for i in (prio.getHead().getPrevMove()):
        print("\nStep {} -> {}:".format(count+1,i))
        puzzleAwal.move(i)
        print(puzzleAwal.getMat())
        count+=1
    print("\nPuzzle solved in {} steps\n{} node discovered in {:.5f} seconds\n".format(len(prio.getHead().getPrevMove()),len(arr),end-startTime))