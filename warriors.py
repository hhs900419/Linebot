import urllib.request as req
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
    titles=root.find_all("td")
    #print(titles)
    account=0
    for title in titles:
        # if(title["class"]=="left "):
        try:
            if(title["csk"] and title["data-stat"] and title["class"]):
                print(title.string )
                try:
                    print(title.a["href"])
                except TypeError:
                    continue
        except KeyError:
            continue
        # if title.=="row":
        #    try:
        #         True
        #     except KeyError:
        #         continue        
    
    return account

URL="https://www.basketball-reference.com/teams/GSW/2022.html"
a=func(URL)
#print(a)