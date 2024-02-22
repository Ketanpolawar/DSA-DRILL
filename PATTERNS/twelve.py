N=int(input("Enter the value of N:"))
def pattern(N):
    for i in range(0,N+1):
        c=0
        for j in range(0,i):
            c=c+1
            print(c,end="")
        for j in range(0,N-(i)):
            print(" ",end="")
        for j in range(0,N-(i+1)):
            print(" ",end="")
        c=c+1
        for j in range(0,i):
            c=c-1
            print(c,end="")
        print("\n")
pattern(N)