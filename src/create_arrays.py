import random

def short(n):
    return [sorted([random.randint(0, 100) for i in range(int(random.sample(range(1, random.randint(n + 1, 20)), n)[i]))], reverse=bool(i % 2)) for i in range(int(n))]