import telethon
from telethon import events

API_ID = 
API_HASH = ''

bot = telethon.TelegramClient('<BOT_TOKEN>', API_ID, API_HASH)

chats = []
groups = []
group_list = ""
unimembers = []
source_group = None


@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond('Showing you the group list...\nUse /groups command to confirm')


@bot.on(events.NewMessage(pattern='/groups'))
async def before_scrape(event):
    async for chat in bot.iter_dialogs():
        try:
            if chat.megagroup:
                groups.append(chat)
        except:
            continue

    for i, g in enumerate(groups):
        group_list += f"{i} - {g.title}\n"

    await event.respond(group_list)
    await event.respond("Select the source group:")
    await bot.await_event(events.NewMessage, check=lambda e: e.is_private and e.message.from_id == event.message.from_id, func=scrape_members)


async def scrape_members(event):
    global source_group
    source_group = int(event.text)
    source_group = groups[source_group]
    async for user in bot.iter_participants(source_group):
        unimembers.append({'id': user.id, 'username': user.username})
    await event.respond("Enter Destination Group:")
    await bot.await_event(events.NewMessage, check=lambda e: e.is_private and e.message.from_id == event.message.from_id, func=add_members)


async def add_members(event):
    destination_group = event.text
    users = unimembers[source_group]
    for user in users:
        try:
            bot.invite_users(destination_group, [user['id']])
        except Exception as e:
            print(e)
            continue

    await event.respond("Members added successfully.")


with bot:
    bot.run_until_disconnected()
