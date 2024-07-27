# Project-Pear
利用Python所做成的Discord的機器人

## 所需套件
```
pip install discord.py==2.3.2 
pip install discord-py-slash-command==4.2.1
pip install beautifulsoup4
pip install requests
pip install pysaucenao==1.6.2 
```

## 配置檔案
- 機器人金鑰  
主資料夾下的 config.json
將 ``YOUR TOKEN`` 替換成在 [discord dev](https://discord.com/developers/applications) 裡面的 bot token
```json
{
    "bot_token":"YOUR TOKEN"
}
```

- 機器人擁有者ID  
位於items資料夾下的data.json
將 ``YOUR DISCORD ID`` 替換成你的 Discord ID (在discord裡面右鍵使用者 即可複製)
```json
{
    "owner_id":"YOUR DISCORD ID"
}
```

## 機器人狀態設定
```py
@client.event
async def on_ready():
    intents = discord.Intents.default()
    await client.change_presence(activity = discord.Streaming(name="title", url="url")) 
    intents.message_content = True
    print(str(datetime.utcnow().astimezone(timezone(timedelta(hours=16)))).split(".",1)[0],"Bot is on ready",client.user)
```
- title為該活動的標題, url為該活動下方按鈕所導向的連結

- 機器人狀態更改
將 ``activity = discord.YOUR ACTIVITY`` 的 ``YOUR ACTIVITY`` 更改成下列的狀態

```
game (遊玩遊戲)
streaming (直播狀態)
watching (正在觀看)
listening (正在聆聽)
```

## Saucenao以圖搜圖功能
- 確保已經安裝 ``pysaucenao`` 功能庫
```
pip install pysaucenao==1.6.2 
```
- 到 [saucenao](https://saucenao.com) 申請一個帳號
- 在 [saucenao.userphp](https://saucenao.com/user.php) 裡面會有你的api key, 將其複製到 ``saucenao.py`` 裡面
  , 替換掉 ``YOUR APIKEY``
```
sauce = SauceNao(api_key="YOUR APIKEY")
```




**作者:** shuili
**discord id:** shuili
**最後更新時間:** 2024-07-27
