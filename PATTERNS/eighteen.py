N=int(input("Enter the value of N:"))
def pattern(N):
    for i in range(N+1):
        c=70
        for j in range (0,i):
            c=c-1
        for j in range(0,i):
            print(chr(c),end="")
            c=c+1
        print("\n")
pattern(N)
