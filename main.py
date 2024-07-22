
def strStr(s1, s2):
    return s1.find(s2)


#Example 1:
#Input: 
haystack = "sadbutsad"
needle = "sad"
print(strStr(haystack, needle))
#Output: 0
#Explanation: "sad" occurs at index 0 and 6.
#The first occurrence is at index 0, so we return 0.

#Example 2:
#Input: 
haystack = "leetcode"
needle = "leeto"
print(strStr(haystack, needle))
#Output: -1
#Explanation: "leeto" did not occur in "leetcode", so we return -1.

 
