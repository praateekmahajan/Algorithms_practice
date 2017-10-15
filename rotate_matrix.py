#CTCI Q1.7
# Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes
# Write a method to rotate the image by 90 degrees. Can you do this in place

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
matrix2 = [['a','b','c','d','e'],['f','g','h','i','j'],['k','l','m','n','o'],['p','q','r','s','t'],['u','v','w','x','y']]

matrix = matrix2

offset = 0
num = len(matrix)

for layer in xrange(num/2):
    last = num - layer - 1
    for j in xrange(layer,last):
        offset = j - layer;
        
        temp = matrix[layer][j]

        matrix[layer][j] = matrix[last-offset][layer]
        matrix[last - offset][layer] = matrix[last][last-offset]
        matrix[last][last-offset] = matrix[j][last]
        matrix[j][last] = temp

print matrix

