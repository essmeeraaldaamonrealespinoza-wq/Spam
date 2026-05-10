# MAFIACHODGNG _bot_multi.py
import asyncio, json, os, random, time
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
import logging

# ---------------------------
# CONFIG
# ---------------------------
TOKENS = [
    "8665961675:AAFtWZLn_DNTXB_n6H4muWF0jE8GbUfZQks",
"8716714960:AAEbsfjpFkzi3VKB4CdNir_0WbaiJNrqfEA",
"7426291434:AAEyxaXfF09vHW_ruxRkJ032HpIq-w2Gm9g",
"8216116259:AAFW0e_nfoPoFsXjrZXfBzAuB133oAQBXxE",
"8520424721:AAF5Ji9woUyHuk0yyxfKSuaYs-bEzbXDAnE",
"8625249508:AAEhXbfjzaCyBqjo9VjZLIu2B2DATi938wg",
"8717916149:AAHgcHV_lDJMta3QOWHGsREd0QG5n4XEQxs",
"8690727515:AAHn2sfz198s-ZUdIIKARcn5Ymsd8yT8RhA",
]

OWNER_ID = 7731577454
SUDO_FILE = "sudo.json"

# ---------------------------
# TEXT LISTS
# ---------------------------
RAID_TEXTS = ["RNDִֶָ𓂃 ࣪˖ ִֶָ👑་༘࿐","NICHI JAATִֶָ𓂃 ࣪˖ ִֶָ👑་༘࿐","HAKLEִֶָ𓂃 ࣪˖ ִֶָ👑་༘࿐","TMKCִֶָ𓂃 ࣪˖ ִֶָ👑་༘࿐","BAUNEִֶָ𓂃 ࣪˖ ִֶָ👑་༘࿐","BITCHִֶָ𓂃 ࣪˖ ִֶָ👑་༘࿐","CHUDִֶָ𓂃 ࣪˖ ִֶָ👑་༘࿐","TMKBִֶָ𓂃 ࣪˖ ִֶָ👑་༘࿐","KAMZORִֶָ𓂃 ࣪˖ ִֶָ👑་༘࿐","TATTI KHAִֶָ𓂃 ࣪˖ ִֶָ👑་༘࿐","CHINNALִֶָ𓂃 ࣪˖ ִֶָ👑་༘࿐","MOTEִֶָ𓂃 ࣪˖ ִֶָ👑་༘࿐","GAREEBִֶָ𓂃 ࣪˖ ִֶָ👑་༘࿐","HIJDEִֶָ𓂃 ࣪˖ ִֶָ👑་༘࿐","LAND LEִֶָ𓂃 ࣪˖ ִֶָ👑་༘࿐","TERI MA RNDIִֶָ𓂃 ࣪˖ ִֶָ👑་༘࿐","CVR KRִֶָ𓂃 ࣪˖ ִֶָ👑་༘࿐","MAR MATִֶָ𓂃 ࣪˖ ִֶָ👑་༘࿐","BHAGAִֶָ𓂃 ࣪˖ ִֶָ👑་༘࿐","KIDEEִֶָ𓂃 ࣪˖ ִֶָ👑་༘࿐","ANDHE LODEִֶָ𓂃 ࣪˖ ִֶָ👑་༘࿐",]
NCEMO_EMOJIS = ["🎐𓍼ֶָ֢⊹ ࣪ ˖","💋𓍼ֶָ֢⊹ ࣪ ˖","✨𓍼ֶָ֢⊹ ࣪ ˖","🍂𓍼ֶָ֢⊹ ࣪ ˖","🍀𓍼ֶָ֢⊹ ࣪ ˖","🪐𓍼ֶָ֢⊹ ࣪ ˖","〽️𓍼ֶָ֢⊹ ࣪ ˖","✴️𓍼ֶָ֢⊹ ࣪ ˖","💠𓍼ֶָ֢⊹ ࣪ ˖","🥀𓍼ֶָ֢⊹ ࣪ ˖","❄️𓍼ֶָ֢⊹ ࣪ ˖","🎗️𓍼ֶָ֢⊹ ࣪ ˖","🎏𓍼ֶָ֢⊹ ࣪ ˖","🪢𓍼ֶָ֢⊹ ࣪ ˖","🐚𓍼ֶָ֢⊹ ࣪ ˖","🫧𓍼ֶָ֢⊹ ࣪ ˖","🦋𓍼ֶָ֢⊹ ࣪ ˖","🪅𓍼ֶָ֢⊹ ࣪ ˖","📍𓍼ֶָ֢⊹ ࣪ ˖","🪄𓍼ֶָ֢⊹ ࣪ ˖","🧸𓍼ֶָ֢⊹ ࣪ ˖","🎋𓍼ֶָ֢⊹ ࣪ ˖"]
HEART_EMOJIS = ["𓆩🩶𓆪","𓆩🩵𓆪","𓆩🩷𓆪","𓆩🤍𓆪","𓆩🖤𓆪","𓆩🤎𓆪","𓆩💜𓆪","𓆩💙𓆪","𓆩💚𓆪","𓆩💛𓆪","𓆩🧡𓆪","𓆩❤️𓆪","𓆩♥️𓆪","𓆩❤️‍🩹𓆪","𓆩💔𓆪","𓆩💝𓆪","𓆩💖𓆪"]
ANIMAL_EMOJIS = ["ˏˋ°•*⁀➷🐶", "ˏˋ°•*⁀➷🐱", "ˏˋ°•*⁀➷🐭", "ˏˋ°•*⁀➷🐹", "ˏˋ°•*⁀➷🐰", "ˏˋ°•*⁀➷🦊", "ˏˋ°•*⁀➷🐻", "ˏˋ°•*⁀➷🐼", "ˏˋ°•*⁀➷🐨", "ˏˋ°•*⁀➷🐯", "ˏˋ°•*⁀➷🦁", "ˏˋ°•*⁀➷🐮", "ˏˋ°•*⁀➷🐷", "ˏˋ°•*⁀➷🐸", "ˏˋ°•*⁀➷🐵", "ˏˋ°•*⁀➷🐔", "ˏˋ°•*⁀➷🐧", "ˏˋ°•*⁀➷🐦", "ˏˋ°•*⁀➷🐤", "ˏˋ°•*⁀➷🦆", "ˏˋ°•*⁀➷🦅", "ˏˋ°•*⁀➷🦉", "ˏˋ°•*⁀➷🦇", "ˏˋ°•*⁀➷🐽", "ˏˋ°•*⁀➷🐗", "ˏˋ°•*⁀➷🐎", "ˏˋ°•*⁀➷🦄", "ˏˋ°•*⁀➷🐝", "ˏˋ°•*⁀➷🪱", "ˏˋ°•*⁀➷🐛", "ˏˋ°•*⁀➷🦋", "ˏˋ°•*⁀➷🐌", "ˏˋ°•*⁀➷🐞"]
MASK_EMOJIS = ["𓂃😉𓂃","𓂃😗𓂃","𓂃😙𓂃 ","𓂃😚𓂃 ","𓂃😘𓂃 ","𓂃🥰𓂃 ","𓂃😍𓂃 ","𓂃😋𓂃 ","𓂃😻𓂃 ","𓂃😽𓂃 ","𓂃😛𓂃 ","𓂃🙈𓂃 "]
CHOCO_EMOJIS = ["𝘛𝘈𝘛𝘛𝘌💝𓂃 ࣪˖ ִֶཐི༏ཋྀ","𝘙𝘕𝘋 💝𓂃 ࣪˖ ִֶཐི༏ཋྀ","𝘛𝘔𝘒𝘉💝𓂃 ࣪˖ ִֶཐི༏ཋྀ","𝘓𝘈𝘕𝘋 𝘓𝘌💝𓂃 ࣪˖ ִֶཐི༏ཋྀ","𝘊𝘏𝘜𝘋 💝𓂃 ࣪˖ ִֶཐི༏ཋྀ","𝘊𝘏𝘐𝘕𝘕𝘈𝘙💝𓂃 ࣪˖ ִֶཐི༏ཋྀ","𝘔𝘈 𝘊𝘏𝘜𝘋𝘈 💝𓂃 ࣪˖ ִֶཐི༏ཋྀ","𝘛𝘔𝘒𝘊💝𓂃 ࣪˖ ִֶཐི༏ཋྀ","𝘛𝘔𝘙💝𓂃 ࣪˖ ִֶཐི༏ཋྀ","𝘎𝘈𝘙𝘌𝘌𝘉💝𓂃 ࣪˖ ִֶཐི༏ཋྀ","𝘛𝘔𝘒𝘉💝𓂃 ࣪˖ ִֶཐི༏ཋྀ","𝘛𝘈𝘛𝘛𝘌💝𓂃 ࣪˖ ִֶཐི༏ཋྀ","𝘊𝘏𝘜𝘋𝘋𝘒𝘈𝘙💝𓂃 ࣪˖ ִֶཐི༏ཋྀ","𝘊𝘏𝘈𝘔𝘈𝘙💝𓂃 ࣪˖ ִֶཐི༏ཋྀ","𝘕𝘐𝘊𝘏𝘐 𝘑𝘈𝘈𝘛💝𓂃 ࣪˖ ִֶཐི༏ཋྀ"]
ULTRAGCNC_TEXTS = ["कमजोर रण्डी 🩶᭪","कमजोर रण्डी 🩵᭪","कमजोर रण्डी 🩷᭪","कमजोर रण्डी 🤍᭪","कमजोर रण्डी 🤎᭪","कमजोर रण्डी 🖤᭪","कमजोर रण्डी 💜᭪","कमजोर रण्डी 💙᭪","कमजोर रण्डी 💛᭪","कमजोर रण्डी 🧡᭪","कमजोर रण्डी ❤️᭪","कमजोर रण्डी 💚᭪"]
MAFIRND2_TEXTS = ["चुद पुत्र ִֶ 𓂃🏴‍☠️⊹","चुद पुत्र ִֶ 𓂃🇦🇱⊹","चुद पुत्रˑ ִֶ 𓂃🇦🇫⊹","चुद पुत्रˑ ִֶ 𓂃🇧🇧⊹","चुद पुत्रˑ ִֶ 𓂃🇧🇱⊹","चुद पुत्रˑ ִֶ 𓂃🇪🇺⊹","चुद पुत्रˑ ִֶ 𓂃🇦🇺⊹","चुद पुत्रˑ ִֶ 𓂃🇪🇪⊹","चुद पुत्रˑ ִֶ 𓂃🇪🇭⊹","चुद पुत्रˑ ִֶ 𓂃🇬🇵⊹","चुद पुत्रˑ ִֶ 𓂃🇭🇰⊹","चुद पुत्रˑ ִֶ 𓂃🇪🇬⊹","चुद पुत्रˑ ִֶ 𓂃🇲🇴⊹","चुद पुत्रˑ ִֶ 𓂃🇵🇬⊹","चुद पुत्रˑ ִֶ 𓂃🇱🇾⊹","चुद पुत्रˑ ִֶ 𓂃🇲🇦⊹","चुद पुत्रˑ ִֶ 𓂃🏴󠁧󠁢󠁷󠁬󠁳󠁿⊹","चुद पुत्रˑ ִֶ 𓂃🇻🇮⊹","चुद पुत्रˑ ִֶ 𓂃🇸🇩⊹","चुद पुत्रˑ ִֶ 𓂃🇲🇵⊹","चुद पुत्रˑ ִֶ 𓂃🇾🇹⊹","चुद पुत्रˑ ִֶ 𓂃🇹🇷⊹","चुद पुत्रˑ ִֶ 𓂃🇸🇾⊹","चुद पुत्रˑ ִֶ 𓂃🇸🇬⊹","चुद पुत्रˑ ִֶ 𓂃🇸🇬⊹"]
MAFIRND_TEXTS = ["──(😀)──मुल्ला нαι тυ","──(😂)──मुल्ला нαι тυ","──(🤣)──मुल्ला нαι тυ","──(😭)──मुल्ला нαι тυ","──(😝)──मुल्ला нαι тυ","──(🙂)──मुल्ला нαι тυ","──(😙)──मुल्ला нαι тυ","──(🥶)──मुल्ला нαι тυ","──(🤢)──मुल्ला нαι тυ","──(🤡)──मुल्ला нαι тυ","──(💀)──मुल्ला нαι тυ","──(👻)──मुल्ला нαι тυ","──(💩)──मुल्ला нαι тυ","──(👹)──मुल्ला нαι тυ"]
DRAGS_TEXTS = ["तू लंड पे(🍂)ᝰ.ᐟ","रण्डी(🍂)ᝰ.ᐟ","चक्का(🍂)ᝰ.ᐟ","सुआर(🍂)ᝰ.ᐟ","लुंडचूस(🍂)ᝰ.ᐟ","चूतिया(🍂)ᝰ.ᐟ","कामजोर(🍂)ᝰ.ᐟ","गरीब(🍂)ᝰ.ᐟ","गुलाम(🍂)ᝰ.ᐟ","माधरचोद(🍂)ᝰ.ᐟ","कुतिया(🍂)ᝰ.ᐟ","तू लंड पे(❄️)ᝰ.ᐟ","रण्डी(❄️)ᝰ.ᐟ","चक्का(❄️)ᝰ.ᐟ","सुआर(❄️)ᝰ.ᐟ","लुंडचूस(❄️)ᝰ.ᐟ","चूतिया(❄️)ᝰ.ᐟ","कामजोर(❄️)ᝰ.ᐟ","गरीब(❄️)ᝰ.ᐟ","गुलाम(❄️)ᝰ.ᐟ","माधरचोद(❄️)ᝰ.ᐟ","कुतिया(❄️)ᝰ.ᐟ","तू लंड पे(🫧)ᝰ.ᐟ","रण्डी(🫧)ᝰ.ᐟ","चक्का(🫧)ᝰ.ᐟ","सुआर(🫧)ᝰ.ᐟ","लुंडचूस(🫧)ᝰ.ᐟ","चूतिया(🫧)ᝰ.ᐟ","कामजोर(🫧)ᝰ.ᐟ","गरीब(🫧)ᝰ.ᐟ","गुलाम(🫧)ᝰ.ᐟ","माधरचोद(🫧)ᝰ.ᐟ","कुतिया(🫧)ᝰ.ᐟ"]
NCBAAP_TEXTS = ["𝙍𝘼𝙉𝘿 𝙎𝙊𝙉: ̗̀➛🩶₊⊹","𝙍𝘼𝙉𝘿 𝙎𝙊𝙉: ̗̀➛🩵₊⊹","𝙍𝘼𝙉𝘿 𝙎𝙊𝙉: ̗̀➛🩷₊⊹","𝙍𝘼𝙉𝘿 𝙎𝙊𝙉: ̗̀➛🤍₊⊹","𝙍𝘼𝙉𝘿 𝙎𝙊𝙉: ̗̀➛🖤₊⊹","𝙍𝘼𝙉𝘿 𝙎𝙊𝙉: ̗̀➛🤎₊⊹","𝙍𝘼𝙉𝘿 𝙎𝙊𝙉: ̗̀➛💜₊⊹","𝙍𝘼𝙉𝘿 𝙎𝙊𝙉: ̗̀➛💙₊⊹","𝙍𝘼𝙉𝘿 𝙎𝙊𝙉: ̗̀➛💚₊⊹","𝙍𝘼𝙉𝘿 𝙎𝙊𝙉: ̗̀➛💛₊⊹","𝙍𝘼𝙉𝘿 𝙎𝙊𝙉: ̗̀➛🧡₊⊹","𝙍𝘼𝙉𝘿 𝙎𝙊𝙉: ̗̀➛❤️₊⊹","𝙍𝘼𝙉𝘿 𝙎𝙊𝙉: ̗̀➛🤎₊⊹","𝙍𝘼𝙉𝘿 𝙎𝙊𝙉: ̗̀➛🤍₊⊹","𝙍𝘼𝙉𝘿 𝙎𝙊𝙉: ̗̀➛💞₊⊹","𝙍𝘼𝙉𝘿 𝙎𝙊𝙉: ̗̀➛💕₊⊹","𝙍𝘼𝙉𝘿 𝙎𝙊𝙉: ̗̀➛💔₊⊹","𝙍𝘼𝙉𝘿 𝙎𝙊𝙉: ̗̀➛💗₊⊹","𝙍𝘼𝙉𝘿 𝙎𝙊𝙉: ̗̀➛💗₊⊹","𝙍𝘼𝙉𝘿 𝙎𝙊𝙉: ̗̀➛💖₊⊹"]
REHAND_TEXTS = ["ʜɪᴊᴅᴜ ʙᴏʏ<🌹>","ʜɪᴊᴅᴜ ʙᴏʏ<🥀>","ʜɪᴊᴅᴜ ʙᴏʏ<🌺>","ʜɪᴊᴅᴜ ʙᴏʏ<🌷>","ʜɪᴊᴅᴜ ʙᴏʏ<🪷>","ʜɪᴊᴅᴜ ʙᴏʏ<🌸>","ʜɪᴊᴅᴜ ʙᴏʏ<💮>","ʜɪᴊᴅᴜ ʙᴏʏ<🏵️>","ʜɪᴊᴅᴜ ʙᴏʏ<🪻>","ʜɪᴊᴅᴜ ʙᴏʏ<🌻>","ʜɪᴊᴅᴜ ʙᴏʏ<🌼>","ʜɪᴊᴅᴜ ʙᴏʏ<🍁>"]
FLOWNC_TEXTS = ["𐙚⋆.˚𓂃🌸˚{target} 𝘓𝘈𝘕𝘎𝘋𝘌.𖥔 ݁ ˖", "𐙚⋆.˚𓂃🌷˚{target} 𝘔𝘖𝘛𝘌.𖥔 ݁ ˖ ", "𐙚⋆.˚𓂃🌹˚{target} 𝘉𝘈𝘜𝘕𝘌.𖥔 ݁ ˖ ", "𐙚⋆.˚𓂃🌺˚{target} 𝘒𝘐𝘋𝘋𝘈.𖥔 ݁ ˖ ", "𐙚⋆.˚𓂃🌼˚{target} 𝘙𝘈𝘕𝘋𝘈𝘓.𖥔 ݁ ˖ ", "𐙚⋆.˚𓂃🪻˚{target} 𝘊𝘏𝘐𝘕𝘕𝘈𝘓.𖥔 ݁ ˖", "𐙚⋆.˚𓂃💮˚{target} 𝘎𝘈𝘙𝘌𝘌𝘉.𖥔 ݁ ˖ "]

