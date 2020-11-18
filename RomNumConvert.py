class Solution:
    def romanToInt(self, s: str) -> int:
        romLib = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        alls = list(s)
        alnum, i = 0, 0
        while i in range(len(alls)-1):
            if romLib[alls[i]] > romLib[alls[i+1]]:
                alnum += romLib[alls[i]]
            elif romLib[alls[i]] == romLib[alls[i+1]]:
                alnum += romLib[alls[i]]
                if i+2 != len(alls):
                    if romLib[alls[i]] == romLib[alls[i+2]]:
                        alnum += romLib[alls[i]]
            elif romLib[alls[i]] < romLib[alls[i+1]]:
                alnum += romLib[alls[i+1]] - romLib[alls[i]]
                i += 1
            i += 1
        return alnum

s = 'MCMXCIV'
transporter = Solution()
print(transporter.romanToInt(s))
