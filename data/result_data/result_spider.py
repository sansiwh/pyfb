import urllib.request
from data.spider_tool.proxy import *
from bs4 import BeautifulSoup

headers={
	"Connection":"close",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36",
    "Cookie":"u=721493343230860; s=fq124vw7g9; webp=0; aliyungf_tc=AQAAAAGV+zc0dQQAGq85cQVvSoYsqrE4; xq_a_token=afe4be3cb5bef00f249343e7c6ad8ac7dc0e17fb; xq_a_token.sig=6QeqeLxu5hi1S21JgtozJ1EZcsQ; xq_r_token=a1e0ac0c42513dcf339ddf01778b49054e341172; xq_r_token.sig=VPMAft0BfpDHm5UE0QJ5oDLYunw; __utmt=1; __utma=1.1379458042.1493343321.1493778350.1493783528.5; __utmb=1.3.10.1493783528; __utmc=1; __utmz=1.1493343321.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); Hm_lvt_1db88642e346389874251b5a1eded6e3=1493369217,1493688491,1493778343,1493779071; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1493784158"
}

url = 'http://www.ssports.com/data/rankMatch_1.html'

# response = urllib.request.urlopen('http://search.cs.com.cn/search?searchword=%E6%AF%94%E7%89%B9%E5%B8%81&channelid=215308')
# html = response.read()

req = urllib.request.Request(url,headers=headers)
html = urllib.request.urlopen(req).read().decode('utf-8')

soup = BeautifulSoup(html, "html.parser")

tr_data = soup.find_all("tr")

for index in range(len(tr_data)):
    print("++++++++++++++++++")
    tr_html = BeautifulSoup(str(tr_data[index]), "html.parser")
    td_data = tr_html.find_all("td")
    print(td_data[1].get_text())
    print(td_data[2].get_text())

    score = td_data[3].get_text()
    score_arr = score.strip().split(":")
    print(score_arr[0].strip()+":"+score_arr[1].strip())
    print(td_data[4].get_text())
    print("------------------")










# news_array = soup.find_all(style="line-height:160%;width:100%;")
#
#
# for index in range(len(news_array)):
#     news_table = BeautifulSoup(str(news_array[index]), "html.parser")
#
#     #print(news_table.td)
#
#     if(news_table.a != None):
#         print("地址:  " + news_table.a['href'])
#         print("标题:  " + news_table.a.get_text())
#         print("+++++++++++++++++++")