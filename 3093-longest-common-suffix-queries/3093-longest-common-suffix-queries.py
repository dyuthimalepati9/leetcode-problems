class TrieNode:
    def __init__(self):
        self.children = {}
        self.best_idx = -1 
class Solution:
    def stringIndices(self, wordsContainer: list[str], wordsQuery: list[str]) -> list[int]:
        root = TrieNode()
        global_best_idx = 0
        for i in range(1, len(wordsContainer)):
            if len(wordsContainer[i]) < len(wordsContainer[global_best_idx]):
                global_best_idx = i
        root.best_idx = global_best_idx
        for idx, word in enumerate(wordsContainer):
            curr = root
            for char in reversed(word):
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
                if curr.best_idx == -1:
                    curr.best_idx = idx
                else:
                    curr_len = len(wordsContainer[idx])
                    best_len = len(wordsContainer[curr.best_idx])
                    if curr_len < best_len:
                        curr.best_idx = idx
        ans = []
        for query in wordsQuery:
            curr = root
            
            for char in reversed(query):
                if char in curr.children:
                    curr = curr.children[char]
                else:
                    break 
            ans.append(curr.best_idx)
        return ans