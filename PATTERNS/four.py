N=int(input("enter the value of N:"))
def pattern(N):
    for i in range(1,N+1):
        for j in range(0,i):
            print(i,end="")
        print("\n")
pattern(N)