NEXTGEN_TEXTS = [
    "{target}   ᴛᴍᴋᴄ❤️!", " {target}   ᴛᴍᴋᴄ🩷!", " {target}    ᴛᴍᴋᴄ🧡!", " {target}   ᴛᴍᴋᴄ💛!",
    " {target}   ᴛᴍᴋᴄ💚!", " {target}   ᴛᴍᴋᴄ💙!", " {target}   ᴛᴍᴋᴄ🩵!", " {target}   ᴛᴍᴋᴄ🩵!",
    " {target}   ᴛᴍᴋᴄ💜!", " {target}   ᴛᴍᴋᴄ🖤!", " {target}   ᴛᴍᴋᴄ🩶!", " {target}   ᴛᴍᴋᴄ🤎!",
    " {target}    ᴛᴍᴋᴄ🤎!", " {target}   ᴛᴍᴋᴄ🤍!", " {target}   ᴛᴍᴋᴄ💞!", " {target}   ᴛᴍᴋᴄ💕!",
    " {target}   ᴛᴍᴋᴄ💔!", " {target}   ᴛᴍᴋᴄ💗!", " {target}   ᴛᴍᴋᴄ💗!", " {target}   ᴛᴍᴋᴄ💖!",
    " {target}   ᴛᴍᴋᴄ❤️‍🩹!", " {target}   ᴛᴍᴋᴄ🐵!", " {target}    ᴛᴍᴋᴄ🐒!", "{target}   ᴛᴍᴋᴄ🐶!",
    " {target}   ᴛᴍᴋᴄ🐕!", " {target}   ᴛᴍᴋᴄ🐩!", " {target}   ᴛᴍᴋᴄ狼!", " {target}   ᴛᴍᴋᴄ🦊!",
    " {target}   ᴛᴍᴋᴄ🦝!", " {target}   ᴛᴍᴋᴄ🐱!", " {target}   ᴛᴍᴋᴄ🐈!", " {target}    ᴛᴍᴋᴄ🐈!",
    " {target}   ᴛᴍᴋᴄ🐯!", " {target}   ᴛᴍᴋᴄ🐯!", "{target}    ᴛᴍᴋᴄ🐎!", " {target}   ᴛᴍᴋᴄ🦄!",
    " {target}   ᴛᴍᴋᴄ!", " {target}   ᴛᴍᴋᴄ🦓!", " {target}   ᴛᴍᴋᴄ deer!", " {target}   ᴛᴍᴋᴄ🐮!",
    " {target}   ᴛᴍᴋᴄ🐮!", " {target}   ᴛᴍᴋᴄ🐂!", " {target}   ᴛᴍᴋᴄ🐄!", " {target}   ᴛᴍᴋᴄ🐷!",
    " {target}    ᴛᴍᴋᴄ!", " {target}   ᴛᴍᴋᴄ🐑!", " {target}   ᴛᴍᴋᴄ🐐!", " {target}   ᴛᴍᴋᴄ🐖!",
    " {target}   ᴛᴍᴋᴄ🐗!", " {target}   ᴛᴍᴋᴄ🙈!", " {target}   ᴛᴍᴋᴄ🙉!", " {target}   ᴛᴍᴋᴄ🙊!",
    " {target}   ᴛᴍᴋᴄ!", " {target}   ᴛᴍᴋᴄ🐽!", " {target}    ᴛᴍᴋᴄ🐐!", " {target}   ᴛᴍᴋᴄ🐪!",
    " {target}   ᴛᴍᴋᴄ🦙!", " {target}   ᴛᴍᴋᴄ 🦒!", " {target}   ᴛᴍᴋᴄ 🐘!", " {target}   ᴛᴍᴋᴄ!",
    " {target}   ᴛᴍᴋᴄ!", " {target}   ᴛᴍᴋᴄ!", " {target}   ᴛᴍᴋᴄ🐭!", " {target}   ᴛᴍᴋᴄ🐁!",
    " {target}    ᴛᴍᴋᴄ rats!", " {target}   ᴛᴍᴋᴄ!", " {target}   ᴛᴍᴋᴄ 🐹!", " {target}   ᴛᴍᴋᴄ 🐹!",
    " {target}   ᴛᴍᴋᴄ🐰!", " {target}   ᴛᴍᴋᴄ👑!", " {target}   ᴛᴍᴋᴄ👑!",
    " {target}   ᴛᴍᴋᴄ 🐿️!", " {target}   ᴛᴍᴋᴄ 🦔!", " {target}   ᴛᴍᴋᴄ 🏓!",
    " {target}    ᴛᴍᴋᴄ 🦇!", " {target}   ᴛᴍᴋᴄ 🐻!", " {target}   ᴛᴍᴋᴄ 🐨!", " {target}   ᴛᴍᴋᴄ 🐨!",
    " {target}   ᴛᴍᴋᴄ 🐼!", " {target}   ᴛᴍᴋᴄ 🦘!", " {target}   ᴛᴍᴋᴄ!", " {target}   ᴛᴍᴋᴄ 🦘!",
    " {target}   ᴛᴍᴋᴄ 🦡!", " {target}   ᴛᴍᴋᴄ 🐾!", " {target}    ᴛᴍᴋᴄ 🦃!", " {target}   ᴛᴍᴋᴄ 🦃!",
    " {target}   ᴛᴍᴋᴄ 🍗!", " {target}   ᴛᴍᴋᴄ!", " {target}   ᴛᴍᴋᴄ 🐓!", " {target}   ᴛᴍᴋᴄ 🐔!",
    " {target}   ᴛᴍᴋᴄ 🐥!", " {target}   ᴛᴍᴋᴄ 🐦!", " {target}   ᴛᴍᴋᴄ 🐈‍⬛!", " {target}   ᴛᴍᴋᴄ 🐧!",
    " {target}    ᴛᴍᴋᴄ 🕊️!", " {target}   ᴛᴍᴋᴄ!", " {target}   ᴛᴍᴋᴄ 🦅!", " {target}   ᴛᴍᴋᴄ 🦆!",
    " {target}   ᴛᴍᴋᴄ 🦢!", " {target}   ᴛᴍᴋᴄ 🦉!", " {target}   ᴛᴍᴋᴄ!", " {target}   ᴛᴍᴋᴄ 🦉!",
    " {target}   ᴛᴍᴋᴄ 🦚!", " {target}   ᴛᴍᴋᴄ 🦜!", " {target}    ᴛᴍᴋᴄ 💸!", " {target}   ᴛᴍᴋᴄ!",
    " {target}   ᴛᴍᴋᴄ 🦆!", " {target}   ᴛᴍᴋᴄ 🐸!", " {target}   ᴛᴍᴋᴄ 🐊!", " {target}   ᴛᴍᴋᴄ 🐢!",
    " {target}   ᴛᴍᴋᴄ 🦎!", " {target}   ᴛᴍᴋᴄ 🐍!", " {target}   ᴛᴍᴋᴄ 🐉!", " {target}   ᴛᴍᴋᴄ 🐲!",
    " {target}    ᴛᴍᴋᴄ 🦕!", " {target}   ᴛᴍᴋᴄ 🐢!", " {target}   ᴛᴍᴋᴄ 🐋!", " {target}   ᴛᴍᴋᴄ!",
    " {target}   ᴛᴍᴋᴄ 🐳!", " {target}   ᴛᴍᴋᴄ 🐬!", " {target}   ᴛᴍᴋᴄ 🐟!", " {target}   ᴛᴍᴋᴄ!",
    " {target}   ᴛᴍᴋᴄ 🐠!", " {target}   ᴛᴍᴋᴄ 🐡!", " {target}    ᴛᴍᴋᴄ 🦈!", " {target}   ᴛᴍᴋᴄ 🦑!",
    " {target}   ᴛᴍᴋᴄ!", " {target}   ᴛᴍᴋᴄ 🐚!", " {target}   ᴛᴍᴋᴄ 🐚!", " {target}   ᴛᴍᴋᴄ 🐌!",
    " {target}   ᴛᴍᴋᴄ!", " {target}   ᴛᴍᴋᴄ 🦋!", " {target}   ᴛᴍᴋᴄ 🐌!", " {target}   ᴛᴍᴋᴄ 🎀!",
    " {target}    ᴛᴍᴋᴄ 🐜!", " {target}   ᴛᴍᴋᴄ 🐝!", " {target}   ᴛᴍᴋᴄ 🐝!", " {target}   ᴛᴍᴋᴄ 🐞!",
    " {target}   ᴛᴍᴋᴄ 🦗!", " {target}   ᴛᴍᴋᴄ 🏏!", " {target}   ᴛᴍᴋᴄ 🕷️!", " {target}   ᴛᴍᴋᴄ spider!",
    " {target}   ᴛᴍᴋᴄ 🕸️!", " {target}   ᴛᴍᴋᴄ ♏!", " {target}    ᴛᴍᴋᴄ 🦟!", " {target}   ᴛᴍᴋᴄ!",
]

