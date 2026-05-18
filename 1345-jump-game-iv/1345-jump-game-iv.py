class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        d = defaultdict(list)
        for i in range(n):
            d[arr[i]].append(i)
        n -= 1
        curr = [0]
        used = set([0])
        set_arr = set()
        jump = 0
        while curr:
            nxt = []
            for i in curr:
                if i == n:
                    return jump
                j = i + 1
                if j <= n and j not in used:
                    nxt.append(j)
                    used.add(j)
                j = i - 1
                if j > 0 and j not in used:
                    nxt.append(j)
                    used.add(j)
                if arr[i] not in set_arr:
                    set_arr.add(arr[i])
                    for j in d[arr[i]]:
                        if j not in used:
                            used.add(j)
                            nxt.append(j)
            curr = nxt
            jump += 1