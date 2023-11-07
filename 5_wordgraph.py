# generate a word cloud
import jieba
import jieba.analyse
import jieba.posseg as pseg
from wordcloud import WordCloud
import matplotlib.pyplot as plt

#generate word cloud 生成词云
stopwords = [line.strip() for line in open('C:/Users/过青灯客/others/stopwords.txt', 'r', encoding='UTF-8').readlines()]
def create_word_cloud(filename):
    text = open("{}.txt".format(filename),encoding='utf-8',errors='ignore').read()
    # jieba cutting words 结巴分词
    wordlist=[]
    words = pseg.cut(text)
    for word, flag in words:
        if len(word)== 1:
            continue
        #if word == '人民日报' or word == '日电' or word =='新华社' or word == '记者' or word =='因此' or word =='这个' or word =='数据库' or word =='资料' or word =='一些':
        if word in stopwords:
            continue
        if flag == 'w' or flag == 'r' or flag == 'm' or flag == 'q' or flag == 'p' or flag == 'c' or flag == 'u' or flag == 'xc':
            continue
        else:
            wordlist.append(word)
    wl = " ".join(wordlist)

    # word cloud settings 设置词云
    wc = WordCloud(
        # setting background color 设置背景颜色
        background_color="white",
        # setting maximum number of words 设置最大显示的词云数
        max_words=2000,
        # setting fonts 这种字体都在电脑字体中，一般路径
        font_path='C:\Windows\Fonts\simfang.ttf',
        height=1200,
        width=1600,
        # setting font sizes 设置字体最大值
        max_font_size=200,
        # setting the number of random state 设置有多少种随机生成状态，即有多少种配色方案
        random_state=100,
        collocations=False
    )

    myword = wc.generate(wl)  # generate wordcloud 生成词云
    # show the graph 展示词云图
    plt.imshow(myword)
    plt.axis("off")
    plt.show()
    wc.to_file('word.png')  # save the graph 把词云保存下

if __name__ == '__main__':
    create_word_cloud('C:/Users/过青灯客/20132021')
