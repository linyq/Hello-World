import time

def getResult(num):
	n = 1
	for i in range(1, num+1):
		n += i
	return n 

def getResult1(num):
	if num == 1:
		return 1
	else:
		return num + getResult1(num-1)
if __name__ == '__main__':
	start1 =time.time()
	print(getResult(200))
	print("for 时间：%-10f"%(time.time()-start1))
	start2 =time.time()
	print(getResult1(200))
	print("递归时间：%10f"%(time.time()-start2))