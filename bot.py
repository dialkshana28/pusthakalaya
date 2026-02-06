import telebot
from telebot import types
import os
from dotenv import load_dotenv

# ======================
# 1. BOT SETUP
# ======================
load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN', '7955194455:AAHjaIOt18YUFUZD5YmYzP57gNIcgH07lZA')  # REPLACE WITH YOUR ACTUAL TOKEN IF NOT USING .env

bot = telebot.TeleBot(BOT_TOKEN)

# ======================
# 2. FAQ DATABASE (Sinhala Library FAQs)
# ======================
faqs = {
    '1': {
        'question': 'පොත් ලබා ගැනීමේ ක්‍රියාවලිය කුමක්ද?',
        'answer': 'පොත් ලබා ගැනීම සඳහා:\n1. පාඨක ගිණුමක් සාදා ගන්න\n2. පුස්තකාල කාටලොග් එකෙන් පොත සොයන්න\n3. පොත රැකියා කරන්න හෝ සෘජුවම ලබා ගන්න\n4. ගෙවීම් ක්‍රියාවලිය සම්පූර්ණ කරන්න (අවශ්‍ය නම්)\n5. පොත එකතු කර ගන්න',
        'category': 'පොත් ලබා ගැනීම'
    },
    '2': {
        'question': 'ගෙවීම් ක්‍රම මොනවාද?',
        'answer': 'අපගේ පුස්තකාලය භාවිතා කරන ගෙවීම් ක්‍රම:\n• බැංකු මාරුව (Peoples Bank)\n• මොබයිල් මුදල් (Dialog, Hutch, Airtel)\n• කාඩ් ගෙවීම් (Visa/Mastercard)\n• පුස්තකාලයේ සෘජුවම මුදල් ගෙවීම',
        'category': 'ගෙවීම්'
    },
    '3': {
        'question': 'පොත් රැකියා කාලය කොපමණද?',
        'answer': 'සාමාන්‍ය පොත්: 14 දින\nවිශේෂ පොත්/සංචාරක පොත්: 7 දින\nඉලෙක්ට්‍රොනික පොත්: 21 දින\n\nකාලය ඉක්මවුණු විට දිනකට රු. 10 ක දඩ අය කෙරේ.',
        'category': 'පොත් රැකියාව'
    },
    '4': {
        'question': 'පොත් ආපසු ලබා දීමේ ප්‍රතිපත්තිය කුමක්ද?',
        'answer': 'පොත් ආපසු දීම සඳහා:\n• පොත් 14 දින ඇතුළත ආපසු ලබා දිය යුතුය\n• හානි සහිත පොත් සඳහා පූර්ණ මිල ගෙවිය යුතුය\n• නැති වූ පොත් සඳහා දෙගුණ මිල ගෙවිය යුතුය\n• ආපසු දීමේදී ඔබේ පාඨක කාඩ්පත ඉදිරිපත් කරන්න',
        'category': 'ප්‍රතිපත්ති'
    },
    '5': {
        'question': 'පාඨක ගිණුම සාදා ගන්නේ කෙසේද?',
        'answer': 'පාඨක ගිණුම සාදා ගැනීම සඳහා:\n1. පුස්තකාලයට පැමිණෙන්න හෝ අපගේ වෙබ් අඩවියෙන් අයදුම් කරන්න\n2. ජාතික හැඳුනුම්පත් අංකය සහිත ලියකියවිලි ඉදිරිපත් කරන්න\n3. පුද්ගලික විස්තර (නම, ලිපිනය, දුරකථන අංකය) ලබා දෙන්න\n4. රු. 200 ක ලියාපදිංචි ගාස්තුව ගෙවන්න\n5. ඔබේ පාඨක කාඩ්පත ලබා ගන්න',
        'category': 'ගිණුම්'
    },
    '6': {
        'question': 'පොත් සෙවීමේ ක්‍රම මොනවාද?',
        'answer': 'පොත් සෙවීම සඳහා ඔබට පහත ක්‍රම භාවිතා කළ හැක:\n• පොතේ නම ඇතුළත් කරන්න\n• කතෲනාමය ඇතුළත් කරන්න\n• විෂය ප්‍රභේදය තෝරන්න (විද්‍යාව, සාහිත්‍යය, ඉතිහාසය)\n• ISBN අංකය ඇතුළත් කරන්න\n• පුස්තකාල වෙබ් අඩවියේ සෙවුම් යන්ත්‍රය භාවිතා කරන්න',
        'category': 'පොත් සෙවීම'
    },
    '7': {
        'question': 'ඉලෙක්ට්‍රොනික පොත් (e-books) ලබා ගන්නේ කෙසේද?',
        'answer': 'ඉලෙක්ට්‍රොනික පොත් ලබා ගැනීම සඳහා:\n1. පාඨක ගිණුමක් සහිතව පුස්තකාල වෙබ් අඩවියට පිවිසෙන්න\n2. "ඉලෙක්ට්‍රොනික පුස්තකාලය" අංශය තෝරන්න\n3. අවශ්‍ය පොත තෝරා "බාගත කරන්න" ඔබන්න\n4. PDF හෝ EPUB ආකෘතියෙන් පොත බාගත කර ගන්න\n5. ඔබේ උපාංගයේ පොත කියවන්න',
        'category': 'ඉලෙක්ට්‍රොනික පුස්තකාලය'
    },
    '8': {
        'question': 'පුස්තකාල වේලාවන් කුමක්ද?',
        'answer': 'පුස්තකාල වේලාවන්:\nසඳුදා - සෙනසුරාදා: උදේ 8:30 - රාත්‍රී 8:00\nඉරිදා: උදේ 9:00 - පස්වරු 4:00\nසෙලසුම් දින: වසා ඇත\n\nවිශේෂ සටහන: රාජ්‍ය නිවාඩු දිනවල වේලාවන් වෙනස් විය හැකිය.',
        'category': 'පුස්තකාල වේලාවන්'
    }
}

