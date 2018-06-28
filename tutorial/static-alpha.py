if __name__ == '__main__':
	rel_dic={}
	text=raw_input()
	for v in text:
		if v.isalpha():
			rel_dic[v.upper()]=rel_dic[v.upper()]+1 if rel_dic.get(v.upper(),0) else 1
	key_lst=sorted(rel_dic)
	for k in key_lst:
		print "{0}: {1}".format(k,rel_dic[k])