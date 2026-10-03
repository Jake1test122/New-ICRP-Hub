# Railway Setup

1. Put these files in a GitHub repository.
2. In Railway, create a New Project and choose **Deploy from GitHub repo**.
3. Select the repository.
4. Open the Railway service's **Variables** tab.
5. Add:
   `DISCORD_TOKEN=your_bot_token_here`
6. Deploy. The start command is already configured as `python main.py`.
7. Check Railway logs until the Discord bot reports that it is ready.
8. Make sure the bot has been invited to the correct Discord server with the required Manage Channels / Manage Roles permissions.
9. Run the setup command in Discord.

Never commit your actual Discord bot token to GitHub.
