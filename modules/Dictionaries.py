from discord.ext import commands
from main import bot_starttime
from main import modules as loaded_modules
from libs.qudict import quDict
import main
import discord
import random

class Dictionaries(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.module_embed_color =  0x80e093
        print(f'Module {self.__class__.__name__} loaded')

    @commands.command(name='dict', help=main.lang["dictionaries_english_only"], description=main.lang["command_meanings_description"], aliases=['whatis', 'meaning', 'meanings'])
    async def dictionary_getmeanings(self, ctx, *, input: str):
        result = await quDict.get_top_meanings(input)
        if result != None:
            embed = discord.Embed(title=main.lang["dictionaries_term"].format(input), color=self.module_embed_color)
            for category in result:
                meanings = ""
                for item in result[category]:
                    meanings += f"- {item};\n"
                embed.add_field(name=f"**{category}**", value=meanings, inline=False)
            await ctx.send(embed=embed)
        else:
            await ctx.send(main.lang["dictionaries_word_not_found"])

    @commands.command(name='synonym', help=main.lang["dictionaries_english_only"], description=main.lang["command_synonyms_description"], usage="hot", aliases=['synonyms'])
    async def dictionary_getsynonyms(self, ctx, *, input: str):
        result = await quDict.get_top_synonyms(input)
        if result != None:
            embed = discord.Embed(title=main.lang["dictionaries_term"].format(input), color=self.module_embed_color)
            formatted = ', '.join(result)
            embed.add_field(name=main.lang["dictionaries_synonyms"], value=formatted, inline=False)
            await ctx.send(embed=embed)
        else:
            await ctx.send(main.lang["dictionaries_word_not_found"])

    @commands.command(name='antonym', help=main.lang["dictionaries_english_only"], description=main.lang["command_antonyms_description"], usage="hot", aliases=['antonyms'])
    async def dictionary_getantonyms(self, ctx, *, input: str):
        result = await quDict.get_top_antonyms(input)
        if result != None:
            embed = discord.Embed(title=main.lang["dictionaries_term"].format(input), color=self.module_embed_color)
            formatted = ', '.join(result)
            embed.add_field(name=main.lang["dictionaries_antonyms"], value=formatted, inline=False)
            await ctx.send(embed=embed)
        else:
            await ctx.send(main.lang["dictionaries_word_not_found"])

    @commands.command(name='urbandict', help=main.lang["dictionaries_english_only"], description=main.lang["command_urbandict_description"], usage="hello", aliases=['ud'])
    async def dictionary_get_urbandict(self, ctx, *, input: str):
        result = await quDict.get_urbandict_definitions(input)
        if result != None:
            embed = discord.Embed(title=main.lang["dictionaries_term"].format(input), color=self.module_embed_color)
            formatted = '\n'.join(result)
            embed.add_field(name=main.lang["dictionaries_urbandict_title"], value=formatted, inline=False)
            await ctx.send(embed=embed)
        else:
            await ctx.send(main.lang["dictionaries_word_not_found"])

def setup(bot):
    bot.add_cog(Dictionaries(bot))