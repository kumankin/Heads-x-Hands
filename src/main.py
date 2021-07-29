import random

def create_arrays(n):
    arrays_len = random.sample(range(random.randint(n, 10)), n)
    # print(arrays_len)
    arrays = []
    # # print(arrays_len)
    for i in range(len(arrays_len)):
        arrays.append([random.randint(0, 100) for j in range(int(arrays_len[i]))])
        if ((i % 2) == 0):
            arrays[i].sort()
        else:
            arrays[i].sort(reverse=True)
    return arrays

def main():
    print(create_arrays(5))
if __name__ == "__main__":
    main()   