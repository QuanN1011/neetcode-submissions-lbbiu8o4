class Solution:
    def decodeString(self, s: str) -> str:
        stack = [] #stores [prev_string, count]
        cur_str = "" 
        count = 0

        res = ""
        for c in s:
            if c == "]":
                prev_str, repeat_count = stack.pop()
                cur_str = prev_str + (repeat_count * cur_str)
            elif c == "[":
                stack.append([cur_str, count])
                cur_str = ""
                count = 0
            elif c.isdigit():
                count = count * 10 + int(c)
            else:
                cur_str += c

        return cur_str
            