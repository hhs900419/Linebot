from transitions.extensions import GraphMachine

from utils import send_text_message, send_button_message
from utils import showoffpages, showhighlightlinks, showroster
from utils import StephenCurryStats, KlayThompsonStats, Draymondstats, Wigginsstats
from utils import showcurryinfo, showklayinfo, showdrayinfo, showwigsinfo



class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_menu(self, event):
        text = event.message.text
        return True

    def is_going_to_backmenu(self, event):
        text = event.message.text
        return text.lower() == "menu"

    def on_enter_menu(self, event):
        print("I'm entering menu")
        reply_token = event.reply_token
        img = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTvxqWQa__fLiQSJ5OrPkTYmeMrnvXNAaXpRQ&usqp=CAU"
        title = 'Welcome to Dubnations!'
        uptext = 'Golden State Warriors\n#Strength in Numbers'
        labels = ['Roster', 'Official Pages', 'Highlights']
        texts = ['Roster', 'Official Pages', 'Highlights']
        send_button_message(reply_token, img, title, uptext, labels, texts)
    
    def is_going_to_official(seif, event):
        print("is going to off")
        text = event.message.text
        return text.lower() == "official pages"
    
    def on_enter_official(self, event):
        print("I'm entering off")
        reply_token = event.reply_token
        showoffpages(reply_token)
        
    def is_going_to_highlights(seif, event):
        print("is going to high")
        text = event.message.text
        return text.lower() == "highlights"
    
    def on_enter_highlights(self, event):
        print("I'm entering high")
        reply_token = event.reply_token
        showhighlightlinks(reply_token)

    def is_going_to_roster(seif, event):
        print("is going to roster")
        text = event.message.text
        return text.lower() == "roster"
    
    def is_going_to_backroster(self, event):
        text = event.message.text
        return text.lower() == "back to roster"
    
    def on_enter_roster(self, event):
        print("I'm entering roster")
        reply_token = event.reply_token
        showroster(reply_token)

    # Stephen Curry
    def is_going_to_StephenCurry(seif, event):
        text = event.message.text
        return text.lower() == "stephen curry"
    
    def is_going_to_backcurry(self, event):
        text = event.message.text
        return text.lower() == "back"

    def on_enter_StephenCurry(self, event):
        print("I'm entering SC")
        reply_token = event.reply_token
        img = "https://www.basketball-reference.com/req/202106291/images/players/curryst01.jpg"
        title = 'Stephen Curry'
        uptext = 'PG #30 Greatest Shooter of All-time\n????????????????????????~~~\n'
        labels = ['Player Stats', 'Player Info', 'Back to Roster']
        texts = ['Player Stats', 'Player Info', 'Back to Roster']
        send_button_message(reply_token, img, title, uptext, labels, texts)

    def is_going_to_currystats(seif, event):
        print("is going to SC30")
        text = event.message.text
        return text.lower() == "player stats"
    
    def on_enter_currystats(self, event):
        print("I'm entering SC30")
        reply_token = event.reply_token
        StephenCurryStats(reply_token)
    
    def is_going_to_curryinfo(seif, event):
        print("is going to SCinfo")
        text = event.message.text
        return text.lower() == "player info"
    
    def on_enter_curryinfo(self, event):
        print("I'm entering SCinfo")
        reply_token = event.reply_token
        showcurryinfo(reply_token)

    # Klay Thompson
    def is_going_to_KlayThompson(seif, event):
        text = event.message.text
        return text.lower() == "klay thompson"
    
    def is_going_to_backklay(self, event):
        text = event.message.text
        return text.lower() == "back"

    def on_enter_KlayThompson(self, event):
        print("I'm entering KT")
        reply_token = event.reply_token
        img = "https://www.basketball-reference.com/req/202106291/images/players/thompkl01.jpg"
        title = 'Klay Thompson'
        uptext = 'SG #11 Splash Brothers\nElite Spot up Shooter\n??????????????????!\n'
        labels = ['Player Stats', 'Player Info', 'Back to Roster']
        texts = ['Player Stats', 'Player Info', 'Back to Roster']
        send_button_message(reply_token, img, title, uptext, labels, texts)

    def is_going_to_klaystats(seif, event):
        print("is going to KT11")
        text = event.message.text
        return text.lower() == "player stats"
    
    def on_enter_klaystats(self, event):
        print("I'm entering KT11")
        reply_token = event.reply_token
        KlayThompsonStats(reply_token)

    def is_going_to_klayinfo(seif, event):
        print("is going to KT11info")
        text = event.message.text
        return text.lower() == "player info"
    
    def on_enter_klayinfo(self, event):
        print("I'm entering KT11info")
        reply_token = event.reply_token
        showklayinfo(reply_token)

    #Draymond Green
    def is_going_to_Draymond(seif, event):
        text = event.message.text
        return text.lower() == "draymond green"
    
    def is_going_to_backdray(self, event):
        text = event.message.text
        return text.lower() == "back"

    def on_enter_Draymond(self, event):
        print("I'm entering DR")
        reply_token = event.reply_token
        img = "https://www.basketball-reference.com/req/202106291/images/players/greendr01.jpg"
        title = 'Draymond Green'
        uptext = 'PF/C #23 Team Defensive Core\n????????????????????????~~\n????????????T???!\n'
        labels = ['Player Stats', 'Player Info', 'Back to Roster']
        texts = ['Player Stats', 'Player Info', 'Back to Roster']
        send_button_message(reply_token, img, title, uptext, labels, texts)

    def is_going_to_draystats(seif, event):
        print("is going to DR23")
        text = event.message.text
        return text.lower() == "player stats"
    
    def on_enter_draystats(self, event):
        print("I'm entering DR23")
        reply_token = event.reply_token
        Draymondstats(reply_token)

    def is_going_to_drayinfo(seif, event):
        print("is going to DR23info")
        text = event.message.text
        return text.lower() == "player info"
    
    def on_enter_drayinfo(self, event):
        print("I'm entering DR23info")
        reply_token = event.reply_token
        showdrayinfo(reply_token)

    #Andrew Wiggins
    def is_going_to_Wiggins(seif, event):
        text = event.message.text
        return text.lower() == "andrew wiggins"
    
    def is_going_to_backwig(self, event):
        text = event.message.text
        return text.lower() == "back"

    def on_enter_Wiggins(self, event):
        print("I'm entering WG")
        reply_token = event.reply_token
        img = "https://www.basketball-reference.com/req/202106291/images/players/wiggian01.jpg"
        title = 'Andrew Wiggins'
        uptext = 'SF #22\n???????????????aka????????????~~\n?????????????????????!\n'
        labels = ['Player Stats', 'Player Info', 'Back to Roster']
        texts = ['Player Stats', 'Player Info', 'Back to Roster']
        send_button_message(reply_token, img, title, uptext, labels, texts)

    def is_going_to_wigstats(seif, event):
        print("is going to WG22")
        text = event.message.text
        return text.lower() == "player stats"
    
    def on_enter_wigstats(self, event):
        print("I'm entering WG22")
        reply_token = event.reply_token
        Wigginsstats(reply_token)

    def is_going_to_wiginfo(seif, event):
        print("is going to WG22info")
        text = event.message.text
        return text.lower() == "player info"
    
    def on_enter_wiginfo(self, event):
        print("I'm entering WG22info")
        reply_token = event.reply_token
        showwigsinfo(reply_token)
    
