from collections import deque
import heapq
minHeap=[]
heapq.heappush(minHeap,-10)
print(heapq.heappop(minHeap))
# stack=deque()
# stack.append(10)
d={"banana":1,"apple":4,"orange":6}
d_sorted=dict(sorted(d.items(),key=lambda x : x[1]))
print (d_sorted)
arr = [(3, 4), (2, 2), (1, 4), (5, 1)]
arr2=sorted(arr,key=lambda x: (x[1] , x[0]))
heap_c=[]
for a in arr:
    heapq.heappush(heap_c,[a[0],a])
while (len(heap_c)!=0):
    x=heapq.heappop(heap_c)
    print(x)    
# print(arr2)

# top=stack.pop()
# print(top)
# map ={}
# map[1]="add"
# map['2']="remove"
# for key in map.keys():
#     print(key)
# if '2=1' in map :
#     print ("hello")    