N=int(input("Enter the value of N:"))
def pattern(N):
    c=64
    for i in range(0,N+1):
        for j in range(0,i):
            print(chr(c),end="")
        c=c+1
        print("\n")
pattern(N)