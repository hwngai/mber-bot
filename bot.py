import logging
import traceback
import html
import json

from telegram import (
    Update,
    User,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    BotCommand
)
from telegram.ext import (
    Application,
    ApplicationBuilder,
    CallbackContext,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters
)
from telegram.constants import ParseMode, ChatAction

import yaml

with open("/app/config.yml", 'r') as f:
    config_yaml = yaml.safe_load(f)

telegram_token = config_yaml["telegram_token"]

logger = logging.getLogger(__name__)
async def start_handle(update: Update, context: CallbackContext):
    user_name = update.message.from_user.first_name
    book_icon = "📚"
    magnifying_glass_icon = "🔍"
    gear_icon = "💌"
    intro_message = (
        f"{book_icon} Xin chào, *{user_name}*! Chào mừng bạn đến với **MBER Bot**!\n\n"
        "Tôi được tạo ra bởi `BaoTho` 👩‍💻 để giúp bạn tìm kiếm và khám phá sách một cách hiệu quả. "
        "Dưới đây là một số lệnh bạn có thể sử dụng:\n\n"
        f"{book_icon} /history - Sách về Lịch sử và Nhân vật Nổi tiếng\n"
        f"{book_icon} /leadership - Sách về Lãnh Đạo và Quản Trị\n"
        f"{book_icon} /development - Sách về Phát Triển Cá Nhân và Tư Duy\n"
        f"{book_icon} /skill - Sách về Kỹ Năng và Sự Nghiệp\n"
        f"{book_icon} /novel - Sách về Tiểu Thuyết và Truyện Ngắn\n"
        f"{book_icon} /technology - Sách về Khoa Học và Công Nghệ\n"
        f"{magnifying_glass_icon} /tophistory - Tìm kiếm hàng đầu về \"Lịch sử và Nhân vật Nổi tiếng\"\n" \
        f"{magnifying_glass_icon} /topleadership - Tìm kiếm hàng đầu về \"Lãnh Đạo và Quản Trị\"\n" \
        f"{magnifying_glass_icon} /topdevelopment - Tìm kiếm hàng đầu về \"Phát Triển Cá Nhân và Tư Duy\"\n" \
        f"{magnifying_glass_icon} /topskill - Tìm kiếm hàng đầu về \"Kỹ Năng và Sự Nghiệp\"\n" \
        f"{magnifying_glass_icon} /topnovel - Tìm kiếm hàng đầu về \"Tiểu Thuyết và Truyện Ngắn\"\n" \
        f"{magnifying_glass_icon} /toptechnology - Tìm kiếm hàng đầu về \"Khoa Học và Công Nghệ\"\n" \
        f"{gear_icon} /contact - Thông tin liên hệ để mượn sách\n\n" \
        "Hãy thoải mái khám phá và tận hưởng hành trình đọc sách của bạn! 📚"
    )
    await update.message.reply_text(intro_message, parse_mode=ParseMode.MARKDOWN)


async def help_handle(update: Update, context: CallbackContext):
    help_message = (
        "Dưới đây là các lệnh bạn có thể sử dụng:\n\n"
        "/history - Sách về Lịch sử và Nhân vật Nổi tiếng\n"
        "/leadership - Sách về Lãnh Đạo và Quản Trị\n"
        "/development - Sách về Phát Triển Cá Nhân và Tư Duy\n"
        "/skill - Sách về Kỹ Năng và Sự Nghiệp\n"
        "/novel - Sách về Tiểu Thuyết và Truyện Ngắn\n"
        "/technology - Sách về Khoa Học và Công Nghệ\n"
        "/tophistory - Tìm kiếm hàng đầu về \"Lịch sử và Nhân vật Nổi tiếng\"\n"
        "/topleadership - Tìm kiếm hàng đầu về \"Lãnh Đạo và Quản Trị\"\n"
        "/topdevelopment - Tìm kiếm hàng đầu về \"Phát Triển Cá Nhân và Tư Duy\"\n"
        "/topskill - Tìm kiếm hàng đầu về \"Kỹ Năng và Sự Nghiệp\"\n"
        "/topnovel - Tìm kiếm hàng đầu về \"Tiểu Thuyết và Truyện Ngắn\"\n"
        "/toptechnology - Tìm kiếm hàng đầu về \"Khoa Học và Công Nghệ\"\n"
        "/contact - Thông tin liên hệ để mượn sách\n\n"
        "Hãy thoải mái sử dụng các lệnh trên để khám phá thế giới sách của bạn! 📚🔍"
    )

    await update.message.reply_text(help_message, parse_mode=ParseMode.MARKDOWN)

