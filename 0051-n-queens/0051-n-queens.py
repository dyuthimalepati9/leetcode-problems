class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        negdiag = set()
        posdiag = set()

        result = []
        board = [["."]*n for i in range(n)]

        def backtrack(r): 
            if r==n:
                copy = ["".join(row) for row in board]
                result.append(copy)
                return
            for c in range(n):
                if c in col or r-c in negdiag or r+c in posdiag:
                    continue
                col.add(c)
                negdiag.add(r-c)
                posdiag.add(r+c)

                board[r][c] = 'Q'
                backtrack(r+1)

                col.remove(c)
                negdiag.remove(r-c)
                posdiag.remove(r+c)

                board[r][c] = '.'
                


        backtrack(0)
        return result



            