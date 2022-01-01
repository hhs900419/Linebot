import os
import bs4
import urllib.request as req

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage


channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"


"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""

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
    titles=root.find_all("td")
    #print(titles)
    account=0
    result = "Warriors Roster:\n"
    for title in titles:
        # if(title["class"]=="left "):
        try:
            if(title["csk"] and title["data-stat"] and title["class"]):
                print(title.string )
                result += format(title.string)
                result += "\n"
                try:
                    print(title.a["href"])
                    result += title.a["href"]
                except TypeError:
                    continue
        except KeyError:
            continue
        # if title.=="row":
        #    try:
        #         True
        #     except KeyError:
        #         continue        
    send_text_message(reply_token, result)