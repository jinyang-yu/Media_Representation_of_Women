# This script is for web scraping from People's Daily. 
# I have obtained permission to access articles from their website. 
# However, there are more than 10,000 articles related to women in People's Daily from 1949 to 2011. 
# Therefore, employing web scraping techniques can expedite the process of obtaining the text. 
# During the course of my web scraping, I encountered a change in the website's address for People's Daily. 
# Consequently, I need to develop a new script that corresponds to the updated link. 
# The script provided below pertains to the updated link structure.
# The scraped articles are stored in text files separately.

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup, NavigableString, Tag
import ssl
import os

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#define the beautifulsoup function
def get_tag(url):
    html = urllib.request.urlopen(url, context=ctx).read()
    dhtml=html.decode("UTF-8")
    soup = BeautifulSoup(dhtml, 'html.parser')
    tags = soup.find_all('a', class_ = 'open_detail_link')
    return tags

#get url
for i in range(536, 538):
    url="http://10.8.11.170/pd/101/search.html?pageSize=20&pageNo="+str(i)+"&searchword=%E6%A0%87%E9%A2%98%3D%E5%A5%B3%20or%20%E8%82%A9%E6%A0%87%E9%A2%98%3D%E5%A5%B3%20or%20%E5%89%AF%E6%A0%87%E9%A2%98%3D%E5%A5%B3&ss=1&tr=A&order=-dataTime%2C%2Bseqid&ty=1&keyword=%E5%A5%B3"
    print (url)
#After getting the url, start parsing the html to get the tag
    tags=get_tag(url)
    #print (tags)
#Repeat text code for in-text links 对文内链接重复text代码
    for tag in tags:
        aurl="http://10.8.11.170"+tag.get('href', None)
        print (aurl)
        ahtml = urllib.request.urlopen(aurl, context=ctx).read()
        adhtml=ahtml.decode("UTF-8")
        asoup = BeautifulSoup(adhtml, 'html.parser')
        asoup_title=asoup.find('div', class_ ='title')
        asoup_date= asoup.find('div', class_ = 'sha_left')
        asoup_text= asoup.find('div', id = 'FontZoom')
#Title wrapping problem 标题换行问题
        #print(asoup_title)
        cotitle=[]
        #print(asoup_title.text)
        for line in asoup_title:
            if isinstance(line, NavigableString):
                #print(line)
                line=line.replace('\n','').replace('\r','').replace('u\3000','')
                cotitle.append(line)
            else:
                cotitle.append(line.text)
        cotitle= ''.join(['%s' %id for id in cotitle])
        print(cotitle)
#Text wrapping problem 文本换行问题
        cotext=[]
        for line in asoup_text:
            if isinstance(line, NavigableString):
                continue
            if isinstance(line, Tag):
            #print(line.text)
                cotext.append(line.text)
        cotext= ''.join(['%s' %id for id in cotext])
        print(cotext)
        #print (asoup_text.text)
        #print (asoup_date.text)
        try:
            file = open(f"{cotitle}.txt","w",encoding='UTF-8')
        except:
            file = open(f"{str(i)}.txt","a",encoding='UTF-8')
        file.write(str(cotitle + asoup_date.text + cotext))
        file.close()
