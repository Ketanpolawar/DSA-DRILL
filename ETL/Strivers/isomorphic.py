str1 = "egg"
str2 = "add"

n = len(str1)
m = len(str2)
onetotwo = {}
twotoone = {}

if n != m:
    print("false")
else:
    is_isomorphic = "true"
    for i in range(n):
        if (str1[i] in onetotwo and onetotwo[str1[i]] != str2[i]) or (str2[i] in twotoone and twotoone[str2[i]] != str1[i]):
            is_isomorphic = "false"
            break
        onetotwo[str1[i]] = str2[i]
        twotoone[str2[i]] = str1[i]
    
    print(is_isomorphic)
