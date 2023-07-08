public class Solution {
    public int singleNumber(int[] nums) {
        int result = 0;
        for (int i = 0; i < nums.length; i++) {
            result = nums[i];
        }
        return result;
    }

    public static void main(String[] args) {
        int[] list = {2, 18, 6, -4, 5, 1};

        Solution sol = new Solution();
        int result = sol.singleNumber(new int[]{3, 4, 4, 3, 3, 3, 3});
        System.out.println(result);
    }
}
