//C# solution to the TwoSum problem. My java solution is twice as fast.

public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        int i = 0;
        int n = 0;
        int size = nums.Length;
        
        for (i = 0; i < size; i++) {                  
            for (n = i + 1; n < size; n++) {
                if (nums[i] + nums[n] == target) {
                    return new int[]{i, n};
                }
            }
        }        
        
        return Array.Empty<int>();
    }
}