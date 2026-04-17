class Solution:
    def simplifyPath(self, path: str) -> str:
        # Split the path into components
        components = path.split('/')
        
        # Stack to keep valid directories
        stack = []
        
        for comp in components:
            if comp == '' or comp == '.':
                continue
            elif comp == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(comp)
        
        # Join the stack into a simplified path
        return '/' + '/'.join(stack)