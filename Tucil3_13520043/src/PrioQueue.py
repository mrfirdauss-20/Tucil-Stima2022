from Node import Node
class PrioQueue:
    def __init__(self) :
        self.queue=[]
    def append(self,puzz):
        #append an elemnt too priotiy queue
        #based on cost
        #if cost is less than the first element in the queue
        #then append to the first element
        #else append to the last element
        #if the queue is empty then append to the first element
        if(len(self.queue)>0):
            i =0
            iter = self.queue[i]
            while(puzz.getCost()>iter.getCost() and i<len(self.queue)-1):
                i+=1
                iter = self.queue[i]
            if(self.queue[i].getCost()<puzz.getCost()):
                self.queue.append(puzz)
            else:
                self.queue.insert(i,puzz)
        else:
            self.queue+=[puzz]
    def prinPrio(self):
        for i in self.queue:
            print(i.getMat())
            print(i.getCost())
    def pop(self):
        return self.queue.pop(0)
    def getHead(self):
        if(len(self.queue)>0):
            return self.queue[0]
        else:
            return None
    def getLen(self):
        return len(self.queue)
    

        