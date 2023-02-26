import math
import pandas as pd
import numpy as np



def Univariate_model(guess_word):
	letter_list=list(guess_word)
	E=0
	for l in letter_list:
		p = freqs_dic[l]  # 359 2309 12593
		E = E + p * math.log2(p)
	return -E

def Binary_model(guess_word):
	p = freqs_dic[guess_word[0]]
	E = p * math.log2(p)
	left = 0
	right = 2
	for i in range(4):
		w = guess_word[left:right]
		p = w_dic[w] / 51812
		E = E + p * math.log2(p)
		left += 1
		right += 1
	return -E


if __name__ == '__main__':
	guess_word = ["APPLE", "FLAIL", "STAGE", "HEADY", "DEBUG", "GIANT", "USAGE", "SOUND", "SALSA", "MAGIC", "eerie"]
	Univariate=[]
	Binary=[]

	df = pd.read_csv('allowed_words.csv')
	freqs_dic = {}
	for i in range(26):
		freqs_dic[df["letter"][i]] = df["freqs"][i]

	df = pd.read_csv("allowed_前后字统计.csv")
	w_dic = {}
	for i in range(503):
		w_dic[df["word"][i]] = df["num"][i]

	for word in guess_word:
		Univariate.append(Univariate_model(word.lower()))
		Binary.append(Binary_model(word.lower()))

	df = pd.DataFrame()
	df["word"]=guess_word
	df["E1"]=Univariate
	df["E2"]=Binary
	print(df)

	df.to_csv("guess2.csv")
