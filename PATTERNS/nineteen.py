N =int(input("Enter the value of N:"))
def pattern(N):
    for i in range(0,N+1):
        for j in range(0,N-i):
            print("*",end="")
        for j in range(0,i):
            print(" ",end="")
            print(" ",end="")
        for j in range(0,N-(i)):
            print("*",end="")
        print("\n",end="")
    for i in range(N+1,-1,-1):
        for j in range(0,N-i):
            print("*",end="")
        for j in range(0,i):
            print(" ",end="")
            print(" ",end="")
        for j in range(0,N-(i)):
            print("*",end="")
        print("\n",end="")    
pattern(N)