import re
import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html,initial,name):
    reg = r'src="(.+?\.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    x = initial
    y = 0
    for imgurl in imglist:
        if imgurl.find('-') == -1 and imgurl.find('_') == -1:
            urllib.urlretrieve(imgurl,str(x)+'_'+name[y]+'.jpg')
            x+=1
            y+=1
    return imglist,x

def getName(html):    

    matchs=re.finditer(r'target="_blank">(.*?)</a>',html,re.S)

    return [match.group(1) for match in matchs]

html1 = getHtml("https://www.douban.com/doulist/164439/?start=0&sort=time&sub_type=")
html2 = getHtml("https://www.douban.com/doulist/164439/?start=25&sort=time&sub_type=")
html3 = getHtml("https://www.douban.com/doulist/164439/?start=50&sort=time&sub_type=")

name1 = getName(html1)
name2 = getName(html2)
name3 = getName(html3)

name1 = [name.strip() for name in name1 if name.find('        ') != -1 and name.find('<') == -1]
name2 = [name.strip() for name in name2 if name.find('        ') != -1 and name.find('<') == -1]
name3 = [name.strip() for name in name3 if name.find('        ') != -1 and name.find('<') == -1]

im1,index = getImg(html1,1,name1)
im2,index = getImg(html2,index,name2)
im3,index = getImg(html3,index,name3)

index = 1

for name in name1:
    print str(index)+'_'+name+','
    index += 1
for name in name2:
    print str(index)+'_'+name+','
    index += 1
for name in name3:
    print str(index)+'_'+name+','
    index += 1
    
    
    
# str.strip() 去掉空格和回车
