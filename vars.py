#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "29382018"))
API_HASH = environ.get("API_HASH", "4734a726c04620c61ec0a28a1ae0d57f")
BOT_TOKEN = environ.get("BOT_TOKEN", "7916183237:AAHIR8r3MvVOZPk7dv2oX_ibhZrTRKUtmlU")
OWNER = int(environ.get("OWNER", "7442532306"))
CREDIT = "ησσв-вσтѕ"
AUTH_USER = os.environ.get('AUTH_USERS', '7442532306').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
