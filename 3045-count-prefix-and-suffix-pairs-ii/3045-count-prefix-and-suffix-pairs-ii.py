from sortedcontainers import SortedList
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        seen = dict()
        sol=0
        lengths_seen=SortedList([1])
        for w in words:
            wlen= len(w)
            for i in lengths_seen:
                if i > wlen:
                    break
                if w[:i] == w[-i:]:
                    newkey=w[:i]
                    if newkey in seen:
                        sol+=seen[newkey]
                i+=1
            seen[w]=seen.get(w,0)+1
            if wlen not in lengths_seen:
                lengths_seen.add(wlen)
        return sol   