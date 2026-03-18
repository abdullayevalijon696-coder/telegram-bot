from telethon import TelegramClient, events
from groq import Groq

# Sozlamalar
api_id = 27241160
api_hash = 'aaad5f8512302f3aacd99f903fc5e568'  
# Groq sozlash
groq_client = Groq(api_key='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')

telegram = TelegramClient('akkount', api_id, api_hash)

@telegram.on(events.NewMessage(incoming=True))
async def aqlli_javob(event):
    if event.is_private:
        try:
            savol = event.text
            response = groq_client.chat.completions.create(
               model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": savol}]
            )
            javob = response.choices[0].message.content
            await event.reply(javob)
        except Exception as e:
            print(f"Xato: {e}")

print("Ishga tushdi...")
telegram.start()
telegram.run_until_disconnected()
