import requests
from lxml import html
from bs4 import BeautifulSoup
import codecs

for i in range(0, 74):
    try:
        url = 'https://fivethirtyeight.com/tag/significant-digits/page/' + \
            str(i)
        print 'Scraping: ' + url
        page = requests.get(url)
        tree = html.fromstring(page.content)

        links = tree.xpath('//a[@class="post-thumbnail"]/@href')

        posts = []
        for link in links:
            print '       Post: ' + link
            page = requests.get(link)
            soup = BeautifulSoup(page.content)
            result = soup.find("div", {"class": "entry-content"})
            posts.append(result.text)

        all_posts = '\n\n--------------------------------\n\n'.join(posts)

        f = codecs.open('data/sig_digs_' + str(i) + '.txt', 'w+', 'utf-8')
        # f.write(all_posts.encode('ascii', errors='ignore'))
        f.write(all_posts)
        f.close()
    except Exception as e:
        print e
        pass
