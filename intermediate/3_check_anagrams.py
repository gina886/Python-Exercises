def anagrams(str1,str2):
    return  sorted(str1) == sorted(str2)
#test
str1="gina"
str2="naga"
print(anagrams(str1,str2))
