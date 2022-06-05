import os
import sys
import time
import asyncio
import random
import telethon.utils
from sys import argv
from telethon import TelegramClient, events
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
from telethon.sessions import StringSession
from Config import STRING, SUDO_IDS, BIO_MESSAGE, API_ID, API_HASH, STRING_SESSION2, STRING_SESSION3, STRING_SESSION4 ,STRING_SESSION5, STRING_SESSION6, STRING_SESSION7, STRING_SESSION8 ,STRING_SESSION9, STRING_SESSION10
from userbot.Config import Config
from userbot.utils import load_module
from userbot import LOAD_PLUG, LOGS, mafiaversion
from pathlib import Path
from var import Var
from userbot.helpers import functions as simpdef


one = STRING_SESSION
two = STRING_SESSION2
three = STRING_SESSION3
four = STRING_SESSION4
five = STRING_SESSION5
six = STRING_SESSION6
seven = STRING_SESSION7
eight = STRING_SESSION8
nine = STRING_SESSION9
ten = STRING_SESSION10


sessionone = ""
sessiontwo = ""
sessionthree = ""
sessionfour = ""
sessionfive = ""
sessionsix = ""
sessionseven = ""
sessioneight = ""
sessionnine = ""
sessionten = ""



que = {}

SUDO_USERS = []
for x in SUDO_IDS:
    SUDO_USERS.append(x)
    
