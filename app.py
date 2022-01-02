import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from fsm import TocMachine
from utils import send_text_message

load_dotenv()

machine = TocMachine(
    states=["user", "menu", "roster", "highlights", "official",
        "StephenCurry", "KlayThompson",
        "currystats", "klaystats",
        "curryinfo", "klayinfo"],
    transitions=[
        {
            "trigger": "advance", 
            "source": "user", 
            "dest": "menu", 
            "conditions": "is_going_to_menu" },
        {
            "trigger": "advance", 
            "source": "menu", 
            "dest": "roster", 
            "conditions": "is_going_to_roster" },
        {
            "trigger": "advance", 
            "source": "menu", 
            "dest": "highlights", 
            "conditions": "is_going_to_highlights" },
        {
            "trigger": "advance", 
            "source": "menu", 
            "dest": "official", 
            "conditions": "is_going_to_official" },
        {
            "trigger": "advance", 
            "source": "roster", 
            "dest": "StephenCurry", 
            "conditions": "is_going_to_StephenCurry" },
        {
            "trigger": "advance", 
            "source": "roster", 
            "dest": "KlayThompson", 
            "conditions": "is_going_to_KlayThompson" },
        # {"trigger": "advance", "source": "roster", "dest": "StephenCurry", "conditions": "is_going_to_StephenCurry" },
        # {"trigger": "advance", "source": "roster", "dest": "StephenCurry", "conditions": "is_going_to_StephenCurry" },
        # {"trigger": "advance", "source": "roster", "dest": "StephenCurry", "conditions": "is_going_to_StephenCurry" },
        # {"trigger": "advance", "source": "roster", "dest": "StephenCurry", "conditions": "is_going_to_StephenCurry" },
        # {"trigger": "advance", "source": "roster", "dest": "StephenCurry", "conditions": "is_going_to_StephenCurry" },
        # {"trigger": "advance", "source": "roster", "dest": "StephenCurry", "conditions": "is_going_to_StephenCurry" },
        # {"trigger": "advance", "source": "roster", "dest": "StephenCurry", "conditions": "is_going_to_StephenCurry" },
        # {"trigger": "advance", "source": "roster", "dest": "StephenCurry", "conditions": "is_going_to_StephenCurry" },
        # {"trigger": "advance", "source": "roster", "dest": "StephenCurry", "conditions": "is_going_to_StephenCurry" },
        # {"trigger": "advance", "source": "roster", "dest": "StephenCurry", "conditions": "is_going_to_StephenCurry" },
        # {"trigger": "advance", "source": "roster", "dest": "StephenCurry", "conditions": "is_going_to_StephenCurry" },
        # {"trigger": "advance", "source": "roster", "dest": "StephenCurry", "conditions": "is_going_to_StephenCurry" },
        # {"trigger": "advance", "source": "roster", "dest": "StephenCurry", "conditions": "is_going_to_StephenCurry" },
        # {"trigger": "advance", "source": "roster", "dest": "StephenCurry", "conditions": "is_going_to_StephenCurry" },
        {
            "trigger": "advance", 
            "source": "StephenCurry", 
            "dest": "currystats", 
            "conditions": "is_going_to_currystats" },
        {
            "trigger": "advance", 
            "source": "StephenCurry", 
            "dest": "curryinfo", 
            "conditions": "is_going_to_curryinfo" },
        {
            "trigger": "advance", 
            "source": "KlayThompson", 
            "dest": "klaystats", 
            "conditions": "is_going_to_klaystats" },
        {
            "trigger": "advance", 
            "source": "KlayThompson", 
            "dest": "klayinfo", 
            "conditions": "is_going_to_klayinfo" },
        {
            "trigger": "advance", 
            "source": ["currystats", "curryinfo"],
            "dest": "StephenCurry", 
            "conditions": "is_going_to_backcurry" },
        {
            "trigger": "advance", 
            "source": ["klaystats", "klayinfo"],
            "dest": "KlayThompson", 
            "conditions": "is_going_to_backklay" },
        {
            "trigger": "advance", 
            "source": ["StephenCurry", "KlayThompson"], 
            "dest": "roster", 
            "conditions": "is_going_to_backroster" },
        {
            "trigger": "advance", 
            "source": [
                "StephenCurry", "currystats", "curryinfo",
                "KlayThompson", "klaystats", "klayinfo" ,"roster", "highlights", "official"], 
            "dest": "menu", 
            "conditions": "is_going_to_backmenu" },
        # {"trigger": "go_back", "source": ["playerstats", "currystats"], "dest": "menu"},
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)



app = Flask(__name__, static_url_path="")


# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text)
        )
    
    return "OK"


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        response = machine.advance(event)
        print("\n")
        print(event)
        print(response)
        if response == False:
            send_text_message(event.reply_token, "Not Entering any State")
        print(f"\nFSM STATE: {machine.state}")

    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
