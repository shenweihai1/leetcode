
# merely using recursion
class Solution(object):
	def reverse_stack(self, stack):
		if len(stack) == 0:
			return []

		top = stack.pop()
		self.reverse_stack(stack)
		self.send_bottom(stack, top)
		return stack

	def send_bottom(self, stack, top):
		if len(stack) == 0:
			stack.append(top)
		else:
			t_top = stack.pop()
			self.send_bottom(stack, top)
			stack.append(t_top)


if __name__ == "__main__":
	obj = Solution()
	print(obj.reverse_stack([1, 2, 3, 4, 5, 6]))