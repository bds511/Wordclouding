import urllib.request
from bs4 import BeautifulSoup



for i in range(730):
    url="https://search.naver.com/search.naver?where=news&se=0&query=%EC%83%88%EB%88%84%EB%A6%AC%EB%8B%B9&ie=utf8&sm=tab_srt&sort=2&photo=0&field=0&reporter_article=&pd=3&ds=2015.01.01&de=2016.01.31&docid=&nso=so%3Ar%2Cp%3Afrom20150101to20160131%2Ca%3Aall&mynews=1&mson=0&refresh_start=0&related=01&de=2016.01.31&docid=&nso=so:r,p:from20150101to20160131,a:all&mynews=2&start="+(1+10*i)+"&refresh_start=0"
    print(url)
    f = urllib.request.urlopen(url).read()
    soup=BeautifulSoup(f, 'html.parser')
    a=soup.find_all('span', class_='default-content')
    print(a[0].get_text())

