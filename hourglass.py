# Hourglass Problem

R = 5
C = 5
def MaxSum(arr):
	max_sum = -50
	if(R < 3 or C < 3):
		return -1
	for i in range(0, R-2):
		for j in range(0, C-2):
			SUM = (arr[i][j] + arr[i][j + 1] + arr[i][j + 2]) + (arr[i + 1][j + 1]) +(arr[i + 2][j] +arr[i + 2][j + 1] + arr[i + 2][j + 2])

			if(SUM > max_sum):
				max_sum = SUM
			else:
				continue
	return max_sum
arr = [[1, -2, 3, 0, 0],
	[0, 0, 0, 0, 0],
	[2, 1, -4, 0, 0],
	[0, 0, 0, 0, 0],
	[1, 1, 0, 1, 0]]
res = MaxSum(arr)

if(res == -1):
	print("Not possible")
else:
	print(f"Max sum of hour glass = ",res)

