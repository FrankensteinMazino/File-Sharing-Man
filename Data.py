# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from pyrogram.types import InlineKeyboardButton

class Data:
    HELP = """
<b> ❏ Perintah Untuk Pengguna BOT
 ├ /start - Mulai Bot
 ├ /about - Tentang Bot ini
 ├ /help - Bantuan Perintah Bot ini
 ├ /ping - Untuk Mengecek Bot Hidup
 └ /uptime - Untuk Melihat Status Bot 
 
 ❏ Perintah Untuk Admin BOT
 ├ /logs - Untuk Melihat Logs Bot
 ├ /setvar - Untuk Mengatur Var Dengan Command Dibot
 ├ /delvar - Untuk Menghapus Var Dengan Command Dibot
 ├ /getvar - Untuk Melihat Salah Satu Var Dengan Command Dibot
 ├ /users - Untuk Melihat Statistik Pengguna Bot
 ├ /batch - Untuk Membuat Link Lebih Dari Satu File
 ├ /speedtest - Untuk Mengetes Kecepatan Server Bot
 └ /broadcast - Untuk Mengirim Pesan Broadcast ke Pengguna Bot
 
👨‍💻 Develoved by </b><a href='https://t.me/faksyiit'>@faksyiit</a>
"""

    close = [
        [InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close")]
    ]

    mbuttons = [
        [
            InlineKeyboardButton("ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
            InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close")
        ],
    ]

    buttons = [
        [
            InlineKeyboardButton("ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ", callback_data="about"),
            InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close")
        ],
    ]

    ABOUT = """
<b>Tentang Bot ini:

@{} adalah Bot Telegram untuk menyimpan Postingan atau File yang dapat Diakses melalui Link Khusus.

 • Creator: @{}
 • Framework: <a href='https://docs.pyrogram.org'>Pyrogram</a>
 • Programming Language: <a href='https://www.python.org'>Python</a>

👨‍💻 Develoved by </b><a href='https://t.me/faksyiit'>@faksyiit</a>
"""
