class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        directories = path.split('/') # ['', neetcode, '', practice, '']

        for name in directories:
            if name == "..":
                if stack: stack.pop() # return back a dir
            elif name == "" or name == ".":
                continue
            else:
                stack.append(name)
        
        return "/" + "/".join(stack)