fail = []
def comic_downloader(comic_number = 0):
    import bs4 as bs
    import random
    import urllib.request
    comic_number = int(comic_number)
    if comic_number == 0:
        comic_number = random.randrange(1500)
    try:
        sauce = urllib.request.urlopen("https://xkcd.com/%d"%comic_number).read()
        soup = bs.BeautifulSoup(sauce,'html.parser')
        t = 0
        for i in soup.find_all('img'):
            if t == 1:
                img_url = i.get('src')
                break
            t+=1
        print ("Downloading Image:",comic_number, i.get('alt'))
        print(i.get('title'))
        urllib.request.urlretrieve("https:"+img_url,i.get('alt').replace('?','Qm').replace('<','sl').replace('>','sr').replace('*','as').replace('~','tl').replace('#','hsh').replace('%','prc').replace('&','and').replace('{','cl').replace('}','cr').replace('\\','bs').replace(':','cln').replace('/','sl').replace('+','plus').replace('|','pipe').replace("'",'quotes').replace('"','quotes') + ".png")
    except:
        print('Lmao Failed.')
        fail.append(comic_number)
def comic_catalogue():
    import bs4 as bs
    import urllib.request
    catalogue = {}
    for i in range(1,1500):
        soup = bs.BeautifulSoup(urllib.request.urlopen("https://xkcd.com/%d"%i).read(),'html.parser')
        catalogue[i] = soup.find_all('title')
    return catalogue

for i in range(1525,1932):
    comic_downloader(i)


    
