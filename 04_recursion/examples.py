"""
Recursion - a funtion that calls itself

Two rules:
1). Base case --> when to stop
2). Recursive case --> call yourself with smaller problem
"""

def countdown(n):
    if n == 0:        # base case -> STOP
        return
    print(n)          # print current number
    countdown(n - 1)  # call yourself with smaller number

def factorial(n):
        if n == 1:          # base case -> STOP
            return 1
        return n * factorial(n - 1)    # recursive case

def fib(n):
     if n == 0:
          return 0
     elif n == 1:
          return 1
     else:
          return fib(n-1) + fib(n-2)
    
if __name__ == "__main__":
    countdown(5)
    print(factorial(5))   
    print(factorial(3))   
    print(fib(6))     # 8
    print(fib(10))     # 55