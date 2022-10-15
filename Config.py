import os

ENVIRONMENT = os.environ.get('ENVIRONMENT', False)

if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('API_ID', 0))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get('API_HASH', None)
    BOT_TOKEN = os.environ.get('BOT_TOKEN', None)
    DATABASE_URL = os.environ.get('DATABASE_URL', None)
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")  # Sqlalchemy dropped support for "postgres" name.
    # https://stackoverflow.com/questions/62688256/sqlalchemy-exc-nosuchmoduleerror-cant-load-plugin-sqlalchemy-dialectspostgre
    MUST_JOIN = os.environ.get('MUST_JOIN', None)
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN.replace("@", "")
else:
    # Fill the Values
    API_ID = 534493
    API_HASH = "ac922823455e814e44020a9f3ee17914"
    BOT_TOKEN = "5752725687:AAHkApA42hWm1wA_JAa94H4ddlDrRisAI0Q"
    DATABASE_URL = "mongodb+srv://my_bot:toshqul96@cluster0.djaqdiv.mongodb.net/?retryWrites=true&w=majority"
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
    MUST_JOIN = "hacker_oken"
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN[1:]