# ======================
# 3. START COMMAND & MAIN MENU
# ======================
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton('📖 FAQ ප්‍රශ්න')
    btn2 = types.KeyboardButton('📚 පොත් සේවාවන්')
    btn3 = types.KeyboardButton('ℹ️ උදව්')
    btn4 = types.KeyboardButton('🏠 ප්‍රධාන මෙනුව')
    markup.add(btn1, btn2, btn3, btn4)
    
    welcome_text = '''
📚 *පුස්තකාල සහායක බොට්* වෙත සාදරයෙන් පිළිගනිමු!

මෙම බොට් ඔබට පුස්තකාල සේවා සම්බන්ධ උපකාර කරයි:

✅ පොත් ලබා ගැනීමේ ක්‍රියාවලිය
✅ ගෙවීම් ක්‍රම
✅ පොත් රැකියා කාලයන්
✅ පාඨක ගිණුම් සේවාවන්
✅ ඉලෙක්ට්‍රොනික පුස්තකාලය

ඔබට අවශ්‍ය සේවාව පහත මෙනුවෙන් තෝරන්න 👇
'''
    
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup, parse_mode='Markdown')

# ======================
# 4. FAQ CATEGORIES MENU
# ======================
@bot.message_handler(func=lambda message: message.text in ['📖 FAQ ප්‍රශ්න', '🏠 ප්‍රධාන මෙනුව'])
def show_faq_categories(message):
    # Group FAQs by category
    categories = {}
    for key, faq in faqs.items():
        cat = faq['category']
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(key)
    
    markup = types.InlineKeyboardMarkup(row_width=2)
    buttons = []
    
    # Create buttons for each category
    for category in sorted(categories.keys()):
        btn = types.InlineKeyboardButton(
            f'📁 {category}',
            callback_data=f'cat_{category}'
        )
        buttons.append(btn)
    
    # Arrange buttons in rows of 2
    for i in range(0, len(buttons), 2):
        if i+1 < len(buttons):
            markup.row(buttons[i], buttons[i+1])
        else:
            markup.row(buttons[i])
    
    markup.add(types.InlineKeyboardButton('🔙 ප්‍රධාන මෙනුවට', callback_data='back_main'))
    
    bot.send_message(
        message.chat.id, 
        'ඔබට අවශ්‍ය කාණ්ඩය තෝරන්න:',
        reply_markup=markup
    )

# ======================
# 5. SHOW QUESTIONS BY CATEGORY
# ======================
@bot.callback_query_handler(func=lambda call: call.data.startswith('cat_'))
def show_questions_by_category(call):
    category = call.data.replace('cat_', '')
    
    markup = types.InlineKeyboardMarkup(row_width=1)
    buttons = []
    
    # Get all FAQs in this category
    category_faqs = [(key, faq) for key, faq in faqs.items() if faq['category'] == category]
    
    for key, faq in category_faqs:
        btn = types.InlineKeyboardButton(
            f'❓ {faq["question"]}',
            callback_data=f'faq_{key}'
        )
        buttons.append(btn)
    
    # Add buttons to markup
    for btn in buttons:
        markup.row(btn)
    
    markup.add(types.InlineKeyboardButton('🔙 කාණ්ඩ ආපසු', callback_data='back_categories'))
    
    bot.edit_message_text(
        f'"{category}" කාණ්ඩයේ ප්‍රශ්න:', 
        call.message.chat.id, 
        call.message.message_id,
        reply_markup=markup
    )

