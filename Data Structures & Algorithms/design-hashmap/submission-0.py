class MyHashMap:

    def __init__(self):
        self.keyArr = []
        self.valueArr = []

    def findIndex(self, key: int) -> int:
        for i in range(len(self.keyArr)):
            if self.keyArr[i] == key:
                return i
        return -1

    def put(self, key: int, value: int) -> None:
        index = self.findIndex(key)

        if index != -1:
            self.valueArr[index] = value
        else:
            self.keyArr.append(key)
            self.valueArr.append(value)

    def get(self, key: int) -> int:
        index = self.findIndex(key)

        if index != -1:
            return self.valueArr[index]
        else:
            return -1

    def remove(self, key: int) -> None:
        index = self.findIndex(key)

        if index != -1:
            self.keyArr.pop(index)
            self.valueArr.pop(index)



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)