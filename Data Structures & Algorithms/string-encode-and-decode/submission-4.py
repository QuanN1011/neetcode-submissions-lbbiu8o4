class Solution:

    def encode(self, strs: List[str]) -> str:
        encodeStr = ""
        for word in strs:
            length = str(len(word))
            encodeStr += length + "#" + word

        return encodeStr
    def decode(self, s: str) -> List[str]:
        decodeStr = []
        i = 0
        length = ""
        while i < len(s):
            c = s[i]
            if ord('0') <= ord(c) <= ord('9'):
                length += c
                i += 1
            elif c == '#':
                n = int(length)
                start = i + 1
                end = start + n
                decodeStr.append(s[start:end])
                i = end
                length = ""
        
        return decodeStr