# Magma Manager v2.1.0

- Removed the Server Moved system and all `/server moved` / `$!server-moved` commands.
- Removed the CEO Recovery system and all `/ceo` / `$!ceo-*` commands.
- Added an Invite Check public panel configurable from `/setup` → **Invites**.
- Added persistent **Check My Invites** button with private invite statistics.
- Added `/setup` → **Reviews** with configurable review channel.
- Added persistent **⭐ Write a Review** button with 1–5 rating and description modal.
- Reviews show stars, reviewer name, description and an attached review button.
- Review panel automatically updates the overall average (for example 4.5/5) and total reviews.
- Added `/magma reviews` and `$!review-setup`.

## 2.0.4 — CEO Bot Removal

- Added `/ceo remove` and `$!ceo-remove` for removing a bot by Discord user ID.
- Requires the existing CEO recovery authorization: server owner/`OWNER_IDS` plus the recovery code.
- Refuses human targets, Magma Manager itself, and bots above/equal to Magma Manager in role hierarchy.
- Records every removal attempt in `ceo_recovery_events`.

## 2.0.3 — CEO Recovery Startup Hotfix

- Fixed Discord.py Cog startup crash caused by Python callback method names beginning with reserved `bot_`.
- Renamed internal CEO bot-report callbacks while keeping `/ceo bot-report` and `$!ceo-bot-report` command names unchanged.
- No `.env` changes required.

# Magma Manager v2.0.1

## Fixed
- Restored DM verification/binding configuration inside `/setup` → **Mass DM**.
- Added a DM Verify channel selector and **Repost DM Verify** button.
- Kept `/dm-accept`, `/dm-accpet`, and added `/dm verify-panel` + `$!dm-verify`.

## Added
- One-time `/server moved code:<code>` emergency migration command.
- Successful activation creates `#new-server-link`, pings `@everyone`, posts the new-server invite, then removes all other channels.
- Activation code is stored only as a SHA-256 hash in source and is permanently consumed in MongoDB.
- `$!server-moved <code>` prefix compatibility command.


# Changelog

## 2.0.0 — Configurable plan sales panels

- Replaced the old `/plans` browse command with dedicated administrator setup commands: `/plan-budget`, `/plan-premium`, `/plan-vps`, `/plan-webhost`, `/plan-bothost`, and `/plan-services`.
- Added matching prefix commands such as `$!plan-budget` and `$!plan-premium`.
- Each setup opens a designed configuration view with channel selection, editable title, description and button text, preview, and Post / Update Panel.
- Public plan panels show only the designed summary and a persistent delivery button.
- Full plan content is read live from the files under `plans/` and delivered privately by DM.
- Members must be bound through the bot-DM panel before plan delivery. Unbound members see only an ephemeral instruction pointing them to the configured DM-accept channel.
- Added persistent plan buttons so published panels continue working after bot restarts.

## 1.2.8 — File-driven plans command

- Added `/plans` with Budget, Premium, VPS, Web Hosting, Bot Hosting and Services categories.
- Added `$!plans` and direct category syntax such as `$!plans budget`; `$plans` and `@!plans` also work.
- Added an interactive professional plan selector.
- Added editable plain-text files under `plans/`; changes are read live without restarting the bot.
- Added the supplied Magma Budget pricing and feature list.
- Added safe placeholders for categories whose prices were not supplied.

## 1.2.6 — Shift restore reliability hotfix

- Rebuilt server shift restore as a fault-tolerant, per-object migration.
- A single Discord `HTTPException` no longer cancels the entire `$!shift`.
- Added simplified fallback creation for roles, categories, text/voice/stage/forum channels.
- Added saved restore mappings so `$!shift` can be safely retried after a partial restore.
- Added legacy v1.2.5 snapshot compatibility and `$!shift-status`.
- Split chat history and bot-data snapshots into MongoDB chunks.
- Preserved the 12-hour invite-stat bridge.
- Added ticket `10003 Unknown Channel` detection and one-time ticket-channel recreation.

# Magma Manager v1.2.4 — Ticket Queue

- Every newly created ticket automatically joins the standard queue.
- Priority queue places urgent tickets before normal tickets.
- Added `/queue list`, `/queue add`, `/queue remove`, `/queue priority`.
- Added prefix commands `$!queue`, `$!add-queue`, `$!remove-queue`, `$!priority-queue`.
- Claim removes a ticket from the waiting queue; unclaim/reopen re-adds it.
- Staff ticket panel now includes a persistent Priority Queue button.
- Queue position is shown when a ticket is created.
- Existing open tickets are migrated to the queue on startup.
- Corrected leftover Shadow ticket component IDs back to Magma Manager IDs.

