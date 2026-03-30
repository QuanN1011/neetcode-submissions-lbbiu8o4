class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # map a...z to 0..26

        for s in strs:
            count = [0] * 26  # list to count freq a - z

            for c in s:
                count[ord(c)-ord("a")] += 1
            res[tuple(count)].append(s)

        return list(res.values())


