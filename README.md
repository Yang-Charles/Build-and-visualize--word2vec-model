# Build-and-visualize--word2vec-model
Build and visualize the word2vec model on sogou news data（SogouCS）


1.数据处理：
本文使用数据集是搜狗实验室公开的SogouCS:news_sohusite_xml.dat 

2.编码后取出内容，并保存为txt文件,在终端输入：
cat news_tensite_xml.dat | iconv -f gbk -t utf-8 -c | grep "<content>"  > corpus.txt


3.模型创建：
Gensim中 Word2Vec 模型的期望输入是进过分词的句子列表，即是某个二维数组。这里我们暂时使用 Python 内置的数组，不过其在输入数据集较大的情况下会占用大量的 RAM。Gensim 本身只是要求能够迭代的有序句子列表，因此在工程实践中我们可以使用自定义的生成器，只在内存中保存单条语句。