# Magma Manager v1.2.3

## Enhanced invites, tickets, transcripts, staff reviews and security

- Added `/reset invited`, `/remove invite`, `/invites reset`, `/invites remove`, `$!reset-invites`, and `$!remove-invite`.
- Invite reset keeps real Discord invite links and starts tracked totals from zero.
- Invite removals never create hidden negative invite debt.
- Rebuilt the ticket staff panel with Lock, Unlock, Claim, Delete, and Delete & Transcript.
- Professional HTML transcripts are delivered to the ticket owner and configured transcript channel.
- Delete & Transcript stops deletion when no transcript copy can be delivered and provides a recovery attachment.
- Staff review embeds now show the applicant mention, display name, username and user ID.
- Added anti-webhook nuke, anti-kick nuke and suspicious permission-escalation protection.
- Product identity remains Magma Manager with Magma Nodes™ branding.

## 1.1.0 — Invite controls, professional tickets, transcripts and security

- Added staff invite commands: `/reset invited`, `/remove invite`, `/invites reset`, `/invites remove`, `$!reset-invites`, and `$!remove-invite`; removals are clamped to the current valid balance.
- Invite reset now stores a per-invite-code Discord-use baseline, so old counters do not return and newly created invite links count immediately.
- Rebuilt the ticket staff panel with Lock, Unlock, Claim, Delete, and Delete & Transcript controls.
- Added ticket lock/unlock permission handling and smart claim/unclaim behaviour.
- Added professional self-contained HTML transcripts with ticket metadata, avatars, attachments and message history.
- Transcripts are sent to the configured transcript channel and directly attempted to the ticket owner.
- Delete & Transcript refuses deletion when no transcript copy was delivered and gives staff a recovery file.
- Staff application review logs now resolve and display the applicant mention, display name, username and ID.
- Enhanced security with webhook protection, kick-nuke detection and suspicious permission-escalation rollback.
- Added `/security server-protection` and `$!security-server-protection`.

## 1.0.0 — Appy-style staff application review logs

- Added `/staffapply logs` to set a private application review channel directly.
- Added a **Create Private Logs** button inside Staff Application Setup.
- Completed applications now post the applicant overview and every answer in the review channel.
- Added Claim, View Full Application, Request Information, Interview, Accept, Reject, Blacklist and Internal Note controls.
- Review messages update automatically when an application is claimed or decided.
- Added `/staffapply pending` to show the active review queue.
- Added `/staffapply review` to open any application by ID.
- Added `/staffapply repost` to recover applications that were submitted before a review channel was configured.
- Added delivery status tracking for missing channels and missing Discord permissions.
- Final application decisions disable further action buttons while keeping the full review record visible.

## 1.2.1 — Enhanced security and ticket-safe links

- Registered ticket channels can now send website, panel, deployment and support links even when anti-link is enabled.
- Added separate anti-invite, duplicate-message spam and dangerous-file protection.
- Added trusted link channels and trusted website domain allow-lists.
- Added new-account join alerts without automatically punishing legitimate members.
- Expanded anti-nuke monitoring to rapid channel creation, role creation and member bans.
- Improved message punishment: ordinary first link violations are removed first; repeated or serious violations can trigger the configured timeout.
- Added `/security health` to verify required Discord permissions and role placement.
- Added professional security warnings with event IDs and clearer action details.
- Optimized ticket detection so MongoDB is queried only when a message contains a link.
- Updated Ticket Setup and Security Setup dashboards with the new controls and live status.

## 1.2.0 — AFK, staff applications, and verified DM binding

- AFK mentions now show the member's reason and exact AFK duration.
- Sending any message automatically removes AFK, restores the nickname, and posts a branded welcome-back message with hours/minutes.
- Staff applications now use 12 understandable questions across three auto-saved steps.
- Added review answers, edit previous step, professional submit confirmation, and safer application review embeds.
- Staff reviewers can request information, interview, or reject; accepting and blacklisting remain administrator-only.
- The DM panel now verifies delivery before marking a member as bound.
- Bound members are saved with a DM channel ID and can receive `/dm user` and bound-audience mass DMs.
- Unbinding removes authorization, categories, and the saved DM channel.
- Added clearer professional branding throughout AFK, application, and DM flows.

