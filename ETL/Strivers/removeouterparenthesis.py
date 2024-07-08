str='(()()(()))'
res=''
count=0
for i in str:
    if i == '(':
        if count > 0:
            res += i
        count += 1
    elif i == ')':
        if count > 1:
            res += i
        count -= 1

print(res)