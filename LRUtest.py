from LRUcache import LRU

def main():
    lru = LRU(5)


    lru.put(1)
    lru.put(2)
    lru.put(3)
    assert lru.get_cache() == [1, 2, 3], "put method failed"
    print("put method passed")

    lru.put(5)
    lru.put(3)

    assert lru.get(2) == 5, "get method failed"
    print("get method passed")

    assert lru.get(6) == -1, "get method with index greater than capacity failed"
    print("get method with index greater than capacity passed")

    lru.put(6)
    assert lru.get_cache() == [1, 2, 3, 5, 6], "get_cache method failed"
    print("get_cache method passed")

    assert lru.get(2) == 3, "get method failed"
    print("get method passed")

    assert lru.get_cache() == [1, 2, 5, 6, 3], "get_cache method failed"
    print("get_cache method passed")

    print("lru implementation completed")
if __name__ == "__main__":
    main()