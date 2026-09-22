class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p,s in zip(position, speed)]
        stack = [] # stores the time

        for p, s in sorted(pair, reverse = True): #[::-1] also to rev
            time = (target - p) / s
            stack.append(time)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)
