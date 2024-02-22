N =int(input("Enter the value of N:"))
def pattern(N):
    i=0
    j=0
    for i in range(N,-1,-1):#-ve iteration
        for j in range(0,i):
            print("*",end="")
        print("\n")
pattern(N)