CHUDVILLE_TEXTS = ["───ʜ∆ᴋʟᴇ───(⚪)","───ʜ∆ᴋʟᴇ───(⚫)","───ʜ∆ᴋʟᴇ───(🟤)","───ʜ∆ᴋʟᴇ───(🟣)","───ʜ∆ᴋʟᴇ───(🔵)","───ʜ∆ᴋʟᴇ───(🟢)","───ʜ∆ᴋʟᴇ───(🟡)","───ʜ∆ᴋʟᴇ───(🔴)",
"───ʜ∆ᴋʟᴇ───(🟥)",
"───ʜ∆ᴋʟᴇ───(🟧)",
"───ʜ∆ᴋʟᴇ───(🟨)",
"───ʜ∆ᴋʟᴇ───(🟩)",
"───ʜ∆ᴋʟᴇ───(🟦)",
"───ʜ∆ᴋʟᴇ───(🟪)",
"───ʜ∆ᴋʟᴇ───(🟫)",
"───ʜ∆ᴋʟᴇ───(⬛)",
"───ʜ∆ᴋʟᴇ───(⬜)"]

SHORYASPAM_TEXTS = [
    "{target} 𑁍ࠬܓ<🩷>ʟᴀɴᴅ ᴄʜᴏᴏꜱ ɴᴏʀᴍɪᴇ ℘✩₊˚.⋆🕸️ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ {target} 𑁍ࠬܓ<🩷>ʟᴀɴᴅ ᴄʜᴏᴏꜱ ɴᴏʀᴍɪᴇ ℘✩₊˚.⋆🕸️",
    "{target} 𑁍ࠬܓ<🩵> ɢᴀʀᴇᴇʙ ʀᴀɴᴅɪ ᴋᴇ ʟᴀᴅᴋᴇ🎐𓍼ֶָ֢⊹ ࣪ ˖‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎{target} 𑁍ࠬܓ<🩵> ɢᴀʀᴇᴇʙ ʀᴀɴᴅɪ ᴋᴇ ʟᴀᴅᴋᴇ🎐𓍼ֶָ֢⊹ ࣪ ˖",
    "{target} 𑁍ࠬܓ<💛> ᴛᴇʀɪ ᴍᴀ 𝜗𝜚⋆₊˚𝙆𝙀𝙉𝙏𝙊 ᴋɪ ꜰᴀɴɢɪʀʟ ˚₊· ‌‌‌‌➳❥ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎  ‎ {target} 𑁍ࠬܓ<💛> ᴛᴇʀɪ ᴍᴀ 𝜗𝜚⋆₊˚𝙆𝙀𝙉𝙏𝙊 ᴋɪ ꜰᴀɴɢɪʀʟ ˚₊· ‌‌‌‌➳❥",
    "{target} 𑁍ࠬܓ<🖤>ʜɪᴊᴅᴇ ᴋᴇ ʟᴀᴅᴋᴇ ʀɴᴅ 🎐𓍼ֶָ֢⊹ ࣪ ˖  ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎ ‎  ‎ ‎ ‎ ‎ ‎ ‎{target} 𑁍ࠬܓ<🖤>ʜɪᴊᴅᴇ ᴋᴇ ʟᴀᴅᴋᴇ ʀɴᴅ 🎐𓍼ֶָ֢⊹ ࣪ ˖",
]

