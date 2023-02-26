import re
import numpy as np
import pandas as pd

def re_match(listOfLines ):
	data=[]
	for  words in  listOfLines:
		# print(words)
		w=list(words)
		# print(w)
		flag=False
		for i in w:
			if i=='*':
				flag=True
				break
		if flag:
			s=re.findall(r'\d+', words)
			# print(s)
			result=float(s[0]+"."+s[1])/pow(10,int(s[2])-5)
			data.append(result)

		else:
			s = re.findall(r'\d+', words)
			result=float(s[0]+"."+s[1])*pow(10,5)
			data.append(result)
	return data

def median(data):
    data.sort()
    half = len(data) // 2
    return (data[half] + data[~half])/2

def sigmoid(X,useStatus):
    if useStatus:
        return 1.0 / (1 + np.exp(-float(X)))
    else:
        return float(X)
def z(lst):
	result=[]
	for x in lst:
		x = float(x - lst.mean()) / lst.std()
		result.append(x)
	return result

def guess(datas):
	result=[]
	for d in datas:
		result.append(sigmoid(d-0.24370987998060506,1))
	print(result)
	return result


if __name__ == '__main__':
	fileHandler  =  open  ("data2.txt",  "r")
	# Get list of all lines in file
	listOfLines  =  fileHandler.readlines()
	fileHandler.close()
	datas=re_match(listOfLines)
	print(datas)
	a = np.array(datas)
	# result=z(a)
	# print(result)

	m=np.median(a)
	print(m) # 0.24370987998060506
	# eerie=9.856329522011877/pow(10,2)
	# print(eerie)
	# print(sigmoid(eerie - m, 1))

	# result=[]
	# for d in datas:
	# 	result.append(sigmoid(d-m,1))
	# print(result)

	result=guess(a)
	# Close file
	df=pd.DataFrame(data=result,columns=['popularity'])
	df.to_csv("popularity_Z-score.csv")



