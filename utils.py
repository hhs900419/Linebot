import os
import bs4
import requests
import urllib.request as req
from bs4 import BeautifulSoup

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, TemplateSendMessage, ButtonsTemplate, MessageTemplateAction


channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
# line_bot_api = LineBotApi(channel_access_token)

def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"


def send_image_url(id, img_url):
    line_bot_api = LineBotApi(channel_access_token)
    message = ImageSendMessage(
        original_content_url=img_url,
        preview_image_url=img_url
    )
    line_bot_api.reply_message(id, message)
    return "OK"


def send_button_message(reply_token, img, title, uptext, labels, texts):
    line_bot_api = LineBotApi(channel_access_token)
    acts = []
    for i, lab in enumerate(labels):
        acts.append(
            MessageTemplateAction(
                label=lab,
                text=texts[i]
            )
        )

    message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            thumbnail_image_url=img,
            title=title,
            text=uptext,
            actions=acts
        )
    )
    line_bot_api.reply_message(reply_token, message)
    return "OK"

def showoffpages(reply_token):
    url1 = "https://www.nba.com/warriors/" #website
    url2 = "https://twitter.com/warriors" #twi
    url3 = "https://www.instagram.com/warriors/" #ins
    url4 = "https://www.basketball-reference.com/teams/GSW/2022.html" #more
    result = "Official Pages~~~\n"
    result += "1. GSW Official Website\n"
    result += url1
    result += "\n2. GSW Twitter Account\n"
    result += url2
    result += "\n3. GSW Instergram Account\n"
    result += url3
    result += "\n4. More Details\n"
    result += url4
    send_text_message(reply_token, result)

def showhighlightlinks(reply_token):
    url1 = "https://www.youtube.com/watch?v=FJN-SMDujNg" #2974
    url2 = "https://www.youtube.com/watch?v=LWc1OU3sfds" #14\n
    url3 = "https://www.youtube.com/watch?v=5H0f5PIiIiI" #klay
    url4 = "https://www.youtube.com/watch?v=2yPL7-nyjTk" #steph
    result = "Highlights!!!!\n"
    result += "1. Greatest Shooter of All-time\n"
    result += url1
    result += "\n2. Klay's NBA 3P Record\n"
    result += url2
    result += "\n3. Klay's highlights\n"
    result += url3
    result += "\n4. Steph's highlights\n"
    result += url4
    send_text_message(reply_token, result)

