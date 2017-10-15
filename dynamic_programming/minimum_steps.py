# Problem Statement: On a positive integer, you can perform any one of the following 3 steps. 
# 1.) Subtract 1 from it. ( n = n - 1 )  , 
# 2.) If its divisible by 2, divide by 2. ( if n % 2 == 0 , then n = n / 2  )
# 3.) If its divisible by 3, divide by 3. ( if n % 3 == 0 , then n = n / 3  ).
# Now the question is, given a positive integer n, find the minimum number of steps that takes n to 1

counter = -1
def greedy_steps(n):
    # Might give wrong answer
    global counter
    counter += 1

    if n==1:
        return counter

    if n%3 == 0:
        return greedy_steps(n/3)
    elif n%2 == 0:
        return greedy_steps(n/2)
    else:
        return greedy_steps(n-1)

print greedy_steps(10)
print "\n"

counter = -1
def recursive(n):
    # Gives the correct answer but checks extremely slow, uncomment following lines to see
#     global counter
#     counter += 1
#     print counter
    if n==1:
        return 0

    if n%3 == 0:
        return min(1+recursive(n-1) , 1 + recursive(n/3))
    elif n%2 == 0:
        return min(1+recursive(n-1) ,1 + recursive(n/2))
    else:
        return 1+recursive(n-1)

print recursive(10)
print "\n"

memo = {1:0}
counter  = -1
def memoization(n):
#     Faster top down method, takes O(n) space
#     global counter
#     counter += 1
#     print counter
    if n in memo:
        return memo[n]
    
    possibility = 1 + memoization(n-1)
    
    if n%3 == 0:
        possibility = min(possibility,1 + memoization(n/3))
    elif n%2 == 0:
        possibility = min(possibility, 1 + memoization(n/2))

    memo[n] = possibility
    return possibility

print memoization(10)
print "\n"
counter = -1
def bottom_up(n):
#   Bottom up down method, takes O(n) space and is the fastest
#     global counter
    memo_n = [-1]
    for i in xrange(1,n+1):        
#         counter += 1
        possibility = 1 + memo_n[i-1]
        if i%3 == 0:
            possibility = min(possibility,1 + memo_n[i/3])
        elif i%2 == 0:
            possibility = min(possibility, 1 + memo_n[i/2])
        memo_n.append(possibility)
#     print counter
    return memo_n[-1]

print bottom_up(10)
