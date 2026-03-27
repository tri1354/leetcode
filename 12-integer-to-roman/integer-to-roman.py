class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        integer = []
        N = num
        for i in range(0, 7, 2):
            n = N % 10
            if n == 0:
                pass
            elif n == 5:
                integer.insert(0, roman[i+1])
            elif n == 9:
                integer.insert(0, roman[i+2])
                integer.insert(0, roman[i])
            elif n == 4:
                integer.insert(0, roman[i+1])
                integer.insert(0, roman[i])
            else:
                for j in range(n%5):
                    integer.insert(0, roman[i])
                if int(n/5) == 1:
                    integer.insert(0, roman[i+1])
            N = int(N/10)
        ans = "".join(integer)
        return ans