class Solution {
    public String longestCommonPrefix(String[] strs) {
        // prefix = strs[0]

        // for word in strs[1:]:
        //     i = 0
        //     # while chars match and within boundaries, increment i
        //     while i < len(prefix) and i < len(word) and prefix[i] == word[i]:
        //         i += 1
            
        //     # else, decrement prefix to be appropriate 
        //     prefix = prefix[:i]

        // return prefix

        String prefix = strs[0];
        for(int i = 1; i < strs.length; i++){
            String word = strs[i];
            int j = 0;

            while (j < prefix.length() && j < word.length()){
                if(prefix.charAt(j) != word.charAt(j)){
                    break;
                }
                j++;
            }
            prefix = prefix.substring(0, j);

        }
        return prefix;
    }
}