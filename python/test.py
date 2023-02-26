import math


def calEntropy(string):
	h = 0.0
	sumt = 0
	letter = [0] * 26
	string = string.lower()
	for i in range(len(string)):
		if string[i].isalpha():
			letter[ord(string[i]) - ord('a')] += 1
			sumt += 1
	print('\n', letter)
	for i in range(26):
		p = 1.0 * letter[i] / sumt
		if p > 0:
			h += -(p * math.log(p, 2))

	return h


test = input("输入一个英文句子：")
print('\n熵为：', calEntropy(test))

'''
letter = [8167,1492,2782,4253,12702,2228,2015,6094,6966,153,772,4025,2406,6749,7507,1929,95,5987,6327,9056,2758,978,2360,150,1974,74]
h = 0
for i in range(26):
    h += -(letter[i]/sum(letter)*math.log(letter[i]/sum(letter),2))
print(h)
'''