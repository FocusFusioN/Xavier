import asyncio
import datetime

from . import *

@bot.on(xavier_cmd(pattern="ping$"))
@bot.on(sudo_cmd(pattern="ping$", allow_sudo=True))
async def pong(xavier):
    if xavier.fwd_from:
        return
    start = datetime.datetime.now()
    event = await eor(xavier, "`β€βππππββ’Β΄")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(
        f"β€βππππββ’\n\n    β  `{ms}`\n    β  __**πππππ**__ **:**  {xavier_mention}"
    )


CmdHelp("ping").add_command(
  "ping", None, "Checks the ping speed of your ΟΞ±Ξ½ΞΉΡΡ"
).add_warning(
  "β Harmless Module"
).add()

# xavier
