from transitions.extensions import GraphMachine

from utils import send_text_message, showroster


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_lobby(self, event):
        text = event.message.text
        return text.lower() == "lobby"

    def on_enter_lobby(self, event):
        print("I'm entering lobby")
        reply_token = event.reply_token
        send_text_message(reply_token, "Welcome to Dubnation!")
        # self.go_back()
    
    def is_going_to_roster(seif, event):
        print("is going to roster")
        text = event.message.text
        return text.lower() == "roster"
    
    def on_enter_roster(self, event):
        print("I'm entering roster")
        reply_token = event.reply_token
        showroster(reply_token)
        # send_text_message(reply_token, "Warriors Roster:")

    def is_going_to_playerstats(seif, event):
        print("is going to player")
        text = event.message.text
        return text.lower() == "name"
    
    def on_enter_playerstats(self, event):
        print("I'm entering roster")
        reply_token = event.reply_token
        send_text_message(reply_token, "Statistics")
        self.go_back()

    def is_going_to_schedule(self, event):
        print("is going to schedule")
        text = event.message.text
        return text.lower() == "check schedule"

    def on_enter_schedule(self, event):
        print("I'm entering Schedule")
        reply_token = event.reply_token
        send_text_message(reply_token, "Warriors upcomming Schedules:")
        self.go_back()

    # def on_exit_state2(self):
    #     print("Leaving state2")

    
    
