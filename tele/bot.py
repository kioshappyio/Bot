import telebot
from telebot import types
import time
import re

TOKEN = "6731784070:AAHNkNOWZJAV6oYKkpFCjXkOO4-Sh3IgcpQ"
CHANNEL_ID = "@sebuahsandaran"
bot = telebot.TeleBot(TOKEN)

# Fungsi untuk meng-escape karakter khusus untuk Markdown V2
def escape_markdown(text):
    return re.sub(r'([_*[\]()~`>#+\-=|{}.!])', r'\\\1', text)

# Pesan sambutan dengan pilihan curhat
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    markup = types.InlineKeyboardMarkup()
    tombol_kirim = types.InlineKeyboardButton("Mulai Curhat", callback_data="pilih_kirim")
    markup.add(tombol_kirim)

    bot.reply_to(
        message,
        "Halo! Selamat datang di **A Shoulder to Cry On**.\n\n"
        "Di sini Anda bisa mencurahkan perasaan dengan aman. Klik tombol di bawah untuk memulai curhat.",
        reply_markup=markup,
        parse_mode="Markdown"
    )

# Memilih apakah curhat anonim atau dengan nama
@bot.callback_query_handler(func=lambda call: call.data == "pilih_kirim")
def pilih_anonim(call):
    markup = types.InlineKeyboardMarkup()
    anonim_button = types.InlineKeyboardButton("Anonim 🕶️", callback_data="anonim")
    tidak_anonim_button = types.InlineKeyboardButton("Dengan Nama 📝", callback_data="tidak_anonim")
    markup.add(anonim_button, tidak_anonim_button)

    bot.send_message(
        call.message.chat.id,
        "Bagaimana Anda ingin mengirim pesan?\n\n"
        "🕶️ *Anonim* - Tidak ada yang tahu siapa Anda.\n"
        "📝 *Dengan Nama* - Pesan akan disertai nama Anda.",
        reply_markup=markup,
        parse_mode="Markdown"
    )

# Meminta pengguna mengetik pesan atau mengirim pesan suara
@bot.callback_query_handler(func=lambda call: call.data in ["anonim", "tidak_anonim"])
def pilih_pesan(call):
    status_anonim = call.data == "anonim"
    bot.send_message(call.message.chat.id, 
                     "Silakan kirim curahan hati Anda di bawah ini.\n\n"
                     "✨ Anda bebas menggunakan semua karakter, simbol, dan emoji!\n"
                     "Silakan kirim pesan teks atau pesan suara.")
    
    # Simpan status anonim dan minta pesan dari pengguna
    bot.register_next_step_handler(call.message, forward_to_channel, status_anonim)

# Meneruskan pesan ke Channel dengan format sesuai pilihan
def forward_to_channel(message, anonim):
    # Validasi pesan sebelum mengirim
    if message.text and not message.text.strip():
        bot.reply_to(message, "⚠️ Pesan tidak boleh kosong. Silakan ketik curahan hati Anda.")
        return

    attempts = 3  # Jumlah upaya untuk mengirim pesan
    for attempt in range(attempts):
        try:
            user_full_name = f"{message.from_user.first_name} {message.from_user.last_name or ''}".strip()
            if anonim:
                caption = f"🕶️ *Curahan Hati Anonim:*\n\n{escape_markdown(message.text or 'Pesan Suara')}"

                if message.voice:
                    # Kirim pesan suara ke Channel
                    bot.send_voice(CHANNEL_ID, message.voice.file_id, caption=caption, parse_mode="MarkdownV2")
                    bot.reply_to(message, "Terima kasih sudah berbagi. Pesan suara Anda telah dikirim ke channel.\n\n"
                                          "Jika Anda belum bergabung, silakan kunjungi: https://t.me/sebuahsandaran")
                    return
            else:
                caption = f"📝 *Curahan Hati dari {escape_markdown(user_full_name)}:*\n\n{escape_markdown(message.text or 'Pesan Suara')}"

                if message.voice:
                    # Kirim pesan suara ke Channel
                    bot.send_voice(CHANNEL_ID, message.voice.file_id, caption=caption, parse_mode="MarkdownV2")
                    bot.reply_to(message, "Terima kasih sudah berbagi. Pesan suara Anda telah dikirim ke channel.\n\n"
                                          "Jika Anda belum bergabung, silakan kunjungi: https://t.me/sebuahsandaran")
                    return

            # Kirim pesan teks ke Channel jika ada teks
            if message.text:
                if anonim:
                    bot.send_message(CHANNEL_ID, caption, parse_mode="MarkdownV2")
                else:
                    bot.send_message(CHANNEL_ID, caption, parse_mode="MarkdownV2")

                bot.reply_to(message, "Terima kasih sudah berbagi. Pesan Anda telah dikirim ke channel.\n\n"
                                      "Jika Anda belum bergabung, silakan kunjungi: https://t.me/sebuahsandaran")
                return  # Keluar dari fungsi jika berhasil mengirim
        except Exception as e:
            if attempt < attempts - 1:  # Cek jika ini bukan upaya terakhir
                time.sleep(2)  # Tunggu sebelum mencoba lagi
                continue  # Coba lagi
            else:
                bot.reply_to(message, f"Gagal mengirim pesan setelah beberapa percobaan: {str(e)}\n\n"
                                      "⚠️ Pastikan Anda tidak menggunakan karakter yang salah dan "
                                      "coba lagi. Semua karakter, simbol, dan emoji diizinkan!")

# Memulai bot
if __name__ == "__main__":
    bot.polling(none_stop=True)
