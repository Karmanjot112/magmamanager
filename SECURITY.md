# Security Notes

- Keep Discord tokens, MongoDB URIs, API keys and passwords only in `.env` or Pterodactyl variables.
- Rotate any credential pasted into a public channel or shared screenshot.
- Give the bot only the permissions needed for enabled features.
- Keep the bot role below the server owner and above only the roles it must manage.
- Review `/security configure` and `/security thresholds` before enabling automatic moderation.
- Whitelist trusted automation accounts that legitimately post links or frequent messages.
- Test lockdown and unlock in a test server first.
- Protect exported backups because they may contain server configuration and IDs, though secrets are filtered.


## v1.2.1 message and ticket protection

- Registered ticket channels bypass anti-link and anti-invite rules only when **Ticket links** is enabled.
- Dangerous executable/script attachments remain protected even inside tickets.
- Use channel and domain allow-lists instead of disabling anti-link for the whole server.
- New-account detection creates an alert only; it does not automatically kick or ban the member.
- Anti-nuke requires View Audit Log and a bot role placed above manageable staff roles.
- Run `/security health` after changing the bot's permissions or role position.
