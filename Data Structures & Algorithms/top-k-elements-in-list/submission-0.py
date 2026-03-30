class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort, first count frequencies
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # find max frequency
        maxFreq = max(freq.values())

        # create buckets for max frequencies, [[], [], [], []]
        buckets = [[] for _ in range(maxFreq + 1)]

        # get the num for each bucket
         # [[], [1], [2], [3]] -> num for each frequency with corr bucket
        for num, f in freq.items():
            buckets[f].append(num)

        # store in result array until reach k length
        result = []
        for frequency in range(maxFreq, 0, -1):
            for num in buckets[frequency]:
                result.append(num)
                if (len(result) == k):
                    return result


        
