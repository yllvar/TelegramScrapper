import os
import sys
import json
import time
from telethon import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserNotMutualContactError, UserPrivacyRestrictedError, UserChannelsTooMuchError, UserBotError, InputUserDeactivatedError

def clear_screen(clear_type: str):
    if clear_type == 'terminal':
        os.system('clear')
    elif clear_type == 'cmd':
        os.system('cls')
    else:
        print('Invalid input!')
        sys.exit()

def get_api_details():
    if os.path.isfile('erfan4lx_log.txt'):
        with open('erfan4lx_log.txt', 'r') as f:
            data = f.readlines()
        api_id = data[0].strip()
        api_hash = data[1].strip()
    else:
        api_id = input('Enter api_id: ')
        api_hash = input('Enter api_hash: ')
        with open('erfan4lx_log.txt', 'a') as f:
            f.write(api_id + '\n' + api_hash)
    return api_id, api_hash

async def scrape_telegram_group(group_username):
    api_id, api_hash = get_api_details()
    client = TelegramClient('session_name', api_id, api_hash)

    async with client:
        try:
            await client.connect()
        except Exception as e:
            print(e)
            sys.exit()

        try:
            entity = await client.get_entity(group_username)
        except Exception as e:
            print(f"Error: {e}")
            sys.exit()

        dialogs = await client(GetDialogsRequest(
            offset_date=None,
            offset_id=0,
            offset_peer=InputPeerEmpty(),
            limit=100,
            hash=0
        ))

        for dialog in dialogs.dialogs:
            if dialog.peer.channel_id == entity.id:
                participants = []
                async for participant in client.iter_participants(dialog.peer, aggressive=True):
                    participants.append(participant.first_name)
                print(f"Members of group {group_username}: {participants}")
                break

if __name__ == '__main__':
    clear_screen_prompt = input('Enter the type of screen you have (terminal/cmd): ').lower()
    clear_screen(clear_screen_prompt)
    group_username = input("Enter the username of the telegram group you want to scrape: ")
    asyncio.run(scrape_telegram_group(group_username))
