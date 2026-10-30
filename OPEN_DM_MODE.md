# Open Discord DM Mode

Magma Manager v1.1.0 supports two mass-DM audiences. The safe server default is `opted_in`:

- `open_dms`: attempt delivery to every non-bot server member. No `/dm enable` opt-in is required.
- `opted_in`: send only to members who enabled the chosen bot notification category.

Discord does not expose the **Allow Direct Messages** toggle through the bot API. The bot therefore attempts each DM. A successful request is counted as delivered; closed DMs, privacy restrictions, or a blocked bot are counted as failed.

Configure the server default with `/dm setup`, or override it with the `audience` option in `/dm all`.


## Authorization panel

Use `/dm-accept channel:#dm-accept` to post the persistent opt-in panel. The `/dm-accpet` typo alias is also supported.
