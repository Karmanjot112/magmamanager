# Magma Manager v1 Deployment Checklist

## Upgrade from a beta build

1. Stop the Pterodactyl server.
2. Download a backup of `.env` and any local files you edited.
3. Upload and extract the v1 ZIP into `/home/container` with overwrite enabled.
4. Restore your existing `.env`; do not replace it with `.env.example`.
5. Add missing variables from `.env.example`, especially `TICKET_PING_USER_ID` and `FORCE_COMMAND_SYNC`.
6. Start the bot and verify `Starting Magma Manager build 1.2.4` appears.
7. Run `/diagnostics`, `/ai test`, `/invites sync`, and `/security status`.
8. Post a fresh `/ticket panel` and `/staffapply panel` if old messages use obsolete component IDs.
9. Configure the security log channel and test security before enabling it.


## Staff applications and DM authorization

1. Configure the staff review channel with `/staffapply setup`.
2. Post a new panel using `/staffapply panel`.
3. Create a `dm-accept` channel and run `/dm-accept channel:#dm-accept`.
4. Members press **Bind Bot DMs** once to connect and enable every notification type.
5. Set `AI_MODEL=gemini-3.6-flash` in the environment when using Gemini.

## Command refresh

The bot normally detects command changes and syncs automatically. When commands are still missing:

1. Set `FORCE_COMMAND_SYNC=1` in Startup/environment variables.
2. Restart once and wait for the console sync message.
3. Return `FORCE_COMMAND_SYNC=0` and restart normally later.

## Open Discord DM audience

1. Run `/dm setup`.
2. Press **Audience: Bound** to switch it to **Audience: Open DMs**.
3. Use `/dm all` and set `confirm_open_dms: True`, or use the setup modal and type `SEND`.
4. For prefix commands, use `$dm-all CONFIRM your message`.

The bot cannot read Discord's **Allow Direct Messages** toggle directly. It attempts delivery and reports closed DMs or blocked bots as failed. Keep broadcasts relevant and infrequent.

## Rollback

Stop the bot, restore the previous source ZIP and the preserved `.env`, then restart. MongoDB records are retained. Configuration backups created by v1 are versioned and checksum-protected.

## Troubleshooting

- **Bot starts but slash commands are missing:** verify `DEVELOPMENT_GUILD_ID`, the `applications.commands` invite scope and force one command sync.
- **Buttons say interaction failed:** use a newly posted panel and inspect the console for the error ID.
- **Invites show zero:** grant Manage Server and run `/invites sync`.
- **AI fails:** run `/ai test` and verify provider, key and model variables.
- **Security does nothing:** it is intentionally disabled until `/security enable` is used.
- **MongoDB fails:** verify Atlas Network Access, database-user credentials and TLS connectivity.


## After upgrading to Magma Manager v1.2.4

1. Run `/dm-accept channel:#dm-accept` again when you need a fresh **Bind Bot DMs** panel.
2. Existing AFK records and draft staff applications continue working.
3. Run `/reset invited` only when you intentionally want every tracked invite statistic to start from zero.
4. Configure the transcript channel from `/ticket setup` or the logging dashboard before using **Delete & Transcript**.
5. Use `FORCE_COMMAND_SYNC=1` for one restart if the new invite or security commands do not appear, then return it to `0`.


## Enhanced security setup

1. Run `/security setup` and review every toggle before enabling security.
2. Keep **Ticket links** enabled so members can send deployment URLs and support links inside registered tickets.
3. Run `/security health` and grant any missing permissions.
4. Use `/security allow-link-channel channel:` for trusted public channels.
5. Use `/security allow-domain domain:` for trusted websites such as your panel or store domain.
6. Set the security log channel with `/security log-channel`.
7. Test with a non-administrator account before using `/security enable`.
