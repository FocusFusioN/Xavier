from . import *

@bot.on(hell_cmd(pattern="gcast ?(.*)"))
@bot.on(sudo_cmd(pattern="gcast ?(.*)", allow_sudo=True))
async def _(event):
    reply_msg = await event.get_reply_message()
    flag = event.text[-4:]
    if reply_msg:
        OwO = reply_msg
    else:
        OwO = str(event.text[7:])
    if OwO == "":
        return await eod(event, "I need something to Gcast.")
    hel_ = await eor(event, "`Gcasting message...`")
    sed = 0
    owo = 0
    if "-all" in flag:
        async for allhell in bot.iter_dialogs():
            chat = allhell.id
            hell = OwO.replace("-all", "")
            try:
                await bot.send_message(chat, hell)
                owo += 1
            except BaseException:
                sed += 1
    elif "-pvt" in flag:
        async for pvthell in bot.iter_dialogs():
            if pvthell.is_user and not pvthell.entity.bot:
                chat = pvthell.id
                hell = OwO.replace("-pvt", "")
                try:
                    await bot.send_message(chat, hell)
                    owo += 1
                except BaseException:
                    sed += 1
    elif "-grp" in flag:
        async for ghell in bot.iter_dialogs():
            if ghell.is_group:
                chat = ghell.id
                hell = OwO.replace("-grp", "")
                try:
                    await bot.send_message(chat, hell)
                    owo += 1
                except BaseException:
                    sed += 1
    else:
        return await hel_.edit("Please give a flag to Gcast message. \n\n**Available flags are :** \nā¢ -all : To Gcast in all chats. \nā¢ -pvt : To Gcast in private chats. \nā¢ -grp : To Gcast in groups.")
    UwU = sed + owo
    if flag == "-all":
        omk = "Chats"
    elif flag == "-pvt":
        omk = "PM"
    elif flag == "-grp":
        omk = "Groups"
    await hel_.edit(f"**Gcast Executed Successfully !!** \n\n**š Sent in :** `{owo} {omk}`\n**š Failed in :** `{sed} {omk}`\n**š Total :** `{UwU} {omk}`")

# This is a bad way. but works just fine (*ļ¹*;)

CmdHelp("gcast").add_command(
  "gcast", "<text/reply> <flag>", "Globally Broadcast the replied or given message based on flag given.", f"gcast Hello -all / {hl}gcast Hello -grp / {hl}gcast Hello -pvt"
).add_info(
  "Global Broadcast. \n**š© Flags :** `-all`, `-pvt`, `-grp`"
).add_warning(
  "ā Harmless Module."
).add()
