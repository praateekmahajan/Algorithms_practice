# Everyone knows what LCS is, lowest common subsequence

str1 = "DEQF"
str2 = "AEQ"
m = len(str1)
n = len(str2)

counter = 0
def recursive(i,j):
#     global counter
#     counter += 1
#     print counter
    if i == -1 or j == -1:
        return 0
    if str1[i] == str2[j]:
        return recursive(i-1,j-1) + 1
    else:
        return max(recursive(i-1,j), recursive(i,j-1))

print recursive(m-1,n-1)
print "\n"

counter = -1
memo = [[-1 for p in xrange(n+1)] for q in xrange(m+1)]
def memoize(i,j):
#     global counter
#     counter += 1
#     print counter

    if i < 0  or j <0:
        return 0
    if memo[i+1][j+1] != -1:
        return memo[i+1][j+1]
    if str1[i] == str2[j]:
        memo[i+1][j+1] = 1 +  memoize(i-1,j-1)
    else:
        memo[i+1][j+1] = max(memoize(i-1,j), memoize(i,j-1))
    return memo[i+1][j+1]
print memoize(m-1,n-1)
print "\n"

counter  = -1
def bottom_up(n,m):
#     global counter
    
    memo = [[0 for p in xrange(m+1)] for q in xrange(n+1)]
    for i in xrange(1,n):
        for j in xrange(1,m):
#             counter += 1
#             print counter

            if str1[i-1] == str2[j-1]:
                memo[i][j] = 1 +  memo[i-1][j-1]
            else:
                memo[i][j] = max(memo[i-1][j], memo[i][j-1])
    return memo[-2][-2]

print bottom_up(len(str1)+1,len(str2)+1)
