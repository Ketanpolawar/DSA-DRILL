public static void main(String args []){
    int A=10;
    int B;
    B=public static int CountSet(A);
    System.out.println(B);
}

public static int CouSet(int num){
    int count=0;
    while(num!=0){
    num&=num-1;
    count=count+1;
    }
    retun count;
}