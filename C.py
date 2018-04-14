from operator import itemgetter

def cut(a, b):
	val = [0,0,0]
	val[0] = 2*a
	val[1] = 2*b
	val[2] = ((a**2 + b**2)**0.5 + a + b)*2-(a+b)*2
	val.sort()
	if val[1]==val[0]:
		val[1] = val[2]
	val[2] = val[2]-val[1]
	val[1] = val[1] - val[0]
	return val

def mor(val, dif):
	l = dif 
	for i in range(0,3):
		for j in val:
			y = j[i]
			if (l-y < 0):
				if i == 2:
					return 0
			else:
				l -= y
	return l


for i in range(0, int(input())):
	n, p = map(int, input().split())
	val = []
	curPer = 0
	for hh in range(n):
		w, h = map(int, input().split())
		curPer += 2*(w+h)
		val.append(cut(w, h))
	val = sorted(val, key=itemgetter(0,1,2))
	dif = p-curPer
	out = None
	if dif <= 0:
		out = curPer
	else:
		out = p-mor(val, dif)
	print("Case #{}: {}".format(i+1, out))