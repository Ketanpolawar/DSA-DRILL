N=int(input("enter the value of N:"))
def pattern(N):
    for i in range(0,N+1):
        c=65
        for j in range(0,i):
            print(chr(c),end="")
            c=c+1
        print("\n")
pattern(N)
