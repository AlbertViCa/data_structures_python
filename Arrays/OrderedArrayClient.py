from OrdererArray import *

maxSize = 1000
ordArr = OrderedArray(maxSize)

ordArr.insert(77)
ordArr.insert(99)
ordArr.insert(44)
ordArr.insert(55)
ordArr.insert(0)
ordArr.insert(12)
ordArr.insert(44)
ordArr.insert(99)
ordArr.insert(77)
ordArr.insert(0)
ordArr.insert(3)

print("Array containing", len(ordArr), "items:", ordArr)

ordArr.delete(0)
ordArr.delete(99)
ordArr.delete(0)
ordArr.delete(0)
ordArr.delete(3)

print("Array after deletions has", len(ordArr), "items:", ordArr)

print("find(44) returns", ordArr.find(44))
print("find(46) returns", ordArr.find(46))
print("find(77) returns", ordArr.find(77))
