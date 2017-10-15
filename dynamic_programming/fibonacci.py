counter = 0

def bottom_up(n):
#     global counter
    a = [0,1]
    for i in xrange(1,n):
#         counter += 1
        a[0],a[1] = [a[1], a[0] + a[1]]
#     print counter

    return a[1]
print bottom_up(20)

memo = {0:0,1:1}
def memoize_fib(n):
#     global counter
#     counter += 1
#     print counter
    if n in memo:
        return memo[n]
    else:
        memo[n] = memoize_fib(n-1) + memoize_fib(n-2)
        return memo[n]
print memoize_fib(20)

def recursive_fib(n):
#     global counter
#     counter += 1
#     print counter
    
    if n==0 or n==1:
        return n
    return recursive_fib(n-1) + recursive_fib(n-2)

print recursive_fib(20)
