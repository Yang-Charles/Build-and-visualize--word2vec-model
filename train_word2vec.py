'''
To train a word2vec model  on SoudouCS data set 
author: yang-charles

'''

from gensim.models import word2vec
from time import time
import os
import logging #引入日志配置
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

begin = time()
sentences = word2vec.Text8Corpus('corpusSeqDone_utf8.txt')  #语料需要提前进行切分
model = word2vec.Word2Vec(sentences, sg=0, min_count=15, size=300, seed=1, iter=8, workers=15)
# min_count在较大的语料集中，我们希望忽略那些只出现过一两次的单词，就可以通过设置min_count参数进行控制
# size参数主要是用来设置神经网络的层数，Word2Vec 中的默认值是设置为100层
# workers参数用于设置并发训练时候的线程数，不过仅当Cython安装的情况下才会起作用
model.save('model2/word2vec_sohucorpus.model')
model.wv.save_word2vec_format('model2/word2vec_sohucorpus.model.bin', binary=True) #以一种c语言可以解析的形式存储词向量
end = time()

print('Total processing time: %d seconds' % (end-begin))
