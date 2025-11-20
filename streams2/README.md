# Streams

Enhanced stream notification cog for Twitch, YouTube, and Picarto with platform-specific role mentions.

## Features

- Monitor Twitch, YouTube, and Picarto streams
- Get notified when streams go live
- **Platform-specific role mentions** - Configure different roles to be mentioned for Twitch vs YouTube vs Picarto streams
- Customizable alert messages
- Auto-delete alerts when stream goes offline
- Ignore reruns and scheduled streams (Twitch)

## Main Changes from Core Cog

This is an enhanced version of the core Red-DiscordBot Streams cog with the following additions:

- **Separate role mentions per platform**: Use `[p]streamalert role twitch` and `[p]streamalert role youtube` to configure different roles for each platform
- Each role can have independent mention settings for Twitch, YouTube, and Picarto
- Falls back to general role mention setting if platform-specific setting is not configured

## Usage

Configure stream alerts:
```
[p]streamalert twitch <channel_name> #discord-channel
[p]streamalert youtube <channel_id> #discord-channel
[p]streamalert picarto <channel_name> #discord-channel
```

Configure platform-specific role mentions:
```
[p]streamalert role @RoleName          # Toggle general mention
[p]streamalert role twitch @RoleName   # Toggle Twitch-specific mention
[p]streamalert role youtube @RoleName  # Toggle YouTube-specific mention
[p]streamalert role picarto @RoleName  # Toggle Picarto-specific mention
```

## Commands

- `[p]streamalert` - Manage stream alerts
- `[p]streamset` - Configure stream settings
- `[p]streams` - List currently live streams

## Credits

Based on the Streams cog from [Red-DiscordBot](https://github.com/Cog-Creators/Red-DiscordBot)
