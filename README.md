# Magma Manager v2.0.1

Production release of the modular Discord management bot for **Magma Nodes™**.

## Included systems

- **Tickets:** professional panel and ticket overview, one reason field, creator/SkyKing ping, claim, close, reopen, transcript, delete confirmation, and automatic deletion after 48 hours without a human message.
- **Staff applications:** public apply panel, status checks, open/close controls, persistent reviewer buttons, accept/reject/more-information/interview workflow, logs, cooldowns, and DM results.
- **Invite tracking:** Join, Leave, Fake, Rejoin (7 days), Valid count, leaderboard, sync, reset, and manual credits.
- **Announcements:** preview, send immediately, schedule, list, cancel, role/everyone ping, image and link-button support.
- **DM system:** staff DM to one user, open-Discord-DM or bot-opt-in mass audiences, member notification preferences, delivery records, and rate-safe campaigns.
- **AI assistant:** native Gemini REST support, `/ai ask`, `$ask`, test/status tools, ticket summaries, reply suggestions, translation, limits, redaction, and safe provider errors.
- **Security:** anti-spam, anti-link, anti-mass-mention, anti-raid, anti-nuke monitoring, whitelist, security logs, emergency lockdown, and permission restoration.
- **Backups:** checksum-protected guild configuration backups with create, list, export, restore and delete tools.
- **Operations:** professional embeds, error IDs, category-aware logging, persistent views, MongoDB indexes, command-change detection, diagnostics, reminders, birthdays, privacy requests, temporary voice channels and statistics.


## v2 Plan Sales Panels

Magma Manager v2 replaces the old public `/plans` browser with administrator-configured plan panels. Each plan gets its own setup command and public button:

```text
/plan-budget      | $!plan-budget
/plan-premium     | $!plan-premium
/plan-vps         | $!plan-vps
/plan-webhost     | $!plan-webhost
/plan-bothost     | $!plan-bothost
/plan-services    | $!plan-services
```

Run a command such as `$!plan-budget #plans`, then use the setup view to choose the channel, edit the title/description/button text, preview it, and post/update the panel. The full plan stays in the matching file under `/plans` and is sent privately when a member clicks the button.

Members must first use the **Bind Bot DMs** panel. If they are not bound, only that member receives an ephemeral instruction pointing to the configured DM-accept channel; the plan is not shown publicly.

## Requirements

- Python 3.11 or newer; Python 3.12 is recommended.
- MongoDB Atlas or another TLS-capable MongoDB deployment.
- Discord bot token and application ID.
- Privileged **Server Members Intent** and **Message Content Intent** enabled in the Discord Developer Portal.

## Pterodactyl installation

1. Stop the existing bot.
2. Back up the current `.env` file.
3. Extract this ZIP directly into `/home/container` and overwrite the old project files.
4. Keep the existing `.env`; compare it with `.env.example` and add any missing variables.
5. Set the startup values:

```text
PY_FILE=main.py
REQUIREMENTS_FILE=requirements.txt
AUTO_UPDATE=0
PY_PACKAGES=
```

6. Start the server. Successful startup includes:

```text
Starting Magma Manager build 2.1.0
Connected to MongoDB database magma_manager
Logged in as Magma Manager
```

The project structure must be `/home/container/main.py`, `/home/container/cogs`, `/home/container/core`, and so on. Do not leave everything inside an extra `MagmaBot_v1.2.4` folder.

## Environment

Copy `.env.example` to `.env` for a new installation. Never share the real token, MongoDB URI, API key or password.

Recommended Gemini configuration:

```env
AI_PROVIDER=gemini
AI_API_KEY=YOUR_GEMINI_API_KEY
AI_MODEL=gemini-3.6-flash
AI_BASE_URL=
```

The native Gemini adapter chooses the official Gemini API base automatically. A custom base URL is optional.

Set the user who should be pinged in every new ticket:

```env
TICKET_PING_USER_ID=DISCORD_USER_ID_OF_SKYKING_10
```

Slash commands are synchronized automatically when their structure changes. Set `FORCE_COMMAND_SYNC=1` for one restart only when Discord still shows an old command list, then return it to `0`.

## First-time server setup

Use these administrator commands after the bot is online:

```text
/setup
/staffapply panel
/ai test
/security log-channel
/security configure
/security thresholds
/security enable
```

Security starts disabled so it cannot moderate members before you review its settings. Test it in a private channel before enabling automatic actions.

## Main commands

### Tickets

```text
/ticket panel
/ticket delete
/ticket delete-transcript
$!ticket-delete
$!ticket-delete-transcript
```

Every current and migrated ticket receives the compact staff panel: **Lock**, **Unlock**, **Claim**, **Delete**, and **Delete & Transcript**. Professional HTML transcripts are delivered to the configured transcript channel and directly attempted to the ticket owner before transcript-based deletion.

### Staff applications

```text
/staffapply setup
/staffapply logs channel:#staff-application-logs
/staffapply panel
/staffapply apply
/staffapply status
/staffapply pending
/staffapply review application_id:STAFF-XXXX
/staffapply repost application_id:STAFF-XXXX
/staffapply open
/staffapply close
```

Use **Staff Application Setup → Review Logs → Create Private Logs** for the easiest Appy-style setup. Every new submission will include the applicant overview, all answers and review buttons. Applications submitted before the logs channel was configured can be recovered with `/staffapply pending` and `/staffapply repost`.

### Invites

```text
/invites stats
/invites leaderboard
/invites sync
/invites remove member:@User amount:1
/invites reset
/reset invited
/remove invite member:@User amount:1
$!invites
$!leaderboard
$!invites-sync
$!reset-invites
$!remove-invite @User 1
```

