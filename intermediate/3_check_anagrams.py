def anagrams(str1,str2):
    return  sorted(str1) == sorted(str2)
#test
str1="gina"
str2="naga"

if anagrams(str1,str2):
    print(f"{str1} and {str2} are composed of the same letters.")
else:
     print(f"{str1} and {str2} are not composed of the same letters.")
