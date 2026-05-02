class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ans = ''
        a = ''
        for i in s:
            if i == '1':
                k -= 1
            a += i
            if k == 0:
                b = a.strip('0').rstrip('0')
                if len(ans) == 0 or len(b) < len(ans):
                    ans = b
                elif b < ans and len(b) <= len(ans):
                    ans = b
                ind = a.index('1')
                a = a[ind+1::]
                k += 1
        return ans
         