async def start_spam():
    global sessionone
    global sessiontwo
    global sessionthree
    global sessionfour
    global sessionfive
    global sessionsix
    global sessionseven
    global sessioneight
    global sessionten
    global sessionnine
    
    if one:
        session_name = str(one)
        print("String 1 Found")
        sessionone = TelegramClient(StringSession(session_name), Var.APP_ID, Var.API_HASH)
        try:
            print("Booting Up The Client 1")
            await sessionone.start()
            botme = await sessionone.get_me()
            await sessionone(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await sessionone(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            sessionone = "one"
            print(e)
            pass
    else:
        print("Session 1 not Found")
        session_name = "startup"
        sessionone = TelegramClient(session_name, Var.APP_ID, Var.API_HASH)
        try:
            await sessionone.start()
        except Exception as e:
            pass
   
    if two:
        session_name = str(two)
        print("String 2 Found")
        sessiontwo = TelegramClient(StringSession(session_name), Var.APP_ID, Var.API_HASH)
        try:
            print("Booting Up The Client 2")
            await sessiontwo.start()
            await sessiontwo(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await sessiontwo(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            botme = await sessiontwo.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 2 not Found")
        pass
        session_name = "startup"
        sessiontwo = TelegramClient(session_name, Var.APP_ID, Var.API_HASH)
        try:
            await sessiontwo.start()
        except Exception as e:
            pass

    if three:
        session_name = str(three)
        print("String 3 Found")
        sessionthree = TelegramClient(StringSession(session_name), Var.APP_ID, Var.API_HASH)
        try:
            print("Booting Up The Client 3")
            await  sessionthree.start()
            await sessionthree(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await sessionthree(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            botme = await sessionthree.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 3 not Found")
        pass
        session_name = "startup"
        sessionthree = TelegramClient(session_name, Var.APP_ID, Var.API_HASH)
        try:
            await sessionthree.start()
        except Exception as e:
            pass

    if four:
        session_name = str(four)
        print("String 4 Found")
        sessionfour = TelegramClient(StringSession(session_name), Var.APP_ID, Var.API_HASH)
        try:
            print("Booting Up The Client 4")
            await sessionfour.start()
            await sessionfour(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await sessionfour(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            botme = await sessionfour.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 4 not Found")
        pass
        session_name = "startup"
        sessionfour = TelegramClient(session_name, Var.APP_ID, Var.API_HASH)
        try:
            await sessionfour.start()
        except Exception as e:
            pass

    if five:
        session_name = str(five)
        print("String 5 Found")
        sessionfive = TelegramClient(StringSession(session_name), Var.APP_ID, Var.API_HASH)
        try:
            print("Booting Up The Client 5")
            await sessionfive.start()
            await sessionfive(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await sessionfive(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            botme = await sessionfive.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 5 not Found")
        pass
        session_name = "startup"
        sessionfive = TelegramClient(session_name, Var.APP_ID, Var.API_HASH)
        try:
            await sessionfive.start()
        except Exception as e:
            pass
                  
    if six:
        session_name = str(six)
        print("String 6 Found")
        sessionsix = TelegramClient(StringSession(session_name), Var.APP_ID, Var.API_HASH)
        try:
            print("Booting Up The Client 6")
            await sessionsix.start()
            await sessionsix(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await sessionsix(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            botme = await sessionsix.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 6 not Found")
        pass
        session_name = "startup"
        sessionsix = TelegramClient(session_name, Var.APP_ID, Var.API_HASH)
        try:
            await sessionsix.start()
        except Exception as e:
            pass

    if seven:
        session_name = str(seven)
        print("String 7 Found")
        sessionseven = TelegramClient(StringSession(session_name), Var.APP_ID, Var.API_HASH)
        try:
            print("Booting Up The Client 7")
            await sessionseven.start()
            await sessionseven(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await sessionseven(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            botme = await sessionseven.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 7 not Found")
        pass
        session_name = "startup"
        sessionseven = TelegramClient(session_name, Var.APP_ID, Var.API_HASH)
        try:
            await sessionseven.start()
        except Exception as e:
            pass    
        
    
    if eight:
        session_name = str(eight)
        print("String 8 Found")
        sessioneight = TelegramClient(StringSession(session_name), Var.APP_ID, Var.API_HASH)
        try:
            print("Booting Up The Client 8")
            await sessioneight.start()
            await sessioneight(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await sessioneight(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            botme = await sessioneight.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 8 not Found")
        pass
        session_name = "startup"
        sessioneight = TelegramClient(session_name, Var.APP_ID, Var.API_HASH)
        try:
            await sessioneight.start()
        except Exception as e:
            pass   
        
    if nine:
        session_name = str(nine)
        print("String 9 Found")
        sessionnine = TelegramClient(StringSession(session_name), Var.APP_ID, Var.API_HASH)
        try:
            print("Booting Up The Client 9")
            await sessionnine.start()
            await sessionnine(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await sessionnine(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            botme = await sessionnine.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 9 not Found")
        pass
        session_name = "startup"
        sessionnine = TelegramClient(session_name, Var.APP_ID, Var.API_HASH)
        try:
            await sessionnine.start()
        except Exception as e:
            pass   
    
  
    if ten:
        session_name = str(ten)
        print("String 10 Found")
        sessionten = TelegramClient(StringSession(session_name), Var.APP_ID, Var.API_HASH)
        try:
            print("Booting Up The Client 10")
            await sessionten.start()
            await sessionten(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAMMER"))
            await sessionten(functions.channels.JoinChannelRequest(channel="@DEADLY_SPAM_BOT"))
            botme = await sessionten.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 10 not Found")
        pass
        session_name = "startup"
        sessionten = TelegramClient(session_name, Var.APP_ID, Var.API_HASH)
        try:
            await sessionten.start()
        except Exception as e:
            pass 
        
        
loop = asyncio.get_event_loop()
loop.run_until_complete(start_spam())  

     
import glob
path = 'userbot/plugins/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))
          

print("""YOUR 𝕄𝔸𝔽𝕀𝔸 𝕌𝕊𝔼ℝ𝔹𝕆𝕋 IS READY TO USE! FOR CHECK YOUR BOT WORKING OR NOT PLEASE TYPE (.alive/.ping) ENJOY YOUR BOT! JOIN FOR MORE FUTURE UPDATES @MAFIA_USERBOT""")

if len(argv) not in (1, 3, 4):
    try:
        sessionone.disconnect()
    except Exception as e:
        pass
    try:
        sessiontwo.disconnect()
    except Exception as e:
        pass
    try:
        sessionthree.disconnect()
    except Exception as e:
        pass
    try:
        sessionfour.disconnect()
    except Exception as e:
        pass
    try:
        sessionfive.disconnect()
    except Exception as e:
        pass
    try:
        sessionsix.disconnect()
    except Exception as e:
        pass
    try:
        sessionseven.disconnect()
    except Exception as e:
        pass
    try:
        sessioneight.disconnect()
    except Exception as e:
        pass
    try:
        sessionnine.disconnect()
    except Exception as e:
        pass
    try:
        sessionten.disconnect()
    except Exception as e:
        pass
else:
    try:
        sessionone.run_until_disconnected()
    except Exception as e:
        pass
    try:
        sessiontwo.run_until_disconnected()
    except Exception as e:
        pass
    try:
        sessionthree.run_until_disconnected()
    except Exception as e:
        pass
    try:
        sessionfour.run_until_disconnected()
    except Exception as e:
        pass
    try:
        sessionfive.run_until_disconnected()
    except Exception as e:
        pass
    try:
        sessionsix.run_until_disconnected()
    except Exception as e:
        pass
    try:
        sessionseven.run_until_disconnected()
    except Exception as e:
        pass
    try:
        sessioneight.run_until_disconnected()
    except Exception as e:
        pass
    try:
        sessionnine.run_until_disconnected()
    except Exception as e:
        pass
    try:
        sessionten.run_until_disconnected()
    except Exception as e:
        pass
