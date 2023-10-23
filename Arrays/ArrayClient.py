import Array

maxSize = 100
arr = Array.Array(maxSize)

arr.insert(77)
arr.insert(99)
arr.insert(99)
arr.insert("foo")
arr.insert("bar")
arr.insert(44)
arr.insert(44)
arr.insert(55)
arr.insert(12.34)
arr.insert(0)
arr.insert("baz")
arr.insert(-17)
arr.insert(999)
arr.insert(999)
arr.insert(999)
arr.insert(999)

print("Array counting", len(arr), "items")
arr.traverse()

print("Search for 12 returns", arr.search(12))

print("Search for 12.34 returns", arr.search(12.34))

print("Deleting 0 returns", arr.delete(0))
print("Deleting 17 returns", arr.delete(17))

print("Setting item at index 3 to 33")
arr.set(3, 33)

print("Arr after deletions has", len(arr), "items")
arr.traverse()

maxNumber = arr.getmaxnumber()
print("Highest value in the array", maxNumber)

print("Highest number deleted", arr.deletemaxnumber())

print("Arr after deletions has", len(arr), "items")
arr.traverse()

newArr = arr.removedupes()
print("newArr after deletions of dupe items", len(newArr), "items")
newArr.traverse()
