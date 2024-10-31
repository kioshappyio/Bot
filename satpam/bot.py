import telebot
from telebot.types import Message
import re

# Ganti dengan API Token Bot Anda
API_TOKEN = '7916485752:AAF2Gh3uxsjJgPN9KuUhTlleGz2-R75pLpQ'
bot = telebot.TeleBot(API_TOKEN)

# Daftar kata negatif yang lebih luas
NEGATIVE_WORDS = [
    'open bo', 'open booking', 'vcs', 'video call sex', 'judi online',
    'slot gacor', 'casino', 'poker online', 'bokep', 'porno', 'film dewasa',
    'sex chat', 'sugar daddy', 'sugar baby', 'fetish', 'sex service', 'escort',
    'pay for sex', 'p4p', 'cybersex', 'camsex', 'onlyfans', 'link terlarang',
    'link bokep', 'link dewasa', 'bandar togel', 'judi bola', 'adult content',
    'link biru', 'rp vulgar', 'open vc', 'open room', 'live cam', 'sexy cam',
    'nonton bokep', 'download bokep', 'hot video', 'live show', 'gratis chip',
    'chip murah', 'judi slot', 'judi domino', 'chip gratis', 'bandar qq',
    'skandal', 'big win', 'promo judi', 'link live', 'situs dewasa',
    'situs judi', 'pornografi', 'pornhub', 'xvideos', 'live hot', 'nfsw',
    'casino online', 'baccarat', 'sexy video', 'open chat', 'bigo live', 'cam live',
    'vc hot', 'open cam', 'sex video', 'viral bokep', 'nonton gratis', 'chip online'
]

# Pola regex yang diperluas
NEGATIVE_PATTERNS = [
    r'\bopen\s?bo\b',               
    r'\bvcs\b',                      
    r'\bjudi\s?online\b',            
    r'\bvideo\s?call\s?sex\b',       
    r'\bslot\s?gacor\b',             
    r'\bbokep\b',                    
    r'\bporn(?:o|hub|ografi)?\b',    
    r'https?://\S+',                
    r'www\.\S+',                     
    r'\bsex\s?chat\b',               
    r'\badult\s?content\b',          
    r'\bpay\s?for\s?sex\b',          
    r'\bsugar\s?baby\b',             
    r'\bsugar\s?daddy\b',            
    r'\bonly\s?fans\b',              
    r'\blink\s?(dewasa|bokep)\b',    
    r'\bbandar\s?togel\b',           
    r'\bcasino\b',                   
    r'\bbig\s?win\b',                
    r'\bpromo\s?judi\b',             
    r'\blive\s?(show|cam)\b',        
    r'\bchip\s?(gratis|murah)\b',    
    r'\bsitus\s?(dewasa|judi)\b',    
    r'\bpoker\s?online\b',           
    r'\bskandal\b',                  
    r'\bxvideos\b',                  
    r'\bsexy\s?(video|cam)\b',       
    r'\bviral\s?bokep\b',            
    r'\bgratis\s?(chip|nonton)\b',   
    r'\bchip\s?online\b',            
    r'\bbaccarat\b',                 
    r'\bnonton\s?gratis\b',          
    r'\bnfsw\b',                     
    r'\b(?:adult|sexy|hot)\s?(?:video|content|link)\b', 
    r'\b(?:free|gifts?)\s?(?:chips?|credits?)\b',  
    r'\b(?:adult|sex|porno|judi|bigo|live|nonton)\s?(?:links?|videos?|streams?)\b',  
    r'(?i)\b(?:pranks?|scams?|frauds?)\b',  
]

# Fungsi untuk memeriksa konten negatif
def contains_negative_content(text: str) -> bool:
    lower_text = text.lower()
    
    # Cek kata negatif langsung
    if any(word in lower_text for word in NEGATIVE_WORDS):
        return True

    # Cek pola regex
    for pattern in NEGATIVE_PATTERNS:
        if re.search(pattern, lower_text):
            return True

    return False

# Handler untuk pesan di grup dan channel
@bot.message_handler(func=lambda message: True, content_types=['text'])
def check_message(message: Message):
    if message.chat.type in ['group', 'supergroup', 'channel']:
        # Deteksi konten negatif
        if contains_negative_content(message.text):
            try:
                # Hapus pesan
                bot.delete_message(message.chat.id, message.message_id)
                print(f"Pesan terhapus: {message.text}")
            except Exception as e:
                print(f"Gagal menghapus pesan: {e}")

# Menjalankan bot
print("Bot sedang berjalan dan memantau pesan di grup dan channel...")
bot.infinity_polling()
