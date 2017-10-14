TCI Q1.5
# One Away: There are three types of edits that can be performed on strings: insert a character, 
# remove a character, or replace a character. Given two strings, write a function to check if 
# they are one edit (or zero edits) away.
str1 = "bdef"
str2 = "bde"


#Time complexity O(n), Space Complexity O(1)
def check(str1,str2):
    if len(str1) - len(str2) == 0:
        #replace method
        return replace(str1,str2)
    elif len(str1) - len(str2) == 1:
        return insertion(str2,str1)
    elif len(str1) - len(str2) == -1:
        return insertion(str1,str2)
    else:
        return False

def replace(str1,str2):
    foundPanga = False
    for i in xrange(len(str1)):
        j = i
        if str1[i] != str2[j]:
            if foundPanga:
                return False
            foundPanga = True
    return True
    
def insertion(smaller,bigger):
    foundPanga = False
    for j in xrange(len(bigger)):
        i = j
        if foundPanga:
            i = j - 1
        if foundPanga == False and i == len(smaller):
            return True        
        if smaller[i] != bigger[j]:
            if foundPanga:
                return False
            foundPanga = True
    return True
            
            
check(str1,str2)