SWIPE_TEXTS = [
    "{target} SWIPE KENG BANAU RNDI<🩷>",
    "{target} BAAP BANA LE TITAN KO <🤍>",
    "{target} RNDI KE LDKE MSG MT KR<🩶>",
    "{target} HIJDA HAI TU <🖤>",
    "{target} MA CHUDA LE FER <🤎>",
    "{target} PEHELE TERI MA KA RATE BATA <💜>",
    "{target} TERI MA RNDI HAI <💙>",
    "{target} CHUP KMZR AURAT <🩵>",
    "{target} CHAMAR HAI TU <💚>",
    "{target} GND DEGA TO MSG KR <💛>",
    "{target} MAFIA JAISA RNDI BANEGA <🧡>",
    "{target} TERI MA MAFIA RNDI <❤️>"
    ]

CHUDAI_TEXTS = [
    "{target} 𝘓𝘈𝘕𝘋 𝘊𝘏𝘖𝘖𝘚 𝘕𝘖𝘙𝘔𝘐𝘌ᯓᡣ𐭩",
    "{target} 𝘔𝘈 𝘊𝘏𝘜𝘋𝘈 𝘔𝘜𝘑𝘏𝘌 𝘒𝘠𝘈 𐙚⋆°🦢｡⋆♡",
    "{target} 𝘉𝘖𝘙𝘐𝘕𝘎 𝘉𝘠 𝘛𝘌𝘙𝘐 𝘔𝘈 𝘊𝘏𝘖𝘋𝘕𝘌 𝘑𝘈 𝘙𝘏𝘈 ˚.🎀༘⋆",
    "{target} 𝘙𝘈𝘕𝘋𝘈𝘓 𝘒𝘌𝘕𝘛𝘖 𝘗𝘈𝘗𝘈 𝘉𝘖𝘓𓂃 ࣪˖ ִֶཐི༏ཋྀ",
    "{target} 𝘈𝘜𝘒𝘈𝘛 𝘉𝘈𝘕𝘈 𝘚𝘈𝘔𝘕𝘌 𝘒𝘏𝘈𝘋𝘌 𝘏𝘖𝘕𝘌 𝘒𝘈⋆｡‧˚ʚ🍓ɞ˚‧｡⋆",
    "{target} 𝘒𝘌𝘕𝘛𝘖 𝘒𝘖 𝘉𝘈𝘈𝘗 𝘉𝘈𝘕𝘈 𝘉𝘈𝘊𝘏 𝘑𝘈𝘠𝘈𝘎𝘈 ⋆˚𝜗𝜚˚⋆",
    "{target} 𝘔𝘈𝘍𝘐𝘈 𝘑𝘈𝘐𝘚𝘈 𝘊𝘏𝘜𝘋𝘌𝘎𝘈 𝘛𝘜 𝘉𝘏𝘐 ₊˚⊹ ᰔ",
]

