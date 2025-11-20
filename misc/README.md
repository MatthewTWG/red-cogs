# Misc

Miscellaneous server utilities including mass role management.

## Features

- **Mass Role Management**: Add or remove roles from all server members at once
- Hierarchy checks for both bot and user permissions
- Progress tracking with live updates
- Detailed success/failure reporting
- Excludes bots from role additions
- Audit log integration

## Commands

### `[p]massrole add <role>`
Add a role to all non-bot members in the server who don't already have it.

**Example:**
```
[p]massrole add @Member
[p]massrole add "Event Participant"
```

**Requirements:**
- User must have "Manage Roles" permission or be an admin
- Bot must have "Manage Roles" permission
- Role must be lower than both the bot's and user's highest role

### `[p]massrole remove <role>`
Remove a role from all members in the server who currently have it.

**Example:**
```
[p]massrole remove @OldEvent
[p]massrole remove "Temporary Access"
```

**Requirements:**
- User must have "Manage Roles" permission or be an admin
- Bot must have "Manage Roles" permission
- Role must be lower than both the bot's and user's highest role

## Notes

- The bot will skip any members it cannot modify due to permission issues
- A progress message will be displayed and updated with the final count
- All role changes are logged in the server's audit log with the command author as the reason
- Bots are automatically excluded from the `add` command
