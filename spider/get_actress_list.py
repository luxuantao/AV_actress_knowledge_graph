from requests_html import HTMLSession


session = HTMLSession()
h = session.get('https://baike.baidu.com/item/AV%E5%A5%B3%E4%BC%98/416320?fr=aladdin', \
    headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0'})
h = h.html
l = h.find('table.table-view div.para')
actresses = set()
for each in l:
    try:
        if each.absolute_links:
            name_length = len(each.text)
            if 3 <= name_length <= 5:
                for link in each.absolute_links:
                    actresses.add((each.text, link))
                    break # 只要一个link
    except:
        pass

with open('data/actresslist.csv', 'w', encoding='utf-8') as f:
    for actress in actresses:
        name, link = actress
        f.write(name + ',' + link + '\n')
