
#t.me/lspwncvv
from telebot import types



def glawnaya():
    mm = types.ReplyKeyboardMarkup(resize_keyboard=True)

    button1 = types.KeyboardButton("⚡️ Накрутка")
    button2 = types.KeyboardButton("☘️ Администрация")
    button3 = types.KeyboardButton("🍩 Личный кабинет")
    mm.add(button1, button3)
    mm.add(button2)
    return mm



def nakrutka():
    nakr = types.ReplyKeyboardMarkup(resize_keyboard=True)
    otv1 = types.KeyboardButton("Instagram")
    otv2 = types.KeyboardButton("Telegram")
    otv3 = types.KeyboardButton("Facebook")
    otv4 = types.KeyboardButton("TikTok")
    otv5 = types.KeyboardButton("VK")
    otv6 = types.KeyboardButton("YouTube")
    otv7 = types.KeyboardButton("Одноклассники")
    otv8 = types.KeyboardButton("Яндекс.Дзен")
    otv9 = types.KeyboardButton("Steam")
    otv10 = types.KeyboardButton("На главную ↩️")

    nakr.add(otv1, otv2, otv5)
    nakr.add(otv4, otv6, otv9)
    nakr.add(otv3, otv7, otv8)
    nakr.add(otv10)
    return nakr



def profl():
    mm = types.ReplyKeyboardMarkup(resize_keyboard=True)

    button1 = types.KeyboardButton("💜 Моя статистика")
    button2 = types.KeyboardButton("💲 Пополнить")
    button3 = types.KeyboardButton("🌐 Общая статистика")
    button4 = types.KeyboardButton("🦎 Статистика за сегодня")
    otv13 = types.KeyboardButton("На главную ↩️")

    mm.add(button2, button1)
    mm.add(button4, button3)
    mm.add(otv13)
    return mm



def popol():
    otvet = types.InlineKeyboardMarkup(row_width=2)

    button1 = types.InlineKeyboardButton("💲 Пополнить", callback_data='good')

    otvet.add(button1)
    return otvet



def popol22():
    mm = types.ReplyKeyboardMarkup(resize_keyboard=True)

    msm1 = types.KeyboardButton("🥝 Киви")
    msm2 = types.KeyboardButton("💵 ЮMoney")
    msm4 = types.KeyboardButton("💶 PAYEER")

    msm6 = types.KeyboardButton("Назад в профиль ↩️")

    mm.add(msm1,msm2,msm4)
    mm.add(msm6)
    return mm



def opl():
    mm = types.ReplyKeyboardMarkup(resize_keyboard=True)

    msm1 = types.KeyboardButton("💎 Я оплатил")
    msm2 = types.KeyboardButton("❌ Отмена")

    mm.add(msm1)
    mm.add(msm2)
    return mm



def instn():
    mm = types.ReplyKeyboardMarkup(resize_keyboard=True)

    msm1 = types.KeyboardButton("👥 Подписчики (Inst)")
    msm2 = types.KeyboardButton("❤️ Лайки (Inst)")
    msm3 = types.KeyboardButton("💈 Просмотры (Inst)")
    msm4 = types.KeyboardButton("Назад (Inst) ↩️")

    mm.add(msm1, msm2, msm3)
    mm.add(msm4)
    return mm



def instnpdp():
    mm = types.ReplyKeyboardMarkup(resize_keyboard=True)

    msm1 = types.KeyboardButton("100 (7₽)")
    msm2 = types.KeyboardButton("1 000 (65₽)")
    msm3 = types.KeyboardButton("10 000 (600₽)")
    msm4 = types.KeyboardButton("Назад к выбору (Inst) ↩️")

    mm.add(msm1, msm2, msm3)
    mm.add(msm4)
    return mm



def instnlike():
    mm = types.ReplyKeyboardMarkup(resize_keyboard=True)

    msm1 = types.KeyboardButton("100 (2₽)")
    msm2 = types.KeyboardButton("1 000 (15₽)")
    msm3 = types.KeyboardButton("10 000 (100₽)")
    msm4 = types.KeyboardButton("Назад к выбору (Inst) ↩️")

    mm.add(msm1, msm2, msm3)
    mm.add(msm4)
    return mm



def instnvid():
    mm = types.ReplyKeyboardMarkup(resize_keyboard=True)

    msm1 = types.KeyboardButton("100 (4₽)")
    msm2 = types.KeyboardButton("1 000 (35₽)")
    msm3 = types.KeyboardButton("10 000 (300₽)")
    msm4 = types.KeyboardButton("Назад к выбору (Inst) ↩️")

    mm.add(msm1, msm2, msm3)
    mm.add(msm4)
    return mm



