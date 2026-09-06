import os
import logging
from logging.handlers import RotatingFileHandler

# Bot Configuration
LOG_FILE_NAME = "bot.log"
PORT = int(os.environ.get("PORT", "10000")) # Render needs 10000, not 5010
OWNER_ID = int(os.environ.get("OWNER_ID", "7653921320"))

MSG_EFFECT = 5046509860389126442

SHORT_URL = os.environ.get("SHORT_URL", "shrinkme.io")
SHORT_API = os.environ.get("SHORT_API", "xxxxxxxxxxx45e6887xxxxxxxxxxx")
SHORT_TUT = os.environ.get("SHORT_TUT", "https://t.me/ANIME_X_FLEX/19")

# Bot Configuration - FIXED TO READ FROM RENDER ENV
SESSION = os.environ.get("SESSION", "BotifyX-Botz")
TOKEN = os.environ.get("BOT_TOKEN") or os.environ.get("TOKEN") or ""
API_ID = int(os.environ.get("API_ID", "0") or "0")
API_HASH = os.environ.get("API_HASH", "")
WORKERS = int(os.environ.get("WORKERS", "5"))

DB_URL = os.environ.get("DB_URL") or os.environ.get("DATABASE_URL") or "mongodb+srv://newsudo:786780@cluster0.pbiae8a.mongodb.net/?appName=Cluster0"
DB_NAME = os.environ.get("DB_NAME", "Cluster0")

# Alias for old code
DB_URI = DB_URL
BOT_TOKEN = TOKEN

FSUBS = [[-1002649539214, True, 10]]
DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1003839222178"))
AUTO_DEL = int(os.environ.get("AUTO_DEL", "300"))
ADMINS = [6426143861, 6426143861]  # put your IDs directly

DISABLE_BTN = True
PROTECT = False

