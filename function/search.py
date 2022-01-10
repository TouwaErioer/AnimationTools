import requests
from bs4 import BeautifulSoup

from utils import input_value_int, get_file_type, input_value, clear

prefix = 'https://assrt.net/'
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                  '97.0.4692.71 Safari/537.36'
}
site = 'https://assrt.net/sub/?searchword=%s'


def run():
    download_path = input_value('请输入工作空间：')
    clear()
    keyword = input_value('请输入关键词：')
    response = requests.get(site % keyword, headers=header)
    soup = BeautifulSoup(response.content, 'lxml')
    sub_item_list = soup.select('.subitem')
    results = []
    for index, sub_item in enumerate(sub_item_list, 1):
        if index != 1 and index != len(sub_item_list):
            title = sub_item.select('.introtitle')[0].get('title')
            url = prefix + str(sub_item.select('.subitem .waves-effect')[0].get('onclick')).replace(
                "javascript:location.href='",
                '').replace(
                "';return false;", '').strip()
            results.append({
                'title': title,
                'url': url
            })
    for index, result in enumerate(results, 1):
        print('%d. %s' % (index, result['title']))
    n = input_value_int('请输入序号：') - 1
    try:
        url = results[n]['url']
        response = requests.get(url, headers=header)
        response.raise_for_status()
        file_name = '%s\\%s.%s' % (download_path, results[n]['title'], get_file_type(url))
        with open(file_name, 'wb') as f:
            f.write(response.content)
        print('下载 %s 成功！' % file_name)
    except IndexError:
        print('序号超出范围')