def tgglaw():
    mm = types.ReplyKeyboardMarkup(resize_keyboard=True)

    msm1 = types.KeyboardButton("👥 Подписчики канала (TG)")
    msm2 = types.KeyboardButton("🫂 Участники группы (TG)")
    msm3 = types.KeyboardButton("💈 Просмотры (TG)")
    msm4 = types.KeyboardButton("Назад (TG) ↩️")

    mm.add(msm1, msm2, msm3)
    mm.add(msm4)
    return mm



def tgpdpd():
    mm = types.ReplyKeyboardMarkup(resize_keyboard=True)

    msm1 = types.KeyboardButton("100 (22₽)")
    msm2 = types.KeyboardButton("1 000 (200₽)")
    msm3 = types.KeyboardButton("10 000 (1,800₽)")
    msm4 = types.KeyboardButton("Назад к выбору (TG) ↩️")

    mm.add(msm1, msm2, msm3)
    mm.add(msm4)
    return mm



def nggrpdpd():
    mm = types.ReplyKeyboardMarkup(resize_keyboard=True)

    msm1 = types.KeyboardButton("100 (22₽)")
    msm2 = types.KeyboardButton("1 000 (200₽)")
    msm3 = types.KeyboardButton("10 000 (1,800₽)")
    msm4 = types.KeyboardButton("Назад к выбору (TG) ↩️")

    mm.add(msm1, msm2, msm3)
    mm.add(msm4)
    return mm



def tgview():
    mm = types.ReplyKeyboardMarkup(resize_keyboard=True)

    msm1 = types.KeyboardButton("100 (3₽)")
    msm2 = types.KeyboardButton("1 000 (27₽)")
    msm3 = types.KeyboardButton("10 000 (250₽)")
    msm4 = types.KeyboardButton("Назад к выбору (TG) ↩️")

    mm.add(msm1, msm2, msm3)
    mm.add(msm4)
    return mm



def vkglaw():
    mm = types.ReplyKeyboardMarkup(resize_keyboard=True)

    msm1 = types.KeyboardButton("👥 Подписчики (VK)")
    msm2 = types.KeyboardButton("❤️ Лайки (VK)")
    msm3 = types.KeyboardButton("💈 Просмотры (VK)")
    msm4 = types.KeyboardButton("Назад (VK) ↩️")

    mm.add(msm1, msm2, msm3)
    mm.add(msm4)
    return mm



def vkpdp():
    mm = types.ReplyKeyboardMarkup(resize_keyboard=True)

    msm1 = types.KeyboardButton("100 (13₽)")
    msm2 = types.KeyboardButton("1 000 (100₽)")
    msm3 = types.KeyboardButton("10 000 (800₽)")
    msm4 = types.KeyboardButton("Назад к выбору (VK) ↩️")

    mm.add(msm1, msm2, msm3)
    mm.add(msm4)
    return mm



def vklike():
    mm = types.ReplyKeyboardMarkup(resize_keyboard=True)

    msm1 = types.KeyboardButton("100 (7₽)")
    msm2 = types.KeyboardButton("1 000 (65₽)")
    msm3 = types.KeyboardButton("10 000 (600₽)")
    msm4 = types.KeyboardButton("Назад к выбору (VK) ↩️")

    mm.add(msm1, msm2, msm3)
    mm.add(msm4)
    return mm



def vlview():
    mm = types.ReplyKeyboardMarkup(resize_keyboard=True)

    msm1 = types.KeyboardButton("100 (8₽)")
    msm2 = types.KeyboardButton("1 000 (75₽)")
    msm3 = types.KeyboardButton("10 000 (700₽)")
    msm4 = types.KeyboardButton("Назад к выбору (VK) ↩️")

    mm.add(msm1, msm2, msm3)
    mm.add(msm4)
    return mm



def ttglaw():
    mm = types.ReplyKeyboardMarkup(resize_keyboard=True)

    msm1 = types.KeyboardButton("👥 Подписчики (TT)")
    msm2 = types.KeyboardButton("❤️ Лайки (TT)")
    msm3 = types.KeyboardButton("💈 Просмотры (TT)")
    msm4 = types.KeyboardButton("Назад (TT) ↩️")

    mm.add(msm1, msm2, msm3)
    mm.add(msm4)
    return mm



def ttpdp():
    mm = types.ReplyKeyboardMarkup(resize_keyboard=True)

    msm1 = types.KeyboardButton("100 (4₽)")
    msm2 = types.KeyboardButton("1 000 (35₽)")
    msm3 = types.KeyboardButton("10 000 (300₽)")
    msm4 = types.KeyboardButton("Назад к выбору (TT) ↩️")

    mm.add(msm1, msm2, msm3)
    mm.add(msm4)
    return mm



