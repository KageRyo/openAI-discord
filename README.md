# openAI-discord
這段代碼是一個用 Python 寫的 Discord 聊天機器人。該機器人會監聽某些命令並做出相應的回應。

當有新消息發送到 Discord 頻道中時，將觸發 on_message 事件監聽器。機器人將檢查消息的格式，並根據命令執行不同的操作。

例如，如果消息以 "AIclearALL" 開頭，機器人將清除所有使用者的聊天紀錄。如果消息以 "AIclear" 開頭，則機器人將清除發送該消息的使用者的聊天紀錄。如果消息以 "AIcode" 或 "AI" 開頭，機器人將將消息發送到 API 以生成回應，然後將回應發送回 Discord 頻道。

chat_history 字典使用使用者的 ID 為鍵，將每個使用者的聊天紀錄存儲起來。model 變量指定在發送消息到 API 時使用的模型。

---

This code is a Discord bot written in Python. The bot listens for certain commands and responds accordingly.

The on_message event listener is triggered whenever a new message is sent in the Discord channel. The bot will check the format of the message and perform different actions based on the command.

For example, if the message starts with "AIclearALL", the bot will clear the chat history for all users. If the message starts with "AIclear", the bot will clear the chat history for the user who sent the message. If the message starts with "AIcode" or "AI", the bot will send the message to an API to generate a response, and then send the response back to the Discord channel.

The chat_history dictionary stores the chat history for each user, using the user's ID as the key. The model variable specifies which model to use when sending the message to the API.

---

```
pip install discord.py
```
```
pip install requests
```
```
pip install json
```

---

by. kageryo@coderyo 2022/12/18 