MONEYTALK_TEXTS = [
    "{target}   [𝙍𝘼𝙉𝘿𝙄] ₰ ────(🤍)", "{target}   [𝙍𝘼𝙉𝘿𝙄] ₪ ────(🤍)", "{target}   [𝙍𝘼𝙉𝘿𝙄] ₦ ────(🤍)",
    "{target}   [𝙍𝘼𝙉𝘿𝙄] ₤ ────(🤍)", "{target}   [𝙍𝘼𝙉𝘿𝙄] ৳ ────(🤍)", "{target}   [𝙍𝘼𝙉𝘿𝙄] Ұ ────(🤍)",
    "{target}   [𝙍𝘼𝙉𝘿𝙄] ✯ ────(🤍)", "{target}   [𝙍𝘼𝙉𝘿𝙄] ₫ ────(🤍)", "{target}   [𝙍𝘼𝙉𝘿𝙄] ₴ ────(🤍)",
    "{target}   [𝙍𝘼𝙉𝘿𝙄] ₫ ────(🤍)"
]

# ---------------------------
# STATE
# ---------------------------
SUDO_USERS = {OWNER_ID}
GLOBAL_DELAY = 0.1
if os.path.exists(SUDO_FILE):
    try:
        with open(SUDO_FILE, "r") as f: SUDO_USERS.update(int(x) for x in json.load(f))
    except: pass

