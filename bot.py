import os
import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


MAIN_MENU = [
    ["🎮 ՄԵՆԱԿ ԽԱՂԱԼ", "⚔️ DUEL"],
    ["👥 ԽԱՂ ԸՆԿԵՐՆԵՐՈՎ", "🏆 ՕՐՎԱ ՄՐՑԱՇԱՐ"],
    ["🥇 LEADERBOARD", "🎁 ՕՐԱԿԱՆ ԲՈՆՈՒՍ"],
    ["👤 ԻՄ ՊՐՈՖԻԼԸ", "👥 ՀՐԱՎԻՐԵԼ ԸՆԿԵՐՆԵՐԻՆ"],
    ["ℹ️ ԿԱՆՈՆՆԵՐ"]
]


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        return

    keyboard = ReplyKeyboardMarkup(
        MAIN_MENU,
        resize_keyboard=True
    )

    await update.message.reply_text(
        "🎮 Բարի գալուստ QuizArena!\n\n"
        "🧠 Խաղա՛։ Մրցի՛ր։ Հաղթի՛ր։\n\n"
        "Ընտրիր խաղի ռեժիմը 👇",
        reply_markup=keyboard
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        return

    await update.message.reply_text(
        "📘 ՕԳՆՈՒԹՅՈՒՆ\n\n"
        "🎮 ՄԵՆԱԿ ԽԱՂԱԼ — խաղա միայնակ\n"
        "⚔️ DUEL — մրցիր ընկերոջդ դեմ\n"
        "👥 ԽԱՂ ԸՆԿԵՐՆԵՐՈՎ — խաղա մի քանի ընկերների հետ\n"
        "🏆 ՕՐՎԱ ՄՐՑԱՇԱՐ — մասնակցիր օրվա մրցմանը\n"
        "🥇 LEADERBOARD — տես առաջատարներին\n"
        "🎁 ՕՐԱԿԱՆ ԲՈՆՈՒՍ — ստացիր ամենօրյա բոնուս\n"
        "👤 ԻՄ ՊՐՈՖԻԼԸ — տես քո վիճակագրությունը\n"
        "👥 ՀՐԱՎԻՐԵԼ ԸՆԿԵՐՆԵՐԻՆ — հրավիրիր ընկերներիդ"
    )


async def menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message:
        return

    text = update.message.text

    if text == "🎮 ՄԵՆԱԿ ԽԱՂԱԼ":
        await update.message.reply_text(
            "🎮 ՄԵՆԱԿ ԽԱՂ\n\n"
            "🧠 Շուտով այստեղ կսկսվի քո առաջին հարցը։\n\n"
            "🔥 Պատրա՞ստ ես:"
        )

    elif text == "⚔️ DUEL":
        await update.message.reply_text(
            "⚔️ DUEL\n\n"
            "Շուտով կկարողանաս մարտահրավեր նետել ընկերոջդ։"
        )

    elif text == "👥 ԽԱՂ ԸՆԿԵՐՆԵՐՈՎ":
        await update.message.reply_text(
            "👥 ԽԱՂ ԸՆԿԵՐՆԵՐՈՎ\n\n"
            "Շուտով կկարողանաս ստեղծել խաղային սենյակ։"
        )

    elif text == "🏆 ՕՐՎԱ ՄՐՑԱՇԱՐ":
        await update.message.reply_text(
            "🏆 ՕՐՎԱ ՄՐՑԱՇԱՐ\n\n"
            "Մրցաշարը շուտով հասանելի կլինի։"
        )

    elif text == "🥇 LEADERBOARD":
        await update.message.reply_text(
            "🥇 LEADERBOARD\n\n"
            "Առաջատարների ցուցակը շուտով կհայտնվի այստեղ։"
        )

    elif text == "🎁 ՕՐԱԿԱՆ ԲՈՆՈՒՍ":
        await update.message.reply_text(
            "🎁 ՕՐԱԿԱՆ ԲՈՆՈՒՍ\n\n"
            "Շուտով կավելացնենք ամենօրյա բոնուսային համակարգը։"
        )

    elif text == "👤 ԻՄ ՊՐՈՖԻԼԸ":
        user = update.effective_user

        await update.message.reply_text(
            "👤 ԻՄ ՊՐՈՖԻԼԸ\n\n"
            f"👤 Անուն՝ {user.first_name}\n"
            f"🆔 ID՝ {user.id}\n\n"
            "⭐ Միավորներ՝ 0\n"
            "🎮 Խաղեր՝ 0\n"
            "🏆 Հաղթանակներ՝ 0"
        )

    elif text == "👥 ՀՐԱՎԻՐԵԼ ԸՆԿԵՐՆԵՐԻՆ":
        await update.message.reply_text(
            "👥 ՀՐԱՎԻՐԵԼ ԸՆԿԵՐՆԵՐԻՆ\n\n"
            "Շուտով այստեղ կլինի քո անձնական referral հղումը։"
        )

    elif text == "ℹ️ ԿԱՆՈՆՆԵՐ":
        await update.message.reply_text(
            "ℹ️ QUIZARENA — ԿԱՆՈՆՆԵՐ\n\n"
            "🧠 Պատասխանիր հարցերին և հավաքիր միավորներ։\n"
            "🔥 Որքան շատ ճիշտ պատասխաններ՝ այնքան բարձր դիրք։\n"
            "🏆 Հաղթիր մրցակիցներիդ և հայտնվիր Leaderboard-ում։"
        )


def main():
    if not TOKEN:
        raise ValueError("TELEGRAM_BOT_TOKEN-ը նշված չէ")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, menu_handler)
    )

    print("🎮 QuizArena Bot started!")

    app.run_polling()


if __name__ == "__main__":
    main()
