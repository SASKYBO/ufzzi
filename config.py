from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
APP_ID = os.environ.get("APP_ID",
"1138829")
APP_HASH = os.environ.get("APP_HASH",
"2395478f1897069f56891121929c5374")
BOT_USERNAME = os.environ.get("BOT_USERNAME",
                           "Qpqpa_bot")
session = os.environ.get("TERMUX",
                        "1BJWap1sBu0Tydlx1yAa9r0JFZexkZaUJriKeJAp90EBYCG1tq9k15YzsZLa00WoD2nyY_SsHpW7EZ9xR_-j2c9E-lauLum74DJRoasT6-wCTfnN9evE-7w9W_mr9JqPXpJESPnyv-wGxiAk2vjUaxFcKNU9uSYiaVafG7XZ4eEPYwQBmH4sk0Jv-dEHA-ub6hrOstFOyB56QkvTmhQQOpsAWwmgFvnjqWFktUdwnkHQsg1sf0pfSy5sbx_IFdlWy-2-NQLXzfzyHBdmoKQ5QCVcrpUIpTXh9AZWxdAIG6xN7n4BQwbq_JP51qs2jgNjeNKpLGYKt1BQBanK5n_Ussk-kXpaP6HY=")
SESSION = os.environ.get("TERMUX",
                        "1BJWap1sBu0Tydlx1yAa9r0JFZexkZaUJriKeJAp90EBYCG1tq9k15YzsZLa00WoD2nyY_SsHpW7EZ9xR_-j2c9E-lauLum74DJRoasT6-wCTfnN9evE-7w9W_mr9JqPXpJESPnyv-wGxiAk2vjUaxFcKNU9uSYiaVafG7XZ4eEPYwQBmH4sk0Jv-dEHA-ub6hrOstFOyB56QkvTmhQQOpsAWwmgFvnjqWFktUdwnkHQsg1sf0pfSy5sbx_IFdlWy-2-NQLXzfzyHBdmoKQ5QCVcrpUIpTXh9AZWxdAIG6xN7n4BQwbq_JP51qs2jgNjeNKpLGYKt1BQBanK5n_Ussk-kXpaP6HY=")
token = os.environ.get("TOKEN",
                      "5348430767:AAEUtqHybH5mY2VqyjwoZqtouuC48BARQK4")
fifthon = TelegramClient(StringSession(session), APP_ID, APP_HASH)
bot = TelegramClient("bot", APP_ID, APP_HASH).start(bot_token=token)
ispay = ['yes']
ispay2 = ['yes']
bot.start()
