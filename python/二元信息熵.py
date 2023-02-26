import math
import pandas as pd

filename = 'test_words.csv'
df = pd.read_csv(filename)
freqs_dic={}
for i in range(26):
    freqs_dic[df["letter"][i]]=df["freqs"][i]
# print(freqs_dic)

df = pd.read_csv("allowed_前后字统计.csv")
w_dic={}
for i in range(503):
    w_dic[df["word"][i]]=df["num"][i]
# print(w_dic)

filename = 'c_wordle.xlsx'
df = pd.read_excel(filename,sheet_name = "Sheet1")
E_list=[]
word_dic={}
for word in df["Word"]:
	p = freqs_dic[word[0]]
	E = p * math.log2(p)
	left = 0
	right = 2
	for i in range(4):
		w = word[left:right]
		p=w_dic[w]/51812
		E=E+p*math.log2(p)
		left += 1
		right += 1
	E_list.append(-E)

df['E'] = E_list
print(df)
#
df.to_csv("c_wordle_二元.csv")
