N=int(input("Enter the value of N"))
def pattern(N):
    
    for i in range (0,N+1):
        c=65
        d=65
        for j in range(0,N-i):
            print(" ",end="")
        for j in range (0,i):
            print(chr(c),end="")
            c=c+1
        c=c-2
        for j in range(0,i-1):
            print(chr(c),end="")
            c=c-1
        print("\n")
pattern(N)