class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        def getprestates(m ,c ,t):
            ans = []
            if t == 1:
                for c2 in graph[c]:
                    if not c2: continue
                    ans.append((m, c2, 2))
            else:
                for m2 in graph[m]:
                    ans.append((m2, c, 1))
            return ans

        def nextfails(m, c, t):
            if t == 1:
                for m2 in graph[m]:
                    if res[(m2, c, 2)] != 2: return False
            else:
                for c2 in graph[c]:
                    if not c2: continue
                    if res[(m, c2, 1)] != 1: return False
            
            return True

        res = defaultdict(int) # mouse, cat, turns
        q = deque()

        for t in range(1, 3):
            for i in range(1, len(graph)):
                #mouse wins
                res[(0, i, t)] = 1
                q.append((0, i, t))

                #cat wins
                res[(i, i, t)] = 2
                q.append((i, i, t))
        
        while q:
            mouse, cat, turn = q.popleft()
            r = res[(mouse, cat, turn)]

            for m, c, t in getprestates(mouse, cat, turn):
                r2 = res[(m, c, t)]
                if r2:
                    continue
                
                #populate prestate
                if r == 3 - turn:
                    res[(m, c, t)] = r
                    q.append((m, c, r))
                elif nextfails(m, c, t):
                    res[(m, c, t)] = 3 - t
                    q.append((m, c, t))
        return res[(1, 2, 1)]