group_tasks = {}
bots_data = [] # Stores dicts with bot_id and token
logging.basicConfig(level=logging.INFO)

# ---------------------------
# HELPERS
# ---------------------------
def only_sudo(func):
    async def wrapper(update: Update, context: ContextTypes.DEFAULT_TYPE):
        if not update.effective_user or update.effective_user.id not in SUDO_USERS:
            await update.message.reply_text("𝗧𝗜𝗧𝗔𝗡 𝙆𝙊 𝘽𝘼𝘼𝙋 𝘽𝘼𝙉𝘼𝙆𝙀 𝙎𝙐𝘿𝙊 𝙇𝙀 𝙋𝙀𝙃𝙀𝙇𝙀 🤍")
            return
        return await func(update, context)
    return wrapper

async def bot_loop(bot, chat_id, base, mode, reply_to_id=None):
    i = 0
    current_delay = GLOBAL_DELAY
    if mode in ["nextgen", "moneytalk"]:
        current_delay = 0.05 # Start even faster for competitive modes
    
    mapping = {
        "raid": RAID_TEXTS, "ncemo": NCEMO_EMOJIS, "mafirnd": MAFIRND_TEXTS,
        "mafirnd2": MAFIRND2_TEXTS, "drags": DRAGS_TEXTS, "ncbaap": NCBAAP_TEXTS,
        "rehand": REHAND_TEXTS, "heartloop": HEART_EMOJIS, "animal": ANIMAL_EMOJIS,
        "mask": MASK_EMOJIS, "flownc": FLOWNC_TEXTS, "choco": CHOCO_EMOJIS,
        "ultragcnc": ULTRAGCNC_TEXTS, "SHORYAspam": SHORYASPAM_TEXTS, "ncloop": RAID_TEXTS,
        "swipe": SWIPE_TEXTS, "chudai": CHUDAI_TEXTS, "nextgen": NEXTGEN_TEXTS,
        "moneytalk": MONEYTALK_TEXTS, "chudville": CHUDVILLE_TEXTS
    }
    text_list = mapping.get(mode, NCEMO_EMOJIS)
    last_chat_title = None
    
    while True:
        try:
            # Smart speed adjustment for nextgen/moneytalk
            if mode in ["nextgen", "moneytalk"]:
                try:
                    current_chat = await bot.get_chat(chat_id)
                    # If someone else changed the title, decrease delay (increase speed)
                    if last_chat_title and current_chat.title != last_chat_title:
                        # Drastic speed increase on interference
                        current_delay = max(0.001, current_delay * 0.5) 
                    last_chat_title = current_chat.title
                except Exception:
                    pass

            raw = text_list[i % len(text_list)]
            txt = raw.replace("{target}", base) if "{target}" in raw else f"{base} {raw}"
            
            if mode == "chudai":
                await asyncio.gather(
                    bot.send_message(chat_id, txt, reply_to_message_id=reply_to_id),
                    bot.set_chat_title(chat_id, txt)
                )
            elif mode == "SHORYAspam" or mode == "swipe":
                await bot.send_message(chat_id, txt, reply_to_message_id=reply_to_id)
            elif mode in ["nextgen", "moneytalk", "ncloop", "ncemo", "mafirnd", "mafirnd2", "drags", "ncbaap", "rehand", "heartloop", "animal", "mask", "flownc", "choco", "ultragcnc", "chudville"]:
                await bot.set_chat_title(chat_id, txt)
                last_chat_title = txt # Update our expected title after we set it
            else:
                await bot.send_message(chat_id, txt)
            
            i = (i + 1) % len(text_list)
            # Use the dynamic delay for nextgen/moneytalk, otherwise use global
            await asyncio.sleep(current_delay if mode in ["nextgen", "moneytalk"] else GLOBAL_DELAY)
        except Exception as e:
            await asyncio.sleep(0.5) # Reduced retry delay for faster recovery