async def error_handle(update: Update, context: CallbackContext) -> None:
    logger.error(msg="Exception while handling an update:", exc_info=context.error)

    # collect error message
    tb_list = traceback.format_exception(None, context.error, context.error.__traceback__)
    tb_string = "".join(tb_list)[:2000]
    update_str = update.to_dict() if isinstance(update, Update) else str(update)
    message = (
        f"An exception was raised while handling an update\n"
        f"<pre>update = {html.escape(json.dumps(update_str, indent=2, ensure_ascii=False))}"
        "</pre>\n\n"
        f"<pre>{html.escape(tb_string)}</pre>"
    )
    print(message)


async def history_handler(update: Update, context: CallbackContext):
    await update.message.reply_text("Chức năng Lịch sử và Nhân vật Nổi tiếng đang được phát triển và sẽ sớm ra mắt! 🚀")

async def leadership_handler(update: Update, context: CallbackContext):
    await update.message.reply_text("Chức năng Lãnh Đạo và Quản Trị đang được phát triển và sẽ sớm ra mắt! 🚀")

async def development_handler(update: Update, context: CallbackContext):
    await update.message.reply_text("Chức năng Phát Triển Cá Nhân và Tư Duy đang được phát triển và sẽ sớm ra mắt! 🚀")

async def skill_handler(update: Update, context: CallbackContext):
    await update.message.reply_text("Chức năng Kỹ Năng và Sự Nghiệp đang được phát triển và sẽ sớm ra mắt! 🚀")

async def novel_handler(update: Update, context: CallbackContext):
    await update.message.reply_text("Chức năng Tiểu Thuyết và Truyện Ngắn đang được phát triển và sẽ sớm ra mắt! 🚀")

async def technology_handler(update: Update, context: CallbackContext):
    await update.message.reply_text("Chức năng Khoa Học và Công Nghệ đang được phát triển và sẽ sớm ra mắt! 🚀")

async def top_history_handler(update: Update, context: CallbackContext):
    await update.message.reply_text("Chức năng Tìm kiếm hàng đầu về Lịch sử và Nhân vật Nổi tiếng đang được phát triển và sẽ sớm ra mắt! 🚀")

async def top_leadership_handler(update: Update, context: CallbackContext):
    await update.message.reply_text("Chức năng Tìm kiếm hàng đầu về Lãnh Đạo và Quản Trị đang được phát triển và sẽ sớm ra mắt! 🚀")

async def top_development_handler(update: Update, context: CallbackContext):
    await update.message.reply_text("Chức năng Tìm kiếm hàng đầu về Phát Triển Cá Nhân và Tư Duy đang được phát triển và sẽ sớm ra mắt! 🚀")

async def top_skill_handler(update: Update, context: CallbackContext):
    await update.message.reply_text("Chức năng Tìm kiếm hàng đầu về Kỹ Năng và Sự Nghiệp đang được phát triển và sẽ sớm ra mắt! 🚀")

async def top_novel_handler(update: Update, context: CallbackContext):
    await update.message.reply_text("Chức năng Tìm kiếm hàng đầu về Tiểu Thuyết và Truyện Ngắn đang được phát triển và sẽ sớm ra mắt! 🚀")

async def top_technology_handler(update: Update, context: CallbackContext):
    await update.message.reply_text("Chức năng Tìm kiếm hàng đầu về Khoa Học và Công Nghệ đang được phát triển và sẽ sớm ra mắt! 🚀")

