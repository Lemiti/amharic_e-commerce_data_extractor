from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerChannel
import pandas as pd
import asyncio

api_id = 215----  # Replace with your actual API ID
api_hash = '0657a56fa0d48ee9c3d0--------'  # Replace with your actual API hash
phone = '+251--------'  # Replace with your phone number

async def main():
    client = TelegramClient('session_name', api_id, api_hash)
    client.start(phone)

    async def scrape_channel(channel_username, limit=100):
        try:
            channel = await client.get_entity(channel_username)
            messages = []
            async for msg in client.iter_messages(channel, limit=limit):
                sender_id = msg.sender.id if msg.sender else None
                messages.append({
                    "date": msg.date,
                    "sender": sender_id,
                    "text": msg.text,
                    "views": msg.views
                })
            return pd.DataFrame(messages)
        except Exception as e:
            print(f"Error scraping {channel_username}: {str(e)}")
            return pd.DataFrame()

    channels = ["@shegerm", "@ethiogebeyam", "@zemengebeya", "https://t.me/HELLOMARKET_AGENT", "https://t.me/efuyegellaMarket", "@abaymart"]  # Remove empty string
    all_data = pd.DataFrame()

    for channel in channels:
        if channel:  # Skip empty strings
            print(f"Scraping {channel}...")
            data = await scrape_channel(channel)
            all_data = pd.concat([all_data, data])

    all_data.to_csv("/content/drive/MyDrive/10Acadamy/data/raw_messages.csv", index=False)
    print("Data saved to '/content/drive/MyDrive/10Acadamy/data/raw_messages.csv'")
    await client.disconnect()

# Run the async main function
if __name__ == '__main__':
    asyncio.run(main())