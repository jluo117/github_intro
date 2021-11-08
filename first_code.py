#hello world
def main():
    print("Hello World")
#fibonacci recursion
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
main()
print(fib(10))