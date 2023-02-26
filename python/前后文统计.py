import Tool
# import pandas as pd
#
# data = {'a': {'x': [1, 1], 'y': [2, 1], 'z': [3, 1]},
#         'b': {'x': [1, 2], 'y': [2, 2], 'z': [3, 2]},
#         'c': {'x': [1, 3], 'y': [2, 3], 'z': [3, 3]}}
# data_pd = pd.DataFrame(data)
#
# print(data_pd)
#
# for row in data_pd.index:
#     print(data_pd.loc[row]['a'])

# for row_id in range(data_pd.shape[0]):
#     print(data_pd.iloc[row_id]['a'])
#
# for index, row in data_pd.iterrows():
#     print(row['a'])

filepath='data/allowed_words.txt'
data=[]
dic={}
listOfLines = Tool.get_txtfile(filepath)
for word in listOfLines:
    left = 0
    right = 2
    for i in range(4):
        w=word[left:right]
        if w in dic:
            dic[w] += 1
        else:
            dic[w] = 1
        left += 1
        right += 1

for key,value in dic.items():
    item_dic={}
    item_dic["word"]=key
    item_dic["num"] = value
    data.append(item_dic)

header = ['word', 'num']  # 数据列名
datas = data

Tool.csv_write('allowed_前后字统计.csv',header=header,datas=datas)

