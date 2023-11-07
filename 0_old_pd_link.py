# This script is for web scraping from People's Daily. 
# I have obtained permission to access articles from their website. 
# However, there are more than 10,000 articles related to women in People's Daily from 1949 to 2011. 
# Therefore, employing web scraping techniques can expedite the process of obtaining the text. 
# During the course of my web scraping, I encountered a change in the website's address for People's Daily. 
# Consequently, I need to develop a new script that corresponds to the updated link. 
# The script provided below pertains to the previous link structure.

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# define the nextpage function
def next_page(url):
    html = urllib.request.urlopen(url, context=ctx).read()
    dhtml=html.decode("gbk")
    soup = BeautifulSoup(dhtml, 'html.parser')
    tags = soup('a')
    nextpage= tags[11]
    url=nextpage.get('href', None)
    return url

# define the beautifulsoup function
def get_tag(url):
    html = urllib.request.urlopen(url, context=ctx).read()
    dhtml=html.decode("gbk")
    soup = BeautifulSoup(dhtml, 'html.parser')
    tags = soup('a')
    return tags

# Input the url and loop. Extract nextpage url. 输入url并循环！！提取出nextpage url
url = next_page(input('Enter - '))
for i in range(1):
    url=next_page(url)
    print (url)
# After getting the url, start parsing the html to get the tag
    tags=get_tag(url)
# Repeat text code for in-text links 对文内链接重复text代码
    for tag in [tags[11+2],tags[12+2],tags[13+2],tags[14+2],tags[15+2],tags[16+2],tags[17+2],tags[18+2],tags[19+2],tags[20+2],tags[21+2],tags[22+2],tags[23+2],tags[24+2],tags[25+2],tags[26+2],tags[27+2],tags[28+2],tags[29+2],tags[30+2]]:
        aurl=tag.get('href', None)
        print (aurl)
        ahtml = urllib.request.urlopen(aurl, context=ctx).read()
        adhtml=ahtml.decode("gbk")
        asoup = BeautifulSoup(adhtml, 'html.parser')
        asoup_title= asoup.find('div', class_ = 'div_biaoti')
        asoup_date= asoup.find('div', class_ = 'div_detail-cl')
        asoup_text= asoup.find('div', id = 'fontzoom')
        print (asoup_title.text)
        print (asoup_text.text)
        file = open(f"{asoup_title.text}.txt","w",encoding='utf-8')
        file.write(str(asoup_title.text + asoup_date.text + asoup_text.text))
        file.close()
