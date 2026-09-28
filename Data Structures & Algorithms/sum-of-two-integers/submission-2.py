class Solution:
    def getSum(self, a: int, b: int) -> int:
        arrayA = self.get_all_bits(a)
        arrayB = self.get_all_bits(b)

        # get max length
        maxLen = max(len(arrayA), len(arrayB))

        # 2. Zero-pad the shorter array to match max_len
        arrayA = [0] * (maxLen - len(arrayA)) + arrayA
        arrayB = [0] * (maxLen - len(arrayB)) + arrayB

        carry = 0
        res = []

        for idx in range(maxLen -1, -1, -1):
            res.append(arrayA[idx] ^ arrayB[idx] ^ carry)
            carry = (arrayA[idx] & arrayB[idx]) | (arrayA[idx] & carry) | (arrayB[idx] & carry)

        if carry == 1:
            res.append(carry)
        
        ans = 0
        for bit in res[::-1]:
            ans = (ans << 1) | bit
            
        # 2. CRITICAL: Force the answer into a 32-bit boundary space
        ans = ans & 0xFFFFFFFF
            
        # 3. Safe 32-bit signed transformation threshold
        return ans if ans <= 0x7FFFFFFF else ~(ans ^ 0xFFFFFFFF)



    def get_all_bits(self, number):
        # Convert negative numbers to their 32-bit unsigned representation
        # e.g., -1 becomes 4294967295 (all 1s in binary)
        number = number & 0xFFFFFFFF
        return [int(bit) for bit in f"{number:b}"]