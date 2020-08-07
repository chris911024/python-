# -*- coding: utf-8 -*
#抓取網頁原始碼
import urllib. request as req
url="https://www.ptt.cc/bbs/A_A/index.html"
#建立一個request 物件，附加request headers 的資訊
request=req.Request(url, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
    })
with req.urlopen(request) as response:
     data=response.read().decode("utf-8")
     #解析原始碼 取得每篇文章的標題
import bs4
root=bs4.BeautifulSoup(data, "html.parser")
titles=root.find_all("div", class_="title")#尋找所有class"title'的div 標籤
for title in titles:
     if title.a !=None: #如果標題包含A標籤(沒有刪除)印出來
        print(title.a.string)
    