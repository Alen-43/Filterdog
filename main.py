from pyrogram import Client


PyrogramBot = Client(
    "PyrogramBot",
    bot_token="5102623936:AAGA7i5H0M80ZM6jqXiHWo4nu4fIA474fJA",
    api_id="10429496",
    api_hash="dc86c8623259c10c4fd1d1b7d8dab96f",
    plugins=dict(root="bot")
)



PyrogramBot.run()
