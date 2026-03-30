class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # counting frequency
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        # get max frequency
        maxFreq = max(freq.values())

        # set buckets for possible frequencies
        # [[], [], [], []]
        buckets = [[]for _ in range(maxFreq + 1)]

        # append nums for buckets
        for num, f in freq.items():
            buckets[f].append(num)

        # get most frequency from the end til it's less than k
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result



