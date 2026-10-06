class Solution:
    def simplifyPath(self, path: str) -> str:
        directories = path.split('/')
        stack = []

        for folder in directories:
            if folder == '..':
                if stack: stack.pop()
            elif folder == '' or folder == '.':
                continue
            else:
                stack.append(folder)

        return '/' + '/'.join(stack)