def showroster(reply_token):
    url="https://www.basketball-reference.com/teams/GSW/2022.html"
    request=req.Request(url,headers={
        "User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    #path = "output.txt"
    #f= open(path,"w",encoding="UTF-8")
    root=bs4.BeautifulSoup(data,"html.parser")
    titles=root.find_all("div",class_="table_container", id="div_roster")
    #print(titles)
    account=0
    result = "---Warriors Roster---\n\n"
    titles=root.tbody
    for tr in titles.children:
        #排除字符串
        if isinstance(tr, bs4.element.Tag):
            #使用find_all()函數找到tr標簽中的所有<td>標簽
            u = tr.find_all("td")
            print(u[0].getText())
            # result += '\U+1F3C0\n'
            result += format(u[0].getText())
            result += "\n"
    result += "-----------------------------\n"
    result += "Star Players:\n"
    result += "Stephen Curry PG #30\n"
    result += "Klay Thompson SG #11\n"
    result += "Draymond Green PF #23\n"
    result += "Andrew Wiggins SF #22\n"
    result += "-----------------------------\n"
    result += "Enter star player name to get more details\n"
    send_text_message(reply_token, result)

#Curry
def StephenCurryStats(reply_token):
    url = 'https://www.basketball-reference.com/players/c/curryst01.html'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    source = requests.get(url, headers=headers).text
    soup = BeautifulSoup(source, 'html.parser')

    seasonstat = soup.find('tr', class_='full_table', id='per_game.2022')
    tds = seasonstat.find_all('td', class_='right')
    print(tds)
    SeasonStats = "\n---------Season 2021-2022---------\n"
    print(len(tds))
    for i in range(0, len(tds)):
        print(tds[i].getText(),end=" ")
    
    fg = float(tds[5].text)*100
    threep = float(tds[8].text)*100
    ft = float(tds[15].text)*100

    SeasonStats += ('Games Played: {} ({} mins/game)\n' .format(tds[0].getText(), tds[2].getText()))
    SeasonStats += ('Game Stats:\n\t{} PTS\n\t{} AST\n\t{} REB\n\t{} STL\n\t{} BLK\n' .format(tds[24].text, tds[19].text, tds[18].text, tds[20].text, tds[21].text))
    SeasonStats += ('Shooting Percentage:\n\tFG: {}  FGA: {}  FG%: {}%\n' .format(tds[3].text, tds[4].text, fg))
    SeasonStats += ('\t3P: {}  3PA: {}  3P%: {}%\n' .format(tds[6].text, tds[7].text, threep))
    SeasonStats += ('\tFT: {}  FTA: {}  FT%: {:.1f}%\n' .format(tds[13].text, tds[14].text, ft))


    careerstat = soup.find('tfoot')
    c_tds = careerstat.find_all('td', class_='right')
    
    CareerStats = "\n-----------Career Stats-----------\n"
    
    c_fg = float(c_tds[5].text)*100
    c_threep = float(c_tds[8].text)*100
    c_ft = float(c_tds[15].text)*100

    CareerStats += ('Games Played: {} ({} mins/game)\n' .format(c_tds[0].getText(), c_tds[2].getText()))
    CareerStats += ('Game Stats:\n\t{} PTS\n\t{} AST\n\t{} REB\n\t{} STL\n\t{} BLK\n' .format(c_tds[24].text, c_tds[19].text, c_tds[18].text, c_tds[20].text, c_tds[21].text))
    CareerStats += ('Shooting Percentage:\n\tFG: {}  FGA: {}  FG%: {}%\n' .format(c_tds[3].text, c_tds[4].text, c_fg))
    CareerStats += ('\t3P: {}  3PA: {}  3P%: {}%\n' .format(c_tds[6].text, c_tds[7].text, c_threep))
    CareerStats += ('\tFT: {}  FTA: {}  FT%: {:.1f}%\n' .format(c_tds[13].text, c_tds[14].text, c_ft))

    result = "\nStephen Curry" + SeasonStats + CareerStats
    result += "\n(enter [back] to go back)\n"
    print(result)
    send_text_message(reply_token, result)

def showcurryinfo(reply_token):
    msg = ""
    msg += "Stephen Curry #30\n"
    msg += "PG\t6-2, 185lb (188cm, 83kg) \n"
    msg += "12th Season\n Draft: Golden State Warriors, 1st round (7th pick, 7th overall), 2009 NBA Draft\n"
    msg += "Awards:\n\t3x NBA Champ\n\t7x All-star\n\t7x All-NBA\n\t2x MVP\n\t2x Scoring Champ\t\n2015~2016 STL Champ\n\t2009~2010 All-rookie\n\t NBA 75th Anniv.Team\n"
    msg += "\n(enter [back] to go back)\n"
    send_text_message(reply_token, msg)

#Klay
def KlayThompsonStats(reply_token):
    playername = "Klay Thompson"
    url = 'https://www.basketball-reference.com/players/t/thompkl01.html'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    source = requests.get(url, headers=headers).text
    soup = BeautifulSoup(source, 'html.parser')

    SeasonStats = "\n---------Season 2021-2022---------\n"
    SeasonStats += "Did Not Play (injury—achilles)\n"

    careerstat = soup.find('tfoot')
    c_tds = careerstat.find_all('td', class_='right')
    
    CareerStats = "\n-----------Career Stats-----------\n"
    
    c_fg = float(c_tds[5].text)*100
    c_threep = float(c_tds[8].text)*100
    c_ft = float(c_tds[15].text)*100

    CareerStats += ('Games Played: {} ({} mins/game)\n' .format(c_tds[0].getText(), c_tds[2].getText()))
    CareerStats += ('Game Stats:\n\t{} PTS\n\t{} AST\n\t{} REB\n\t{} STL\n\t{} BLK\n' .format(c_tds[24].text, c_tds[19].text, c_tds[18].text, c_tds[20].text, c_tds[21].text))
    CareerStats += ('Shooting Percentage:\n\tFG: {}  FGA: {}  FG%: {}%\n' .format(c_tds[3].text, c_tds[4].text, c_fg))
    CareerStats += ('\t3P: {}  3PA: {}  3P%: {}%\n' .format(c_tds[6].text, c_tds[7].text, c_threep))
    CareerStats += ('\tFT: {}  FTA: {}  FT%: {:.1f}%\n' .format(c_tds[13].text, c_tds[14].text, c_ft))

    result = "\n" + playername + SeasonStats + CareerStats
    result += "\n(enter [back] to go back)\n"
    print(result)
    send_text_message(reply_token, result)

def showklayinfo(reply_token):
    info = "Klay Thompson #11\n"
    info += "SG\t6-6, 215lb (198cm, 97kg)\n"
    info += "8th Season\n Draft: Golden State Warriors, 1st round (11th pick, 11th overall), 2011 NBA Draft\n"
    info += "Award:\n"
    info += "\t3x NBA Champ\n\t5x All-star\n\t2x All-NBA\n\t2018~2019 All-defensive\n\t2011~2012 All-rookie\n"
    info += "\n(enter [back] to go back)\n"
    send_text_message(reply_token, info)

#Dray
def Draymondstats(reply_token):
    playername = "Draymond Green"
    url = 'https://www.basketball-reference.com/players/g/greendr01.html'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    source = requests.get(url, headers=headers).text
    soup = BeautifulSoup(source, 'html.parser')

    seasonstat = soup.find('tr', class_='full_table', id='per_game.2022')
    tds = seasonstat.find_all('td', class_='right')
    print(tds)
    SeasonStats = "\n---------Season 2021-2022---------\n"
    print(len(tds))
    for i in range(0, len(tds)):
        print(tds[i].getText(),end=" ")
    
    fg = float(tds[5].text)*100
    threep = float(tds[8].text)*100
    ft = float(tds[15].text)*100

    SeasonStats += ('Games Played: {} ({} mins/game)\n' .format(tds[0].getText(), tds[2].getText()))
    SeasonStats += ('Game Stats:\n\t{} PTS\n\t{} AST\n\t{} REB\n\t{} STL\n\t{} BLK\n' .format(tds[24].text, tds[19].text, tds[18].text, tds[20].text, tds[21].text))
    SeasonStats += ('Shooting Percentage:\n\tFG: {}  FGA: {}  FG%: {}%\n' .format(tds[3].text, tds[4].text, fg))
    SeasonStats += ('\t3P: {}  3PA: {}  3P%: {}%\n' .format(tds[6].text, tds[7].text, threep))
    SeasonStats += ('\tFT: {}  FTA: {}  FT%: {:.1f}%\n' .format(tds[13].text, tds[14].text, ft))


    careerstat = soup.find('tfoot')
    c_tds = careerstat.find_all('td', class_='right')
    
    CareerStats = "\n-----------Career Stats-----------\n"
    
    c_fg = float(c_tds[5].text)*100
    c_threep = float(c_tds[8].text)*100
    c_ft = float(c_tds[15].text)*100

    CareerStats += ('Games Played: {} ({} mins/game)\n' .format(c_tds[0].getText(), c_tds[2].getText()))
    CareerStats += ('Game Stats:\n\t{} PTS\n\t{} AST\n\t{} REB\n\t{} STL\n\t{} BLK\n' .format(c_tds[24].text, c_tds[19].text, c_tds[18].text, c_tds[20].text, c_tds[21].text))
    CareerStats += ('Shooting Percentage:\n\tFG: {}  FGA: {}  FG%: {}%\n' .format(c_tds[3].text, c_tds[4].text, c_fg))
    CareerStats += ('\t3P: {}  3PA: {}  3P%: {}%\n' .format(c_tds[6].text, c_tds[7].text, c_threep))
    CareerStats += ('\tFT: {}  FTA: {}  FT%: {:.1f}%\n' .format(c_tds[13].text, c_tds[14].text, c_ft))

    result = "\n" + playername + SeasonStats + CareerStats
    result += "\n(enter [back] to go back)\n"
    print(result)
    send_text_message(reply_token, result)

def showdrayinfo(reply_token):
    msg = ""
    msg += "Draymond Green #23\n"
    msg += "PF/C\t6-6, 230lb (198cm, 104kg) \n"
    msg += "9th Season\n Draft: Golden State Warriors, 2nd round (5th pick, 35th overall), 2012 NBA Draft\n"
    msg += "Awards:\n\t3x NBA Champ\n\t3x All-star\n\t2x All-NBA\n\t6x All-Defensive\n\t2016~2017 STL Champ\n\t2016~2017 DPOY\n"
    msg += "\n(enter [back] to go back)\n"
    send_text_message(reply_token, msg)

#Wiggs
def Wigginsstats(reply_token):
    playername = "Andrew Wiggins"
    url = 'https://www.basketball-reference.com/players/w/wiggian01.html'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    source = requests.get(url, headers=headers).text
    soup = BeautifulSoup(source, 'html.parser')

    seasonstat = soup.find('tr', class_='full_table', id='per_game.2022')
    tds = seasonstat.find_all('td', class_='right')
    print(tds)
    SeasonStats = "\n---------Season 2021-2022---------\n"
    print(len(tds))
    for i in range(0, len(tds)):
        print(tds[i].getText(),end=" ")
    
    fg = float(tds[5].text)*100
    threep = float(tds[8].text)*100
    ft = float(tds[15].text)*100

    SeasonStats += ('Games Played: {} ({} mins/game)\n' .format(tds[0].getText(), tds[2].getText()))
    SeasonStats += ('Game Stats:\n\t{} PTS\n\t{} AST\n\t{} REB\n\t{} STL\n\t{} BLK\n' .format(tds[24].text, tds[19].text, tds[18].text, tds[20].text, tds[21].text))
    SeasonStats += ('Shooting Percentage:\n\tFG: {}  FGA: {}  FG%: {}%\n' .format(tds[3].text, tds[4].text, fg))
    SeasonStats += ('\t3P: {}  3PA: {}  3P%: {}%\n' .format(tds[6].text, tds[7].text, threep))
    SeasonStats += ('\tFT: {}  FTA: {}  FT%: {:.1f}%\n' .format(tds[13].text, tds[14].text, ft))


    careerstat = soup.find('tfoot')
    c_tds = careerstat.find_all('td', class_='right')
    
    CareerStats = "\n-----------Career Stats-----------\n"
    
    c_fg = float(c_tds[5].text)*100
    c_threep = float(c_tds[8].text)*100
    c_ft = float(c_tds[15].text)*100

    CareerStats += ('Games Played: {} ({} mins/game)\n' .format(c_tds[0].getText(), c_tds[2].getText()))
    CareerStats += ('Game Stats:\n\t{} PTS\n\t{} AST\n\t{} REB\n\t{} STL\n\t{} BLK\n' .format(c_tds[24].text, c_tds[19].text, c_tds[18].text, c_tds[20].text, c_tds[21].text))
    CareerStats += ('Shooting Percentage:\n\tFG: {}  FGA: {}  FG%: {}%\n' .format(c_tds[3].text, c_tds[4].text, c_fg))
    CareerStats += ('\t3P: {}  3PA: {}  3P%: {}%\n' .format(c_tds[6].text, c_tds[7].text, c_threep))
    CareerStats += ('\tFT: {}  FTA: {}  FT%: {:.1f}%\n' .format(c_tds[13].text, c_tds[14].text, c_ft))

    result = "\n" + playername + SeasonStats + CareerStats
    result += "\n(enter [back] to go back)\n"
    print(result)
    send_text_message(reply_token, result)

def showwigsinfo(reply_token):
    msg = ""
    msg += "Andrew Wiggins #22\n"
    msg += "SF\t6-7, 197lb (201cm, 89kg) \n"
    msg += "7th Season\n Draft: Cleveland Cavaliers, 1st round (1st pick, 1st overall), 2014 NBA Draft\n"
    msg += "Awards:\n\t2014-2015 All-Rookie\n\t2014-2015 ROY\n"
    msg += "\n(enter [back] to go back)\n"
    send_text_message(reply_token, msg)