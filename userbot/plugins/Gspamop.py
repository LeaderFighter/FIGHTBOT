from userbot.utils import admin_cmd as mafiafightbot
from userbot import bot as mafiaopbolte
from telethon.errors.rpcerrorlist import UserAlreadyParticipantError
from telethon.tl.functions.messages import ImportChatInviteRequest
from userbot.utils import sudo_cmd
@mafiaopbolte.on(mafiafightbot(pattern="gspam"))
@mafiaopbolte.on(sudo_cmd(pattern=f"gspam$", allow_sudo=True))
async def mafia(fight):
  try:
       await fight.client(ImportChatInviteRequest('hE8sJZOZ-L9mODA1'))
  except UserAlreadyParticipantError:
        pass
  except:
        await fight.client(ImportChatInviteRequest('hE8sJZOZ-L9mODA1'))
        return
  async for msg in fight.client.iter_messages(-1001475750241):
   if msg:
    await fight.client.send_message(fight.chat_id, msg)