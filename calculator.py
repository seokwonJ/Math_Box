# 기본 계산기
def add(x,y):
	return x+y
def multiplicate(x,y):
	return x*y
def subtract(x, y):
	return x-y
def devise(x,y):
	return x//y
def root (x,y):
	return x^2
def squared(x,y):
	return x**y
print("계산을 입력하시오: ",end = " ")
a = list(map(str,input().split()))
n1, n2 = int(a[0]),int(a[2])
if a[1] == "+":
	print(add(n1,n2))
if a[1] == "-":
	print(subtract(n1,n2)
if a[1] == "*":
	print(multiplicate(x,y))


