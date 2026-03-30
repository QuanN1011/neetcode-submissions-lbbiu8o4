class Solution {
    public int[] twoSum(int[] nums, int target) {
       HashMap<Integer, Integer> prev = new HashMap<>();

       for(int i = 0; i < nums.length; i++){
        int value = nums[i];
        int diff = target - value;
        if(prev.containsKey(diff)){
            return new int[] {prev.get(diff), i};
        }
        prev.put(value, i);
       }
       return new int[]{};
    }
}