def ttlike():
    mm = types.ReplyKeyboardMarkup(resize_keyboard=True)

    msm1 = types.KeyboardButton("100 (10₽)")
    msm2 = types.KeyboardButton("1 000 (95₽)")
    msm3 = types.KeyboardButton("10 000 (900₽)")
    msm4 = types.KeyboardButton("Назад к выбору (TT) ↩️")

    mm.add(msm1, msm2, msm3)
    mm.add(msm4)
    return mm



def ttview():
    mm = types.ReplyKeyboardMarkup(resize_keyboard=True)

    msm1 = types.KeyboardButton("100 (2₽)")
    msm2 = types.KeyboardButton("1 000 (15₽)")
    msm3 = types.KeyboardButton("10 000 (100₽)")
    msm4 = types.KeyboardButton("Назад к выбору (TT) ↩️")

    mm.add(msm1, msm2, msm3)
    mm.add(msm4)
    return mm



def ytglaw():
    mm = types.ReplyKeyboardMarkup(resize_keyboard=True)

    msm1 = types.KeyboardButton("👥 Подписчики (YT)")
    msm2 = types.KeyboardButton("❤️ Лайки (YT)")
    msm3 = types.KeyboardButton("💈 Просмотры (YT)")
    msm4 = types.KeyboardButton("Назад (YT) ↩️")

    mm.add(msm1, msm2, msm3)
    mm.add(msm4)
    return mm



def ytpdpd():
    mm = types.ReplyKeyboardMarkup(resize_keyboard=True)

    msm1 = types.KeyboardButton("100 (66₽)")
    msm2 = types.KeyboardButton("1 000 (600₽)")
    msm3 = types.KeyboardButton("10 000 (5,800₽)")
    msm4 = types.KeyboardButton("Назад к выбору (YT) ↩️")

    mm.add(msm1, msm2, msm3)
    mm.add(msm4)
    return mm



def ytlike():
    mm = types.ReplyKeyboardMarkup(resize_keyboard=True)

    msm1 = types.KeyboardButton("100 (10₽)")
    msm2 = types.KeyboardButton("1 000 (95₽)")
    msm3 = types.KeyboardButton("10 000 (900₽)")
    msm4 = types.KeyboardButton("Назад к выбору (YT) ↩️")

    mm.add(msm1, msm2, msm3)
    mm.add(msm4)
    return mm



def ytview():
    mm = types.ReplyKeyboardMarkup(resize_keyboard=True)

    msm1 = types.KeyboardButton("100 (14₽)")
    msm2 = types.KeyboardButton("1 000 (130₽)")
    msm3 = types.KeyboardButton("10 000 (1,200₽)")
    msm4 = types.KeyboardButton("Назад к выбору (YT) ↩️")

    mm.add(msm1, msm2, msm3)
    mm.add(msm4)
    return mm



def stimglaw():
    mm = types.ReplyKeyboardMarkup(resize_keyboard=True)

    msm1 = types.KeyboardButton("👥 Подписчики (Steam)")
    msm2 = types.KeyboardButton("📣 Отзывы (Steam)")
    msm4 = types.KeyboardButton("Назад (Steam) ↩️")

    mm.add(msm1, msm2)
    mm.add(msm4)
    return mm



def stimpdp():
    mm = types.ReplyKeyboardMarkup(resize_keyboard=True)

    msm1 = types.KeyboardButton("10 (65₽)")
    msm2 = types.KeyboardButton("100 (600₽)")
    msm3 = types.KeyboardButton("1 000 (5,800₽)")
    msm4 = types.KeyboardButton("Назад к выбору (Steam) ↩️")

    mm.add(msm1, msm2, msm3)
    mm.add(msm4)
    return mm



def stimotzv():
    mm = types.ReplyKeyboardMarkup(resize_keyboard=True)

    msm1 = types.KeyboardButton("10 (500₽)")
    msm2 = types.KeyboardButton("100 (450₽)")
    msm3 = types.KeyboardButton("1 000 (4,000₽)")
    msm4 = types.KeyboardButton("Назад к выбору (Steam) ↩️")

    mm.add(msm1, msm2, msm3)
    mm.add(msm4)
    return mm



def fbglaw():
    mm = types.ReplyKeyboardMarkup(resize_keyboard=True)

    msm1 = types.KeyboardButton("👥 Участники группы (FB)")
    msm2 = types.KeyboardButton("❤️ Лайки (FB)")
    msm3 = types.KeyboardButton("💈 Просмотры (FB)")
    msm4 = types.KeyboardButton("Назад (FB) ↩️")

    mm.add(msm1, msm2, msm3)
    mm.add(msm4)
    return mm



def fbpdpgr():
    mm = types.ReplyKeyboardMarkup(resize_keyboard=True)

    msm1 = types.KeyboardButton("100 (92₽)")
    msm2 = types.KeyboardButton("1 000 (890₽)")
    msm4 = types.KeyboardButton("Назад к выбору (FB) ↩️")

    mm.add(msm1, msm2)
    mm.add(msm4)
    return mm



