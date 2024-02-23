N=int(input("Enter the value for N:"))
def pattern(N):
    for i in range(N):
        for j in range(N):
            if(i==0)|(j==0)|(j==N-1)|(i==N-1):
                print("*",end="")
            else:
                print(" ",end="")
        print("\n",end="")
pattern(N)