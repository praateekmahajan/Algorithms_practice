# Weighted Scheduling
# Given n jobs, their start times, finish times and weigh
# compute the jobs that can be completed with the highest weight

start = [0,3,5,9,13]
finish = [4,7,10,13,18]
w = [10,100,10,1,10]
first = finish[0]

def compute_p(start,finish):
    #p(i) returns the highest value of j < i, where finish[j] < start[i]
    p = [-1 for i in xrange(len(start))]
    for temp in xrange(len(start)-1,0,-1):
        temp_list = []
        for i in xrange(temp-1,-1,-1):
            if start[temp] >= finish[i]:
                temp_list.append(i)
        if len(temp_list)>0:
            p[temp] = max(temp_list)
    return p

p = compute_p(start,finish)


def greedy(n):
#     global counter
#     counter += 1 
#     print counter

    current = finish[0]
    s = w[0]
    
    for i in xrange(0,n+1):
        if current <= start[i]:
            s += w[i]
            current = finish[i]
    return s

print greedy(len(start)-1)
print "\n"
counter = 0
def recursive(n):
#         global counter
#         counter += 1 
#         print counter
        if n<0:
            return 0
        return max(w[n] + recursive(p[n]), recursive(n-1))

print recursive(len(start)-1)
print "\n"

memo = {}
counter = 0
def memoize(n):
#     global counter
#     counter += 1 
#     print counter
    
    if n < 0:
        return 0
    elif n in memo:
        return memo[n]
    else:
        possibility = max(w[n] + memoize(p[n]), memoize(n-1))
        memo[n] = possibility
        return memo[n]
    
# print w[len(start) - 1]
print memoize(len(start) - 1)
print "\n"

counter = 0
memo = {-1:0}

def bottom_up(n):
    global counter
    for i in xrange(0,n+1):
        counter += 1 
        possibility = max(w[i] + memo[p[i]], memo[i-1])
        memo[i] = possibility
#     print counter
    return memo[n]

print bottom_up(len(start)-1)
print '\n'
sol = []

def solution(n):
    if n<0:
        return
    if w[n] + memo[p[n]] > memo[n-1]:
        print n
        return solution(p[n])
    else:
        solution(n-1)

solution(len(start)-1)
