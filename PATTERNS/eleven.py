N = int(input("Enter the value of N:"))
def pattern(N):
    for i in range(0,N+1):
        if(i%2==0):
            c=1
        else:
            c=0
        for j in range(0,i):
            print(1-c,end="")
            c=1-c
        print("\n")
pattern(N)
