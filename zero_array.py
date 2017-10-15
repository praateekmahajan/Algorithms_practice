#CTCI Q1.8
# Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.
def m_n_space(matrix):
    rows = []
    cols = []
    
    for i in xrange(len(matrix)):
        for j in xrange(len(matrix[0])):
            if matrix[i][j] == 0:
                if i not in rows:
                    rows.append(i)
                if j not in cols:
                    cols.append(j)

    for i in rows:
        for j in xrange(len(matrix[0])):
            matrix[i][j] = 0

    for j in cols:
        for i in xrange(len(matrix)):
            matrix[i][j] = 0
    print rows,cols
    return matrix
matrix = [[1,2,0,4],[5,6,7,8],[0,10,11,12]]
first_set = False

print m_n_space(matrix)
