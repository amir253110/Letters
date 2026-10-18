💌 Aytilmagan xatlar
Yo'qotish yoki ajralishdan keyin o'zingga g'amxo'rlik qilish uchun shaxsiy kundalik. U Telegram Mini App ko'rinishida ishlaydi. Bu yerda:
hech qachon yuborilmaydigan xatlar yoziladi,
kayfiyat kuzatiladi,
har bir xatga iliq, qo'llab-quvvatlovchi javob beriladi.
Javoblarni neytral "hamroh" ovozi beradi. Ilova hech qachon yo'qotilgan odam nomidan gapirmaydi.
Fayllar
Fayl	Vazifasi
index.html	Mini App. Bitta fayl: HTML, CSS va JS ichida. Framework yoki build talab qilmaydi
bot.py	Mini Appni ochib beradigan kichik bot. Ma'lumotlarga tegmaydi
README.md	Shu qo'llanma
Maxfiylik haqida qisqacha
Backend, AI API va analitika yo'q. Javoblar telefonning o'zida, tayyor ro'yxatdan tanlanadi.
Saqlash joyi. Ma'lumotlar Telegram CloudStorage'da saqlanadi. U har bir foydalanuvchi va har bir bot uchun alohida, boshqalar ko'ra olmaydi. Zaxira nusxa qurilmaning localStorage'ida turadi.
Shifrlash. CloudStorage Telegram serverlarida turadi va oxirigacha shifrlanmagan.
PIN-kod ekranni begona ko'zdan yopadi, lekin ma'lumotni shifrlamaydi.
Bot bilan bog'liqlik. CloudStorage aynan shu botga bog'langan. Boshqa botga o'tsangiz, eski ma'lumotlar ko'rinmaydi. Shuning uchun avval Sozlamalar → Eksport qilib oling.
1. Botni yaratish (BotFather)
Telegram'da @BotFather (https://t.me/BotFather) ni oching va /newbot buyrug'ini yuboring.
Botga nom va username bering, masalan aytilmagan_xatlar_bot.
BotFather bergan tokenni hech kimga ko'rsatmang.
Agar eski token biror joyda ko'rinib qolgan bo'lsa, uni bekor qiling:
/mybots → botni tanlang → API Token → Revoke current token.
Yangi tokenni oling.
2. index.html ni joylashtirish (HTTPS shart)
A variant — GitHub Pages
github.com da yangi repozitoriy oching, masalan aytilmagan-xatlar.
Repozitoriy Public bo'lishi kerak.
Pullik rejada Private ham ishlaydi.
Add file → Upload files orqali index.html ni yuklang va Commit bosing.
Settings → Pages bo'limini oching:
Source: Deploy from a branch,
Branch: main va / (root),
Save bosing.
1–2 daqiqadan keyin manzil chiqadi, masalan:
https://USERNAME.github.io/aytilmagan-xatlar/
Shu manzilni brauzerda ochib ko'ring. Ilova Telegram'siz ham ishlaydi, faqat ma'lumot qurilmada saqlanadi.
B variant — Cloudflare Pages
dash.cloudflare.com → Workers & Pages → Create → Pages → Upload assets.
Loyihaga nom bering va index.html turgan papkani yuklang.
Deploy bosing. Manzil https://NOM.pages.dev ko'rinishida bo'ladi.
Har safar index.html ni yangilasangiz, uni qayta yuklang. Telegram eski versiyani keshda saqlashi mumkin, shuning uchun Mini Appni yopib, qayta oching.
3. Mini Appni botga ulash
Quyidagi yo'llardan birini yoki ikkalasini ishlating.
a) Menyu tugmasi (eng oddiy)
BotFather'da /setmenubutton buyrug'ini yuboring va botni tanlang.
2-bosqichdagi HTTPS manzilni yuboring.
Tugma matnini yuboring: 💌 Ochish.
b) To'liq Mini App (t.me/bot/app havolasi bilan)
BotFather'da /newapp buyrug'ini yuboring va botni tanlang.
Nom, qisqa tavsif va 640×360 rasm yuboring.
GIF so'ralsa, /empty deb yuborsangiz bo'ladi.
Mini App manzilini yuboring.
Qisqa nom bering, masalan xatlar.
Havola tayyor bo'ladi: https://t.me/BOT_USERNAME/xatlar.
bot.py ishga tushganda menyu tugmasini o'zi ham o'rnatadi.
4. bot.py ni kompyuterda ishga tushirish
Python 3.9 yoki undan yangi versiyani o'rnating (python.org).
Terminal (yoki Windows'da CMD) oching va kutubxonani o'rnating:
pip install "python-telegram-bot>=21,<23"
bot.py faylining boshidagi ikki qatorni to'ldiring:
TOKEN = "123456:ABC..."                                   # yangi token
WEBAPP_URL = "https://USERNAME.github.io/aytilmagan-xatlar/"
Botni ishga tushiring:
python bot.py
Telegram'da botga /start yuboring va 💌 Ochish tugmasini bosing.
Eslatmalar:
Bot faqat kompyuter yoniq va bot.py ishlab turgan paytda /start ga javob beradi.
Menyu tugmasi va t.me/... havolasi esa bot o'chiq bo'lsa ham Mini Appni ochaveradi.
5. Xavfsizlik bo'limi
"Yordam kerakmi?" tugmasi har doim yuqorida turadi. U quyidagilarni beradi:
yaqin odamga xabar yuborish (Telegram'ning o'z chat tanlash oynasi orqali, hech narsa avtomatik yuborilmaydi),
103 (tez tibbiy yordam) raqami.
Og'ir so'zlar aniqlansa, masalan "yashagim kelmayapti", hamroh javob o'rniga muloyim yordam kartasi chiqadi.
Kayfiyat uzoq og'ir bo'lsa, ya'ni oxirgi 7 kunning 5 tasida o'rtacha 2 yoki undan past bo'lsa, ishongan odam yoki psixolog bilan gaplashishni taklif qiluvchi karta chiqadi.
6. 👑 Princess bo'limi
Princess — quvnoq, kitobsevar do'st va yordamchi personaj. U sevgili emas.
Imkoniyatlari:
Suhbat. Yozish indikatori va tezkor javoblar bor: "Yaxshiman", "Charchadim", "Qiyin", "Kitob tavsiya qil".
Vaqtga bog'liq savollar. Ular faqat tab ochilganda chiqadi, bildirishnoma yuborilmaydi:
tong 6–10,
kun 12–15,
kech 17–20,
tun 21–24.
Javoblar saqlanadi. Har bir javob (kayfiyat va qayd) Kayfiyat va G'amxo'rlik ma'lumotlariga yoziladi. "So'nggi qaydlar" bo'limida ko'rinadi.
Kunlik ritual: bitta minnatdorlik va ertaga uchun bitta kichik maqsad. Ertasi kuni "bajardingmi?" deb so'raladi.
Kitob burchagi: kitob nomi, holati, qayd va sahifa. Princess kuniga bir marta "Qaysi sahifadasan?" deb so'raydi.
"Bugungi kunim": Princess kunini qanday o'tkazgani haqida 65 ta qisqa qator. Ketma-ket ikki kun bir xil qator chiqmaydi.
Javoblar soni: 150 dan ortiq o'zbekcha javob, kayfiyat va kalit so'zlar bo'yicha guruhlangan. Kalit so'zlar: dars, ovqat, uyqu, yolg'iz, charchoq, kitob.
Sozlamalar: ism (standart — "Princess"), savollarni yoqish yoki o'chirish, suhbatni tozalash.
Qat'iy qoidalar (kodda tekshiriladi):
Xavf so'zlari (masalan, "yashagim kelmayapti"):
oddiy suhbat to'xtaydi,
iliq javob beriladi,
yaqin odamga yozish va 103 tugmalari chiqadi,
"Yordam kerakmi?" oynasi ochiladi.
Romantik yoki bog'liqlik so'zlari: Princess mehribon, lekin aniq javob beradi: u do'st va yordamchi. Yaqin odamlarga yo'naltiradi.
Boshqa birov bo'lib gapirish so'ralsa, Princess rad etadi. Yo'qotilgan odamni hech qachon tilga olmaydi.
"Sevaman", rashk, janjal, "qayerda eding" kabi gaplar javoblar ro'yxatida umuman yo'q.
Ovqat yoki uyqu yo'qligi aytilsa, bitta kichik qadam taklif qilinadi.
5 kundan ortiq kayfiyat past bo'lsa, ishongan odam yoki psixolog bilan gaplashish taklif qilinadi (kuniga bir martadan ko'p emas).
Ochiqlik: birinchi xabarda Princess o'zi haqiqiy odam emasligini va mutaxassis o'rnini bosmasligini aytadi.
7. Texnik tafsilotlar
Saqlash kalitlari: letters, checks, settings, draft, princess (kitoblar, ritual), pchat (oxirgi 200 xabar).
Suhbat yozuvi: suhbat bulutga 1,2 soniya kechikish bilan yoziladi. Ilova yopilayotganda darhol yoziladi.
Bo'laklash: qiymat 3800 belgidan uzun bo'lsa, letters_0, letters_1, … bo'laklarga bo'linadi. Asosiy kalitda __chunks__:N:slot:uzunlik belgisi turadi.
Ikki slot: bo'laklar navbatma-navbat ikki slotga yoziladi (letters_0… va letters_b0…). Ko'rsatkich faqat yangi slot to'liq yozilgandan keyin almashadi. Shu sababli saqlash o'rtasida ilova yopilib qolsa ham, bulutdagi nusxa buzilmaydi.
Emoji xavfsizligi: emoji (surrogate juftligi) hech qachon ikkiga bo'linmaydi.
Sinxronlash: har bir hujjat {ts, data} ko'rinishida saqlanadi. Ochilganda bulut va qurilma nusxalaridan yangisi tanlanadi, eskisi yangilanadi.
Telegram'dan tashqarida (oddiy brauzerda) faqat localStorage ishlatiladi. U ham ishlamasa, xotirada (sahifa yopilguncha) saqlanadi.