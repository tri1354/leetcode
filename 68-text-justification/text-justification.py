class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        output = []
        check = 0
        width = 0
        for i in range(len(words)):
            if width + len(words[i]) + (i - check) > maxWidth:
                line = ""
                spaces = maxWidth - width
                gaps = i - check - 1
                if gaps == 0:
                    line = words[check] + " " * spaces
                else:
                    even = spaces // gaps
                    remain = spaces % gaps
                    for j in range(check, i):
                        line += words[j]
                        if j != i - 1:
                            line += " " * even
                            if remain > 0:
                                line += " "
                                remain -= 1
                output.append(line)
                check = i
                width = 0
            width += len(words[i])
        last = ""
        for i in range(check, len(words)):
            if i != check:
                last += " "
            last += words[i]
        last += " " * (maxWidth - len(last))
        output.append(last)

        return output