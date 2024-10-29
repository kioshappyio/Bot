import telebot
import io

# Inisialisasi bot dengan token kamu
bot = telebot.TeleBot("7828687831:AAE-_vEmVVbHQWrqKejYnP0Ba3_1mqzTlNE")

# ID channel atau grup (ganti sesuai kebutuhan)
GROUP_ID = -1002461819274

# Fungsi menangani komentar anonim (teks dan pesan suara)
@bot.message_handler(func=lambda message: message.reply_to_message and message.chat.id == GROUP_ID)
def anonymize_reply(message):
    try:
        if message.text or message.caption:  # Jika komentar berupa teks atau caption
            content = message.text or message.caption or "(pesan kosong)"
            
            # Hapus pesan asli dan kirim ulang secara anonim
            bot.delete_message(message.chat.id, message.message_id)
            bot.send_message(
                GROUP_ID,
                f"💬 *Komentar Anonim:*\n\n{content}",
                parse_mode='Markdown',
                reply_to_message_id=message.reply_to_message.message_id
            )

        elif message.voice:  # Jika komentar berupa pesan suara
            # Mendapatkan informasi file
            file_info = bot.get_file(message.voice.file_id)
            downloaded_file = bot.download_file(file_info.file_path)

            # Simpan file suara dalam buffer
            voice_buffer = io.BytesIO(downloaded_file)
            voice_buffer.name = "anon_voice.ogg"

            # Hapus pesan asli
            bot.delete_message(message.chat.id, message.message_id)

            # Kirim ulang pesan suara secara anonim
            bot.send_voice(
                GROUP_ID,
                voice=voice_buffer,
                caption="💬 *Komentar Anonim (Pesan Suara)*",
                parse_mode='Markdown',
                reply_to_message_id=message.reply_to_message.message_id
            )
    except Exception as e:
        print(f"Error: {e}")

# Jalankan bot
print("Bot berjalan...")
bot.infinity_polling()
