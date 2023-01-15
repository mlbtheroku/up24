import os

class Config(object):

    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("BOT_TOKEN", "5945346287:AAE3gmyeGs-oK2UxcgbTDWjr48an4iv-oSY")

    # The Telegram API things
    # Get these values from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", 22681384))
    API_HASH = os.environ.get("API_HASH", "14ae45755537c723aab0564a80d723a9")

    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "5468192421").split())

    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"

    # Telegram maximum file upload size
    TG_MAX_FILE_SIZE = 2097152000

    # chunk size that should be used with requests
    CHUNK_SIZE = 128

    # Generate screenshots for file after uploading
    # Defaults to True
    SCREENSHOTS = os.environ.get("SCREENSHOTS", "True")

    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")

    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    
    # Update channel for Force Subscribe
    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "-1001523739263")
    
    # Log channel for banning spammers
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -1001860694129))

    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096

    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = int(os.environ.get("TIME_LIMIT", 800))
    
    # dict to hold the ReQuest queue
    ADL_BOT_RQ = {}

    # watermark file
    DEF_WATER_MARK_FILE = ""

    # Sql Database url
    #DB_URI = os.environ.get("DATABASE_URL", "")

    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    # Banned Unwanted Members..
    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
    
    SESSION_NAME = os.environ.get("SESSION_NAME", "1shree")
    
    SLEEP_TIME = int(os.environ.get("SLEEP_TIME", 5))
    
    BOT_OWNER = os.environ.get("BOT_OWNER", 1445283714)
    
    CAPTION = "Uploaded by @All_Movie_Rockers"
    
    MONGODB_URI = os.environ.get("MONGODB_URI", "")
    
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
    
    START_TEXT = ""
    PROGRESS = ""
