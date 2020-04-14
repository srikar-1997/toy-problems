from LRUcache import LRU

def main():
    lru = LRU(5)


    lru.put(1)
    lru.put(2)
    lru.put(3)

    assert lru.get_cache() == "[1, 2, 3]", "put method failed"
    print("put method passed")

    lru.put(4)
    lru.put(5)

    assert lru.get(2) == "3", "get method failed"
    print("get method passed")

    lru.put(6)
    lru.get_cache() == "[2, 3, 4, 5, 6]", "get_cache method failed"
    print("get_cache method passed")

if __name__ == "__main__":
    main()