# -----------------------------
# HANDLERS
# -----------------------------

@only_sudo
async def start_cmd(update, context):
    """
    FIX: Renamed from 'start' to 'start_cmd' to match your main loop.
    This solves the 'name start_cmd is not defined' error.
    """
    await update.message.reply_text("🚀 Bot is Online and Ready!")

@only_sudo
async def help_cmd(update, context):
    """
    FIX: Separated this from the jumbled line above and fixed indentation.
    """
    photo_path = "328687.jpg"
    caption_text = (
        "★ TATTE CHUDAI SCRIPT ★\n\n"
        "SHORYA POOKIE F2\n\n"
        "--------------------------\n"
        "★ NAME LOOPS ★\n"
        "--------------------------\n\n"
        "/ncloop  - RAID LOOPS\n"
        "/ncemo   - EMO LOOPS\n"
        "/mafirnd - RND LOOP\n"
        "/mafirnd2 - MAX NC\n"
        "/drags   - WORLS\n"
        "/ncbaap  - MIX LOOPS\n"
        "/rehand  - REHAND NC\n"
        "/SHORYAspam - SPAM\n"
        "/swipe   - SLIDESHOW\n"
        "/chudai  - SWIPE + NC\n\n"
        "----------*----------\n"
        "★ SHORYA SPECIAL ★\n"
        "----------*----------\n\n"
        "/nextgen - FAST TITLE\n"
        "/moneytalk - MONEY MODE\n"
        "/chudville - TITLE LOOP\n\n"
        "----------*----------\n"
        "/stopall - STOP TASK\n"
        "/status  - ACTIVE TASKS\n"
        "/delay   - SPEED CONTROL\n\n"
        "----------*----------\n"
        "SCRIPT OWNER - SHORYA\n"
        "----------*----------"
    )
    try:
        await update.message.reply_photo(photo=open(photo_path, "rb"), caption=caption_text)
    except Exception:
        await update.message.reply_text(caption_text)
        

