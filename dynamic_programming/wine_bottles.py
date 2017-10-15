#Imagine you have a collection of N wines placed next to each other on a shelf.
# The price of the wines is given in an array, the ith index of array is the price for wine i. 

# Because the wines get better every year, supposing today is the year 1, on year y the price of the i-th wine will 
# be y*A[i], i.e. y-times the value that current year.

# You want to sell all the wines you have, but you want to sell exactly one wine per year, starting on this year.
# One more constraint - on each year you are allowed to sell only either the leftmost or the rightmost wine on the 
# shelf and you are not allowed to reorder the wines on the shelf 

# You want to find out, what is the maximum profit you can get, if you sell the wines in optimal order.

A = [2,3,5,1,4]
N = len(A)

st = 0
en = len(A)-1

counter = 0
cache = [[-1 for j in xrange(N)]  for i in xrange(N)]

def greedy_solution(A,start,end,year):
#     global counter 
#     counter += 1
#     print counter
    if start>end:
        return 0
    if A[start]<A[end]:
#         print str(A[start]) + "*" + str(year)
        return A[start]*year + greedy_solution(A,start+1,end,year+1)
    else:
#         print str(A[end]) + "*" + str(year)
        return A[end]*year + greedy_solution(A,start,end-1,year+1)

print greedy_solution(A,0,en,1)


def recursive_solution(A,start,end,year):
#     global counter
#     counter += 1
#     print counter
    if start > end:
        return 0
    return max((A[start] * year + recursive_solution(A,start+1,end,year+1)),
               A[end]*year + recursive_solution(A,start,end-1,year+1))

print recursive_solution(A,0,en,1)

def memoize(A,start,end):
#     global counter
#     counter += 1
#     print counter
    if start > end:
        return 0
    
    if cache[start][end] != -1:
        return cache[start][end]

    year = N - (end - start + 1) + 1;
    cache[start][end] = max(A[start] * year + memoize(A,start+1,end), 
                            A[end] * year + memoize(A,start,end-1))
    
    return cache[start][end]

print memoize(A,st,N-1)
