from os import environ

API_ID = int(environ.get("API_ID", "26910777"))
API_HASH = environ.get("API_HASH", "8601f2f24993f6fdbcbac3bb27ceec38")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

# Make Bot Admin In Log Channel With Full Rights
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1003677136948"))
ADMINS = int(environ.get("ADMINS", "5232142502"))

# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = environ.get("DB_URI", "mongodb+srv://King:Cobra765592@cluster0.qy4m5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = environ.get("DB_NAME", "tsjoinrequetbot")

# If this is True Then Bot Accept New Join Request 
NEW_REQ_MODE = bool(environ.get('NEW_REQ_MODE', False))
