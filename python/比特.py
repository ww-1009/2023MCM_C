import math
import pandas as pd
import Tool

filename = 'allowed_words.csv'
df = pd.read_csv(filename)

word_dic = {}
for i in range(26):
	word_dic[df["letter"][i]] = df["包含单词的个数"][i]
print(word_dic)

filepath = 'data/test_words.txt'

word_datas = []

count = Tool.get_txtLineNum(filepath)
listOfLines = Tool.get_txtfile(filepath)
for line in listOfLines:
	word = line.strip()
	letter_list = list(word)
	item_dic = {}
	item_dic["word"] = word
	p = 1
	for l in letter_list:
		p = p * (word_dic[l] / 12593)  # 359 2309 12593
	i = -math.log2(p)  # 信息熵
	item_dic["p"] = p
	item_dic["i"] = i
	word_datas.append(item_dic)
print(word_datas)

header = ['word', 'p', 'i']  # 数据列名
datas = word_datas

Tool.csv_write('信息熵_allowed.csv',header=header,datas=datas)