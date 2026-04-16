class Solution:
    def longestValidParentheses(self, s: str) -> int:

        # count=0
        # maxlen=0
        # stk=[-1]
        # for i in range(len(s)):
        #     if s[i]=="(":
        #         stk.append(i)
        #     else:
        #         stk.pop()
        #         # count+=1
        #         if not stk:
        #             stk.append(i)
        #         else:
        #             maxlen=max(maxlen, i-stk[-1])
            
        # return maxlen
            
        left =0
        right =0
        maxlen = 0
        for ch in s:
            if ch == '(':
                left += 1
            else:
                right += 1
            if left == right:
                maxlen = max(maxlen, 2 * right)
            elif right > left:
                left = right = 0

        left=right=0
        for ch in reversed(s):
            if ch==")":
                right +=1
            else:
                left+=1
            if right==left:
                maxlen=max(maxlen,2*left)
            elif left>right:
                left=right=0
            

        return maxlen