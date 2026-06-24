class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        value_count = r - l + 1
        initial_dp = list(range(value_count))
        transition_matrix = [[0] * value_count for _ in range(value_count)]
        for row in range(1, value_count):
            for col in range(value_count - row, value_count):
                transition_matrix[row][col] = 1
        def multiply_matrices(matrix_a, matrix_b):
            size = len(matrix_a)
            result = [[0] * size for _ in range(size)]
            for row in range(size):
                for mid in range(size):
                    if matrix_a[row][mid] == 0:
                        continue

                    for col in range(size):
                        result[row][col] = (result[row][col]+ matrix_a[row][mid] * matrix_b[mid][col]) % MOD

            return result

        def matrix_power(matrix, power):
            size = len(matrix)
            result = [[1 if row == col else 0 for col in range(size)] for row in range (size)]
            while power:
                if power & 1:
                    result = multiply_matrices(result, matrix)
                matrix = multiply_matrices(matrix, matrix)
                power >>= 1
            return result
        powered_transition = matrix_power(transition_matrix, n - 2)
        answer = 0

        for row in range(value_count):
            for col in range(value_count):
                answer = (answer + powered_transition[row][col] * initial_dp[col]) % MOD
        return (answer * 2) % MOD
