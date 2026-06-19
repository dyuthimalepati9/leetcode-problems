MOD = 10**9+7
class StringHashing:
    def __init__(self,arr):
        self.hash = [0]*(len(arr)+1)
        self.pow = [1]*(len(arr)+1)
        for i in range(len(arr)):
            self.hash[i+1] = (self.hash[i]*131+arr[i])%MOD
            self.pow[i+1] = (self.pow[i]*131)%MOD
    def query(self,start,end):
        return (self.hash[end]-(self.hash[start]*self.pow[end-start]))%MOD
class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        if arr==[0]*(len(arr)):
            return [0,len(arr)-1]
        arr = arr[::-1]
        count = 0
        while arr and arr[-1]==0:
            arr.pop()
            count += 1
        arr = arr[::-1]
        pref = [0]
        for i in arr:
            pref.append(pref[-1]+i)
        sh = StringHashing(arr)
        i = 0;j = 0
        while i<len(arr):
            j = max(j,i+1)
            while j<len(arr) and arr[j]==0:
                j += 1
            if j+i<len(arr)-i-1 and sh.query(0,i+1)==sh.query(j,j+i+1)==sh.query(len(arr)-i-1,len(arr)) and pref[len(arr)-i-1]-pref[j+i+1]==0:
                return [count+i,count+j+i+1]
            i += 1
        return [-1,-1]