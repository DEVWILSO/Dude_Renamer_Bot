import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "19902008")

API_HASH = os.environ.get("API_HASH", "d973fa8af375787c85dd6d2dfac94d7e")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6102180205:AAEKLprCQhVe5yxZkjP4-zMLrYj1C653TEo") 

FORCE_SUB = os.environ.get("FORCE_SUB", "Anime_Dub_Tam") 

DB_NAME = os.environ.get("DB_NAME","madflixbotz")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://monitgmoni:MoniTG007@cluster0.bxwiejd.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "30"))

START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/9acca333738f41eba89f8.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5204439926').split()]

PORT = os.environ.get("PORT", "8080")
