import telebot
import random

API_TOKEN = '8095394662:AAFy_zeP_P1ecxJiydknncRghTnJUIZH-q4'
bot = telebot.TeleBot(API_TOKEN)

cards = {
    "The Fool": {
        "meaning": "Awal baru, petualangan, kebebasan.",
        "narrative": "Kartu ini menggambarkan seseorang yang bersiap untuk memulai perjalanan baru. Mereka membawa sedikit barang dan tampak ceria, siap untuk menghadapi apa pun yang ada di depan.",
        "advice": "Ambil risiko dan jangan takut untuk mencoba hal baru. Ini saat yang tepat untuk memulai sesuatu yang baru."
    },
    "The Magician": {
        "meaning": "Kekuatan, keterampilan, kemampuan.",
        "narrative": "The Magician menggunakan semua alat yang ada untuk mencapai tujuannya. Ia memiliki semua yang diperlukan untuk sukses.",
        "advice": "Percayalah pada kemampuan Anda sendiri. Anda memiliki semua sumber daya yang diperlukan untuk mencapai impian Anda."
    },
    "The High Priestess": {
        "meaning": "Intuisi, rahasia, pengetahuan dalam.",
        "narrative": "Dia duduk di depan tirai, melambangkan pengetahuan yang tersembunyi dan keinginan untuk memahami diri sendiri.",
        "advice": "Percayalah pada insting Anda dan dengarkan suara batin Anda. Ini adalah saat yang tepat untuk refleksi."
    },
    "The Empress": {
        "meaning": "Kesuburan, kreativitas, ibu.",
        "narrative": "Kartu ini mencerminkan kekuatan feminin dan cinta. The Empress melambangkan pertumbuhan dan kreativitas.",
        "advice": "Jaga kesehatan dan kesejahteraan Anda. Luangkan waktu untuk merawat diri sendiri dan orang-orang terkasih."
    },
    "The Emperor": {
        "meaning": "Stabilitas, struktur, kekuatan.",
        "narrative": "The Emperor menunjukkan kekuatan dan stabilitas. Dia adalah pemimpin yang bijaksana.",
        "advice": "Ambil kendali atas situasi Anda. Gunakan kekuatan dan pengetahuan Anda untuk mencapai tujuan."
    },
    "The Hierophant": {
        "meaning": "Tradisi, spiritualitas, ajaran.",
        "narrative": "Kartu ini melambangkan kepercayaan dan ajaran. Ini adalah panggilan untuk mencari pengetahuan dari tradisi.",
        "advice": "Cari bimbingan dari orang-orang berpengalaman. Jangan ragu untuk mengikuti ajaran yang baik."
    },
    "The Lovers": {
        "meaning": "Cinta, harmoni, pilihan.",
        "narrative": "Kartu ini mencerminkan hubungan yang kuat dan pilihan penting dalam hidup.",
        "advice": "Dengarkan hati Anda dan buat pilihan yang mencerminkan nilai-nilai Anda."
    },
    "The Chariot": {
        "meaning": "Kendali, kekuatan, keberanian.",
        "narrative": "The Chariot melambangkan perjalanan dan kendali atas situasi.",
        "advice": "Kendalikan arah hidup Anda dan hadapi tantangan dengan percaya diri."
    },
    "Strength": {
        "meaning": "Kekuatan, keberanian, pengendalian diri.",
        "narrative": "Kartu ini menunjukkan kekuatan batin dan keberanian untuk menghadapi rintangan.",
        "advice": "Gunakan ketenangan dan pengendalian diri Anda untuk mengatasi tantangan."
    },
    "The Hermit": {
        "meaning": "Refleksi, pencarian, kebijaksanaan.",
        "narrative": "The Hermit menggambarkan perjalanan introspeksi dan pencarian kebenaran.",
        "advice": "Luangkan waktu untuk diri sendiri dan cari tahu apa yang benar-benar Anda inginkan."
    },
    "Wheel of Fortune": {
        "meaning": "Perubahan, siklus, takdir.",
        "narrative": "Kartu ini mencerminkan siklus kehidupan dan perubahan yang tak terduga.",
        "advice": "Terima perubahan dengan lapang dada. Ini adalah bagian dari perjalanan hidup."
    },
    "Justice": {
        "meaning": "Keadilan, kebenaran, keseimbangan.",
        "narrative": "Justice melambangkan pentingnya kebenaran dan keadilan dalam hidup.",
        "advice": "Bersikaplah jujur dan adil dalam keputusan Anda. Keseimbangan adalah kunci."
    },
    "The Hanged Man": {
        "meaning": "Pengorbanan, perspektif baru.",
        "narrative": "Kartu ini menunjukkan pentingnya melihat situasi dari sudut pandang yang berbeda.",
        "advice": "Terkadang, Anda perlu mengorbankan sesuatu untuk mendapatkan pemahaman yang lebih dalam."
    },
    "Death": {
        "meaning": "Akhir, transformasi, transisi.",
        "narrative": "Death melambangkan perubahan besar dan transformasi.",
        "advice": "Terima akhir sebagai bagian dari siklus kehidupan. Setiap akhir adalah awal baru."
    },
    "Temperance": {
        "meaning": "Keseimbangan, moderasi, harmoni.",
        "narrative": "Kartu ini menunjukkan pentingnya keseimbangan dan harmoni dalam hidup.",
        "advice": "Jaga keseimbangan antara berbagai aspek kehidupan Anda untuk mencapai kebahagiaan."
    },
    "The Devil": {
        "meaning": "Ketergantungan, batasan, materialisme.",
        "narrative": "Kartu ini mencerminkan ketergantungan dan batasan yang mungkin menghalangi kebebasan Anda.",
        "advice": "Identifikasi dan hadapi batasan dalam hidup Anda. Bebaskan diri dari yang mengekang."
    },
    "The Tower": {
        "meaning": "Kekacauan, perubahan mendasar.",
        "narrative": "The Tower menunjukkan perubahan mendasar yang mungkin sulit tetapi diperlukan.",
        "advice": "Terima kekacauan sebagai peluang untuk membangun kembali dengan lebih baik."
    },
    "The Star": {
        "meaning": "Harapan, inspirasi, ketenangan.",
        "narrative": "Kartu ini melambangkan harapan dan inspirasi di masa depan.",
        "advice": "Tetaplah optimis dan percaya bahwa yang terbaik akan datang."
    },
    "The Moon": {
        "meaning": "Ilusi, ketidakpastian, intuisi.",
        "narrative": "The Moon menunjukkan ketidakpastian dan pentingnya mendengarkan intuisi.",
        "advice": "Jangan biarkan ketidakpastian menakut-nakuti Anda. Dengarkan suara hati Anda."
    },
    "The Sun": {
        "meaning": "Kebahagiaan, kesuksesan, vitalitas.",
        "narrative": "Kartu ini menunjukkan kesuksesan dan kebahagiaan yang menyinari hidup Anda.",
        "advice": "Rayakan keberhasilan Anda dan nikmati momen kebahagiaan."
    },
    "Judgment": {
        "meaning": "Penilaian, kebangkitan, keputusan.",
        "narrative": "Kartu ini menunjukkan saat-saat refleksi dan penilaian atas tindakan masa lalu.",
        "advice": "Ambil waktu untuk mengevaluasi pilihan Anda dan bergerak maju dengan bijaksana."
    },
    "The World": {
        "meaning": "Pencapaian, kesuksesan, integrasi.",
        "narrative": "The World mencerminkan pencapaian dan kesuksesan dalam hidup.",
        "advice": "Rayakan pencapaian Anda dan gunakan pengalaman untuk tumbuh lebih jauh."
    },
    "Ace of Wands": {
        "meaning": "Awal baru, inspirasi, peluang.",
        "narrative": "Kartu ini melambangkan energi dan semangat baru untuk memulai proyek.",
        "advice": "Jangan ragu untuk mengejar impian Anda. Ini adalah waktu yang tepat untuk beraksi."
    },
    "Two of Wands": {
        "meaning": "Perencanaan, keputusan, potensi.",
        "narrative": "Kartu ini menunjukkan saat di mana Anda harus membuat keputusan penting.",
        "advice": "Tentukan tujuan Anda dan buat rencana untuk mencapainya."
    },
    "Three of Wands": {
        "meaning": "Ekspansi, foresight, pertumbuhan.",
        "narrative": "Kartu ini melambangkan pertumbuhan dan kemajuan yang signifikan.",
        "advice": "Jangan takut untuk mengambil langkah besar ke depan. Kesuksesan sudah dekat."
    },
    "Four of Wands": {
        "meaning": "Perayaan, stabilitas, keberhasilan.",
        "narrative": "Kartu ini menunjukkan waktu untuk merayakan pencapaian dan stabilitas.",
        "advice": "Rayakan momen ini dengan orang-orang terkasih Anda. Kebahagiaan ada di sekitar Anda."
    },
    "Five of Wands": {
        "meaning": "Persaingan, konflik, pertikaian.",
        "narrative": "Kartu ini mencerminkan tantangan dan persaingan dalam hidup.",
        "advice": "Hadapi tantangan ini dengan semangat dan cari cara untuk berkolaborasi."
    },
    "Six of Wands": {
        "meaning": "Kemenangan, pengakuan, keberhasilan.",
        "narrative": "Kartu ini melambangkan keberhasilan dan pengakuan atas usaha Anda.",
        "advice": "Rayakan kemenangan Anda, tetapi tetaplah rendah hati dan ingat untuk berterima kasih kepada yang mendukung Anda."
    },
    "Seven of Wands": {
        "meaning": "Pertahanan, keberanian, ketahanan.",
        "narrative": "Kartu ini menunjukkan perlunya mempertahankan posisi Anda.",
        "advice": "Jadilah berani dalam menghadapi tantangan. Pertahankan keyakinan Anda dan jangan menyerah."
    },
    "Eight of Wands": {
        "meaning": "Pergerakan cepat, komunikasi, berita.",
        "narrative": "Kartu ini mencerminkan kecepatan dan kemajuan yang cepat.",
        "advice": "Bersiaplah untuk perubahan cepat. Jadilah proaktif dan ambil langkah-langkah yang diperlukan."
    },
    "Nine of Wands": {
        "meaning": "Ketekunan, keberanian, ketahanan.",
        "narrative": "Kartu ini melambangkan ketahanan dan keberanian meskipun menghadapi rintangan.",
        "advice": "Tetaplah kuat dan teruskan meskipun menghadapi kesulitan. Anda hampir sampai."
    },
    "Ten of Wands": {
        "meaning": "Beban, tanggung jawab, tekanan.",
        "narrative": "Kartu ini mencerminkan beban yang berat dan tanggung jawab yang harus dipikul.",
        "advice": "Carilah cara untuk mengurangi beban Anda. Jangan ragu untuk meminta bantuan jika perlu."
    },
    "Page of Wands": {
        "meaning": "Antusiasme, eksplorasi, ide baru.",
        "narrative": "Kartu ini menunjukkan semangat dan rasa ingin tahu yang besar.",
        "advice": "Ikuti hasrat Anda dan jangan takut untuk menjelajahi ide-ide baru."
    },
    "Knight of Wands": {
        "meaning": "Energi, gairah, petualangan.",
        "narrative": "Kartu ini melambangkan semangat dan keberanian untuk mengejar petualangan.",
        "advice": "Ambil risiko dan berani untuk mengejar impian Anda dengan semangat."
    },
    "Queen of Wands": {
        "meaning": "Kreativitas, kepercayaan diri, kepemimpinan.",
        "narrative": "Kartu ini mencerminkan kekuatan feminin dan kreativitas yang kuat.",
        "advice": "Percayalah pada diri sendiri dan gunakan kreativitas Anda untuk memimpin dan menginspirasi."
    },
    "King of Wands": {
        "meaning": "Visi, kekuatan, kewirausahaan.",
        "narrative": "Kartu ini menunjukkan kepemimpinan dan kemampuan untuk melihat jauh ke depan.",
        "advice": "Ambil inisiatif dan gunakan visi Anda untuk menciptakan masa depan yang lebih baik."
    },
    "Ace of Cups": {
        "meaning": "Cinta baru, emosi, hubungan.",
        "narrative": "Kartu ini melambangkan awal baru dalam cinta dan hubungan.",
        "advice": "Terbukalah untuk cinta dan emosi baru. Ini adalah waktu untuk terhubung dengan orang lain."
    },
    "Two of Cups": {
        "meaning": "Koneksi, kemitraan, kesetiaan.",
        "narrative": "Kartu ini mencerminkan hubungan yang kuat dan saling mendukung.",
        "advice": "Hargai hubungan Anda dan berinvestasilah dalam komunikasi dan kerjasama."
    },
    "Three of Cups": {
        "meaning": "Perayaan, persahabatan, komunitas.",
        "narrative": "Kartu ini menunjukkan waktu untuk merayakan dengan teman-teman.",
        "advice": "Nikmati kebersamaan dengan orang-orang terkasih. Rayakan momen kebahagiaan."
    },
    "Four of Cups": {
        "meaning": "Refleksi, ketidakpuasan, keinginan.",
        "narrative": "Kartu ini mencerminkan ketidakpuasan dan perlunya refleksi.",
        "advice": "Luangkan waktu untuk merenung dan cari tahu apa yang benar-benar Anda inginkan."
    },
    "Five of Cups": {
        "meaning": "Kehilangan, penyesalan, harapan.",
        "narrative": "Kartu ini mencerminkan rasa kehilangan dan penyesalan.",
        "advice": "Meski ada kehilangan, tetaplah mencari harapan dan peluang baru."
    },
    "Six of Cups": {
        "meaning": "Nostalgia, kenangan, anak-anak.",
        "narrative": "Kartu ini mencerminkan kenangan indah dari masa lalu.",
        "advice": "Ingatlah momen indah dalam hidup Anda dan hargai pelajaran yang dipelajari."
    },
    "Seven of Cups": {
        "meaning": "Pilihan, imajinasi, ilusi.",
        "narrative": "Kartu ini menunjukkan banyak pilihan yang dapat membingungkan.",
        "advice": "Pilih dengan bijak dan jangan biarkan ilusi menghalangi jalan Anda."
    },
    "Eight of Cups": {
        "meaning": "Meninggalkan, pencarian, perubahan.",
        "narrative": "Kartu ini mencerminkan keputusan untuk meninggalkan sesuatu demi pencarian baru.",
        "advice": "Terkadang, meninggalkan yang lama adalah cara terbaik untuk menemukan apa yang Anda cari."
    },
    "Nine of Cups": {
        "meaning": "Kepuasan, kenyamanan, kebahagiaan.",
        "narrative": "Kartu ini menunjukkan pencapaian kebahagiaan dan kepuasan.",
        "advice": "Syukuri pencapaian Anda dan nikmati kebahagiaan yang ada."
    },
    "Ten of Cups": {
        "meaning": "Keluarga, kebahagiaan, harmoni.",
        "narrative": "Kartu ini mencerminkan kebahagiaan dan harmoni dalam hubungan keluarga.",
        "advice": "Hargai waktu bersama keluarga dan ciptakan kenangan indah bersama mereka."
    },
    "Page of Cups": {
        "meaning": "Kreativitas, perasaan, intuisi.",
        "narrative": "Kartu ini menunjukkan kemampuan untuk merasakan dan berimajinasi.",
        "advice": "Buka hati Anda untuk inspirasi dan biarkan kreativitas mengalir."
    },
    "Knight of Cups": {
        "meaning": "Romansa, idealisme, perasaan.",
        "narrative": "Kartu ini melambangkan romansa dan perasaan yang mendalam.",
        "advice": "Ikuti kata hati Anda dan jangan ragu untuk mengejar cinta."
    },
    "Queen of Cups": {
        "meaning": "Empati, kepekaan, intuisi.",
        "narrative": "Kartu ini mencerminkan kekuatan emosional dan kepekaan.",
        "advice": "Dengarkan suara hati Anda dan percayalah pada intuisi Anda."
    },
    "King of Cups": {
        "meaning": "Kemandirian, keseimbangan, kebijaksanaan.",
        "narrative": "Kartu ini menunjukkan kemampuan untuk mengendalikan emosi dengan bijaksana.",
        "advice": "Pertahankan keseimbangan antara emosi dan logika dalam pengambilan keputusan."
    },
    "Ace of Swords": {
        "meaning": "Kejelasan, kebenaran, keputusan.",
        "narrative": "Kartu ini melambangkan kejelasan dan kebenaran yang datang.",
        "advice": "Jadilah jujur pada diri sendiri dan orang lain. Keputusan yang baik datang dari kebenaran."
    },
    "Two of Swords": {
        "meaning": "Keputusan, kebuntuan, ketidakpastian.",
        "narrative": "Kartu ini mencerminkan keputusan sulit yang harus diambil.",
        "advice": "Ambil waktu untuk merenung dan cari cara untuk mengatasi kebuntuan ini."
    },
    "Three of Swords": {
        "meaning": "Kesedihan, kehilangan, penyesalan.",
        "narrative": "Kartu ini mencerminkan rasa sakit dan kesedihan yang dalam.",
        "advice": "Izinkan diri Anda untuk merasakan kesedihan dan ambil waktu untuk menyembuhkan."
    },
    "Four of Swords": {
        "meaning": "Istirahat, pemulihan, refleksi.",
        "narrative": "Kartu ini menunjukkan pentingnya istirahat dan pemulihan.",
        "advice": "Ambil waktu untuk merenung dan beristirahat. Ini saat yang tepat untuk memulihkan energi."
    },
    "Five of Swords": {
        "meaning": "Konflik, kekalahan, pengkhianatan.",
        "narrative": "Kartu ini mencerminkan konflik dan konsekuensi dari tindakan.",
        "advice": "Hindari konflik yang tidak perlu dan cobalah untuk menemukan jalan damai."
    },
    "Six of Swords": {
        "meaning": "Perpindahan, perjalanan, melepaskan.",
        "narrative": "Kartu ini menunjukkan transisi menuju tempat yang lebih baik.",
        "advice": "Biarkan masa lalu pergi dan berfokuslah pada masa depan yang lebih cerah."
    },
    "Seven of Swords": {
        "meaning": "Penipuan, ketidakjujuran, strategi.",
        "narrative": "Kartu ini mencerminkan tindakan yang tidak etis atau penipuan.",
        "advice": "Hati-hati dengan orang-orang di sekitar Anda. Kejujuran harus menjadi prioritas."
    },
    "Eight of Swords": {
        "meaning": "Keterjebakan, ketakutan, ketidakberdayaan.",
        "narrative": "Kartu ini menunjukkan perasaan terjebak dalam situasi sulit.",
        "advice": "Ketahuilah bahwa Anda memiliki kekuatan untuk keluar dari situasi ini. Carilah cara baru."
    },
    "Nine of Swords": {
        "meaning": "Kecemasan, ketakutan, mimpi buruk.",
        "narrative": "Kartu ini mencerminkan kecemasan dan ketakutan yang terus menghantui.",
        "advice": "Bicarakan kekhawatiran Anda dengan seseorang. Jangan biarkan ketakutan mengendalikan Anda."
    },
    "Ten of Swords": {
        "meaning": "Kekalahan, pengkhianatan, akhir.",
        "narrative": "Kartu ini menunjukkan akhir yang menyakitkan dari sebuah situasi.",
        "advice": "Walaupun terasa menyakitkan, ini adalah kesempatan untuk memulai kembali dan bangkit."
    },
    "Page of Swords": {
        "meaning": "Kecerdasan, observasi, keingintahuan.",
        "narrative": "Kartu ini melambangkan semangat keingintahuan dan analisis.",
        "advice": "Gunakan pikiran Anda untuk mencari kebenaran. Bertanyalah dan jangan ragu untuk belajar."
    },
    "Knight of Swords": {
        "meaning": "Kecepatan, tindakan, keberanian.",
        "narrative": "Kartu ini menunjukkan tindakan cepat dan semangat yang tinggi.",
        "advice": "Bertindaklah dengan cepat dan berani, tetapi juga pertimbangkan konsekuensinya."
    },
    "Queen of Swords": {
        "meaning": "Kejujuran, ketajaman, kebijaksanaan.",
        "narrative": "Kartu ini mencerminkan kekuatan dan kejujuran dalam pemikiran.",
        "advice": "Jadilah jujur dan gunakan kebijaksanaan Anda dalam mengambil keputusan."
    },
    "King of Swords": {
        "meaning": "Kepemimpinan, keadilan, intelektualitas.",
        "narrative": "Kartu ini menunjukkan kemampuan untuk memimpin dengan intelektualitas dan keadilan.",
        "advice": "Gunakan pikiran logis dan adil dalam situasi yang dihadapi."
    },
    "Ace of Pentacles": {
        "meaning": "Kesempatan, keuangan, stabilitas.",
        "narrative": "Kartu ini melambangkan peluang baru dalam hal keuangan dan material.",
        "advice": "Ambil kesempatan untuk membangun fondasi yang stabil dalam hidup Anda."
    },
    "Two of Pentacles": {
        "meaning": "Keseimbangan, multitasking, perubahan.",
        "narrative": "Kartu ini mencerminkan kemampuan untuk menyeimbangkan berbagai aspek hidup.",
        "advice": "Pertahankan keseimbangan dalam hidup Anda dan jangan ragu untuk beradaptasi."
    },
    "Three of Pentacles": {
        "meaning": "Kerjasama, kolaborasi, pencapaian.",
        "narrative": "Kartu ini menunjukkan pentingnya bekerja sama dengan orang lain.",
        "advice": "Bekerjalah dengan tim untuk mencapai tujuan bersama. Kolaborasi sangat penting."
    },
    "Four of Pentacles": {
        "meaning": "Kepemilikan, pengendalian, keserakahan.",
        "narrative": "Kartu ini menunjukkan keinginan untuk mempertahankan kekayaan dan keamanan.",
        "advice": "Hati-hati agar tidak terjebak dalam keserakahan. Ingatlah pentingnya berbagi."
    },
    "Five of Pentacles": {
        "meaning": "Kekurangan, kesulitan, pengabaian.",
        "narrative": "Kartu ini mencerminkan perasaan kekurangan dan kesulitan finansial.",
        "advice": "Jangan ragu untuk meminta bantuan. Ada dukungan di sekitar Anda."
    },
    "Six of Pentacles": {
        "meaning": "Kedermawanan, keseimbangan, berbagi.",
        "narrative": "Kartu ini menunjukkan pentingnya memberi dan menerima.",
        "advice": "Berbagi dengan orang lain akan membawa kebahagiaan. Jaga keseimbangan dalam memberi dan menerima."
    },
    "Seven of Pentacles": {
        "meaning": "Investasi, evaluasi, kesabaran.",
        "narrative": "Kartu ini mencerminkan waktu untuk mengevaluasi kemajuan dan hasil.",
        "advice": "Luangkan waktu untuk menilai investasi Anda dan bersabarlah. Hasil akan datang."
    },
    "Eight of Pentacles": {
        "meaning": "Kerja keras, dedikasi, keterampilan.",
        "narrative": "Kartu ini menunjukkan pentingnya kerja keras dan dedikasi.",
        "advice": "Terus tingkatkan keterampilan Anda. Kerja keras akan membuahkan hasil."
    },
    "Nine of Pentacles": {
        "meaning": "Kemandirian, pencapaian, kenyamanan.",
        "narrative": "Kartu ini mencerminkan pencapaian dan kenyamanan yang didapat dari kerja keras.",
        "advice": "Nikmati hasil kerja Anda. Hargai kemandirian dan pencapaian Anda."
    },
    "Ten of Pentacles": {
        "meaning": "Warisan, stabilitas, tradisi.",
        "narrative": "Kartu ini menunjukkan kekayaan yang diwariskan dan stabilitas keluarga.",
        "advice": "Hargai tradisi dan warisan yang telah Anda terima. Bangun fondasi untuk generasi mendatang."
    },
    "Page of Pentacles": {
        "meaning": "Peluang, belajar, ambisi.",
        "narrative": "Kartu ini menunjukkan semangat untuk belajar dan mengejar peluang.",
        "advice": "Manfaatkan peluang yang datang. Jadilah penasaran dan ambisius."
    },
    "Knight of Pentacles": {
        "meaning": "Tanggung jawab, ketekunan, stabilitas.",
        "narrative": "Kartu ini melambangkan tanggung jawab dan ketekunan dalam mencapai tujuan.",
        "advice": "Bekerjalah dengan tekun dan bertanggung jawab. Keberhasilan membutuhkan waktu."
    },
    "Queen of Pentacles": {
        "meaning": "Kepedulian, keamanan, praktis.",
        "narrative": "Kartu ini menunjukkan sifat praktis dan kepedulian terhadap orang lain.",
        "advice": "Gunakan kepraktisan Anda untuk menciptakan keamanan bagi diri sendiri dan orang lain."
    },
    "King of Pentacles": {
        "meaning": "Keberhasilan, kekuasaan, stabilitas.",
        "narrative": "Kartu ini mencerminkan keberhasilan dalam hal keuangan dan stabilitas.",
        "advice": "Gunakan keberhasilan Anda untuk memberikan dukungan kepada orang lain."
    }
}

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Selamat datang di Bot Tarot! Ketik /draw untuk menarik kartu tarot.")

@bot.message_handler(commands=['draw'])
def draw_card(message):
    card = random.choice(list(cards.keys()))
    card_info = cards[card]
    response = (
        f"Kartu yang Anda tarik: *{card}*\n\n"
        f"Makna: {card_info['meaning']}\n"
        f"Narasi: {card_info['narrative']}\n"
        f"Nasihat: {card_info['advice']}"
    )
    bot.send_message(message.chat.id, response, parse_mode='Markdown')

if __name__ == "__main__":
    bot.polling(none_stop=True)
