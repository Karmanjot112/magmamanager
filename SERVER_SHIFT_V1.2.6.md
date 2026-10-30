# Magma Manager v1.2.6 — Shift Restore Reliability Fix

## What was fixed

- `$!shift` no longer aborts the complete restore when one Discord role, category, channel, forum, icon, or permission set returns `HTTPException`.
- Each object is restored independently. Unsupported properties are retried with a simplified safe fallback.
- Restore output now shows the first exact Discord HTTP status/code for skipped items.
- `$!shift` is retry-safe: role/channel mappings are saved and reused instead of creating duplicates after a partial restore.
- v1.2.5 snapshot compatibility was added for common legacy snapshot field/collection names.
- Snapshot chat history and bot data are chunked into separate MongoDB documents to avoid the MongoDB 16 MB document limit.
- Added `$!shift-status`.
- 12-hour invite bridge remains available when the bot stays in both servers.

## Ticket 10003 fix

Ticket creation now verifies that a newly created channel still exists before posting the ticket UI. If Discord returns `10003 Unknown Channel`, Magma Manager recreates the ticket channel once and updates MongoDB. If another bot/rule deletes the retry as well, the stale ticket record is removed and the user gets a clear Audit Log message.

## Commands

- `$!shift-copy` — snapshot with 200 messages per readable text channel.
- `$!shift-copy 500` — custom history limit, maximum 1000 per channel.
- `$!shift` — restore in the new server.
- `$!shift-status` — show snapshot/restore/bridge state.

## Permissions

For migration, the user running the command must be the server owner or have Discord Administrator. Magma Manager must have Manage Roles and Manage Channels; Administrator is recommended during migration.
