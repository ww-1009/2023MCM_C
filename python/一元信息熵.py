import math
import pandas as pd
import Tool

filename = 'allowed_words.csv'
df = pd.read_csv(filename)

freqs_dic = {}
for i in range(26):
	freqs_dic[df["letter"][i]] = df["freqs"][i]
print(freqs_dic)

filepath = 'data/test_words.txt'

word_datas = []

count = Tool.get_txtLineNum(filepath)
listOfLines = Tool.get_txtfile(filepath)
for line in listOfLines:
	word = line.strip()
	letter_list = list(word)
	# exist=[]
	item_dic = {}
	item_dic["word"] = word
	p = 1
	E = 0
	for l in letter_list:
		p = freqs_dic[l]  # 359 2309 12593
		# i=-math.log2(p) # 信息熵
		E = E + p * math.log2(p)
	item_dic["E"] = -E
	word_datas.append(item_dic)
print(word_datas)

header = ['word', 'E']  # 数据列名
datas = word_datas

Tool.csv_write('信息熵_test2.csv',header=header,datas=datas)
