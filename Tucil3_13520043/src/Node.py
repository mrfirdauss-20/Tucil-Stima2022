import numpy as np
class Node:
    def __init__(self, depth, prevMove, mat):
        self.depth =depth 
        self.prevMove = prevMove.copy()
        self.mat = np.copy(mat)
        self.cost = 0
    
    def move(self,comm):
        y,x=np.where(self.mat==16)
        if(comm == "up"):
            i=y[0]-1
            self.swapCell([y[0],x[0]],[i,x[0]])
        elif(comm=="down"):
            i=y[0]+1
            self.swapCell([y[0],x[0]],[i,x[0]])
        elif (comm=="left"):
            i=x[0]-1
            self.swapCell([y[0],x[0]],[y[0],i])
        elif (comm=="right"):
            i=x[0]+1
            self.swapCell([y[0],x[0]],[y[0],i])
        self.prevMove+=[comm]
        self.cost=self.countCost()
        
            
    def swapCell(self,i,j   ):
        self.mat[i[0]][i[1]],self.mat[j[0]][j[1]]=self.mat[j[0]][j[1]],self.mat[i[0]][i[1]]

    def countCost(self):
        count =0
        for i in range (4):
            for j in range(4):
                for m in range (i,4):
                    if(m!=i):
                        for n in range (4):
                            if(self.mat[i][j]>self.mat[m][n]):
                                count+=1
                    else:
                        for n in range (j,4):
                            if(self.mat[i][j]>self.mat[m][n]):
                                count+=1
        return count+self.depth

    def printKurangI(self):
        for i in range (4):
            for j in range(4):
                count=0
                for m in range (i,4):
                    if(m!=i):
                        for n in range (4):
                            if(self.mat[i][j]>self.mat[m][n]):
                                count+=1
                    else:
                        for n in range (j,4):
                            if(self.mat[i][j]>self.mat[m][n]):
                                count+=1
                print("Nilai kurang dari ({}) adalah {}".format(self.mat[i][j],count))

    def getDepth(self):
        return self.depth

    def getCost(self):
        return self.cost

    def getMat(self):
        return self.mat

    def getPrevMove(self):
        return self.prevMove

    def isEqualWith(self,bro):
        if(bro==None):
            return False
        else:
            return np.array_equal(self.mat,bro.mat)