public class Solution {
    // DO NOT MODIFY THE ARGUMENTS WITH "final" PREFIX. IT IS READ ONLY
    public int singleNumber(final int[] A) {
        int ans = 0;
        int count;
        
        // Iterate through each bit position
        for (int i = 0; i < 32; i++) {
            count = 0;
            
            // Count the number of occurrences of the current bit position
            for (int j = 0; j < A.length; j++) {
                if (((A[j] >> i) & 1) == 1) {
                    count++;
                }
            }
            
            // If the count is not divisible by 3, set the bit in the answer
            if (count % 3 == 1) {
                ans |= (1 << i);
            }
        }
        
        return ans;
    }
}
