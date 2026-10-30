# Magma Manager Staff Application Review Logs

## Fast setup

1. Run `/staffapply setup`.
2. Open **Review Logs**.
3. Select an existing private channel or press **Create Private Logs**.
4. Configure the reviewer role and accepted staff role.
5. Post the public application panel.

Alternative command:

```text
/staffapply logs channel:#staff-application-logs
```

## Reviewing applications

Every completed application is posted with:

- Applicant mention, display name, username, user ID and account information
- Submission time and application status
- Every question and answer
- Claim/Unclaim controls
- View Full Application
- Request More Information
- Move to Interview
- Accept, Reject and Blacklist
- Private internal notes

Useful commands:

```text
/staffapply pending
/staffapply review application_id:STAFF-XXXX
/staffapply repost application_id:STAFF-XXXX
```

`repost` is used for older applications that were submitted while no review channel was configured.

## Required bot permissions in the review channel

- View Channel
- Send Messages
- Embed Links
- Read Message History

The optional **Create Private Logs** button also requires **Manage Channels**.
