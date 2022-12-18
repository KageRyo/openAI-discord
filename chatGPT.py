import discord
import requests
import json

# 設置 Discord intents
intents = discord.Intents().all()
intents.message_content = True
client = discord.Client(intents=intents)

channel_id = "channelID"

# 建立字典以接續對話
chat_history = {}

@client.event
async def on_message(message):
    # 取得使用者 ID 和聊天內容
    user_id = message.author.id
    chat_content = message.content
    # 如果訊息的格式符合 "AIclear"，則進行處理
    if chat_content == "AIclear":
        # 將使用者的聊天紀錄清除
        chat_history[user_id] = []
        # 將文本傳回 Discord 頻道
        channel=client.get_channel(channel_id)
        await message.channel.send("已清除聊天紀錄")
        return
    # 如果訊息的格式符合 "AI" + 內容 + "，則進行處理
    if chat_content.startswith('AI"'):
        # 去除頭尾的雙引號
        chat_content = chat_content.strip('"')
        # 將字符串分割成三個部分，取出第二個部分的內容
        chat_content = chat_content.split('"')[1]
    else:
        # 如果訊息的格式不符合，則跳過不處理
        return
    # 如果使用者 ID 不在字典中，則新增一個記錄
    if user_id not in chat_history:
        chat_history[user_id] = []

    # 取得使用者的聊天紀錄
    user_history = chat_history[user_id]

    # 如果聊天次數大於 30，則清除除了前一次聊天紀錄以外的記憶
    if len(user_history) > 30:
        user_history = user_history[-1:]

    # 使用 OpenAI API 回覆使用者的訊息
    headers = {
        "Authorization": "Bearer openaiAPI"
    }
    data = {
    "model": "text-davinci-003",
    "prompt": f"{' '.join(user_history)} {chat_content}",
    "max_tokens": 1024,
    "temperature": 0.5,
}
    response = requests.post("https://api.openai.com/v1/completions", headers=headers, json=data)
    if response.status_code == 200:
        jsondata = response.json()
        print(response.json())
        response_text = jsondata['choices'][0]['text']
        # 將回覆的文本傳回 Discord 頻道
        channel=client.get_channel(channel_id)
        await message.channel.send(response_text)
    else:
        # 處理錯誤
        print(response.json())
        pass

    # 將使用者的聊天紀錄加入聊天紀錄中
    user_history.append(chat_content)
client.run("token")
