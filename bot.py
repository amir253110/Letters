"""
Aytilmagan xatlar — tiny launcher bot for the Telegram Mini App.

The bot only opens the Mini App. It never reads, stores or processes letters:
all user data lives inside the Mini App (Telegram CloudStorage / localStorage).

Requirements:  pip install "python-telegram-bot>=21,<23"
Run:           python bot.py
"""

import logging
import sys

from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    MenuButtonWebApp,
    Update,
    WebAppInfo,
)
from telegram.error import Conflict, InvalidToken
from telegram.ext import Application, CommandHandler, ContextTypes

# ---- Fill these two constants -------------------------------------------
TOKEN = "PUT_NEW_TOKEN_HERE"          # from @BotFather (use a fresh token)
WEBAPP_URL = "https://amir253110.github.io/Letters/"   # GitHub Pages address (NOT the .git link)
# -------------------------------------------------------------------------

BUTTON_TEXT = "💌 Ochish"

START_TEXT = (
    "Salom 🤍\n\n"
    "Bu — «Aytilmagan xatlar». Bu yerda aytilmay qolgan so'zlaringni "
    "yozishing, kayfiyatingni kuzatishing va o'zingga kichik g'amxo'rlik "
    "qilishing mumkin.\n\n"
    "Xatlaring faqat senga ko'rinadi. Tayyor bo'lganingda, pastdagi tugmani bos."
)

HELP_TEXT = (
    "Agar hozir juda og'ir bo'lsa, ishongan bir odamingga yoz yoki qo'ng'iroq qil. 🤍\n"
    "O'zingni xavfsiz his qilmasang — 103 (tez tibbiy yordam)."
)

logging.basicConfig(
    format="%(asctime)s %(levelname)s %(name)s: %(message)s", level=logging.INFO
)
# Keep HTTP request logs quiet (they would print the token-bearing URLs)
logging.getLogger("httpx").setLevel(logging.WARNING)
log = logging.getLogger("aytilmagan-xatlar")


def web_app_button() -> InlineKeyboardMarkup:
    """Inline keyboard with a single button that opens the Mini App."""
    return InlineKeyboardMarkup(
        [[InlineKeyboardButton(BUTTON_TEXT, web_app=WebAppInfo(url=WEBAPP_URL))]]
    )


async def post_init(app: Application) -> None:
    """Set the default chat menu button (bottom-left) to open the Mini App."""
    await app.bot.set_chat_menu_button(
        menu_button=MenuButtonWebApp(text=BUTTON_TEXT, web_app=WebAppInfo(url=WEBAPP_URL))
    )
    me = await app.bot.get_me()
    log.info("Bot @%s ishga tushdi. Mini App: %s", me.username, WEBAPP_URL)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """/start: warm greeting + button. Also pins the menu button for this chat."""
    await update.effective_message.reply_text(START_TEXT, reply_markup=web_app_button())
    try:
        await context.bot.set_chat_menu_button(
            chat_id=update.effective_chat.id,
            menu_button=MenuButtonWebApp(text=BUTTON_TEXT, web_app=WebAppInfo(url=WEBAPP_URL)),
        )
    except Exception as exc:  # menu button is a nice-to-have, never crash /start
        log.warning("Menu button not set for chat: %s", exc)


async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """/yordam: short static safety message (no data processing)."""
    await update.effective_message.reply_text(HELP_TEXT, reply_markup=web_app_button())


async def on_error(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Short, readable error messages instead of long tracebacks."""
    err = context.error
    if isinstance(err, Conflict):
        log.error(
            "Bot boshqa joyda ham ishlab turibdi (Conflict). Boshqa terminal/oynalarni yoping "
            "yoki BotFather'da tokenni Revoke qilib, yangisini qo'ying."
        )
        return
    log.error("Xato: %s", err, exc_info=err)


def main() -> None:
    if TOKEN == "8680136333:AAFL64FTCRWXIqM1oOHSL70ncKmQl9eYqsY" or not TOKEN.strip():
        sys.exit("TOKEN ni bot.py faylining boshida to'ldiring (BotFather'dan olingan yangi token).")
    if not WEBAPP_URL.startswith("https://") or WEBAPP_URL == "https://amir253110.github.io/Letters/":
        sys.exit("WEBAPP_URL ni to'ldiring: index.html joylashgan HTTPS manzil.")
    if "github.com/" in WEBAPP_URL or WEBAPP_URL.endswith(".git"):
        sys.exit("WEBAPP_URL repozitoriy havolasi bo'lmasligi kerak. "
                 "To'g'ri ko'rinish: https://NAME.github.io/REPO/")

    try:
        app = Application.builder().token(TOKEN).post_init(post_init).build()
    except InvalidToken:
        sys.exit("TOKEN noto'g'ri. BotFather'dan olingan tokenni to'liq nusxalang.")
    app.add_error_handler(on_error)
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler(["yordam", "help"], help_cmd))
    # drop_pending_updates: ignore old messages queued while the bot was off
    app.run_polling(allowed_updates=Update.ALL_TYPES, drop_pending_updates=True)


if __name__ == "__main__":
    main()
