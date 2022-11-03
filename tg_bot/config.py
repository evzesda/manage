from tg_bot.sample_config import Config


class Development(Config):
    OWNER_ID = 1954780613  # my telegram ID
    OWNER_USERNAME = "gemini_hakutakaa"  # my telegram username
    API_KEY = "5699365911:AAH3flpfHQ6k_4k17PA0DSmuKfFm0dPLrw8"  # my api key, as provided by the botfather
    SQLALCHEMY_DATABASE_URI = 'postgres://xefvomva:ITUQ4uaQlxZwQajl0hV5VPjgYL6falXF@jelani.db.elephantsql.com/xefvomva'  # sample db credentials
    MESSAGE_DUMP = '-1001686544997' # some group chat that your bot is a member of
    USE_MESSAGE_DUMP = True
    SUDO_USERS = [1954780613]  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['translation']
    WEBHOOK = False
    URL = None
    PORT = 5432
    DEL_CMDS = False  # Whether or not you should delete "blue text must click" commands
    STRICT_GBAN = True
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = False  # banhammer marie sticker
    ALLOW_EXCL = ["!","+"]  # Allow ! commands as well as /