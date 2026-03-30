class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # declare list res
        # loop through each word in list strs
            # set list count for a ... z -> 0 ... 26
            # loop through each letter in each word
                # set count with key letter - a += 1
            # append res at key count using tuple with the word

        # return values of list res

        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)

        return list(res.values())


