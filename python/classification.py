import pandas as pd
import Tool

# filename = '信息熵_test3.csv'
# df = pd.read_csv(filename)
#
# word_dic={}
# for i in range(359):
#     word_dic[df["word"][i]]=df["E"][i]
# print(word_dic)
#
# data1=[]
# data2=[]
# data3=[]
# for key,value in word_dic.items():
# 	lst = list(set(key))
# 	item_dic1={}
# 	item_dic2 = {}
# 	item_dic3 = {}
# 	if len(lst)==5:
# 		item_dic1["word"]=key
# 		item_dic1["E"] = value
# 		data1.append(item_dic1)
# 	elif len(lst)==4:
# 		item_dic2["word"] = key
# 		item_dic2["E"] = value
# 		data2.append(item_dic2)
# 	elif len(lst)==3:
# 		item_dic3["word"] = key
# 		item_dic3["E"] = value
# 		data3.append(item_dic3)
# print(data1)
# print(data2)
# print(data3)
#
# header = ['word', 'E']  # 数据列名
# datas1 = data1
# datas2 = data2
# datas3 = data3
#
# Tool.csv_write('信息熵1.csv',header=header,datas=datas1)
# Tool.csv_write('信息熵2.csv',header=header,datas=datas2)
# Tool.csv_write('信息熵3.csv',header=header,datas=datas3)


filename = 'c_wordle.xlsx'
df = pd.read_excel(filename,sheet_name = "Sheet1")

word_dic={}
for i in range(359):
    word_dic[df["Word"][i]]=df["E"][i]
print(word_dic)

classification=[]
for key,value in word_dic.items():
	lst = list(set(key))
	if len(lst)>=5:
		classification.append(1)
	elif len(lst)==4:
		classification.append(2)
	elif len(lst)<=3:
		classification.append(3)
df['classification'] = classification
print(df)

# df.to_csv("c_wordle.csv")