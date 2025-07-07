class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        if s[0]=="]" or s[0]==")" or s[0]=="}":
            return False
        for i in s:
            if i in "{([":
                stack.append(i)
            elif i =="}":
                if stack and stack[-1]=="{":
                    stack.pop()
                else:
                    stack.append(i)
            elif i ==")":
                if stack and stack[-1]=="(":
                    stack.pop()
                else:
                    stack.append(i)
            elif i =="]":
                if stack and stack[-1]=="[":
                    stack.pop()
                else:
                    stack.append(i)
        if stack==[]:
            return True
        else:
            return False
sol=Solution()
print(sol.isValid("()[]{}"))