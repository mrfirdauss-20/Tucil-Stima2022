import numpy as np
class myConvexHull:
  def __init__(self,pairOfSeries):
    self.ver = self.ConvexHull(pairOfSeries)
    self.full = pairOfSeries

  def ConvexHull(self,P):
    P= sorted(P, key=lambda x: x[0])
    a=[P[0]]+self.getPoints(P[0],P[-1],P[1:-1],False)+[P[-1]]+self.getPoints(P[0],P[-1],P[1:-1],True)
    s=np.array(a)
    return s

  def getPoints(self, mostLeft, mostRight, listOfP,isTop):
    if(len(listOfP)<=1):
      if(len(listOfP)==0):
        return []
      elif((self.getDetOf3Points(mostLeft,mostRight,listOfP[0])>0 and not isTop) or(self.getDetOf3Points(mostLeft,mostRight,listOfP[0])<0 and isTop)):
        return []
      else:
        return [listOfP[0]]
    idx=-1
    maxDist = 0
    for i in range(len(listOfP)):
      temp=self.getDetOf3Points(mostLeft,mostRight,listOfP[i])
      if(temp<maxDist and not isTop ):
        idx=i
        maxDist=temp
      elif(temp>maxDist and isTop ):
        idx=i
        maxDist=temp
    if(idx==-1):
      return []
    if(isTop):
      right=self.getPoints(listOfP[idx],mostRight,listOfP[idx+1:],True)
      left =self.getPoints(mostLeft,listOfP[idx],listOfP[0:idx],True) 
      return right+[listOfP[idx]]+left  
    else:
      left =self.getPoints(mostLeft,listOfP[idx],listOfP[0:idx],False)
      right=self.getPoints(listOfP[idx],mostRight,listOfP[idx+1:],False)
      return left+[listOfP[idx]]+right    
      
  def getDetOf3Points(self,p1,p2,p):
    nilai_kanan=p1[0]*p2[1]+p[0]*p1[1]+p2[0]*p[1]
    nilai_kiri=p[0]*p2[1]+p2[0]*p1[1]+p1[0]*p[1]
    return nilai_kanan -nilai_kiri