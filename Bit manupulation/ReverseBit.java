public class Solution {
    public long reverse(long a) {
        long result = 0;
        int bitLength = 32; // Assuming long is 64 bits in Java
        
        for (int i = 0; i < bitLength; i++) {
            result <<= 1; // Shift the result to the left by 1 bit
            result |= (a & 1); // Take the least significant bit of a and set it to the least significant bit of result
            a >>= 1; // Shift a to the right by 1 bit
        }
        
        return result;
    }
}
