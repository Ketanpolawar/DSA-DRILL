bills=[5,5,5,10,20,5]
flag=1
five=0
ten=0
for i in bills:
    if i==5:
        five=five+1
    elif i==10:
        if five>0:
            five=five-1
            ten=ten+1
        else:
            flag=0
            break
    elif i==20:
        if five>=1 and ten >=1:
            ten=ten-1
            five=five-1
        elif five>=3:
            five=five-3
        else:
            flag=0
            break
print(flag)
        

        