class Solution(object):

    def check_by_stack(self, A):
        stack = []
        for ch in A:
            if ch == '(':
                stack.append(ch)
            elif ch == ')':
                if not (stack and stack.pop() == '('):
                    return False

        return not stack

    def check_by_calculation(self, A):
        count = 0
        for ch in A:
            if ch == '(': 
                count += 1
            elif ch == ')':
                count -= 1
                if count < 0:
                    return False

        return count <= 0

    def get_lf_unbalanced(self, A):
        l, r = 0, 0
        for ch in A:
            l += 1 if ch == '(' else 0
            if l == 0:
                r += 1 if ch == ')' else 0
            else:
                l -= 1 if ch == ')' else 0

        return l, r

    def get_lf_unbalanced_by_stack(self, A):
        stack = []
        for ch in A:
            if ch == '(':
                stack.append(ch)
            elif ch == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(')')

        return stack


if __name__ == "__main__":
    obj = Solution()
    A = "(()())()"
    print(obj.check_by_stack(A))
    print(obj.check_by_calculation(A))
    print(obj.get_lf_unbalanced(A))
    print(obj.get_lf_unbalanced_by_stack(A))
    A = "(()())())))"
    print(obj.check_by_stack(A))
    print(obj.check_by_calculation(A))
    print(obj.get_lf_unbalanced(A))
    print(obj.get_lf_unbalanced_by_stack(A))
    
