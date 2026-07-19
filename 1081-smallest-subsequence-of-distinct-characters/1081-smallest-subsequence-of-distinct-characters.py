class Solution:
    def smallestSubsequence(self, s: str) -> str:
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1
        in_stack = [False] * 26
        stack = []
        for ch in s:
            freq[ord(ch) - ord('a')] -= 1
            if in_stack[ord(ch) - ord('a')]:
                continue
            while (
                stack and
                stack[-1] > ch and
                freq[ord(stack[-1]) - ord('a')] > 0
            ):
                in_stack[ord(stack.pop()) - ord('a')] = False
            stack.append(ch)
            in_stack[ord(ch) - ord('a')] = True
        return "".join(stack)