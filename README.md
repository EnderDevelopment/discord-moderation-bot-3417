# Discord Moderation Bot

A versatile Discord bot for moderation, invite tracking, tickets, and security.

## Features

- Basic moderation commands (kick, ban, unban, clear)
- Invite tracking
- Ticket management
- Welcome and goodbye messages
- Basic security measures

## Requirements

- Python 3.8 or higher
- discord.py
- python-dotenv
- sqlite3

## Installation

1. Clone the repository:

```bash

git clone https://github.com/EnderDevelopment/discord-moderation-bot.git

cd discord-moderation-bot

```

2. Install the required packages:

```bash

pip install -r requirements.txt

```

3. Create a `.env` file in the root directory and add your Discord bot token:

```env

DISCORD_TOKEN=your_discord_bot_token

```

## Usage

1. Run the bot:

```bash

python main.py

```

2. Use the following commands in your Discord server:

| Command | Description |
|---------|-------------|
| !ping | Check if the bot is online |
| !kick @user [reason] | Kick a user from the server |
| !ban @user [reason] | Ban a user from the server |
| !unban user#discriminator | Unban a user from the server |
| !clear [amount] | Clear a specified number of messages |
| !ticket | Create a support ticket |

## Configuration

- **Welcome/Goodbye Messages**: Create text channels named `welcome` and `goodbye` for the bot to send messages.
- **Security**: Add words to the `security.py` file to filter out inappropriate language.

---

## Generated with EnderDevelopment

This plugin was generated in minutes with [EnderDevelopment](https://enderdevelopment.com) — the AI platform that turns your ideas into working Minecraft plugins, Discord bots and FiveM scripts.

**Want your own?** [Generate this project on EnderDevelopment](https://dash.enderdevelopment.com?utm_source=github&utm_medium=readme&utm_campaign=discord-moderation-bot&utm_content=bottom) — describe it in one sentence and get the full source code.