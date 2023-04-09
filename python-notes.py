######################## Loops ########################
for i in range(2, 6):
  print(i)

for i in range(5, 1, -1):
  print(i)


######################## Math ########################
import math
print(math.floor(3 / 2))
print(math.ceil(3 / 2))
print(math.sqrt(2))
print(math.pow(2, 3))

# division
print(5 / 2) # decimal division
print(5 // 2) # int round down (not towards 0) division

# max / min int
float("inf")
float("-inf")


######################## Arrays ########################
arr = [1, 2 ,3]
n = 5
arr = [1] * n # init array of size n with 1s
arr.insert(1, 7) # insert 7 at index 1, O(n)

# use as a stack
arr.append(4)
arr.append(5)
arr.pop() # remove and return last item

# sublists (slicing)
arr[1:3] # sublist of arr from index 1 to 3 not including 3

# unpacking
a, b, c = [1, 2, 3]

# looping through
for n in arr:
  print(n)

# enumerate
for i, n in enumerate(arr):
  print(i, n)

# reverse
arr.reverse()

# sorting
arr.sort()
arr.sort(reverse=True)
arr.sort(key=lambda x: len(x)) # sort by length

# list comprehension
arr = [i for i in range(5)]

# 2d lists
arr = [[0] * 4 for i in range(4)] # 4 x 4 grid of all 0s


######################## Strings ########################
s = "abc"
s2 = s[0:2]
s += "def" # O(n)

# conversions
int("123")
str(123)

# ascii value
ord("a")

# combine list of strings
strings = ["ab", "cd", "ef"]
"".join(strings) # join all the strings with "" between each


######################## Queues ########################
from collections import deque
queue = deque()
queue.append(1)
queue.popleft()
queue.append(2)
queue.popright()


######################## HashSet ########################
# search: O(n)
# insert/remove: O(n)
# NO DUPLICATES
mySet = set()
mySet.add(1)
mySet.add(2)
len(mySet) # 2
1 in mySet # True
mySet.remove(2)
2 in mySet # False


######################## HashMap ########################
# search: O(1)
# insert/remove: O(1)
myMap = {}
myMap["alice"] = 88
myMap["bob"] = 77
myMap["alice"] = 80
print(myMap) # {'alice': 80, 'bob': 77}
"alice" in myMap # True
myMap.pop("alice")
"alice" in myMap # False
myMap.get("key", 0) # get the value associated w key if exists, else return 0

# looping
myMap = { "alice": 90, "bob": 70}
for key in myMap:
  print(key, myMap[key])

for val in myMap.values():
  print(val)

for key, val in myMap.items():
  print(key, val)


######################## Tuples ########################
tup = (1, 2, 3)
myMap = { (1, 2): 3} # can be used as key for hash map/set


######################## Heaps ########################
# .top(): O(1)
# .insert(): O(log n)
# .remove(): O(log n)
# .heapify(): O(n log n)
import heapq

minHeap = []
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 4)

print(minHeap[0]) # min is always at index 0

while len(minHeap):
  print(heapq.heappop(minHeap)) # 2, 2, 3, 4

# MAX heaps -> mult by -1 before and after inserting into heap
maxHeap = []
heapq.heappush(maxHeap, -3)
heapq.heappush(maxHeap, -2)
heapq.heappush(maxHeap, -4)
print(-1 * maxHeap[0]) # max at index 0

# build heap from arr
arr = [2, 1, 8, 4, 5]
heapq.heapify(arr) # arr: [1, 2, 4, 5, 8]


# Classes
class MyClass:
  # ctor
  def __init__(self, nums):
    # create member vars
    self.nums = nums
    self.size = len(nums)
  
  # create methods
  def getLength(self):
    return self.size