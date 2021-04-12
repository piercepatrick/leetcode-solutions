class Solution {
    public int xorOperation(int n, int start) {
        int[] nums = new int[n];
        int xor_arr = 0;
        
        for (int i =0; i < nums.length; i++) {
            nums[i] = start + 2*i;
            xor_arr = xor_arr ^ nums[i];
        }
        
        return xor_arr;
    }
}