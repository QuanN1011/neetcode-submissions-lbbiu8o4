class Solution {
    public int majorityElement(int[] nums) {
        // major = math.floor(len(nums)/2)
        // count = {}

        // for num in nums:
        //     count[num] = count.get(num, 0) + 1

        // for c in count:
        //     if count[c] > major:
        //         return c

        int major = nums.length/2;
        HashMap<Integer, Integer> count = new HashMap<>();

        for (int num : nums){
            count.put(num, count.getOrDefault(num, 0) + 1);

        }

        for (int c : count.keySet()){
            if (count.get(c) > major){
                return c;
            }
        }
        return 0;
    }
}