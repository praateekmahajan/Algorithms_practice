heck Permutation: Given two strings, write a method to decide if one is a permutation of the other.

str1 = "abcfd"
str2 = "dcbea"

#Time complexity O(n), Space Complexity O(c), where c = character set, 
# c here  is 26 representing for lowercase letters
def check_permutation(str1,str2):
    temp_list1 = [0 for i in xrange(26)]
    temp_list2 = [0 for i in xrange(26)]
    
    if len(str1) != len(str2):
        return False
    for i in xrange(len(str1)):
        ascii1 = ord(str1[i]) - 97
        ascii2 = ord(str2[i]) - 97
        
        temp_list1[ascii1] += 1
        temp_list2[ascii2] += 1
    for i in xrange(26):
        if temp_list1[i] == temp_list2[i]:
            continue
        else:
            return False
    return True
check_permutation(str1,str2)
