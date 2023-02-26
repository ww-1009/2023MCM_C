import Tool


filepath='data/allowed_words.txt'
word_dic={"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,
		  "i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,
		  "q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,
		  "y":0,"z":0}

letter_dic={"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,
		  "i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,
		  "q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,
		  "y":0,"z":0}

FirstLetter_dic={"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,
		  "i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,
		  "q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,
		  "y":0,"z":0}

LastLetter_dic={"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,
		  "i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,
		  "q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,
		  "y":0,"z":0}

count = Tool.get_txtLineNum(filepath)
listOfLines  =  Tool.get_txtfile(filepath)
for  line in  listOfLines:
	word=line.strip()
	letter_list=list(word)
	FirstLetter_dic[letter_list[0]]=FirstLetter_dic[letter_list[0]]+1 # 首字母
	LastLetter_dic[letter_list[4]] = LastLetter_dic[letter_list[4]] + 1 # 最后字母
	# 字母出现次数
	for i in letter_list:
		word_dic[i]=word_dic[i]+1

	# 包含某个单词的出现次数
	lst = list(set(word))
	for m in lst:
		letter_dic[m]=letter_dic[m]+1
# print(word_dic)
# print(letter_dic)

letter_num=count*5
print(letter_num)
datas_freqs=[]
for key,value in word_dic.items():
	freqs=value/letter_num
	item_dic={}
	item_dic["letter"]=key
	item_dic["num"]=value
	item_dic["freqs"]=freqs
	item_dic["包含单词的个数"] = letter_dic[key]
	item_dic["百分比"] = letter_dic[key]/count
	item_dic["首字母出现次数"] = FirstLetter_dic[key]
	item_dic["末尾字母出现次数"] = LastLetter_dic[key]
	datas_freqs.append(item_dic)
print(datas_freqs)


header = ['letter', 'num','freqs','包含单词的个数',"百分比","首字母出现次数","末尾字母出现次数"]  # 数据列名
datas = datas_freqs

Tool.csv_write('allowed_words.csv',header=header,datas=datas)
