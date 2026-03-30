class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> freq = new HashMap<>();
        for (int num : nums){
            freq.put(num, freq.getOrDefault(num, 0) + 1);
        }

        int maxFreq = Collections.max(freq.values());

        List<List<Integer>> buckets = new ArrayList<>();
        for (int i = 0; i <= maxFreq; i++){
            buckets.add(new ArrayList<>());
        }

        for(Map.Entry<Integer, Integer> entry : freq.entrySet()){
            int num = entry.getKey();
            int f = entry.getValue();
            buckets.get(f).add(num);
        }

        List<Integer> resultList = new ArrayList<>();
        for (int i = maxFreq; i >= 1; i--) {
            for (int num : buckets.get(i)) {
                resultList.add(num);
                if (resultList.size() == k) {
                    // Convert to array and return
                    int[] result = new int[k];
                    for (int j = 0; j < k; j++) {
                        result[j] = resultList.get(j);
                    }
                    return result;
                }
            }
        }

        return new int[0]; // fallback, should not happen
    }
}
