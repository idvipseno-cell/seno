import os

# إعدادات البوت الرئيسية
# تم التعديل لضمان عدم توقف الـ Build في Railway إذا لم تكن المتغيرات موجودة بعد
MAIN_BOT_TOKEN = os.getenv("MAIN_BOT_TOKEN", "")
ADMIN_IDS_RAW = os.getenv("ADMIN_IDS", "0")
ADMIN_IDS = [int(id.strip()) for id in ADMIN_IDS_RAW.split(",") if id.strip().isdigit()]

# قناة الاشتراك الإجباري
REQUIRED_CHANNEL = os.getenv("REQUIRED_CHANNEL", "")

# --- قائمة التفاعلات ---
STANDARD_REACTIONS = ["👍", "❤️", "🔥", "🥰", "👏", "😁", "🤔", "🤯", "😱", "🎉", "🤩", "🙏", "👌", "🕊", "💯", "🤣", "⚡️", "🏆", "💎", "🍓", "🍾", "👀", "💪", "🙌", "🤝"]
PREMIUM_REACTIONS = ["👨‍💻", "🐳", "🤝", "😇", "🫡", "🤔", "🎯", "🏆", "💔", "🌚", "⚡️", "🍌", "🗿", "🆒", "🍓", "🍑", "🍾", "🍿", "🍕", "🍔", "🍟", "🍦", "🍩", "🍪", "🎂"]
ALL_REACTIONS = list(set(STANDARD_REACTIONS + PREMIUM_REACTIONS))

# إعدادات قاعدة البيانات
# استخدام مسار نسبي لضمان العمل في بيئات مختلفة مثل Railway
DB_PATH = os.getenv("DB_PATH", "bot_data.db")
