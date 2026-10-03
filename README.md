# ICRP Hub Server Pack

Replit-ready automatic Hub builder.

1. Upload this ZIP's files to Replit.
2. Put the bot token in Replit Secrets as `DISCORD_TOKEN`.
3. Run `main.py`.
4. Invite the bot with Manage Channels and Manage Roles.
5. Run `!setup_hub` in the Hub server as an administrator.

It creates the renamed ICRP Hub roles, categories, text channels and voice channels represented by the supplied screenshots. Matching existing channel/role names are skipped to reduce duplicates.

Sensitive role permissions are intentionally not auto-granted. Review the final Discord permission hierarchy yourself.
