# Discord-Active-Developer-Badge
A simple Discord bot built with Nextcord to help you get the Discord Active Developer Badge.

Hello everyone! If you want to get the Discord Active Developer Badge, you just need to follow a few simple steps. But before starting, make sure you have a Discord Bot Token:

1. Open the official Discord Developer Portal: https://discord.com/developers/applications
2. Choose your application or create a new one, depending on your preference.
3. Go to the **Bot** tab in the settings on the left. Under **Privileged Gateway Intents**, enable all options. Then, scroll down to **Bot Permissions** and give the **Administrator** permission. These are required for the bot to work properly.
4. Above, you will see a **Reset Token** button — click it and copy your token.
5. In the **Installation** section, copy the Discord Bot invite link and add your bot to any server you want.

---

After obtaining your token, follow these steps:

1. Clone this repository:  
```bash
git clone https://github.com/ukp1eeee/Discord-Active-Developer-Badge
````

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Place your bot token in `token.txt` (if you don’t have one, return to the guide above).
4. Run the bot:

```bash
python main.py
```

5. After the bot is running, use the slash command: `/ping`.
   The bot will reply:

```
Pong! You successfully activated the Discord Active Developer Badge
```

Now, wait about 24 hours and visit the official site: [https://discord.com/developers/active-developer](https://discord.com/developers/active-developer). Follow Discord’s instructions, and bingo  you will get your badge!

---

I’ll be very glad if this repository helps you get your badge! ^_^



