class Array(object):
    def __init__(self, initialSize):
        self.__a = [None] * initialSize
        self.__nItems = 0

    def __len__(self):
        return self.__nItems

    def get(self, n):
        if 0 <= n <= self.__nItems:
            return self.__a[n]

    def set(self, n, value):
        if 0 <= n < self.__nItems:
            self.__a[n] = value

    def insert(self, item):
        self.__a[self.__nItems] = item
        self.__nItems += 1

    def find(self, item):
        for j in range(self.__nItems):
            if self.__a[j] == item:
                return j
        return -1

    def search(self, item):
        return self.get(self.find(item))

    def delete(self, item):
        for j in range(self.__nItems):
            if self.__a[j] == item:
                self.__nItems -= 1
                for k in range(j, self.__nItems):
                    self.__a[k] = self.__a[k + 1]
                return True
        return False

    def traverse(self, function=print):
        for j in range(self.__nItems):
            function(self.__a[j])

    def getmaxnumber(self):
        current = 0
        if self.__nItems > 0:
            for i in range(self.__nItems):
                if isinstance(self.__a[i], (int, float)) and float(self.__a[i]) > current:
                    current = self.__a[i]
        return current

    def deletemaxnumber(self):
        maxNumber = self.getmaxnumber()
        self.delete(maxNumber)
        return maxNumber

    def removedupes(self):
        newArr = Array(self.__nItems)
        for i in range(self.__nItems):
            if newArr.find(self.__a[i]) == -1:
                newArr.insert(self.__a[i])
        return newArr