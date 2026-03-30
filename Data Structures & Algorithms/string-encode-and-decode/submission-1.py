class Solution:

    def encode(self, strs: List[str]) -> str:
        encodeStr = ""
        for word in strs:
            length = len(word)
            encodeStr += str(length)
            encodeStr += "#"
            encodeStr += word

        return encodeStr
    def decode(self, s: str) -> List[str]:
        decodeStr = []
        i = 0
        length = ''
        while i < len(s):
            c = s[i]
            if ord('0') <= ord(c) <= ord('9'):
                length += c
                i += 1
            elif c == '#':
                n = int(length)
                decodeStr.append(s[i+1: (i+1) + n])
                i += (n+1)
                length = ""

                
        return decodeStr
