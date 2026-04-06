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

if __name__ == "__main__":
    countdown(5)