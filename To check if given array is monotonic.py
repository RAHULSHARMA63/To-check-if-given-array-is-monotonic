def isMonotonic(A):

	return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
			all(A[i] >= A[i + 1] for i in range(len(A) - 1)))

A = [6, 7, 4, 4]

print(isMonotonic(A))