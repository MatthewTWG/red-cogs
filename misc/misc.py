import logging
from typing import List

import discord
from redbot.core import commands
from redbot.core.utils.mod import get_audit_reason

log = logging.getLogger("red.misc")


class Misc(commands.Cog):
    """Miscellaneous server utilities."""

    def __init__(self, bot):
        self.bot = bot

    async def red_delete_data_for_user(self, **kwargs):
        """Nothing to delete"""
        return

    @staticmethod
    def pass_hierarchy_check(ctx: commands.Context, role: discord.Role) -> bool:
        """
        Determines if the bot has a higher role than the given one.
        """
        return ctx.guild.me.top_role > role

    @staticmethod
    def pass_user_hierarchy_check(ctx: commands.Context, role: discord.Role) -> bool:
        """
        Determines if a user is allowed to add/remove/edit the given role.
        """
        return ctx.author.top_role > role or ctx.author == ctx.guild.owner

    @commands.group(invoke_without_command=True)
    @commands.guild_only()
    @commands.admin_or_permissions(manage_roles=True)
    async def massrole(self, ctx: commands.Context):
        """Mass role management commands."""
        await ctx.send_help()

    @massrole.command(name="add")
    async def massrole_add(self, ctx: commands.Context, role: discord.Role):
        """
        Add a role to all members in the server.

        Use double quotes if the role contains spaces.
        """
        if not self.pass_user_hierarchy_check(ctx, role):
            await ctx.send(
                f"I cannot let you add {role.name} because that role is higher than or equal to your highest role in the Discord hierarchy."
            )
            return

        if not self.pass_hierarchy_check(ctx, role):
            await ctx.send(
                f"I cannot give {role.name} to members because that role is higher than or equal to my highest role in the Discord hierarchy."
            )
            return

        if not ctx.guild.me.guild_permissions.manage_roles:
            await ctx.send('I need the "Manage Roles" permission to do that.')
            return

        members = [m for m in ctx.guild.members if not m.bot and m.get_role(role.id) is None]

        if not members:
            await ctx.send(f"All non-bot members already have the {role.name} role.")
            return

        progress_msg = await ctx.send(f"Adding {role.name} to {len(members)} members...")

        success_count = 0
        failed_count = 0
        reason = get_audit_reason(ctx.author)

        for member in members:
            try:
                await member.add_roles(role, reason=reason)
                success_count += 1
            except discord.Forbidden:
                failed_count += 1
                log.warning(f"Failed to add {role.name} to {member} due to permissions")
            except discord.HTTPException as e:
                failed_count += 1
                log.error(f"Failed to add {role.name} to {member}: {e}")

        result_msg = f"Added {role.name} to {success_count} members."
        if failed_count > 0:
            result_msg += f"\nFailed to add role to {failed_count} members."

        await progress_msg.edit(content=result_msg)

    @massrole.command(name="remove")
    async def massrole_remove(self, ctx: commands.Context, role: discord.Role):
        """
        Remove a role from all members in the server.

        Use double quotes if the role contains spaces.
        """
        if not self.pass_user_hierarchy_check(ctx, role):
            await ctx.send(
                f"I cannot let you remove {role.name} because that role is higher than or equal to your highest role in the Discord hierarchy."
            )
            return

        if not self.pass_hierarchy_check(ctx, role):
            await ctx.send(
                f"I cannot remove {role.name} from members because that role is higher than or equal to my highest role in the Discord hierarchy."
            )
            return

        if not ctx.guild.me.guild_permissions.manage_roles:
            await ctx.send('I need the "Manage Roles" permission to do that.')
            return

        members = [m for m in ctx.guild.members if m.get_role(role.id) is not None]

        if not members:
            await ctx.send(f"No members have the {role.name} role.")
            return

        progress_msg = await ctx.send(f"Removing {role.name} from {len(members)} members...")

        success_count = 0
        failed_count = 0
        reason = get_audit_reason(ctx.author)

        for member in members:
            try:
                await member.remove_roles(role, reason=reason)
                success_count += 1
            except discord.Forbidden:
                failed_count += 1
                log.warning(f"Failed to remove {role.name} from {member} due to permissions")
            except discord.HTTPException as e:
                failed_count += 1
                log.error(f"Failed to remove {role.name} from {member}: {e}")

        result_msg = f"Removed {role.name} from {success_count} members."
        if failed_count > 0:
            result_msg += f"\nFailed to remove role from {failed_count} members."

        await progress_msg.edit(content=result_msg)