async def contact_handler(update: Update, context: CallbackContext):
    await update.message.reply_text("Chức năng Thông tin liên hệ để mượn sách đang được phát triển và sẽ sớm ra mắt! 🚀")


async def post_init(application: Application):
    await application.bot.set_my_commands([
        BotCommand("/history", "Lịch sử và nhân vật nổi tiếng"),
        BotCommand("/leadership", "Lãnh Đạo và Quản Trị"),
        BotCommand("/development", "Phát Triển Cá Nhân và Tư Duy"),
        BotCommand("/skill", "Kỹ Năng và Sự Nghiệp"),
        BotCommand("/novel", "Tiểu Thuyết và Truyện Ngắn"),
        BotCommand("/technology", "Khoa Học và Công Nghệ"),
        BotCommand("/tophistory", "Top search \"Lịch sử và nhân vật nổi tiếng\""),
        BotCommand("/topleadership", "Top search \"Lãnh Đạo và Quản Trị\""),
        BotCommand("/topdevelopment", "Top search \"Phát Triển Cá Nhân và Tư Duy\""),
        BotCommand("/topskill", "Top search \"Kỹ Năng và Sự Nghiệp\""),
        BotCommand("/topnovel", "Top search \"Tiểu Thuyết và Truyện Ngắn\""),
        BotCommand("/toptechnology", "Top search \"Khoa Học và Công Nghệ\""),
        BotCommand("/contact", "Thông tin mượn sách"),
    ])


def run_bot() -> None:
    application = (
        ApplicationBuilder()
        .token(telegram_token)
        .concurrent_updates(True)
        .http_version("1.1")
        .get_updates_http_version("1.1")
        .post_init(post_init)
        .build()
    )

    # add handlers
    user_filter = filters.ALL

    application.add_handler(CommandHandler("start", start_handle, filters=user_filter))
    application.add_handler(CommandHandler("help", help_handle, filters=user_filter))

    history_handler_cmd = CommandHandler("history", history_handler, filters=user_filter)
    leadership_handler_cmd = CommandHandler("leadership", leadership_handler, filters=user_filter)
    development_handler_cmd = CommandHandler("development", development_handler, filters=user_filter)
    skill_handler_cmd = CommandHandler("skill", skill_handler, filters=user_filter)
    novel_handler_cmd = CommandHandler("novel", novel_handler, filters=user_filter)
    technology_handler_cmd = CommandHandler("technology", technology_handler, filters=user_filter)
    top_history_handler_cmd = CommandHandler("tophistory", top_history_handler, filters=user_filter)
    top_leadership_handler_cmd = CommandHandler("topleadership", top_leadership_handler, filters=user_filter)
    top_development_handler_cmd = CommandHandler("topdevelopment", top_development_handler, filters=user_filter)
    top_skill_handler_cmd = CommandHandler("topskill", top_skill_handler, filters=user_filter)
    top_novel_handler_cmd = CommandHandler("topnovel", top_novel_handler, filters=user_filter)
    top_technology_handler_cmd = CommandHandler("toptechnology", top_technology_handler, filters=user_filter)
    contact_handler_cmd = CommandHandler("contact", contact_handler, filters=user_filter)

    application.add_handler(history_handler_cmd)
    application.add_handler(leadership_handler_cmd)
    application.add_handler(development_handler_cmd)
    application.add_handler(skill_handler_cmd)
    application.add_handler(novel_handler_cmd)
    application.add_handler(technology_handler_cmd)
    application.add_handler(top_history_handler_cmd)
    application.add_handler(top_leadership_handler_cmd)
    application.add_handler(top_development_handler_cmd)
    application.add_handler(top_skill_handler_cmd)
    application.add_handler(top_novel_handler_cmd)
    application.add_handler(top_technology_handler_cmd)
    application.add_handler(contact_handler_cmd)

    application.add_error_handler(error_handle)

    application.run_polling()


if __name__ == "__main__":
    run_bot()