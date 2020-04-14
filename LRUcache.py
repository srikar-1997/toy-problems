class LRU:

    def __init__(self, capacity) :
        self.capacity = capacity
        self.lis = []
    
    def put(self, value):
        if not value in self.lis and len(self.lis) < self.capacity :
            self.lis.append(value)
        
        elif not value in self.lis and len(self.lis) >= self.capacity :
            self.lis.remove(self.lis[0])
            self.lis.append(value)
        else :
            self.lis.remove(value)
            self.lis.append(value)
        return


    def get(self, index):
        if index > self.capacity :
            return -1
        else :
            i = self.lis[index]
            self.lis.remove(self.lis[index])
            self.lis.append(i)
            return i

    def get_cache(self) :
        return self.lis

# def main():
#     lru = LRU(5)
#     # lru.put(1)
#     # lru.put(2)
#     lru.put(3)
#     lru.put(4)
#     lru.put(5)
#     lru.put(6)
#     # lru.put(4)
#     lru.put(4)
#     print(lru.get_cache())
# if __name__ == "__main__":
#     main()