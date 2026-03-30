class Solution {
    public int removeElement(int[] nums, int val) {
        // k = 0
        // for i in range(len(nums)):
        //     if nums[i] != val:
        //         nums[k] = nums[i]
        //         k += 1

        // return k

        int k = 0;
        for(int i = 0; i < nums.length; i++){
            if (nums[i] != val){
                nums[k] = nums[i];
                k++;
            }
        }
        return k;
    }
}