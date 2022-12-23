# openAI-discord
這段代碼使用 Discord Python 庫創建了一個 Discord 機器人，該機器人可以在 Discord 頻道中與用戶互動。 機器人會監聽頻道中的特定消息，並相應地回應。

機器人會監聽下列消息：

+ "AIclearALL"：清除所有用戶的聊天歷史記錄。
+ "AIclear"：清除發送該消息的用戶的聊天歷史記錄。
+ "AIcode" + 內容：使用 "code-davinci-002" 模型將內容發送到 OpenAI API 以生成響應。
+ "AI" + 內容：使用 "text-davinci-003" 模型將內容發送到 OpenAI API 以生成響應。
對於所有其他消息，機器人不做任何操作。

對於每個用戶，都會在字典中存儲其聊天歷史記錄，用戶的 ID 為鍵，其之前的消息列表為值。 這使機器人可以跟蹤對話並生成更加語境相關的響應。

機器人使用 OpenAI API 生成對用戶消息的響應。 它將用戶的消息和指定的模型一起發送到 API，並接收以 JSON 對象形式的響應。 然後，它從 JSON 對象中提取響應文本並將其發送回 Discord 頻道。

---

This code is using the Discord Python library to create a Discord bot that can interact with users in a Discord channel. The bot listens for specific messages in the channel, and responds accordingly.

The bot listens for the following messages:

+ "AIclearALL": Clears the chat history for all users.
+ "AIclear": Clears the chat history for the user who sent the message.
+ "AIcode" + content: Sends the content to an OpenAI API with the "code-davinci-002" model to generate a response.
+ "AI" + content: Sends the content to an OpenAI API with the "text-davinci-003" model to generate a response.
For all other messages, the bot does nothing.

The chat history for each user is stored in a dictionary, with the user's ID as the key and a list of their previous messages as the value. This allows the bot to keep track of the conversation and generate more contextually appropriate responses.

The bot uses the OpenAI API to generate responses to user messages. It sends the user's message to the API, along with the specified model, and receives a response in the form of a JSON object. It then extracts the response text from the JSON object and sends it back to the Discord channel.

---

在使用這段代碼之前，您需要使用 pip 安裝以下 package：

+ discord
+ requests
+ json  
您可以使用以下命令來安裝這些 package：
```
pip install discord
pip install requests
pip install json  
```
請注意，您還需要先安裝 Python，並在安裝包之前確保已在正確的虛擬環境中運行。

---

如果您有任何問題歡迎向 CodeRyo 團隊聯繫，您可以透過以下電子郵件發送您的提問或於此 repo 發佈 issue。  
If you have any questions, please don't hesitate to contact the CodeRyo team. You can send your questions via email or create an issue in this repo.  
```
hello@coderyo.com
```

---

歡迎大家對本項目進行貢獻！如果你想發送一個 pull request，請先 fork 本項目並在本地做出你的修改。然後，在你的 fork 上發送一個 pull request，我們會審核你的修改並考慮合併到主分支。感謝你的貢獻！  
Welcome to contribute to this project! If you want to send a pull request, please first fork the project and make your changes locally. Then, send a pull request on your fork, and we will review your changes and consider merging them into the master branch. Thank you for your contribution!
