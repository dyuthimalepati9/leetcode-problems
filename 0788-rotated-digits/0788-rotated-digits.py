class Solution:
    def rotatedDigits(self, n: int) -> int:
        valid = {2, 5, 6, 9}
        invalid = {3, 4, 7}
        total = 0
        for index in range(1, n + 1):
            number = index
            flag = False
            while number > 0:
                if number % 10 in invalid:
                    flag = False
                    break
                else:
                    if number % 10 in valid: flag = True
                    number //= 10
            if flag == True:
                total += 1
        return total 