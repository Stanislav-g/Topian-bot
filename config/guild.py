"""
MIT License
Copyright (c) 2020 GamingGeek

Permission is hereby granted, free of charge, to any person obtaining a copy of this software
and associated documentation files (the "Software"), to deal in the Software without restriction,
including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE
FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""


from .constants import ConfigOpt, DISCORD_CONVERTERS
from .errors import *
import discord
import inspect
import asyncio
import json


options = dict()


class Config:
    __slots__ = ('options', 'loaded', '_bot', '_guild', '_db', '_data')

    def __init__(self, guild, **kwargs):
        self.options = options
        self.loaded: bool = False
        self._bot = kwargs.pop('bot')
        self._guild = self._bot.get_guild(guild) or guild
        self._db = kwargs.pop('db')
        self._data = {}

    @ConfigOpt(name='main.prefix', accepts=str, default='$', options=options)
    async def prefix(self, value: str):
        '''Prefix | The prefix used before all Fire commands'''
        self._bot.logger.info(
            f'$GREENSetting $CYANmain.prefix $GREENto $CYAN{value} $GREENfor guild $CYAN{self._guild}')
        await self.update('main.prefix', value)

    @ConfigOpt(name='main.fetch_offline', accepts=bool, default=True, hidden=True, options=options)
    async def fetch_offline(self, value: bool):
        '''Fetch Offline | Manually set by Geek#8405 for larger guilds that do not need all members cached'''
        self._bot.logger.info(
            f'$GREENSetting $CYANmain.fetch_offline $GREENto $CYAN{value} $GREENfor guild $CYAN{self._guild}')
        await self.update('main.fetch_offline', value)

    @ConfigOpt(name='log.moderation', accepts=discord.TextChannel, default=None, options=options)
    async def mod_logs(self, value: discord.TextChannel):
        '''Moderation Logs | The channel where moderation actions are logged'''
        self._bot.logger.info(
            f'$GREENSetting $CYANlog.moderation $GREENto $CYAN{value} $GREENfor guild $CYAN{self._guild}')
        await self.update('log.moderation', value.id)

    @ConfigOpt(name='log.action', accepts=discord.TextChannel, default=None, options=options)
    async def action_logs(self, value: discord.TextChannel):
        '''Action Logs | The channel where miscellaneous actions are logged, e.g. deleted messages'''
        self._bot.logger.info(
            f'$GREENSetting $CYANlog.action $GREENto $CYAN{value} $GREENfor guild $CYAN{self._guild}')
        await self.update('log.action', value.id)

    @ConfigOpt(name='mod.mutedrole', accepts=discord.Role, default=None, options=options)
    async def muted_role(self, value: discord.Role):
        '''Muted Role | The role which will be used when muting a user. If not set, it will default to a role called "Muted"'''
        self._bot.logger.info(
            f'$GREENSetting $CYANmod.mutedrole $GREENto $CYAN{value} $GREENfor guild $CYAN{self._guild}')
        await self.update('mod.mutedrole', value.id)

    @ConfigOpt(name='mod.antieveryone', accepts=bool, default=None, options=options)
    async def anti_everyone(self, value: bool):
        '''Anti Everyone | Prevents those without permission from sending messages containing @everyone (as they're most likely just advertising/sending copypasta etc.'''
        self._bot.logger.info(
            f'$GREENSetting $CYANmod.antieveryone $GREENto $CYAN{value} $GREENfor guild $CYAN{self._guild}')
        await self.update('mod.antieveryone', value)

    @ConfigOpt(name='mod.linkfilter', accepts=[str], default=[], options=options)
    async def link_filter(self, value: list):
        '''Link Filter | The filters of which any links found will be deleted (unless they have Manage Messages)'''
        valid = ['discord', 'youtube', 'twitch', 'twitter',
                 'paypal', 'malware', 'shorteners', 'gifts']
        if any(v not in valid for v in value):
            raise TypeMismatchError(type=', '.join(
                [v for v in value if v not in valid]), accepted=', '.join(valid), option='mod.linkfilter')
        self._bot.logger.info(
            f'$GREENSetting $CYANmod.linkfilter $GREENto $CYAN{value} $GREENfor guild $CYAN{self._guild}')
        await self.update('mod.linkfilter', value)

    @ConfigOpt(name='excluded.filter', accepts=[int], default=[], options=options)
    async def filter_exclude(self, value: list):
        '''Filter Exclusion | Channel, role and user IDs that are excluded from link filters and duplicate message deletion'''
        self._bot.logger.info(
            f'$GREENSetting $CYANexcluded.filter $GREENto $CYAN{value} $GREENfor guild $CYAN{self._guild}')
        await self.update('excluded.filter', value)

    @ConfigOpt(name='mod.globalbans', accepts=bool, default=False, options=options)
    async def global_bans(self, value: bool):
        '''Global Bans | Global ban checking on member join, powered by KSoft.Si API'''
        self._bot.logger.info(
            f'$GREENSetting $CYANmod.globalbans $GREENto $CYAN{value} $GREENfor guild $CYAN{self._guild}')
        await self.update('mod.globalbans', value)

    @ConfigOpt(name='mod.autodecancer', accepts=bool, default=False, options=options)
    async def auto_decancer(self, value: bool):
        '''Auto Decancer | Renames those with "cancerous" names (non-ascii chars) to John Doe'''
        self._bot.logger.info(
            f'$GREENSetting $CYANmod.autodecancer $GREENto $CYAN{value} $GREENfor guild $CYAN{self._guild}')
        await self.update('mod.autodecancer', value)

    @ConfigOpt(name='mod.autodehoist', accepts=bool, default=False, options=options)
    async def auto_dehoist(self, value: bool):
        '''Auto Dehoist | Renames those with "hoisted" names (starts with non a-z char) to John Doe'''
        self._bot.logger.info(
            f'$GREENSetting $CYANmod.autodehoist $GREENto $CYAN{value} $GREENfor guild $CYAN{self._guild}')
        await self.update('mod.autodehoist', value)

    @ConfigOpt(name='mod.nospam', accepts=int, default=0, options=options)
    async def spam_prevention(self, value: int):
        '''Spam Prevention | Detect and delete spam using ChatWatch'''
        self._bot.logger.info(
            f'$GREENSetting $CYANmod.nospam $GREENto $CYAN{value} $GREENfor guild $CYAN{self._guild}')
        await self.update('mod.nospam', value)

    @ConfigOpt(name='mod.autorole', accepts=discord.Role, default=None, options=options, premium=True)
    async def auto_role(self, value: discord.Role):
        '''Auto Role (Premium) | The role given to users upon joining the server'''
        self._bot.logger.info(
            f'$GREENSetting $CYANmod.autorole $GREENto $CYAN{value} $GREENfor guild $CYAN{self._guild}')
        await self.update('mod.autorole', value.id)

    @ConfigOpt(name='mod.autorole.waitformsg', accepts=bool, default=False, options=options, premium=True)
    async def auto_role(self, value: discord.Role):
        '''Auto Role - Wait for message | Waits for the user to send a message to give the auto role'''
        self._bot.logger.info(
            f'$GREENSetting $CYANmod.autorole.waitformsg $GREENto $CYAN{value} $GREENfor guild $CYAN{self._guild}')
        await self.update('mod.autorole.waitformsg', value)

    @ConfigOpt(name='commands.modonly', accepts=[discord.TextChannel], default=[], options=options)
    async def mod_only(self, value: list):
        '''Moderator Channels | The channels where only moderators can run commands'''
        self._bot.logger.info(
            f'$GREENSetting $CYANcommands.modonly $GREENto $CYAN{value} $GREENfor guild $CYAN{self._guild}')
        await self.update('commands.modonly', [c.id for c in value])

    @ConfigOpt(name='commands.adminonly', accepts=[discord.TextChannel], default=[], options=options)
    async def admin_only(self, value: list):
        '''Admin channels | The channels where only admins can run commands'''
        self._bot.logger.info(
            f'$GREENSetting $CYANcommands.adminonly $GREENto $CYAN{value} $GREENfor guild $CYAN{self._guild}')
        await self.update('commands.adminonly', [c.id for c in value])

    @ConfigOpt(name='greet.joinchannel', accepts=discord.TextChannel, default=None, options=options)
    async def join_channel(self, value: discord.TextChannel):
        '''Join Message Channel | The channel where join messages are sent'''
        self._bot.logger.info(
            f'$GREENSetting $CYANgreet.joinchannel $GREENto $CYAN{value} $GREENfor guild $CYAN{self._guild}')
        await self.update('greet.joinchannel', value.id)

    @ConfigOpt(name='greet.leavechannel', accepts=discord.TextChannel, default=None, options=options)
    async def leave_channel(self, value: discord.TextChannel):
        '''Leave Message Channel | The channel where leave messages are sent'''
        self._bot.logger.info(
            f'$GREENSetting $CYANgreet.leavechannel $GREENto $CYAN{value} $GREENfor guild $CYAN{self._guild}')
        await self.update('greet.leavechannel', value.id)

    @ConfigOpt(name='greet.joinmsg', accepts=str, default=None, options=options)
    async def join_message(self, value: str):
        '''Join Message | The server's custom join message'''
        self._bot.logger.info(
            f'$GREENSetting $CYANgreet.joinmsg $GREENto $CYAN{value} $GREENfor guild $CYAN{self._guild}')
        await self.update('greet.joinmsg', value)

    @ConfigOpt(name='greet.leavemsg', accepts=str, default=None, options=options)
    async def leave_message(self, value: str):
        '''Leave Message | The server's custom leave message'''
        self._bot.logger.info(
            f'$GREENSetting $CYANgreet.leavemsg $GREENto $CYAN{value} $GREENfor guild $CYAN{self._guild}')
        await self.update('greet.leavemsg', value)

    @ConfigOpt(name='disabled.commands', accepts=[str], default=[], options=options)
    async def disabled_commands(self, value: list):
        '''Disabled Commands | Commands that can only be ran by moderators (those with Manage Messages permission)'''
        [value.remove(v) for v in value if not self._bot.get_command(v)]
        self._bot.logger.info(
            f'$GREENSetting $CYANdisabled.commands $GREENto $CYAN{value} $GREENfor guild $CYAN{self._guild}')
        await self.update('disabled.commands', value)

    @ConfigOpt(name='utils.autoquote', accepts=bool, default=False, options=options)
    async def auto_quote(self, value: bool):
        '''Automatic Quotes | Automatically quotes messages when a message link is sent'''
        self._bot.logger.info(
            f'$GREENSetting $CYANutils.autoquote $GREENto $CYAN{value} $GREENfor guild $CYAN{self._guild}')
        await self.update('utils.autoquote', value)

    @ConfigOpt(name='utils.quotehooks', accepts=bool, default=True, options=options)
    async def quote_hooks(self, value: bool):
        '''Quote Webhooks | Whether or not to use webhooks for quoting/snipes'''
        self._bot.logger.info(
            f'$GREENSetting $CYANutils.quotehooks $GREENto $CYAN{value} $GREENfor guild $CYAN{self._guild}')
        await self.update('utils.quotehooks', value)

    @ConfigOpt(name='utils.badname', accepts=str, default=None, options=options)
    async def bad_name(self, value: str):
        '''Bad Name | The name used for decancer and dehoist. If not set, John Doe + discrim is used'''
        self._bot.logger.info(
            f'$GREENSetting $CYANutils.badname $GREENto $CYAN{value} $GREENfor guild $CYAN{self._guild}')
        await self.update('utils.badname', value)

    @ConfigOpt(name='utils.public', accepts=bool, default=False, options=options)
    async def public_guild(self, value: bool):
        '''Public Guild | Makes your server viewable on https://fire.gaminggeek.space/discover (and joinable if a vanity url is set)'''
        self._bot.logger.info(
            f'$GREENSetting $CYANutils.public $GREENto $CYAN{value} $GREENfor guild $CYAN{self._guild}')
        await self.update('utils.public', value)

    @ConfigOpt(name='tickets.parent', accepts=discord.CategoryChannel, default=None, options=options)
    async def ticket_parent(self, value: discord.CategoryChannel):
        '''Tickets Category | The category where ticket channels are created. If this is not set, tickets are disabled'''
        self._bot.logger.info(
            f'$GREENSetting $CYANtickets.parent $GREENto $CYAN{value} $GREENfor guild $CYAN{self._guild}')
        await self.update('tickets.parent', value.id)

    @ConfigOpt(name='tickets.increment', accepts=int, default=0, options=options)
    async def ticket_increment(self, value: int):
        '''Ticket Increment | The number tickets will start incrementing from'''
        await self.update('tickets.increment', value)

    @ConfigOpt(name='tickets.limit', accepts=int, default=0, options=options)
    async def ticket_limit(self, value: int):
        '''Ticket Limit | The number tickets a user can open, 0 = Unlimited'''
        self._bot.logger.info(
            f'$GREENSetting $CYANtickets.limit $GREENto $CYAN{value} $GREENfor guild $CYAN{self._guild}')
        await self.update('tickets.limit', value)

    @ConfigOpt(name='tickets.name', accepts=str, default='ticket-{increment}', options=options)
    async def ticket_name(self, value: str):
        '''Ticket Name | The name used for ticket channels'''
        self._bot.logger.info(
            f'$GREENSetting $CYANtickets.name $GREENto $CYAN{value} $GREENfor guild $CYAN{self._guild}')
        await self.update('tickets.name', value)

    @ConfigOpt(name='tickets.channels', accepts=[discord.TextChannel], default=[], options=options, hidden=True)
    async def ticket_channels(self, value: list):
        '''Ticket Channels | All ticket channels in the guild'''
        await self.update('tickets.channels', [v.id for v in value])

    def get(self, option):
        if option not in self.options:
            raise InvalidOptionError(option)
        if self.options[option]['premium'] and self._guild.id not in self._bot.premium_guilds:
            # Return default value if not premium :)
            return self.options[option]['default']
        if self.options[option]['restricted'] and self._guild.id not in self.options[option]['restricted']:
            # Return default value if restricted :)
            return self.options[option]['default']
        if option not in self._data:
            # Return default value if it's not even in the config :)
            return self.options[option]['default']
        accept = self.options[option]['accepts']
        acceptlist = False
        if isinstance(self._guild, discord.Guild):
            converter = None
            if isinstance(accept, list):
                accept = accept[0]
                acceptlist = True
            if accept in DISCORD_CONVERTERS['bot']:
                converter = getattr(
                    self._bot, DISCORD_CONVERTERS['bot'][accept])
            elif accept in DISCORD_CONVERTERS['guild']:
                converter = getattr(
                    self._guild, DISCORD_CONVERTERS['guild'][accept])
            if converter and inspect.ismethod(converter):
                if acceptlist:
                    return [converter(d) for d in self._data[option]]
                return converter(self._data[option])
        return self._data[option]

    async def set(self, opt: str, value):
        if opt not in self.options:
            raise InvalidOptionError(opt)
        option = self.options[opt]
        if value == option['default']:  # Bypass all checks if default
            await self.update(opt, value)
            return self.get(opt)
        if option['premium'] and self._guild.id not in self._bot.premium_guilds:
            raise RestrictedOptionError(opt, 'premium guilds only')
        if option['restricted'] and self._guild.id not in option['restricted']:
            raise RestrictedOptionError(opt, 'select guilds only')
        setter = option['setter']
        if not inspect.isfunction(setter):
            raise OptionConfigError(option)
        if not isinstance(option['accepts'], list) and not isinstance(value, option['accepts']) and value is not None:
            raise TypeMismatchError(
                type=value.__class__.__name__, accepted=option['accepts'].__name__, option=opt)
        if isinstance(option['accepts'], list):
            accepts = option['accepts'][0]
            if not isinstance(value, list) or any(not isinstance(v, accepts) for v in value):
                if isinstance(value, list) and len(value) >= 1:
                    raise TypeMismatchError(type=[t.__class__.__name__ for t in value if not isinstance(
                        t, accepts)], accepted=[t.__name__ for t in option['accepts']], option=opt)
                raise TypeMismatchError(
                    type=value.__class__.__name__, accepted=option['accepts'].__class__.__name__, option=opt)
        await setter(self, value)
        return self.get(opt)

    async def update(self, option: str, value):
        changed = False  # Don't need to save if nothing changed lol
        default = self.options[option]['default']
        if value == default:
            v = self._data.pop(option, None)
            changed = True if v else False
        elif self._data.get(option, None) != value:
            self._data[option] = value
            changed = True
        if changed:
            await self.save()

    async def load(self):
        if isinstance(self._guild, int):
            self._guild = self._bot.get_guild(self._guild)
        query = 'SELECT * FROM guildconfig WHERE gid=$1;'
        conf = await self._db.fetch(query, self._guild.id)
        if not conf:
            self._data = await self.init()
            self.loaded = True
            return
        else:
            self._data = json.loads(conf[0]['data'])
            items = [(k, v) for k, v in tuple(self._data.items())]
            for opt, val in items:
                if opt not in self.options:
                    self._data.pop(opt)
                elif val == self.options[opt]['default']:
                    self._data.pop(opt)
            self.loaded = True

    async def save(self):
        con = await self._db.acquire()
        async with con.transaction():
            query = 'UPDATE guildconfig SET data = $1 WHERE gid = $2;'
            await self._db.execute(query, json.dumps(self._data), self._guild.id)
        await self._db.release(con)
        self._bot.logger.info(f'$GREENSaved config for $CYAN{self._guild}')

    async def init(self):
        con = await self._db.acquire()
        async with con.transaction():
            query = 'INSERT INTO guildconfig (\"gid\", \"data\") VALUES ($1, $2);'
            await self._db.execute(query, self._guild.id, json.dumps({}))
        await self._db.release(con)
        self._bot.logger.info(f'$GREENInitiated config for $CYAN{self._guild}')
        return {}

    def __repr__(self):
        return f'<Config guild={self._guild} loaded={self.loaded}>'

    def __str__(self):
        return f'<Config guild={self._guild} loaded={self.loaded}>'