# ======================
# 6. SHOW FAQ ANSWER WITH NAVIGATION
# ======================
@bot.callback_query_handler(func=lambda call: call.data.startswith('faq_'))
def show_faq_answer(call):
    faq_id = call.data.replace('faq_', '')
    
    if faq_id in faqs:
        faq = faqs[faq_id]
        faq_keys = list(faqs.keys())
        current_index = faq_keys.index(faq_id)
        
        # Navigation buttons
        prev_id = faq_keys[(current_index - 1) % len(faq_keys)]
        next_id = faq_keys[(current_index + 1) % len(faq_keys)]
        
        markup = types.InlineKeyboardMarkup(row_width=2)
        markup.row(
            types.InlineKeyboardButton('◀️ පෙර', callback_data=f'faq_{prev_id}'),
            types.InlineKeyboardButton('▶️ ඊළඟ', callback_data=f'faq_{next_id}')
        )
        markup.add(types.InlineKeyboardButton(f'🔙 {faq["category"]} කාණ්ඩය', callback_data=f'cat_{faq["category"]}'))
        markup.add(types.InlineKeyboardButton('🏠 ප්‍රධාන මෙනුව', callback_data='back_main'))
        
        answer_text = f'''
❓ *ප්‍රශ්නය:*
{faq["question"]}

📝 *පිළිතුර:*
{faq["answer"]}

🔖 *කාණ්ඩය:* {faq["category"]}
'''
        
        try:
            bot.edit_message_text(
                answer_text,
                call.message.chat.id,
                call.message.message_id,
                reply_markup=markup,
                parse_mode='Markdown'
            )
        except Exception as e:
            # Fallback if Markdown fails
            bot.edit_message_text(
                answer_text.replace('*', ''),
                call.message.chat.id,
                call.message.message_id,
                reply_markup=markup
            )
    else:
        bot.answer_callback_query(call.id, 'ප්‍රශ්නය හමු නොවීය!', show_alert=True)

# ======================
# 7. BACK BUTTON HANDLERS
# ======================
@bot.callback_query_handler(func=lambda call: call.data == 'back_categories')
def back_to_categories(call):
    # Group FAQs by category
    categories = {}
    for key, faq in faqs.items():
        cat = faq['category']
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(key)
    
    markup = types.InlineKeyboardMarkup(row_width=2)
    buttons = []
    
    for category in sorted(categories.keys()):
        btn = types.InlineKeyboardButton(
            f'📁 {category}',
            callback_data=f'cat_{category}'
        )
        buttons.append(btn)
    
    for i in range(0, len(buttons), 2):
        if i+1 < len(buttons):
            markup.row(buttons[i], buttons[i+1])
        else:
            markup.row(buttons[i])
    
    markup.add(types.InlineKeyboardButton('🔙 ප්‍රධාන මෙනුවට', callback_data='back_main'))
    
    bot.edit_message_text(
        'ඔබට අවශ්‍ය කාණ්ඩය තෝරන්න:',
        call.message.chat.id,
        call.message.message_id,
        reply_markup=markup
    )

@bot.callback_query_handler(func=lambda call: call.data == 'back_main')
def back_to_main(call):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton('📖 FAQ ප්‍රශ්න')
    btn2 = types.KeyboardButton('📚 පොත් සේවාවන්')
    btn3 = types.KeyboardButton('ℹ️ උදව්')
    btn4 = types.KeyboardButton('🏠 ප්‍රධාන මෙනුව')
    markup.add(btn1, btn2, btn3, btn4)
    
    bot.send_message(
        call.message.chat.id,
        'ප්‍රධාන මෙනුවට ආපසු ගියා! ඔබට අවශ්‍ය සේවාව තෝරන්න 👇',
        reply_markup=markup
    )

