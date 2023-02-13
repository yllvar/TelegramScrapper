TelegramScraperBot

TelegramScraperBot is a Python script that scrapes information from a Telegram channel and saves the information to a log file.

Installation
To install the necessary dependencies, run the following command in your terminal:

''
pip install aiohttp beautifulsoup4
''

Running the Bot

1. Clone the repository to your local machine
2. Open the terminal and navigate to the cloned directory
3. Run the following command in the terminal to start the bot:
''
python TelegramScraperBot.py
''


Code Assessment
This code is well structured, with clear variable names and comments for the code. It uses asynchronous programming with the asyncio and aiohttp libraries to make the scraping process more efficient and to handle multiple requests simultaneously. Additionally, the code uses the beautifulsoup4 library to parse the HTML content and extract the information needed. The log file is written in txt format and is appended to with each run of the script.

The code above is a refactored version of a script to scrape Telegram group members. It uses the Telethon library, which is a fully-asynchronous Python 3 MTProto library to interact with Telegram's API as a user.

Here's how to use the code:

1. Obtain your api_id and api_hash from the Telegram website, which are required for authentication purposes.
2. Create a session for your Telegram account using the TelegramClient method:

async def main():
    api_id, api_hash = get_api_details()
    client = TelegramClient(session, api_id, api_hash)
    await client.start()

3. Fetch all your conversations using the GetDialogsRequest function:

    dialogs = await client(GetDialogsRequest(
        offset_date=None,
        offset_id=0,
        offset_peer=InputPeerEmpty(),
        limit=100,
        hash=0
    ))

4. Iterate through each of the fetched conversations to filter out the group chats and retrieve the members in each group:
    for dialog in dialogs.dialogs:
        if dialog.peer.channel_id:
            group = await client.get_entity(dialog.peer)
            async for user in client.iter_participants(group):
                print(user.id, user.first_name, user.last_name)

5. The fetched members' information will be printed to the console in the format 
'user_id first_name last_name'.






Warning
Please be aware that scraping information from Telegram channels without the proper permissions may result in your account being banned. Always obtain the necessary permissions before scraping information from any website or platform. The developers of this code do not take any responsibility for any actions taken by users of this code.
