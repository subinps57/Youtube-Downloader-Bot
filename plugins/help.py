from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"നിലവിൽ Playlist സപ്പോർട്ട് ചെയ്യുന്നില്ല . പക്ഷേ ഉടൻ വരും..."
    await message.reply_text(helptxt)
