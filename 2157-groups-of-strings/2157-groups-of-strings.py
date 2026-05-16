SIMILAR_MASK = 1 << 26
CHAR_MASKS = {char: 1 << i for i, char in enumerate(string.ascii_lowercase)}
get_bits = lambda word: functools.reduce(
    operator.or_, (CHAR_MASKS[char] for char in word)
)
class Solution:
    def groupStrings(self, words: List[str]) -> List[int]:
        max_size = 1
        num_groups = len(words)
        disjoint_set = list(range(num_groups + 1))
        sizes = [1] * (num_groups + 1)
        def find(i):
            while (parent := disjoint_set[i]) != i:
                disjoint_set[i] = disjoint_set[parent]
                i = parent
            return parent
        def union(i, j):
            nonlocal max_size, num_groups
            if (i := find(i)) == (j := find(j)):
                return
            if sizes[i] < sizes[j]:
                i, j = j, i
            disjoint_set[j] = i
            sizes[i] += sizes[j]
            max_size = max(max_size, sizes[i])
            num_groups -= 1
        seen = {}
        for i, word in enumerate(words, start=1):
            bits = get_bits(word)
            if peer := seen.get(bits):
                union(peer, i)
                continue
            for mask in CHAR_MASKS.values():
                complement = bits ^ mask
                if peer := seen.get(complement):
                    union(peer, i)
                if bits & mask:
                    similar = complement ^ SIMILAR_MASK
                    if peer := seen.get(similar):
                        union(peer, i)
                    else:
                        seen[similar] = i
            seen[bits] = i
        return num_groups, max_size   