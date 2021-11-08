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
def say_bye():
    print("Bye")

#fizzbuzz
def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
main()
print(fib(10))

fizzbuzz(15)

say_bye()