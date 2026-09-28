class Solution:
    def simplifyPath(self, path: str) -> str:
        directories = path.split('/')
        stack = []

        for name in directories:
            if name == "..":
                if stack: stack.pop()
            elif name == "" or name == ".":
                continue
            else:
                stack.append(name)

        return "/" + "/".join(stack)
