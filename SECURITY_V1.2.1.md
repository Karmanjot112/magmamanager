# Magma Security v1.2.1

## Ticket-safe links

Registered ticket channels are detected from the `tickets` collection. When **Ticket links** is enabled, members can send normal website, control-panel, deployment, log and support URLs inside tickets even if public-channel anti-link is enabled.

Dangerous executable/script attachments are still checked separately.

## New protection

- General message flood detection
- Duplicate-message spam detection
- Discord invite blocking
- General anti-link with trusted domains
- Mass-mention protection
- Dangerous attachment filtering
- New-account join alerts
- Rapid-join anti-raid lockdown
- Expanded anti-nuke monitoring
- Professional event IDs and security logs

## Recommended commands

```text
/security setup
/security health
/security log-channel channel:#security-logs
/security ticket-links allowed:true
/security allow-link-channel channel:#advertisements
/security allow-domain domain:yourpanel.example
/security enable
```

Use a non-administrator test account before enabling security for the whole server.
