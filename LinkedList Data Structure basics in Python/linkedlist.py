class Node:
    def __init__(self, value):
        self.data = value
        self.Next = None

class LinkedList:
    
    
    def __init__(self, value):
        self.Start = Node(value)
        self.length = 1
    
    def Insert(self, value):
        cur = self.Start
        while cur.Next is not None:
            cur = cur.Next
        cur.Next = Node(value)
        self.length += 1
                
    def Sort(self):        
        for i in range(1, self.length):
            temp = self.Getting(i)
            index = i
            while(index is not 0 and self.Getting(index - 1) > temp):
                self.Setting(index, self.Getting(index - 1))
                index =index- 1
            
            self.Setting(index, temp)
    
    def Getting(self, index):
        i = 0
        cur = self.Start
        value = None
        
        while cur.data is not None:
            if i == index:
                value = cur.data
                break
            i += 1
            cur = cur.Next
        return value
    
    def Setting(self, index, value):
        i = 0
        cur = self.Start
        while cur.data is not None:
            if i == index:
                cur.data = value
                break
            i += 1
            cur = cur.Next
    
    def Print(self):
        cur = self.Start
        while cur.Next is not None:
            print(cur.data)
            cur = cur.Next
        print(cur.data)
    def BS(self, data):
            start = 0
            last = self.length - 1
            index = -1
            while last >= start:
                mid = int((start + last) / 2)
                val = self.Getting(mid)
                if(val == data):
                    index = mid
                    break
                elif data > val:
                    start = mid+1
                elif data < val:
                    last = mid-1


            if index > -1:
                print(f"Found {data} at index {index}")
            else:
                print(f"{data} is not found!!")
print("========  6.1  ============================")        
print()
x = LinkedList(999)
x.Insert(6435)
x.Insert(28)
x.Insert(3)
print("before sorting ")
x.Print()
x.Sort()
print()
print("after sorting")
x.Print()
print()
print("========  6.2  ============================")
print()
x.BS(999)
x.BS(23)

===============================================================================




import time
athar=[]
class Node:
    def __init__(self, value):
        self.data = value
        self.Next = None

class LinkedList:
    
    def __init__(self, value=None):
        self.Start = Node(value)
        self.length = 1
    
    def Insert(self, value):
        start=time.clock()

        ptr = self.Start
        while ptr.Next != None:
            ptr = ptr.Next
        ptr.Next = Node(value)
        end = time.clock()

        print(f"It took {end-start} time in Linked List  ")
    def PrintAll(self):
        
        ptr = self.Start
        while ptr.Next != None:
            print(ptr.data)
            ptr = ptr.Next
        print(ptr.data)
        
def List():
    start=time.clock()
    athar.append(3)
    end=time.clock()
    print(f"It took {end-start} time in List  ")
    
L1=LinkedList()
L1.Insert(23)
List()
