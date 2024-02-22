N=int(input("Enter the value of N:"))
def pattern(N):
    for i in range (0,N):
        for j in range (0,N-i):
            print(" ",end="")
        for j in range(0,2*i+1):
            print("*",end="")
        print("\n")
pattern(N)
