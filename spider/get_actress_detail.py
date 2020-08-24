from requests_html import HTMLSession
from tqdm import tqdm


session = HTMLSession()
details = []

with open('data/actresslist.csv', 'r', encoding='utf-8') as f:
    with open('data/actressinfo.csv', 'w', encoding='utf-8') as f1:
        with open('data/actressworks.csv', 'w', encoding='utf-8') as f2:
            f1.write('name,height,weight,measurements,birthday,constellation,link,pic\n')
            f2.write('name,work\n')
            
            for line in tqdm(f):
                name, link = line.split(',')
                h = session.get(link, headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0'})
                h = h.html
                attrs = h.find('dt.basicInfo-item.name')
                values = h.find('dd.basicInfo-item.value')
                d = {'中文名': 'null', '身高': 'null', '体重': 'null', '三围': 'null', '出生日期': 'null', '星座': 'null', '代表作品': 'null'}
                for attr, value in zip(attrs, values):
                    attr = attr.text
                    attr = ''.join(attr.split()) # 处理中间出现空格的情况
                    value = value.text
                    if attr in d:
                        d[attr] = value
                for k, v in d.items():
                    details.append((name, k, v))
                details.append((name, '链接', link.strip()))
                pic = h.find('div.summary-pic img')
                if len(pic):
                    pic = pic[0].attrs['src']
                else:
                    pic = 'null'
                details.append((name, '照片', pic))

                f1.write(name+','+d['身高']+','+d['体重']+','+d['三围']+','+d['出生日期']+','+d['星座']+','+link.strip()+',"'+pic+'"\n')
                if d['代表作品'] != 'null':
                    for work in d['代表作品'].strip().rstrip('等').split('、'):
                        f2.write(name+','+work+'\n')

with open('data/triples.csv', 'w', encoding='utf-8') as f:
    for name, attr, value in details:
        f.write(name + ',' + attr + ',' + value + '\n')
