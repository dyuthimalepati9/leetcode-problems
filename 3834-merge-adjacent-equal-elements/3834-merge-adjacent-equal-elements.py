class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:

        stack = []
        
        for curr in nums:
            
            while stack and stack[-1] == curr:
                curr+= stack.pop()
            stack.append(curr)

        return stack
    