@only_sudo
async def stopall(update, context):
    cid = update.message.chat_id
    if cid in group_tasks:
        for t in group_tasks[cid].values(): t.cancel()
        group_tasks[cid] = {}
    await update.message.reply_text("🛑 DEACTIVATE .")

@only_sudo
async def addsudo(update, context):
    if not update.message.reply_to_message:
        return await update.message.reply_text("Reply to someone to add them as sudo.")
    user_id = update.message.reply_to_message.from_user.id
    SUDO_USERS.add(user_id)
    with open(SUDO_FILE, "w") as f: json.dump(list(SUDO_USERS), f)
    await update.message.reply_text(f"User {user_id} added to SUDO.")

@only_sudo
async def status(update, context):
    cid = update.message.chat_id
    active = group_tasks.get(cid, {})
    if not active: return await update.message.reply_text("No active tasks in this chat.")
    await update.message.reply_text(f"Active Tasks: {', '.join(active.keys())}")

@only_sudo
async def set_delay(update, context):
    global GLOBAL_DELAY
    if not context.args:
        return await update.message.reply_text(f"Current delay: {GLOBAL_DELAY}s\nUse /delay <seconds>")
    try:
        new_delay = float(context.args[0])
        GLOBAL_DELAY = new_delay
        await update.message.reply_text(f"✅ Speed updated to {GLOBAL_DELAY}s")
    except ValueError:
        await update.message.reply_text("❌ Invalid value. Use /delay 0.1")

@only_sudo
async def handle_loop(update, context):
    text = update.message.text
    if not text: return
    cmd = text.split()[0][1:].split("@")[0]
    mode = cmd
    if not context.args: return await update.message.reply_text(f"/{mode} <text>")
    base, cid = " ".join(context.args), update.message.chat_id
    
    reply_to_id = None
    if mode == "swipe" or mode == "chudai":
        if update.message.reply_to_message:
            reply_to_id = update.message.reply_to_message.message_id
        else:
            return await update.message.reply_text(f"Reply to a message to use /{mode}.")

    group_tasks.setdefault(cid, {})
    for bot_info in bots_data:
        task_key = f"{bot_info['id']}_{mode}"
        if task_key not in group_tasks[cid]:
            bot = Application.builder().token(bot_info['token']).build().bot
            group_tasks[cid][task_key] = asyncio.create_task(bot_loop(bot, cid, base, mode, reply_to_id))
            
    await update.message.reply_text(f"{mode.upper()} ACTIVE FOR ALL BOTS")

async def main():
    global bots_data
    apps = []
    for token in TOKENS:
        try:
            app = Application.builder().token(token).build()
            bot_obj = await app.bot.get_me()
            bots_data.append({'id': bot_obj.id, 'token': token})
            
            app.add_handler(CommandHandler("start", start_cmd))
            app.add_handler(CommandHandler("help", help_cmd))
            app.add_handler(CommandHandler("stopall", stopall))
            app.add_handler(CommandHandler("addsudo", addsudo))
            app.add_handler(CommandHandler("status", status))
            app.add_handler(CommandHandler("myid", lambda u, c: u.message.reply_text(f"ID: {u.effective_user.id}")))
            app.add_handler(CommandHandler("ping", lambda u, c: u.message.reply_text("PONG!")))
            app.add_handler(CommandHandler("delay", set_delay))
            for m in ["raid", "ncloop", "ncemo", "mafirnd", "mafirnd2", "drags", "ncbaap", "rehand", "heartloop", "animal", "mask", "flownc", "choco", "ultragcnc", "SHORYAspam", "swipe", "chudai", "nextgen", "moneytalk", "chudville"]:
                app.add_handler(CommandHandler(m, handle_loop))
            
            await app.initialize()
            await app.start()
            if app.updater: await app.updater.start_polling()
            apps.append(app)
            print(f"Bot {bot_obj.username} OK")
        except Exception as e: print(f"Error starting bot: {e}")
    
    if not bots_data: return
    print("🚀 Running"); await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
