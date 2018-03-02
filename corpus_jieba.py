#-*-coding:utf-8-*-

# 送给word2vec的文件是需要分词的
import jieba
filePath = 'corpus.txt' #语料路径
fileSeqWordDonePath = 'corpusSeqDone.txt'# 分词后生成路径

fileTrainRead = []
with open(filePath, 'r', encoding='utf-8') as fileTrainRaw: #python3
#with open(filePath) as fileTrainRaw:
	for line in fileTrainRaw:
		fileTrainRead.append(line)
print(len(fileTrainRead))


#MemoryError:避免三重循环,避免大量使用字典的多次嵌套
#在python里，大数据处理一定要减少字典使用,字典主要是用来统计用，不用来计算。 建议你考虑numpy.array做
def PrintListChinese(list):
	for i in range(len(list)):
		print (list[i])

#jieba分词
fileTrainSeg=[]
for i in range(len(fileTrainRead)):
	#使用结巴分词的时候并不是从0到结尾的全部都进行分词，而是对[9:-11]分词，因为sougouCS原始数据集中有起始的<content> 和结尾的</content>，将其去掉
	fileTrainSeg.append([' '.join(list(jieba.cut(fileTrainRead[i][9:-11], cut_all=False)))])
	if i % 100 == 0 :
		print (i)

with open(fileSeqWordDonePath, 'w') as fw: #'w'参数必须得写，不写的话，默认的是只读方式（即‘r’）
	for i in range(len(fileTrainSeg)):
		#fw.write(fileTrainSeg[i][0].encoding('utf-8'))#fw.write()只能输出str字符串，'str' object has no attribute 'encoding'
		#fw.write(fileTrainSeg[i][0].dedcode('utf-8'))#  'str' object has no attribute 'decode',python3里str默认为unicode,只能编码encode ,不能解码 decode

		fw.write(fileTrainSeg[i][0])
		fw.write('\n')#TypeError: a bytes-like object is required, not 'str',返回被转换文本的str表示,在python2.x中是bytes，在python3.x中是unicode
    
'''注意'''
#1.写入和读取要保持一致。如果写入时采用文本方式，则读取时也应采用文本方式；如果写入时采用二进制方式，则读取时也应采用二进制方式。
#2.如果以文本方式打开向文件中写入数据时，每碰到一个“换行”，就会将其转化为“回车+换行”。在读取时，一旦遇到“回车+换行”就将其转化为“换行”
#3.而二进制方式则会将数据按照在内存中的存储形式原样输出到文件中。
