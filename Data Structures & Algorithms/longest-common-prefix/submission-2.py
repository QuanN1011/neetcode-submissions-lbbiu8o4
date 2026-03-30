class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # set first word to be prefix
        # increment through list and check each string
            # if char at index is not in prefix, remove from prefix

        # return prefix

        prefix = strs[0]

        for word in strs[1:]:
            i = 0
            # while chars match and within boundaries, increment i
            while i < len(prefix) and i < len(word) and prefix[i] == word[i]:
                i += 1
            
            # else, decrement prefix to be appropriate 
            prefix = prefix[:i]

        return prefix
            



