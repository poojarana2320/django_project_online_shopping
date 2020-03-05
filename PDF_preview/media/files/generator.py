# def gen():
# 	n=1
# 	print n
# 	yield n

# 	n+=1
# 	print n
# 	yield n

# 	n+=1
# 	print n
# 	yield n
# a=gen()
# next(a)
# next(a)
# next(a)	

def fun():
	for i in range(4):
		yield i

for i in fun():
	print i		


