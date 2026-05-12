# OPDC Bot

A Discord bot built in Python for the OPDC server. Handles admin commands, a basic economy system, and welcome messages. Economy data (like each user's balance) is persisted in MongoDB.

---

## Stack

- **Python** — discord.py
- **MongoDB** — stores economy data per user

---

## Structure

```
├── Bot.py          # Entry point
├── settings.py     # Config and env vars
├── Functions/      # Command handlers (admin, economy, welcome)
└── Database/       # MongoDB connection and models
```

---

## Features

- **Admin** — moderation commands for server management
- **Economy** — basic currency system with balances stored per user
- **Welcome** — greets new members when they join the server

---

## Running locally

```bash
pip install -r requirements.txt
# set your bot token and MongoDB URI in settings.py or .env
python Bot.py
```

---

## License

MIT
