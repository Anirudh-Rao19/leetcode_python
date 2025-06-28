#find the first occurence of substring in string
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            z=haystack.index(needle)
            return z
        else:
            return -1
sol=Solution()
print(sol.strStr("leetcode","leet"))
print(sol.strStr("leetcode","leeto"))
print(sol.strStr("leetcode","code"))
