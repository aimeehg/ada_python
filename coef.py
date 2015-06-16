import numpy
def CoefIter(n,k):
#coeficiente binomial
	C = numpy.tile(0, (n+1,k+1))
	
	for i in range(0,n+1):
		C[i][0] = 1
	for i in range(1,n+1):
		C[i][1] = i
	for i in range(2,k+1):
		C[i][i] = 1
	for i in range(3,n+1):
		for j in range(2,i):
			if j <= k:
				C[i][j] = C[i-1][j-1] + C[i-1][j]
	return C[n][k]

print CoefIter(5,3)