# Messages Configuration - same as yours
MESSAGES = {
    "START": "<b>›› ʜᴇʏ!! {mention}× sᴇɴᴘᴀɪ 🎊\n</b><blockquote><b>ᴜɴʟᴏᴄᴋ ᴛʜᴇ ᴇɴɪɢᴍᴀ ᴏꜰ ᴏɴɢᴏɪɴɢ ᴀɴɪᴍᴇ ᴡʜᴇʀᴇ ᴅᴇsɪʀᴇ ʟɪɴɢᴇʀs ʙᴇʏᴏɴᴅ ᴇᴠᴇʀʏ ꜰʀᴀᴍᴇ, ᴅʀᴀᴡɪɴɢ ʏᴏᴜ ɪɴᴛᴏ ᴀ ʀᴇᴀʟᴍ ᴏꜰ ʜɪᴅᴅᴇɴ ꜰᴀɴᴛᴀsɪᴇs ᴀɴᴅ sɪʟᴇɴᴛ ᴏʙsᴇssɪᴏɴs.</b></blockquote>\n<blockquote>››ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href='https://t.me/Anime_Hub_Tami'>彡 Eren€ 彡</a></blockquote>",
    "FSUB": "<blockquote>›› ʜᴇʏ {mention}× sᴇɴᴘᴀɪ 🎊</blockquote>\n<blockquote><b>ʏᴏᴜʀ ғɪʟᴇ ɪs ʀᴇᴀᴅʏ ‼️ ʟᴏᴏᴋs ʟɪᴋᴇ ʏᴏᴜ ʜᴀᴠᴇɴ'ᴛ sᴜʙsᴄʀɪʙᴇᴅ ᴛᴏ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ʏᴇᴛ, sᴜʙsᴄʀɪʙᴇ ɴᴏᴡ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ғɪʟᴇs</b></blockquote>",
    "ABOUT": "<b>›› ғᴏʀ ᴍᴏʀᴇ: <a href='https://t.me/Anime_Hub_Tamil'>Cʟɪᴄᴋ ʜᴇʀᴇ</a>\n<blockquote expandable>›› ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ: <a href='https://t.me/Anime_Hub_Tamil'>ᴀɴɪᴍᴇ_ʜᴜʙ_ᴛᴀᴍɪʟ`</a> \n›› ᴏᴡɴᴇʀ: @Eren_157\n›› ʟᴀɴɢᴜᴀɢᴇ: <a href='https://docs.python.org/3/'>Pʏᴛʜᴏɴ 3</a> \n›› ʟɪʙʀᴀʀʏ: <a href='https://docs.pyrogram.org/'>Pʏʀᴏɢʀᴀᴍ ᴠ2</a> \n›› ᴅᴀᴛᴀʙᴀsᴇ: <a href='https://www.mongodb.com/docs/'>Mᴏɴɢᴏ ᴅʙ</a> \n›› ᴅᴇᴠᴇʟᴏᴘᴇʀ: @ZENCURSE</b></blockquote>",
    "CHANNELS":"<b>›› ᴀɴɪᴍᴇ ᴄʜᴀɴɴᴇʟ: <a href='https://t.me/Anime_Hub_Tamil'>ᴀɴɪᴍᴇ_ʜᴜʙ_ɴᴀᴛɪᴏɴx</a>\n<blockquote expandable>›› ᴍᴏᴠɪᴇs: <a href='https://t.me/AniPlex_Tamil'>ᴀɴɪ_ᴍᴏᴠɪᴇ's ᴍᴀɴɪᴀ</a>\n›› ᴀɴɪᴍᴇ ᴇᴅɪᴛᴢ: <a href='https://t.me/Anime_Hub_Tamil'>ᴀɴɪᴍᴇ'ᴢ ᴇᴅɪᴛ'ᴢ</a>\n›› ᴀᴅᴜʟᴛ ᴄʜᴀɴɴᴇʟs: <a href='https://t.me/Anime_Hub_Tamil'>𝖧𝖺𝗇𝗆𝖾 𝖥𝗅𝗂𝗑</a>\n›› ᴍᴀɴʜᴡᴀ ᴄʜᴀɴɴᴇʟ: <a href='https://t.me/Anime_Hub_Tamil'>Animes ✨</a>\n›› ᴄᴏᴍᴍᴜɴɪᴛʏ: <a href='https://t.me/Anime_Hub_Tamil'>ᴏᴛᴀᴋᴜғʟɪx</a>\n›› ᴅᴇᴠᴇʟᴏᴘᴇʀ: @ZENCURSE</b></blockquote>",
    "REPLY": "<b>ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ sᴇɴᴘᴀɪ!!</b>",
    "SHORT_MSG": "<blockquote><b>✧ TOKEN EXPIRED</b></blockquote>\n<blockquote>›› ᴘʟᴇᴀsᴇ ᴠᴇʀɪғʏ ᴛᴏ ʀᴇɢᴀɪɴ ᴀᴄᴄᴇss ᴛᴏ ᴛʜᴇ ғɪʟᴇs\n›› ᴠᴀʟɪᴅ ᴄʀᴇᴅɪᴛs: 5 ᴄʀᴇᴅɪᴛs</blockquote>\n────────────────────────\n<blockquote>›› ᴡʜᴀᴛ ɪs ᴀ ᴛᴏᴋᴇɴ?</blockquote>\n<blockquote>≡ ᴇᴀᴄʜ ᴀᴅ ʙʏᴘᴀss ʀᴇᴡᴀʀᴅ ʏᴏᴜ ᴡɪᴛʜ 5 ᴄʀᴇᴅɪᴛs.ᴏɴᴇ ᴄʀᴇᴅɪᴛ ɪs ᴄᴏɴsᴜᴍᴇᴅ ᴘᴇʀ ғɪʟᴇ/ʟɪɴᴋ ᴀᴄᴄᴇss.</blockquote>",
    "START_PHOTO": "https://ibb.co/hJHGFfxs",
    "FSUB_PHOTO": "https://ibb.co/hJHGFfxs",
    "SHORT_PIC": "https://ibb.co/hJHGFfxs",
    "SHORT": "https://ibb.co/mC9H5kmF",
    "SHORT_VERIFY": "https://ibb.co/rGg6R2q6",
    "PREMIUM_PLANS_PIC": "https://ibb.co/8Dzq5n9G",
    "QR_PAYMENT_PIC": "https://ibb.co/kVPDT5cP"
}

def LOGGER(name: str, client_name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    formatter = logging.Formatter(
        f"[%(asctime)s - %(levelname)s] - {client_name} - %(name)s - %(message)s",
        datefmt='%d-%b-%y %H:%M:%S'
    )
    file_handler = RotatingFileHandler(LOG_FILE_NAME, maxBytes=50_000_000, backupCount=10)
    file_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    return logger
