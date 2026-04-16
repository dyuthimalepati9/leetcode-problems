from functools import lru_cache

class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:

        @lru_cache(maxsize=None)
        def recursion(left, right, count=0):
            if left > right:
                return 0
            
            while left + 1 <= right and boxes[left] == boxes[left + 1]:
                left += 1
                count += 1
            
            count += 1

            answer = (count ** 2) + recursion(left + 1, right)

            for i in range(left + 1, right + 1):
                if boxes[left] == boxes[i]:
                    answer = max(
                        answer,
                        recursion(i, right, count) + recursion(left + 1, i - 1)
                    )
                
            return answer

        
        return recursion(0, len(boxes) - 1)