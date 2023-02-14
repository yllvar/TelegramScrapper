Telegram Group Scraper

Introduction:
This is a Telegram bot written in Python that allows you to scrape members from a Telegram group and add them to another group. It utilizes the telethon library to interact with the Telegram API.

To use the bot, you'll need to open a Telegram conversation with the bot and type "/start". The bot will respond with a message indicating that it is showing you the group list and to use the "/groups" command to confirm.

Once you've sent the "/groups" command, the bot will respond with a list of groups that it is a part of. The groups are numbered, and you'll need to select one by typing the number of the group you want to use as the source group.

The bot will then ask you to enter the destination group. You can either type the name of the destination group or the destination group's username, if the group has one.

The bot will then attempt to add all the members from the source group to the destination group. Once the process is complete, the bot will respond with a message indicating that the members were added successfully.

Requirements:
1. Python 3.x
2. Telethon library
3. Telebot library
4. Telegram API key

Installation:
1. Install the required libraries by running the following command:
"
pip install telethon
pip install telebot
"

2. Replace the placeholder BOT_TOKEN in the code with your own Telegram API key.

Usage:
1. Start the bot by running the following command:
"
python bot.py
"

2. In your Telegram client, start a chat with the bot and use the /start command to initiate the process.

3. The bot will show you a list of groups. Use the /groups command to confirm.

4. Select the source group by typing its name in the chat.

5. The bot will ask you to enter the destination group.

6. The bot will start adding members from the source group to the destination group.

Limitations:
Due to limitations imposed by Telegram, the bot can only add a limited number of members per minute. If you add too many members too quickly, your account may be temporarily banned. The code has a sleep function in place to avoid this, but it's always a good idea to keep an eye on the bot and stop it if necessary.

Conclusion:
This bot provides a convenient way to scrape members from a Telegram group and add them to another group. However, be cautious when using it and always follow Telegram's terms of service to avoid any issues with your account.




