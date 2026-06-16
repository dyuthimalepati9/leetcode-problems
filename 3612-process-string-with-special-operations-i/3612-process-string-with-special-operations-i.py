class Solution:
    def processStr(self, s: str) -> str:
        answer = []

        for c in s:
            if 'a' <= c <= 'z':
                answer.append(c)
            elif c == '#':
                answer += answer
            elif c == '*':
                if answer:
                    answer.pop()
            elif c == '%':
                answer.reverse()

        return ''.join(answer)