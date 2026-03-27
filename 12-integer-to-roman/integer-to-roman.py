class Solution:
    def intToRoman(self, num: int) -> str:
        romans = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        values = [1000, 900, 500, 400,  100,  90,  50,   40,  10,   9,    5,   4,    1]
        ans = ""
        for i in range(len(values)):
            while num >= values[i]:
                ans += romans[i]
                num -= values[i]
        return ans


        # roman = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        # integer = []
        # N = num
        # for i in range(0, 7, 2):
        #     n = N % 10
        #     if n == 0:
        #         pass
        #     elif n == 5:
        #         integer.insert(0, roman[i+1])
        #     elif n == 9:
        #         integer.insert(0, roman[i+2])
        #         integer.insert(0, roman[i])
        #     elif n == 4:
        #         integer.insert(0, roman[i+1])
        #         integer.insert(0, roman[i])
        #     else:
        #         for j in range(n%5):
        #             integer.insert(0, roman[i])
        #         if n//5 == 1:
        #             integer.insert(0, roman[i+1])
        #     N //= 10
        # ans = "".join(integer)
        # return ans