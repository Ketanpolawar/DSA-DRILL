N = int(input("Enter the Value of N :"))
def pattern(N):
    for i in range(0,N):
        for j in range(0,N-1):
             print(" ",end="")
        for j in range(0,2*i+1):
            print("*",end="")
        print("\n")
    for i in range(N-2,-1,-1):
        for j in range(0,N-1):
             print(" ",end="")
        for j in range(0,2*i+1):
            print("*",end="")
        print("\n")
    
pattern(N)
