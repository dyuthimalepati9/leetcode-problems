class Solution:
    def factorial(self, n: int) -> int:
        ans = 1
        for i in range(1,n+1):
            ans *= i
        return ans

    def getPermutation(self, n: int, k: int) -> str:
        lst = [i for i in range(1,n+1)]
        idx = 0

        while k>1:
            num_can_swap = len(lst) - idx
            ft = self.factorial(num_can_swap)
            t_ft = ft // num_can_swap

            t_idx = (k-1)//t_ft
            if (idx+t_idx) == len(lst):
                lst[idx:] = lst[idx:][::-1]
                break
            lst[idx] , lst[idx+t_idx] = lst[idx+t_idx] , lst[idx]
            lst[idx+1:] = sorted(lst[idx+1:])
            k -= t_idx*t_ft
            idx += 1

        lst = [str(i) for i in lst]
        return ''.join(lst) 