if __name__ == '__main__':
	rel=raw_input().split()
	print rel
	if rel[1]=='+':
		print int(rel[0])+int(rel[2])
	elif rel[1]=='-':
		print int(rel[0])-int(rel[2])
	elif rel[1]=='*':
		print int(rel[0])*int(rel[2])
