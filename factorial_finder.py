# factorial finder

n = 7

def fac(n):
	if n == 1:
		return 1
	elif n == 0:
		return 1
	else:
		return n*fac(n-1)


a = fac(n)
print(a)