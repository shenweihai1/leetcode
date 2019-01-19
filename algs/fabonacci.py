
# log(n)
class Solution(object):

	@staticmethod
	def multiply(x, y):
		x1, x2, x3, x4 = x 
		y1, y2, y3, y4 = y
		return (x1 * y1 + x2 * y3, x1 * y2 + x2 * y4, x3 * y1 + x4 * y3, x3 * y2 + x4 * y4)

	@staticmethod
	def matrix_pow(matrix, n):
		if n == 1:
			return matrix

		if n % 2 == 1:
			return Solution.multiply(matrix, 
									 Solution.multiply(Solution.matrix_pow(matrix, (n-1)/2), 
									 				   Solution.matrix_pow(matrix, (n-1)/2)))
		else:
			return Solution.multiply(Solution.matrix_pow(matrix, n/2), 
				                     Solution.matrix_pow(matrix, n/2))


	def get(self, n):
		if n == 1 or n == 2: return 1
		# pow((0, 1, 1, 1), n - 1) * (1, 1)
		x1, x2, x3, x4 = Solution.matrix_pow((0, 1, 1, 1), n - 1)
		return x1 + x2


if __name__ == "__main__":
	obj = Solution()
	for i in range(1, 100):
		print("i: %s, fabo: %s" % (i, obj.get(i)))
