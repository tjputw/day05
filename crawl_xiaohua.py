#爬取糗事百科笑话段子
import requests, urllib
import urllib.request
from lxml import etree

url = 'https://www.qiushibaike.com/text/page/%d/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
}
#获取页面内容
def main():
    page = int(input('请输入要下载的页码数：'))
    for i in range(page):
        response = requests.get(url=url%(i+1), headers= headers, verify=False)
        response.encoding = 'utf-8'
        res = response.text
        content = etree.HTML(res)
        # 下载笑话内容
        lists = content.xpath("//div[@class='content']/span/text()")
        for ls in lists:
            with open('./download/笑话/第%d页笑话.txt'%(i+1), mode='a',encoding='utf-8') as fp:
                if ls == None:
                    pass
                fp.write(ls)
        print('------------第%d页下载成功-------------'%(i+1))

if __name__ == '__main__':
    main()