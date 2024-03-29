public class Solution {
    public int solve(int A) {
        int flag=1;
        int count=0;
        while(A!=0 & flag==1){
            int B=A&1;
            if(B==0){
                count=count+1;
            }
            else{
                flag=0;  
            }
            A=A>>1;
        }
        return count;
    }
    
}