def fblike():
    mm = types.ReplyKeyboardMarkup(resize_keyboard=True)

    msm1 = types.KeyboardButton("100 (68₽)")
    msm2 = types.KeyboardButton("1 000 (650₽)")
    msm3 = types.KeyboardButton("10 000 (6,000₽)")
    msm4 = types.KeyboardButton("Назад к выбору (FB) ↩️")

    mm.add(msm1, msm2, msm3)
    mm.add(msm4)
    return mm



def fbpros():
    mm = types.ReplyKeyboardMarkup(resize_keyboard=True)

    msm1 = types.KeyboardButton("100 (38₽)")
    msm2 = types.KeyboardButton("1 000 (350₽)")
    msm3 = types.KeyboardButton("10 000 (3,250₽)")
    msm4 = types.KeyboardButton("Назад к выбору (FB) ↩️")

    mm.add(msm1, msm2, msm3)
    mm.add(msm4)
    return mm



def okglaw():
    mm = types.ReplyKeyboardMarkup(resize_keyboard=True)

    msm1 = types.KeyboardButton("👥 Подписчики (OK)")
    msm2 = types.KeyboardButton("❤️ Лайки (OK)")
    msm3 = types.KeyboardButton("💈 Просмотры (OK)")
    msm4 = types.KeyboardButton("Назад (OK) ↩️")

    mm.add(msm1, msm2, msm3)
    mm.add(msm4)
    return mm



def okpdp():
    mm = types.ReplyKeyboardMarkup(resize_keyboard=True)

    msm1 = types.KeyboardButton("100 (38₽)")
    msm2 = types.KeyboardButton("1 000 (350₽)")
    msm3 = types.KeyboardButton("10 000 (3,250₽)")
    msm4 = types.KeyboardButton("Назад к выбору (OK) ↩️")

    mm.add(msm1, msm2, msm3)
    mm.add(msm4)
    return mm



def oklike():
    mm = types.ReplyKeyboardMarkup(resize_keyboard=True)

    msm1 = types.KeyboardButton("100 (20₽)")
    msm2 = types.KeyboardButton("1 000 (180₽)")
    msm3 = types.KeyboardButton("10 000 (1,500₽)")
    msm4 = types.KeyboardButton("Назад к выбору (OK) ↩️")

    mm.add(msm1, msm2, msm3)
    mm.add(msm4)
    return mm



def okview():
    mm = types.ReplyKeyboardMarkup(resize_keyboard=True)

    msm1 = types.KeyboardButton("100 (12₽)")
    msm2 = types.KeyboardButton("1 000 (100₽)")
    msm3 = types.KeyboardButton("10 000 (900₽)")
    msm4 = types.KeyboardButton("Назад к выбору (OK) ↩️")

    mm.add(msm1, msm2, msm3)
    mm.add(msm4)
    return mm



def yadglaw():
    mm = types.ReplyKeyboardMarkup(resize_keyboard=True)

    msm1 = types.KeyboardButton("👥 Подписчики (Я.Д)")
    msm2 = types.KeyboardButton("❤️ Лайки (Я.Д)")
    msm3 = types.KeyboardButton("💈 Просмотры (Я.Д)")
    msm4 = types.KeyboardButton("Назад (Я.Д) ↩️")

    mm.add(msm1, msm2, msm3)
    mm.add(msm4)
    return mm



def yadpdp():
    mm = types.ReplyKeyboardMarkup(resize_keyboard=True)

    msm1 = types.KeyboardButton("100 (80₽)")
    msm2 = types.KeyboardButton("1 000 (750₽)")
    msm3 = types.KeyboardButton("10 000 (7,000₽)")
    msm4 = types.KeyboardButton("Назад к выбору (Я.Д) ↩️")

    mm.add(msm1, msm2, msm3)
    mm.add(msm4)
    return mm



def yadlike():
    mm = types.ReplyKeyboardMarkup(resize_keyboard=True)

    msm1 = types.KeyboardButton("100 (80₽)")
    msm2 = types.KeyboardButton("1 000 (750₽)")
    msm3 = types.KeyboardButton("10 000 (7,000₽)")
    msm4 = types.KeyboardButton("Назад к выбору (Я.Д) ↩️")

    mm.add(msm1, msm2, msm3)
    mm.add(msm4)
    return mm



def yadview():
    mm = types.ReplyKeyboardMarkup(resize_keyboard=True)

    msm1 = types.KeyboardButton("100 (16₽)")
    msm2 = types.KeyboardButton("1 000 (140₽)")
    msm3 = types.KeyboardButton("10 000 (1,200₽)")
    msm4 = types.KeyboardButton("Назад к выбору (Я.Д) ↩️")

    mm.add(msm1, msm2, msm3)
    mm.add(msm4)
    return mm


