class Solution:
    def nearestPalindromic(self, n: str) -> str:
        k = len(n)
        cands = {str(c:=pow(10,k)+1), str((c-1)//10-1)}         
        pref = (str(int(n[:(k + 1)//2])+i) for i in (-1,0,1))   
        for left in pref:
            rght = left[-2::-1] if k%2 else left[::-1]          
            cands.add(left + rght)                              
        cands.discard(n)                                        
        return min(cands, key=lambda x:                       
                   (abs(int(x) - int(n)), int(x)))