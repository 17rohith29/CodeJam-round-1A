def cut(a, b):
	val = [0,0,0]
	val[0] = 2*a
	val[1] = 2*b
	val[2] = ((a**2 + b**2)**0.5 + a + b)*2-(a+b)*2
	return [min(val), max(val)]

def mor(val, dif):
	l = dif 
	for j in val:
		a,b = j[0],j[1]
		if (l-a) < 0:
			return l
		elif (l-b) < 0:
		        return 0
		else:
			l -= b
	return l


for i in range(0, int(input())):
	n, p = map(int, input().split())
	val = []
	curPer = 0
	for hh in range(n):
		w, h = map(int, input().split())
		curPer += 2*(w+h)
		val.append(cut(w, h))
	dif = p-curPer
	out = None
	if dif <= 0:
		out = curPer
	else:
		out = p-mor(val, dif)
	print("Case #{}: {}".format(i+1, out))
