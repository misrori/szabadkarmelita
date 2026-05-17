import requests
import os

# Read environment variables (will come from Secrets)
TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]


# Compose the Telegram message
message = (
    'mehet a foglalás'
)

# Send message via Telegram Bot API
import requests

url = 'https://form.jotform.com/261341956633359/' # A megadott űrlap URL-je

try:
    response = requests.get(url)
    print(f"Státuszkód: {response.status_code}")

except:
    print("Hiba: Nem sikerült csatlakozni a weboldalhoz. Lehet, hogy nem elérhető vagy probléma van az internetkapcsolattal.")

print(str(response.content))

if "jelenleg nem" in str(response.content)==False:
    telegram_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    t = requests.post(telegram_url, json={
        "chat_id": CHAT_ID,
        "text": "message"
    })

    print("Message sent!")