The reset command keeps Discord invite links active but sets tracked statistics to zero using a per-invite-code baseline. Removing credit is limited to the member's current valid balance, so it cannot create hidden debt against future invites. The bot needs **Manage Server** to read invite usage. Historical Leave, Fake and Rejoin data that was never tracked cannot be reconstructed.

### Announcements

```text
/announcement preview
/announcement send
/announcement schedule
/announcement edit
/announcement list
/announcement cancel
```

### DMs

```text
/dm enable
/dm disable
/dm user
/dm all
```

Mass DM supports **Open Discord DMs** and **Bot opt-ins**. Open-DM mode does not require `/dm enable`; it attempts delivery to every non-bot member. Discord does not expose the privacy toggle directly, so closed DMs or blocked bots are counted as failed deliveries instead of crashing the campaign.

### AI

```text
/ai ask
/ai test
/ai status
$ask your question
$ai-test
$ai-status
```

### Security

```text
/security status
/security configure
/security thresholds
/security whitelist-add
/security whitelist-remove
/security log-channel
/security events
/security server-protection
/security lockdown
/security unlock
```

### Backup and diagnostics

```text
/backup_create
/backup_list
/backup_restore
/backup_export
/backup_delete
/diagnostics
```

## Discord permissions

Use least privilege. Features may require View Channels, Send Messages, Embed Links, Attach Files, Read Message History, Manage Messages, Manage Channels, Manage Roles, Moderate Members, Manage Server, View Audit Log, Move Members and Manage Threads. The bot role must be above any member or role it needs to moderate or assign.

## Data and safety

- Secrets remain in environment variables and are excluded from exports and backups.
- AI responses are labelled as drafts and do not approve payments, refunds, applications or moderation decisions.
- Security actions are configurable and disabled by default.
- Unknown command failures return an error ID while the full traceback remains in the console.
- Backups are guild-scoped and checksum-validated before restoration.

## Development tests

Production dependencies are in `requirements.txt`. Test-only packages are in `requirements-dev.txt`.

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
pytest -q
python -m compileall -q .
```

## Release

This package is **Magma Manager v1.2.4**, not a beta build. See `CHANGELOG.md` and `DEPLOYMENT.md` for the release summary and upgrade checklist.

## Gemini model-format hotfix (v1.0.1)

Use the model ID only:

```env
AI_PROVIDER=gemini
AI_MODEL=gemini-3.6-flash
AI_BASE_URL=
```

If an older model value was saved in MongoDB, run `/ai reset-model`, then `/ai model gemini-3.6-flash`, followed by `/ai test`.

## Professional setup dashboards

Open the complete control centre with `$!setup` or `/setup`. Dedicated dashboards are also available through `/ticket setup`, `/staffapply setup`, `/security setup`, `/invites setup`, `/announcement setup`, `/dm setup`, `/backup_setup`, and `/setup logging`.

Every dashboard uses Magma branding, live settings overviews, buttons, status toggles, channel selectors, role selectors, and safe configuration forms.


## DM authorization panel

Post the persistent authorization panel with:

```text
/dm-accept channel:#dm-accept
```

The compatibility alias `/dm-accpet` also works. Members press **Bind Bot DMs** once to bind their account and enable every ticket, application, delivery, order, payment, deal, giveaway, maintenance, and security notification category. Discord privacy settings must still allow the bot to send a direct message.

## Staff application flow

The staff form contains 12 clear questions across three saved steps. Each step saves automatically. After the final step, the member sees **Application filled successfully** and can press **Submit Application**.


## v1.2.0 feature update

### AFK system

- `$afk <reason>` or `/afk set` stores the reason and start time.
- Mentioning an AFK member shows their reason and time away.
- The first message from the AFK member removes AFK automatically and sends a branded welcome-back message.

### Enhanced staff applications

- Twelve clear questions are split into three Discord-safe modal steps.
- Answers save after each step.
- Applicants can edit the previous step, preview every answer, and confirm submission.
- Reviewers receive a professional overview with account age, server join time, and review controls.

### Verified DM binding

Post the panel with `/dm-accept channel:#dm-accept`. Members press **Bind Bot DMs**. The bot first sends a test DM; only successful delivery creates the saved binding. Staff can then use `/dm user` and administrators can use the bound mass-DM audience. Discord privacy settings can still block delivery later.


## Enhanced security (v1.2.1)

Magma Security now includes anti-spam, duplicate-message detection, anti-link, anti-invite, mass-mention protection, dangerous-file filtering, anti-raid, new-account alerts and expanded anti-nuke monitoring. Registered ticket channels can still receive normal support links when `ticket_links_allowed` is enabled.

Useful commands:

```text
/security setup
/security health
/security ticket-links allowed:true
/security allow-link-channel channel:#links
/security allow-domain domain:example.com
/security log-channel channel:#security-logs
```

## v2.0.1 DM Verify

DM Verify panel can be configured from `/setup` → **Mass DM** using the channel selector.
Admins can also use `/dm verify-panel`, `/dm-accept`, or `$!dm-verify #channel`.

## v2.1.0 Community Panels

The old Server Moved and CEO Recovery extensions were removed.

Use `/setup` and open **Invites** to select a channel and post a persistent **Check My Invites** button. Members receive Join, Leave, Fake, Rejoin (7 days), Adjustment, and Valid counts ephemerally.

Use `/setup` and open **Reviews** to select a review channel and post a persistent **Write a Review** button. Members rate 1–5 stars and add a description. Reviews show the member name, stars, description, and a Write a Review button. The main panel automatically shows the live overall average such as **4.5/5** and total review count. One member has one review and submitting again updates it.

Admin shortcuts: `$!review-setup` and `/magma reviews`.
