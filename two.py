N=int(input("Enter the value of N : "))
i=0
for i in range(0,N+1):
    for j in range(0,i):
        print('*',end="")
    print("\n")