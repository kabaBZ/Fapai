import requests
from lxml import etree


headers = {
    'Origin': 'https://www1.rmfysszc.gov.cn',
    'Referer': 'https://www1.rmfysszc.gov.cn/news/pmgg.shtml',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46'
}
params = {
    'search':'',
    'fid1':'',
    'fid2':'',
    'fid3':'',
    'page': 1,
    'include':' 0',
}
url = 'https://www1.rmfysszc.gov.cn/News/Handler.aspx'
def parse():
    response = requests.get(url = url , headers= headers, params= params)
    if response:
        page_text = response.json()['html']
        page_flag = response.json()['page'] #提取信息判断是否是最后一页post(212797)
        print(page_flag)
        tree_page = etree.HTML(page_flag)
        flag = tree_page.xpath('//a[last()]/@onclick')[0]
        print(flag)
        tree = etree.HTML(page_text)
        tr_list = tree.xpath('//table/tbody/tr')
        for tr in tr_list:
            name = tr.xpath('./td/span/a/@title')
            company = tr.xpath('./td[2]/span/@title')
            date = tr.xpath('./td[3]/span/text()')
            print(name,company,date)
        if flag == 'post(212797)':
            params['page'] += 1
            return parse()
        else:
            print('结束！')
parse()

