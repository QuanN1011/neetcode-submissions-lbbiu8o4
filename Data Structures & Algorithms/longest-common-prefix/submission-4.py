class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # set prefix as the first word
        # loop through starting from second word
            # if length is shorter, decrement prefix
        # return prefix


        prefix = strs[0]
        for word in strs[1:]:
            j = 0

            while j < len(word) and j < len(prefix):
                if prefix[j] != word[j]:
                    break
                j += 1
            prefix = prefix[:j]
        return prefix
            