## 1.1.2 — Staff application and DM authorization

- Replaced the staff application with 10 clear, understandable questions.
- Fixed step progression that previously trapped applicants on the same page.
- Added a clear “Application filled” state and reliable submission confirmation.
- Application submission now remains successful even if the review channel cannot be posted to.
- Added persistent `/dm-accept` authorization panel with enable, status, and disable buttons.
- Added `/dm-accpet` compatibility alias for the common typo.
- Clicking Enable Bot DMs opts the member into every notification category and sends a test DM.
- Added branded review and authorization embeds.
- Updated the Gemini default to `gemini-3.6-flash`; legacy 2.0/2.5 Flash values migrate automatically.
- Removed deprecated sampling parameters from Gemini 3.5/3.6 requests.

## 1.1.1 — Open Discord DM Audience

- Added an **Audience: Open DMs / Opted-in** toggle to `/dm setup` with `opted_in` kept as the safe default.
- Added an `audience` choice to `/dm all`.
- Open-DM mode, when deliberately selected and confirmed, attempts delivery to every non-bot server member without requiring `/dm enable`.
- `/dm user` now attempts direct delivery without requiring a bot-specific opt-in.
- Discord-closed DMs and blocked bots are counted as failed deliveries.
- Preserved opt-in preferences for automated ticket/application alerts and opt-in broadcasts.
- Added rate-limited delivery reports with targeted, delivered, failed, and skipped counts.

## 1.1.0 — Professional Setup UI

- Added a branded control centre for all major Magma Manager modules.
- Added live ticket, staff application, security, invite, announcement, DM, backup, logging and branding dashboards.
- Added buttons, toggles, role selectors, channel selectors and safe configuration modals.
- Ticket setup now shows limits, roles, routing, DM state, categories and the one-question member form.
- Security setup now shows rules, punishment, whitelist totals, status toggles and recent events.
- Added dashboard commands for each module while keeping existing management commands.
- Updated build identity from beta/hotfix builds to Magma Manager v1.1.0.

## v1.0.1 — Gemini model-format hotfix

### Fixed

- Normalizes plain model IDs, `models/...` resource names, quoted values, and copied full Gemini endpoint URLs.
- Prevents malformed model names from reaching the Gemini API.
- Adds `/ai reset-model` and `$ai-reset-model` to remove an old MongoDB model override.
- Shows the normalized model in AI status and provider-test responses.

## v1.0.0 — Production release

### Added

- Professional ticket overview and 48-hour inactivity deletion.
- Dedicated staff-application command group and public panel.
- Invite statistics for Join, Leave, Fake, Rejoin (7 days) and Valid.
- Announcement preview, immediate delivery and scheduled delivery.
- Member opt-in DM preferences, direct staff DM and mass DM campaigns.
- Native Gemini API adapter with health testing and clearer errors.
- Configurable anti-spam, anti-link, anti-mention, anti-raid and anti-nuke security.
- Emergency lockdown/unlock with saved permission restoration.
- Guild configuration backup v2 with checksum validation.
- Professional embed helpers, audit log IDs and user-facing error IDs.
- Command-tree change detection to avoid unnecessary Discord sync operations.

### Fixed

- Persistent ticket and application buttons after restarts.
- Ticket panel view missing its bot reference.
- Invalid modal labels and modal-to-modal interaction failures.
- Expired interactions during slower ticket/report operations.
- MongoDB TLS certificate handling and index conflicts.
- Duplicate null AI interaction IDs.
- Gemini HTTP 400 handling and model endpoint construction.
- Duplicate staff/knowledge decorators and reserved command method names.

### Changed

- Version reset from all beta packages to the first stable release: **v1.0.0**.
- Production requirements no longer install pytest packages on every startup.
- Security remains disabled until an administrator explicitly enables it.
## 2.0.2 — CEO Recovery Safety Patch

- Added owner-only `/ceo give`, `/ceo servers`, `/ceo bot-report`, and `/ceo audit`.
- Recovery code is a second factor only; `OWNER_IDS` or guild ownership is always required.
- Added temporary one-use guild invite DM report for recovery.
- Added audited CEO Recovery Administrator role, kept below the bot role.
- Added Security/Titanium bot inventory report without automatic bot removal.
