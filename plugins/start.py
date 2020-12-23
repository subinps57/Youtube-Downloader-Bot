from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel", url="https://t.me/subin_works")],
        [InlineKeyboardButton(
            "Report Bugs 😊", url="https://t.me/subinps")]
    ])
    welcomed = f"ഹലോ മിസ്റ്റർ <b>{message.from_user.first_name}</b>\nകൂടുതൽ അറിയാനും സഹായങ്ങൾകും/help ഉപയോഗിക്കുക "
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
