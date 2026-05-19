import requests

BOT_TOKEN = "8855987219:AAEVTyQGB8oNJFv_PSYFW-9bVlRCUTtfqmg"
CHAT_ID = "1128479805"

def send_sos_sms(to_number, message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    data = {
        "chat_id": CHAT_ID,
        "text": message
    }

    requests.post(url, data=data)
