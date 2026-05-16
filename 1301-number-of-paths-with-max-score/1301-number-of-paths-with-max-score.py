class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 1000000007
        
        @cache
        def dp(row: int, col: int) -> Tuple[int]:
            numRows, numCols = len(board), len(board[0])
            if row >= numRows or col >= numCols or board[row][col] == 'X':
                return(-inf, 0)
            score = ord(board[row][col]) - ord('0')
            if board[row][col] == 'E':
                score = 0
            if row == numRows - 1 and col == numCols - 1:
                return (0, 1)
            option1 = dp(row + 1, col)
            option2 = dp(row, col + 1)
            option3 = dp(row + 1, col + 1)
            count, ans = 0, score + max(option1[0], option2[0], option3[0])
            if score + option1[0] == ans: 
                count = (count + option1[1]) % MOD
            if score + option2[0] == ans: 
                count = (count + option2[1]) % MOD
            if score + option3[0] == ans:
                count = (count + option3[1]) % MOD
            return (ans, count % MOD)

        ans = dp(0, 0)
        return [max(ans[0], 0), ans[1]]