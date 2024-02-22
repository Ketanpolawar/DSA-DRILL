N=int(input("Enter The value of N:"))
def pattern(N):
    c=0
    for i in range(0,N+1):
        for j in range(0,i):
            print(c+1,end="")
            print(" ",end="")
            c=c+1
        print("\n")
pattern(N)