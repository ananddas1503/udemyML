# factorial finder
# git link : https://github.com/ananddas1503/udemyML
# git profile = ananddas1503

# code to determine a factorial of an integer


n = int(input("enter an integer: "))

def fac(n):
	if n == 1:
		return 1
	elif n == 0:
		return 1
	else:
		return n*fac(n-1)


a = fac(n)
print(f'factorial of {n} is {a}')