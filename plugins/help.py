from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"നിലവിൽ SL8 Bot Playlist സപ്പോർട്ട് ചെയ്യുന്നില്ല . പക്ഷേ ഉടൻ വരും...\nഎന്നെ നിർമിച്ചത് @subinps ആണ്.\nYoutube Video Download ചെയ്യാൻ എന്നെ ഉപയോഗിക്കാം.😉\n ഏതെങ്കിലമൊരു Youtube Video - യുടെ Link എനിക്ക് അയച്ച് തന്നിട്ട് ഏതു quality and foremat (Audio or Video) എന്ന്  സെലക്ട് ചെയ്താൽ മതി.\n ബാക്കി പിന്നെ ഞാൻ നോക്കിക്കോളാ😌\n നിങ്ങളുടെ അടുത്ത് Youtube Video യുടെ Link ഇല്ലെങ്കിൽ @vid എന്ന് ടൈപ്പ് ചെയ്ത് ഒരു space അടിച്ചാൽ നിങ്ങള്ക് ടെലഗ്രാമിലൂടെ തന്നെ  Youtube വീഡിയോകൾ സെർച്ച് ചെയ്യാൻ പറ്റും.അങ്ങനെ കിട്ടുന്ന ലിങ്ക് എനിക്ക് അയച്ച് തന്നാൽ മതി😉\n\nഎന്തെകിലും Bugs ഉണ്ടെങ്കിൽ എൻ്റെ ആശാണോട് -@subinps പറഞ്ഞാ മതി.😁"
    await message.reply_text(helptxt)
