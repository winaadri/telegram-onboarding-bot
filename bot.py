from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    ChatJoinRequestHandler
)

# ⚠️ PEGA AQUÍ TU TOKEN (NO LO COMPARTAS)
BOT_TOKEN = "8288208060:AAFVRYFL2p-tYQlMgMRfSZ0Vv27v8aAv-3E"

# Enlaces
RECOMMENDED_CHANNEL_TENNIS = "https://t.me/+LbrDbhg_RHpkMmRh"
RECOMMENDED_CHANNEL_BASKET = "https://t.me/+GLiqr_Lc0QkxNTAx"
INSTAGRAM_LINK = "https://www.instagram.com/winaanalista?igsh=MWVicGo1dHEydjVreg=="

# Función para escapar caracteres especiales de MarkdownV2
# NO escapamos '*' para que la negrita funcione
def escape_md_v2_keep_bold(text: str) -> str:
    escape_chars = r'\_[]()~`>#+-=|{}.!'
    return ''.join(f'\\{c}' if c in escape_chars else c for c in text)

# Mensaje base (SIN Instagram)
RAW_WELCOME_MESSAGE = (
    "🚨 *GRACIAS POR TU SOLICITUD PARA SEGUIR A WINA (HAY MUCHAS SOLICITUDES)*\n\n"
    "Mientras tanto, te recomiendo que te unas a los canales de la familia\n\n"
    "🎾 *WINA TENIS:* 👉 {link_tennis}\n"
    "🏀 *WINA BASKET:* 👉 {link_basket}\n"
)

async def handle_join_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.chat_join_request.from_user

    # 1️⃣ Reemplazamos links normales
    message_with_links = RAW_WELCOME_MESSAGE.format(
        link_tennis=RECOMMENDED_CHANNEL_TENNIS,
        link_basket=RECOMMENDED_CHANNEL_BASKET
    )

    # 2️⃣ Escapamos TODO el texto
    escaped_message = escape_md_v2_keep_bold(message_with_links)

    # 3️⃣ Añadimos Instagram (NO se escapa)
    escaped_message += (
        "\n📸 *INSTAGRAM:* 👉 [CLICK AQUI]("
        + INSTAGRAM_LINK +
        ")\n\n"
        "\\(Canales gestionados por expertos en cada deporte\\)"
    )

    await context.bot.send_message(
        chat_id=user.id,
        text=escaped_message,
        parse_mode="MarkdownV2",
        disable_web_page_preview=True
    )

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(ChatJoinRequestHandler(handle_join_request))
    print("🤖 bienvenido_acceso_bot activo (sin aprobar solicitudes)...")
    app.run_polling()

if __name__ == "__main__":
    main()
