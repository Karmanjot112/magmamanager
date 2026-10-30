# Ticket Queue — v1.2.4

New tickets automatically enter the standard queue. Priority tickets sort before standard tickets.

## Slash commands
- `/queue list` — show up to 25 waiting tickets.
- `/queue add` — add/re-add the current ticket.
- `/queue remove` — remove the current ticket from waiting queue.
- `/queue priority enabled:true` — put current ticket in priority queue.
- `/queue priority enabled:false` — return it to standard queue.

## Prefix commands
- `$!queue`
- `$!add-queue`
- `$!remove-queue`
- `$!priority-queue on`
- `$!priority-queue off`

Claimed, closed, archived, and deleted tickets are not shown in the waiting queue.
