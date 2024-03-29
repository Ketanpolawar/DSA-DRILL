public static void int(int [] num){
int ans=0;
for(int i=0 ;i<num.length;i++){

    ans=ans^i;
}
return ans;
}