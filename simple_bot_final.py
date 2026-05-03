#!/usr/bin/env python3
"""
90 Kunlik Life Balance Bot - MINIMAL VERSIYA
Python 3.14 uchun, muammosiz!
"""

import logging
from datetime import datetime
import pytz

# Logging
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# ============================================
# 🔑 TOKENNI BU YERGA QOYING! 🔑
# ============================================
TELEGRAM_BOT_TOKEN = "8646706234:AAHX2F17s69oEezgpUE3EYMv5nJIhfhPA10"
# ============================================

# Tashkent vaqti
TIMEZONE = pytz.timezone('Asia/Tashkent')


def get_welcome_message(first_name):
    """Salom xabari"""
    return f"""
🌟 Assalomu alaykum, {first_name}!

90 kunlik Life Balance Bot ishga tushdi!

📅 Bugun: {datetime.now(TIMEZONE).strftime('%d.%m.%Y')}

🎯 MAQSADLAR:
1. ✅ Har kuni 5 vaqt namoz
2. ✅ Soat 23:00 uyqu, 06:00 turish
3. ✅ Instagram/Reels 0 daqiqa
4. ✅ Har kuni 30 daqiqa sport
5. ✅ Qarzni yopish rejasi (120 mln)

📱 BOT BUYRUQLARI:
/start - Botni ishga tushirish
/reja - 90 kunlik reja
/bugun - Bugungi vazifalar
/statistika - Progress
/motivatsiya - Ilhom
/help - Yordam

Tayyor bo'lsangiz, /bugun buyrug'i bilan boshlaymiz!

Alloh yo'lida omad! 💪
"""


def get_reja_message():
    """90 kunlik reja"""
    return """
📊 90 KUNLIK LIFE BALANCE REJASI

🗓 FAZA 1: Iymoniy asos (MAY - 30 kun)
✅ Har kuni 5 vaqt namoz
✅ 15 daqiqa Qur'on o'qish
✅ Instagram/Reels BUTUNLAY o'chirish
✅ 23:00 uyqu, 06:00 turish

🗓 FAZA 2: Hayot tartibga solish (IYUN - 30 kun)
✅ Uyqu tizimi barqaror
✅ Har kuni 30 daqiqa sport/yurish
✅ Ovqatlanish tartibga tushadi
✅ Maqsad: 8-10 kg tushirish

🗓 FAZA 3: Biznes qayta qurish (IYUL - 30 kun)
✅ Qarz strategiyasi: oyiga 15-20 mln
✅ Canary Group qayta tashkil
✅ Lead generation tizimi
✅ Haftasiga 3+ yangi client

💰 QARZ REJASI (120 mln):
May: 15 mln | Iyun: 20 mln | Iyul: 25 mln
Avgust: 25 mln | Sentyabr: 20 mln | Oktyabr: 15 mln

🎯 6 oyda qarz yopiladi!
"""


def get_bugun_message():
    """Bugungi vazifalar"""
    today = datetime.now(TIMEZONE).strftime('%d.%m.%Y')
    return f"""
📅 BUGUN: {today}

🌅 ERTALAB (06:00-10:30)
06:00 - Bomdod namozi
06:30 - 15 daq Qur'on
07:00 - Nonushta
07:30 - Deep Work (3 soat)

🌞 KUNDUZI (10:30-16:00)
10:30 - Peshin namozi
11:00 - Client meeting
13:00 - Tushlik
16:00 - Asr namozi

🌆 KECHQURUN (16:00-23:00)
16:30 - 30 daq sport
19:30 - Shom namozi
20:00 - Oila vaqti
21:30 - Xufton namozi
22:00 - Kitob (telefonsiz!)
23:00 - UYQU!

⚠️ Instagram/Reels MAN!
"""


def get_statistika_message():
    """Statistika"""
    return """
📊 PROGRESS

🕌 Namoz: __ / 5 (bugun)
😴 Uyqu: __ kun tartibda  
📱 Instagram: __ kun bo'sh
🏃 Sport: __ kun
⚖️ Vazn: __ kg
💰 Qarz: __ mln to'landi

Qo'lda hisoblab boring!
"""


def get_motivatsiya():
    """Tasodifiy motivatsiya"""
    import random
    messages = [
        "💪 Har kuni bitta qadam!",
        "🌅 Bomdod - kunning kaliti.",
        "📵 Instagram vaqtni o'g'irlaydi.",
        "🕌 Namoz - Alloh bilan aloqa.",
        "💼 Sifatli client - tinchlik.",
        "📖 Kitob - aql ozuqasi.",
        "😴 Erta uxlash - hikmat.",
        "🔥 Har kun - imtihon!",
        "🎯 90 kun tez o'tadi!",
    ]
    return random.choice(messages)


def get_help_message():
    """Yordam"""
    return """
📱 BOT BUYRUQLARI:

/start - Boshlash
/reja - 90 kunlik reja
/bugun - Bugungi vazifalar
/statistika - Progress
/motivatsiya - Ilhom
/help - Yordam

Omad! 💪
"""


def handle_message(message_text, first_name):
    """Xabarlarni qayta ishlash"""
    command = message_text.strip().lower()
    
    if command == '/start':
        return get_welcome_message(first_name)
    elif command == '/reja':
        return get_reja_message()
    elif command == '/bugun':
        return get_bugun_message()
    elif command == '/statistika':
        return get_statistika_message()
    elif command == '/motivatsiya':
        return get_motivatsiya()
    elif command == '/help':
        return get_help_message()
    else:
        return "Buyruqni tushunmadim. /help ni bosing."


def main():
    """Botni ishga tushirish"""
    import requests
    import time
    
    # Token tekshirish
    if TELEGRAM_BOT_TOKEN == "SIZNING_TOKENINGIZNI_BU_YERGA_QOYING":
        print("❌ XATO: Token sozlanmagan!")
        return
    
    BASE_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}"
    
    logger.info("✅ Bot ishga tushdi!")
    logger.info("📱 Telegram da /start ni bosing!")
    
    offset = 0
    
    while True:
        try:
            # Yangi xabarlarni olish
            response = requests.get(
                f"{BASE_URL}/getUpdates",
                params={'offset': offset, 'timeout': 30}
            )
            
            if response.status_code == 200:
                updates = response.json().get('result', [])
                
                for update in updates:
                    offset = update['update_id'] + 1
                    
                    if 'message' in update:
                        message = update['message']
                        chat_id = message['chat']['id']
                        first_name = message['from'].get('first_name', 'Foydalanuvchi')
                        text = message.get('text', '')
                        
                        # Javob tayyorlash
                        reply = handle_message(text, first_name)
                        
                        # Javob yuborish
                        requests.post(
                            f"{BASE_URL}/sendMessage",
                            json={'chat_id': chat_id, 'text': reply}
                        )
                        
                        logger.info(f"Xabar yuborildi: {chat_id}")
            
            time.sleep(1)
            
        except KeyboardInterrupt:
            logger.info("Bot to'xtatildi")
            break
        except Exception as e:
            logger.error(f"Xato: {e}")
            time.sleep(5)


if __name__ == '__main__':
    main()
