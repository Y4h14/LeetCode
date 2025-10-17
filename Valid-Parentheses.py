class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        if not s:
            return False

        for i in s:
            if i in ['(', '[', '{']:
                stack.append(i)
            elif i in [')', ']', '}']:
                if not stack:
                    return False
                j = stack.pop()
                if j == '(' and i != ')':
                    return False
                elif j == '[' and i != ']':
                    return False
                elif j == '{' and i != '}':
                    return False

        if stack:
            return False
        return True