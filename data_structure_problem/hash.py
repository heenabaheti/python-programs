class HashFunction:
    def __init__(self):
        hash_key = None

    @staticmethod
    def hashing_func(key):
        hash_key = key // 11
        return hash_key

    @staticmethod
    def insert(hash_list, key, value):
        hash_list[key].append(value)


def main():
    hashing = HashFunction()
    hash_table = [[] for i in range(10)]
    print(hash_table)
    val = int(input("Enter key value for Hashing"))
    value = hashing.hashing_func(val)
    hashing.insert(hash_table, value, val)
    print(hash_table)

if __name__ == '__main__':
    main()





