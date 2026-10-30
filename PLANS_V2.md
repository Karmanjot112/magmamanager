# Magma Manager v2 Plan Panels

The old `/plans` browse menu was replaced by administrator-configured sales panels.

## Configuration commands

- `/plan-budget` or `$!plan-budget`
- `/plan-premium` or `$!plan-premium`
- `/plan-vps` or `$!plan-vps`
- `/plan-webhost` or `$!plan-webhost`
- `/plan-bothost` or `$!plan-bothost`
- `/plan-services` or `$!plan-services`

You can optionally mention the destination channel in the prefix command, for example:

`$!plan-budget #plans`

The setup view lets an administrator choose the destination channel, edit the public title/description/button label, preview the panel, and post/update it.

## Member delivery

The public panel only shows a short designed description and a button. The full plan is read live from the matching file in `/plans` and sent by DM.

If the member has not used **Bind Bot DMs**, the plan is not exposed publicly. Only that member sees an ephemeral message directing them to the configured DM connection channel. If no DM connection channel is configured, the private warning tells them to contact staff.

Plan content files:

- `plans/budget.txt`
- `plans/premium.txt`
- `plans/vps.txt`
- `plans/web_host.txt`
- `plans/bot_host.txt`
- `plans/services.txt`
