import csv


def get_txtfile(filepath):
	fileHandler  =  open  (filepath,  "r")
	# Get list of all lines in file
	listOfLines  =  fileHandler.readlines()
	# Close file
	fileHandler.close()
	return listOfLines


def get_txtLineNum(filepath):
	return len(open(filepath, 'r').readlines())


def csv_write(filepath,header,datas):
	with open(filepath, 'w', newline='', encoding='utf-8') as f:
		writer = csv.DictWriter(f, fieldnames=header)  # 提前预览列名，当下面代码写入数据时，会将其一一对应。
		writer.writeheader()  # 写入列名
		writer.writerows(datas)  # 写入数据


def harmonic_mean(data):  # 计算调和平均数
	total = 0
	for i in data:
		if i == 0:  # 处理包含0的情况
			return 0
		total += 1 / i
	return len(data) / total