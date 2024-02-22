N=int(input("Enter the Value of N"))
def pattern(N):
    for i in range (N,-1,-1):
        for j in range(1,i+1):
            print(j,end="")
        print("\n")
pattern(N)