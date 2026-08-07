class Solution:
    def smallestNumber(self, num: str, target: int) -> str:
        def construct_number(required, length):
            digits = []
            for digit in range(9, 1, -1):
                while required % digit == 0:
                    digits.append(digit)
                    required //= digit
            digits.extend([1] * max(0, length - len(digits)))
            return "".join(map(str, reversed(digits)))
        n = len(num)
        temp = target
        for prime in [2, 3, 5, 7]:
            while temp % prime == 0:
                temp //= prime
        if temp != 1:
            return "-1"
        required_factors = [target] * (n + 1)
        for i, digit in enumerate(map(int, num)):
            if digit == 0: 
                break
            required_factors[i + 1] = required_factors[i] // gcd(required_factors[i], digit)
        if required_factors[-1] == 1:
            return num
        zero_pos = num.find("0") % n
        for pos in range(zero_pos, -1, -1):
            curr_req = required_factors[pos]
            remaining_len = n - 1 - pos
            for new_digit in range(int(num[pos]) + 1, 10):
                suffix = construct_number(curr_req // gcd(curr_req, new_digit), remaining_len)
                if len(suffix) <= remaining_len:
                    return num[:pos] + str(new_digit) + suffix
        return construct_number(target, n + 1)   