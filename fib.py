# Fibonacci munbers module

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end = ' ')
        a, b = b, a + b
    print()

def fib_list(n):
    a, b = 0, 1
    res = []
    while a < n:
        res.append(a)
        a, b = b, a + b
    return res

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        print("n < fib(%s):" % sys.argv[1], *fib_list(int(sys.argv[1])))