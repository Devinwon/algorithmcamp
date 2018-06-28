if __name__=="__main__":
	start,end=raw_input().split()
	start=start.split(":")
	end=end.split(":")
	start=list(map(int,start))
	end=list(map(int,end))
	total=end[0]*3600+end[1]*60+end[2]-(start[0]*3600+start[1]*60+start[2])
	if total<0:
		total+=3600*24
	print total