# ======================
# 8. LIBRARY SERVICES MENU
# ======================
@bot.message_handler(func=lambda message: message.text == '📚 පොත් සේවාවන්')
def library_services(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    services = [
        ('පොත් සෙවීම', 'search_books'),
        ('පොත් රැකියාව', 'book_reservation'),
        ('පොත් ආපසු දීම', 'return_books'),
        ('පාඨක ගිණුම', 'reader_account'),
        ('ඉලෙක්ට්‍රොනික පුස්තකාලය', 'e_library'),
        ('සම්බන්ධ කර ගන්න', 'contact_us')
    ]
    
    buttons = []
    for text, data in services:
        buttons.append(types.InlineKeyboardButton(text, callback_data=data))
    
    # Arrange in rows of 2
    for i in range(0, len(buttons), 2):
        if i+1 < len(buttons):
            markup.row(buttons[i], buttons[i+1])
        else:
            markup.row(buttons[i])
    
    markup.add(types.InlineKeyboardButton('🔙 ප්‍රධාන මෙනුව', callback_data='back_main'))
    
    bot.send_message(
        message.chat.id,
        'පොත් සේවා තෝරන්න:',
        reply_markup=markup
    )

# ======================
# 9. SERVICE HANDLERS
# ======================
@bot.callback_query_handler(func=lambda call: call.data in ['search_books', 'book_reservation', 'return_books', 'reader_account', 'e_library', 'contact_us'])
def handle_services(call):
    service_info = {
        'search_books': '''
🔎 *පොත් සෙවීම*

පොත් සෙවීම සඳහා:

1. පුස්තකාල වෙබ් අඩවිය බලන්න:
   🔗 https://pusthakalaya.lk/search

2. පුස්තකාල ඇප් එක භාවිතා කරන්න:
   📱 Android/iOS හි "Pusthakalaya" ඇප් එක බාගත කරන්න

3. පුස්තකාල කාටලොග් යන්ත්‍රය භාවිතා කරන්න
        ''',
        'book_reservation': '''
📅 *පොත් රැකියාව*

පොත් රැකියා කිරීම සඳහා:

1. පාඨක ගිණුමක් සහිතව පුස්තකාල වෙබ් අඩවියට පිවිසෙන්න
2. අවශ්‍ය පොත සොයා "රැකියා කරන්න" බොත්තම ඔබන්න
3. රැකියා කිරීමේ දිනය තහවුරු කරන්න
4. පොත ලබා ගැනීමට පුස්තකාලයට පැමිණෙන්න

⚠️ රැකියා කළ පොත් 3 දින ඇතුළත ලබා නොගත්හොත් රැකියාව අවලංගු වේ
        ''',
        'return_books': '''
↩️ *පොත් ආපසු දීම*

පොත් ආපසු දීම සඳහා:

1. පොත සමග ඔබේ පාඨක කාඩ්පත ගෙන එන්න
2. පුස්තකාල ගිවිසුම් කාවුළුවට පැමිණෙන්න
3. පොත භාණ්ඩාගාරිකයාට භාර දෙන්න
4. ගිවිසුම් කාඩ්පත ලබා ගන්න

📍 ලිපිනය: 123, පුස්තකාල මාර්ගය, කොළඹ 07
📞 දුරකථන: 011-2345678
        ''',
        'reader_account': '''
👤 *පාඨක ගිණුම*

පාඨක ගිණුම සාදා ගැනීම/නවීකරණය:

✅ ලියාපදිංචි වීම: රු. 200
✅ වාර්ෂික නවීකරණය: රු. 100
✅ අවශ්‍ය ලියකියවිලි:
   - ජා.හැ.ප. පිටපත
   - ලිපින සාක්ෂිය
   - ඡායාරූපය (පාස්පෝර්ට් ප්‍රමාණය)

පුස්තකාල කාර්යාලයට පැමිණ ඉහත ලියකියවිලි සමග අයදුම් කරන්න.
        ''',
        'e_library': '''
💻 *ඉලෙක්ට්‍රොනික පුස්තකාලය*

ඩිජිටල් පොත් සහ සම්පත් ලබා ගැනීම:

🌐 වෙබ් අඩවිය: https://pusthakalaya.lk/e-library
📱 ඇප් එක: "Pusthakalaya Digital" (Android/iOS)
📧 ලොගින් වීම: ඔබේ පාඨක ගිණුමේ ඊමේල් සහ මුරපදය

ඇතුළත් වන සම්පත්:
• 10,000+ ඉලෙක්ට්‍රොනික පොත්
• විද්‍යාත්මක ලිපි
• ශිෂ්‍යත්ව පත්‍රිකා
• ඓතිහාසික ලේඛන
        ''',
        'contact_us': '''
📞 *සම්බන්ධ කර ගන්න*

පුස්තකාල සම්බන්ධතා විස්තර:

🏢 ලිපිනය:
123, පුස්තකාල මාර්ගය
කොළඹ 07
ශ්‍රී ලංකාව

☎️ දුරකථන:
011-2345678 (ප්‍රධාන කාර්යාලය)
077-1234567 (ජංගම සහාය)

📧 ඊමේල්:
info@pusthakalaya.lk
support@pusthakalaya.lk

⏰ වේලාවන්:
සඳු-සෙන: 8:30 AM - 8:00 PM
ඉරිදා: 9:00 AM - 4:00 PM
        '''
    }
    
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('🔙 සේවා මෙනුව', callback_data='library_services'))
    markup.add(types.InlineKeyboardButton('🏠 ප්‍රධාන මෙනුව', callback_data='back_main'))
    
    bot.edit_message_text(
        service_info[call.data],
        call.message.chat.id,
        call.message.message_id,
        reply_markup=markup,
        parse_mode='Markdown'
    )

