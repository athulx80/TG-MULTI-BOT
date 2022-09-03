from pyrogram import Client, filters, idle
import pyrogram
from pyrogram.errors import FloodWait
from helper.fsub import ForceSub 
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from helper.add_new import add_user
from variables import STAT_STICK, PICS, ADMIN, DELAY, B_TEXT
from plugins.utils.logo_maker import generate_logo
import asyncio
import random
import time
from helper.errors import capture_err
from plugins.utils.http import get


@Client.on_message(filters.private & filters.command("start"))
async def start_message(bot, message):
    FSub = await ForceSub(bot, message)
    if FSub == 400:
        return 
    await add_user(bot, message)     
    await message.reply_chat_action("Typing")          
    await message.reply_photo(
        photo=random.choice(PICS),
        caption=f"Hello {message.from_user.mention}👋🏻\nI'am A Multi Featured Bot With Many Variety Features.\neg:- Telegarph, Channel ID, User ID, Fun, Group Id, Sticker id, kang, and othersetc...\nYou can see My commands by below button...",               
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("✨️ Support", url="https://t.me/BETA_SUPPORT"),
            InlineKeyboardButton("📢 Updates", url="https://t.me/Beta_BoTZ")
            ],[            
            InlineKeyboardButton("ℹ️ Help", callback_data="help"),
            InlineKeyboardButton("🤖 𝐀𝐁𝐎𝐔𝐓", callback_data="about")               
            ]]
            )
        )
       
         
@Client.on_message(filters.command("id"))
async def id_message(bot, message):
    FSub = await ForceSub(bot, message)
    if FSub == 400:
        return 
    await message.reply_text(
    text = f"""<i>
<u>👁️‍🗨️YOUR DETAILS</u>

○ ID : <code>{message.from_user.id}</code>
○ DC : <code>{message.from_user.dc_id}</code>
○ First Name : <code>{message.from_user.first_name}<code>
○ UserName : @{message.from_user.username}
○ link : <code>https://t.me/{message.from_user.username}</code>

Thank You For Using Me❣️</i>""",
    reply_markup=InlineKeyboardMarkup( [[
        InlineKeyboardButton("✨️ Support", url="https://t.me/BETA_SUPPORT"),
        InlineKeyboardButton("📢 Updates", url="https://t.me/Beta_BoTZ")
        ]]
        )
    )

@Client.on_message(filters.command(["stickerid"]))
async def stickerid(bot, message): 
    FSub = await ForceSub(bot, message)
    if FSub == 400:
        return 
    if message.reply_to_message.sticker:
       await message.reply(f"**Sticker ID is**  \n `{message.reply_to_message.sticker.file_id}` \n \n ** Unique ID is ** \n\n`{message.reply_to_message.sticker.file_unique_id}`", quote=True)
    else: 
       await message.reply("Oops !! Not a sticker file")





@Client.on_message(filters.command("logosq") & filters.incoming & filters.text & ~filters.forwarded & filters.private)
async def logosq(bot, message):
    FSub = await ForceSub(bot, message)
    if FSub == 400:
        return 
    try:
      text = message.text.replace("logosq","").replace("/","").replace("[ᗷETᗩ]","").strip().upper()
      
      if text == "":
        return await message.reply_text("**To Make Logo -** /logo Your Name\n**To Make Square Logo - ** /logosq Your Name\n\n**♻️ Example:**\n/logo BETA\n/logosq BETA")
  
      x = await message.reply_text("`🔍 Generating Logo For You...`")  
      logo = await generate_logo(text,True)
  
      if "telegra.ph" not in logo:
        return await x.edit("`❌ Something Went Wrong...`\n\nReport This Error In [ᗷETᗩ]")
        
      if "error" in logo:
        return await x.edit(f"`❌ Something Went Wrong...`\n\nReport This Error In [ᗷETᗩ] \n\n`{logo}`")
        
      await x.edit("`🔄 Done Generated... Now Sending You`")
      
      logo_id = logo.replace("https://graph.org//file/","").replace(".jpg","").strip()
      
      await message.reply_photo(logo,caption = "**🖼 Logo Generated By TG-MULTI-BOT**",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Upload As File 📁", callback_data=f"flogo {logo_id}")]]))
      await x.delete()
    except FloodWait:
      pass
    except Exception as e:
      try:
        await x.delete()
      except:
        pass
      return await message.reply_text("`❌ Something Went Wrong...`\n\nReport This Error In [ᗷETᗩ]")

@Client.on_message(filters.command("logo") & filters.incoming & filters.text & ~filters.forwarded & filters.private)
async def logo(bot, message):
  FSub = await ForceSub(bot, message)
    if FSub == 400:
        return 
  try:
    text = message.text.replace("logo","").replace("/","").replace("@TechZLogoMakerBot","").strip().upper()
    
    if text == "":
      return await message.reply_text("**To Make Logo -** /logo Your Name\n**To Make Square Logo - ** /logosq Your Name\n\n**♻️ Example:**\n/logo BETAs\n/logosq MKN")

    x = await message.reply_text("`🔍 Generating Logo For You...`")  
    logo = await generate_logo(text)

    if "telegra.ph" not in logo:
      return await x.edit("`❌ Something Went Wrong...`\n\nReport This Error In [ᗷETᗩ]")
      
    if "error" in logo:
      return await x.edit(f"`❌ Something Went Wrong...`\n\nReport This Error In [ᗷETᗩ] \n\n`{logo}`")
      
    await x.edit("`🔄 Done Generated... Now Sending You`")

    logo_id = logo.replace("https://graph.org//file/","").replace(".jpg","").strip()
    await message.reply_photo(logo,caption = "**🖼 Logo Generated By TG-MULTI-BOT**",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Upload As File 📁", callback_data=f"flogo {logo_id}")]]))
    await x.delete()
  except FloodWait:
    pass
  except Exception as e:
    try:
      await x.delete()
    except:
      pass
    return await message.reply_text("`❌ Something Went Wrong...`\n\nReport This Error In [ᗷETᗩ]")


@Client.on_callback_query(filters.regex("flogo"))
async def logo_doc(_,query):
  await query.answer()
  try:
    x = await query.message.reply_text("`🔄 Sending You The Logo As File`")
    await query.message.edit_reply_markup(reply_markup=None)
    link = "https://telegra.ph//file/" + query.data.replace("flogo","").strip() + ".jpg"
    await query.message.reply_document(link,caption="**🖼 Logo Generated By [ᗷETᗩ]**")
  except FloodWait:
    pass
  except Exception as e:
    try:
      return await x.edit(f"`❌ Something Went Wrong...`\n\nReport This Error In [ᗷETᗩ] \n\n`{str(e)}`")
    except:
      return
    
  return await x.delete()



@Client.on_message(filters.command("repo") & ~filters.edited)
@capture_err
async def repo(_, message):
    users = await get(
        "https://api.github.com/repos/jeolpaul/TG-MULTI-BOT/contributors"
    )
    list_of_users = ""
    count = 1
    for user in users:
        list_of_users += (
            f"**{count}.** [{user['login']}]({user['html_url']})\n"
        )
        count += 1

    text = f"""[Github](https://github.com/Jeolpaul/TG-MULTI-BOT) | [Updates](t.me/beta_botz)
```----------------
| Contributors |
----------------```
{list_of_users}"""
    await Client.send_message(
        message.chat.id, text=text, disable_web_page_preview=True
    )


