import bs4
import urllib.request as req
from bs4 import BeautifulSoup

def playerstats():
    nickname = 0
    url = 'https://www.basketball-reference.com/players/c/curryst01.html'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    source = requests.get(url, headers=headers).text
    soup = BeautifulSoup(source, 'html.parser')
    
    photos = soup.find_all('img')
    imglink = photos[1]['src']
    # send_image_url(reply_token, imglink)

    # bio = soup.find('div', {"id": "meta"})
    # ps = bio.find_all('p')

    # result = '\U0001F4DC\U0001F4DC\U0001F4DC\n'
    # if(ps[0].text[:13] == 'Pronunciation'):
    #     result += get(ps[0])
    #     result += "FullName: "
    #     result += get(ps[1])
    #     if(ps[2].text[1] == '('):
    #         nickname = 1
    #     if nickname:
    #         result += ("Nickname: {}\n" .format(ps[2].text[2:-2]))
    #         result += get(ps[3])
    #         result += ('Height and Weight: {}' .format(get(ps[4])))
    #         for p in ps[5:]:
    #             result += get(p)
    #     else:
    #         result += get(ps[2])
    #         result += ('Height and Weight: {}' .format(get(ps[3])))
    #         for p in ps[4:]:
    #             result += get(p)
    # else:
    #     result += "FullName: "
    #     result += get(ps[0])
    #     if(ps[1].text[1] == '('):
    #         nickname = 1
    #     if nickname:
    #         result += ("Nickname: {}\n" .format(ps[1].text[2:-2]))
    #         result += get(ps[2])
    #         result += ('Height and Weight: {}' .format(get(ps[3])))
    #         for p in ps[4:]:
    #             result += get(p)
    #     else:
    #         result += get(ps[1])
    #         result += ('Height and Weight: {}' .format(get(ps[2])))
    #         for p in ps[3:]:
    #             result += get(p)

    # push_message(userid, result)

    stat = soup.find('div', class_='stats_pullout')
    ps = stat.find_all('p')



    curStat = ""
    carStat = ""

    curStat += ('\U0001F525\U0001F525\U0001F525 {}\n' .format(ps[0].text))
    curStat += ('Games Played: {}\n' .format(ps[2].text))
    curStat += ('Average Per Game: {} PTS, {} AST, {} REB\n' .format(ps[4].text, ps[8].text, ps[6].text))
    curStat += ('Accuracy: {} FG%, {} FG3%, {} FT%, {} eFG%\n' .format(ps[10].text, ps[12].text, ps[14].text, ps[16].text))
    # push_message(userid, curStat)

    carStat += ('\U0001F474\U0001F474\U0001F474 {}\n' .format(ps[1].text))
    carStat += ('Games Played: {}\n' .format(ps[3].text))
    carStat += ('Average Per Game: {} PTS, {} AST, {} REB\n' .format(ps[5].text, ps[9].text, ps[7].text))
    carStat += ('Accuracy: {} FG%, {} FG3%, {} FT%, {} eFG%\n' .format(ps[11].text, ps[13].text, ps[15].text, ps[17].text))
    # push_message(userid, carStat)
    
    print(curStat)
    print(carStat)
def func(url):
    request=req.Request(url,headers={
        "User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    #path = "output.txt"
    #f= open(path,"w",encoding="UTF-8")
    import bs4
    root=bs4.BeautifulSoup(data,"html.parser")
    titles=root.find_all("div",class_="table_container", id="div_roster")
    #titles=root.findall("div")
    #except TypeError:
     #   True
    titles=root.tbody
    print(titles)
    for tr in titles.children:
        #排除字符串
        if isinstance(tr, bs4.element.Tag):
            #使用find_all()函數找到tr標簽中的所有<td>標簽
            u = tr.find_all("td")
            print(u[0].getText())
    #print(titles)
    # for title in titles:
    #     print(title)
    account=0
    
    return account

URL="https://www.basketball-reference.com/teams/GSW/2022.html"
a=func(URL)
#print(a)