# Back to services menu
@bot.callback_query_handler(func=lambda call: call.data == 'library_services')
def back_to_services(call):
    markup = types.InlineKeyboardMarkup(row_width=2)
    services = [
        ('පොත් සෙවීම', 'search_books'),
        ('පොත් රැකියාව', 'book_reservation'),
        ('පොත් ආපසු දීම', 'return_books'),
        ('පාඨක ගිණුම', 'reader_account'),
        ('ඉලෙක්ට්‍රොනික පුස්තකාලය', 'e_library'),
        ('සම්බන්ධ කර ගන්න', 'contact_us')
    ]
    
    buttons = []
    for text, data in services:
        buttons.append(types.InlineKeyboardButton(text, callback_data=data))
    
    for i in range(0, len(buttons), 2):
        if i+1 < len(buttons):
            markup.row(buttons[i], buttons[i+1])
        else:
            markup.row(buttons[i])
    
    markup.add(types.InlineKeyboardButton('🔙 ප්‍රධාන මෙනුව', callback_data='back_main'))
    
    bot.edit_message_text(
        'පොත් සේවා තෝරන්න:',
        call.message.chat.id,
        call.message.message_id,
        reply_markup=markup
    )

# ======================
# 10. HELP COMMAND
# ======================
@bot.message_handler(func=lambda message: message.text == 'ℹ️ උදව්')
def send_help(message):
    help_text = '''
🆘 *උදව් මාර්ගෝපදේශ*

*ප්‍රධාන විධාන:*
• /start - බොට් ආරම්භ කිරීම
• මෙනු බොත්තම් භාවිතා කරන්න

*ප්‍රශ්න තෝරා ගැනීම:*
1️⃣ "📖 FAQ ප්‍රශ්න" බොත්තම ඔබන්න
2️⃣ කාණ්ඩයක් තෝරන්න (උදා: පොත් රැකියාව)
3️⃣ ප්‍රශ්නයක් තෝරන්න
4️⃣ පිළිතුර කියවන්න
5️⃣ "◀️ පෙර" / "▶️ ඊළඟ" භාවිතා කර අනෙකුත් ප්‍රශ්න බලන්න

*තාක්ෂණික ගැටළු:*
බොට් ගැටළු සඳහා අප හා සම්බන්ධ වන්න:
📧 support@pusthakalaya.lk
📱 @pusthakalaya_support (Telegram)

ඔබේ ප්‍රශ්නය මෙහි නොමැති නම්, කරුණාකර පුස්තකාල සේවාදායකයා සම්බන්ධ කර ගන්න.
    '''
    bot.send_message(message.chat.id, help_text, parse_mode='Markdown')

# ======================
# 11. HANDLE UNKNOWN MESSAGES
# ======================
@bot.message_handler(func=lambda message: True)
def handle_unknown(message):
    if message.text and not message.text.startswith('/'):
        bot.reply_to(message, 
            'මට ඒ තේරුම් ගත නොහැක. 😅\n\nකරුණාකර පහත මෙනු බොත්තම් භාවිතා කරන්න:\n• 📖 FAQ ප්‍රශ්න\n• 📚 පොත් සේවාවන්\n• ℹ️ උදව්\n• 🏠 ප්‍රධාන මෙනුව'
        )

# ======================
# 12. BOT STARTUP
# ======================
if __name__ == '__main__':
    print("✅ Pusthakalaya Assistant Bot started successfully!")
    print("⏰ Bot is running... Press Ctrl+C to stop")
    print("="*50)
    
    try:
        bot.polling(none_stop=True, interval=0, timeout=20)
    except Exception as e:
        print(f"❌ Error starting bot: {e}")
        print("💡 Make sure your BOT_TOKEN is correct in .env file or replace 'YOUR_BOT_TOKEN_HERE' in code")