class Solution {

    public String encode(List<String> strs) {
        StringBuilder encode = new StringBuilder();
        for(String word: strs){
            int length = word.length();
            encode.append(length).append("#").append(word);
        }
        return encode.toString();
    }
    public List<String> decode(String str) {
        List<String> decode = new ArrayList<>();
        int i = 0;
        String length = "";

        while(i < str.length()){
            char c = str.charAt(i);
            if(Character.isDigit(c)){
                length += c;
                i++;
            }
            else if(c == '#'){
                int n = Integer.parseInt(length);
                decode.add(str.substring(i + 1, i + 1 + n));
                i += n + 1; // move past '#' and the word
                length = ""; // reset for next word
            }
        }
        return decode;
    }
}
