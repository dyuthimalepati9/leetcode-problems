class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n=len(nums)
        nxt=[-1]*n
        idx={}
        for i, x in enumerate(nums):
            if x not in idx:
                idx[x]=i
            else:
                nxt[i]=idx[x]
                idx[x]=i
        ans=[0]*n
        for x, h in idx.items():
            if nxt[h]==-1: continue
            total, prefix=0, 0
            vz, j=0, h
            while j!=-1:
                total+=j
                vz+=1
                j=nxt[j]
            j=h
            for i in range(vz-1, -1, -1):
                 ans[j]=(2*i-vz+2)*j+2*prefix-total
                 prefix+=j
                 j=nxt[j]
        return ans