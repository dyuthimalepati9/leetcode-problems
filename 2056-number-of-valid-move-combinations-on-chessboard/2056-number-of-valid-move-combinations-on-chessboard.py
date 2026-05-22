from itertools import product
class Solution:
    def countCombinations(self, pieces: list[str], positions: list[list[int]]) -> int:
        dirs = {
            'rook': [(1,0), (-1,0), (0,1), (0,-1)],
            'bishop': [(1,1), (1,-1), (-1,1), (-1,-1)],
            'queen': [(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]
                }
        n = len(pieces)
        dests = []
        steps = 0
        for piece, (row, col) in zip(pieces, positions):
            lst = []
            for dr, dc in dirs[piece]:
                nr, nc = row, col
                step = 0
                while (1 <= nr+dr and nr+dr <= 8) and (1 <= nc+dc and nc+dc <= 8):
                    nr += dr
                    nc += dc
                    step += 1
                    lst.append((row, col, dr, dc, step))
                    steps = max(steps, step)
            lst.append((row, col, 0, 0, 0))
            dests.append(lst)
        cnt = 0
        for case in product(*dests):
            ok = True
            for t in range(steps+1):
                seen = set()
                for r0, c0, dr, dc, st in case:
                    step = min(t, st)
                    row = r0 + dr*step
                    col = c0 + dc*step
                    if (row, col) in seen:
                        ok = False
                        break
                    seen.add((row, col))
                if not ok:
                    break
            if ok:
                cnt += 1
        return cnt   