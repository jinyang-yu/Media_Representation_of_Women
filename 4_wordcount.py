# counting words. First use jieba to cut words.
import jieba
from jieba import analyse
import jieba.posseg as pseg

# original text
stopwords = [line.strip() for line in open('C:/Users/过青灯客/others/stopwords.txt', 'r', encoding='UTF-8').readlines()]
article=open('C:/Users/过青灯客/20132021.txt',encoding='utf-8',errors='ignore').read()
words=pseg.cut(article)
#jieba.enable_paddle() # Paddle mode. It is supported after version 0.40, but not supported by earlier versions.
#words = pseg.cut(article,use_paddle=True) # paddle mode
#words = jieba.lcut(article, cut_all = False)
wordcounts = {}
for word, flag in words:
    if len(word) == 1:
        continue
    if flag == 'w' or flag == 'r' or flag == 'm' or flag == 'q' or flag == 'p' or flag == 'c' or flag == 'u' or flag == 'xc':
        continue
    if word in stopwords:
        continue
    else:
        wordcounts[word] = wordcounts.get(word,0) + 1
wordcount = list(wordcounts.items())
wordcount.sort(key = lambda x: x[1], reverse = True) #Arrange in reverse order, according to the second parameter
wordnumber = int(51)
for i in range(1, wordnumber):
    word,count = wordcount[i]
    print ("{0:<10}{1:>5}".format(word, count))
