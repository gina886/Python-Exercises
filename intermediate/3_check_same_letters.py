def chek_same_le(str1,str2):
    return  sorted(str1) == sorted(str2) #sorted(）是 Python 的内置函数，它会将字符串中的字符排序，并返回一个新的排序后的列表
#test
str1="gina"
str2="naga"

if chek_same_le(str1,str2):
    print(f"{str1} and {str2} are composed of the same letters.")
else:
     print(f"{str1} and {str2} are not composed of the same letters.")
