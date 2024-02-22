N=int(input("Enter the value of N:"))
def pattern(N):
    i=0
    j=0
    for i in range(0,N+2):
        for j in range(1,i):
            print(j,end="")
        print("\n")
    
pattern(N)