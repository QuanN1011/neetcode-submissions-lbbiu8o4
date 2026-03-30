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
            # check if number
            if ord('0') <= ord(c) <= ord('9'):
                length += c
                i += 1
            # else reach the separator character
            elif c == '#':
                n = int(length) # get length
                start = i + 1
                end = start + n
                decodeStr.append(s[start: end])
                i = start + n
                length = ""

                
        return decodeStr
