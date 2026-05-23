def countPerms(s: str, k: int) -> (int, OrderedDict[str, int], str):
  freq = OrderedDict(sorted(Counter(s).items()))
  n, ret, toPermute = 0, 1, {}
  while ret <= k and freq:
    c, v = freq.popitem(last=True)
    n += v
    ret *= comb(n, v) 
    toPermute[c] = v
  return ret, dict(reversed(toPermute.items())), ''.join(c * v for c, v in freq.items())
class Solution:
  def smallestPalindrome(self, s: str, k: int) -> str:
    h = len(s) // 2
    sHalf = s[:h]
    totalPerms, toPermute, prefix = countPerms(sHalf, k)
    if k > totalPerms: return ''
    freqSum = sum(toPermute.values())
    ret = [prefix]
    while toPermute:
      for c, cFreq in toPermute.items():
        bracket = totalPerms * cFreq // freqSum
        if k > bracket:
          k -= bracket
          continue
        ret.append(c)
        freqSum -= 1
        totalPerms = bracket
        if cFreq > 1: toPermute[c] = cFreq - 1
        else: toPermute.__delitem__(c)
        break
    s2 = ''.join(ret)
    if len(s) % 2:  return s2 + s[h] + s2[::-1]
    else:           return s2 +        s2[::-1]  