def insertionSort(alist):
   for index in range(1,len(alist)):
       currentvalue = alist[index]
       position = index
       while position>0 and alist[position-1]>currentvalue:
           alist[position]=alist[position-1]
           position = position-1
       alist[position]=currentvalue

alist = list(map(int,input().split()))
insertionSort(alist)
for j in alist:
    print(j,end=" ")
