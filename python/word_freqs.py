import numpy as np
import csv
import Tool


def get_letterFreqs():
	ALLWORDTXT = 'data/allowed_words.txt'
	word_dic = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0,
				"i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0,
				"q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0,
				"y": 0, "z": 0}

	freqs_dic = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0,
				 "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0,
				 "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0,
				 "y": 0, "z": 0}

	count = Tool.get_txtLineNum(ALLWORDTXT)
	letter_num = count * 5
	listOfLines2 = Tool.get_txtfile(ALLWORDTXT)
	for line in listOfLines2:
		word = line.strip()
		letter_list = list(word)
		# 字母出现次数
		for i in letter_list:
			word_dic[i] = word_dic[i] + 1

	for key, value in word_dic.items():
		freqs_dic[key] = value / letter_num
	return freqs_dic


if __name__ == '__main__':
	# filepath='data/test_words.txt'
	freqs_dic = get_letterFreqs()
	print(freqs_dic)
# word_datas=[]
# # fileHandler1  =  open  (filepath,  "r")
# # # Get list of all lines in file
# # listOfLines1  =  fileHandler1.readlines()
# # for  line in  listOfLines1:
# words=["apple","flail","stage","heady","debug","giang","usage","sound","salsa","magic","eerie"]
# for word in words:
# 	# word=line.strip()
# 	item_dic={}
# 	item_dic["word"] = word
# 	l_word=list(word)
# 	freqs_datas=[]
# 	for i in range(5):
# 		item_dic[str(i+1)] = freqs_dic[l_word[i]]
# 		freqs_datas.append(freqs_dic[l_word[i]])
#
# 	# item_dic["avg"] = np.mean(freqs_datas) # 平均值
# 	item_dic["avg"] = Tool.harmonic_mean(freqs_datas) # 平均值
# 	item_dic["var"] = np.var(freqs_datas)  # 计算总体方差
# 	item_dic["std"] = np.std(freqs_datas)  # 计算总体标准差
# 	word_datas.append(item_dic)
#
# print(word_datas)
#
# header = ['word', '1','2','3',"4","5","avg","var","std"]  # 数据列名
# datas = word_datas
#
# with open('guess_avg.csv', 'w', newline='', encoding='utf-8') as f:
# 	writer = csv.DictWriter(f, fieldnames=header)  # 提前预览列名，当下面代码写入数据时，会将其一一对应。
# 	writer.writeheader()  # 写入列名
# 	writer.writerows(datas)  # 写入数据
