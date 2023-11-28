import os, requests, discord, time, random, threading, user_agent, tls_client, uuid, asyncio
from threading import Thread
from discord.ext import commands
from discord_webhook import DiscordWebhook, DiscordEmbed
from discord import *

def get_all_tokens(filename:str): #returns all tokens in a file as token from email:password:token
    all_tokens = []
    for j in open(filename, "r").read().splitlines():
        if ":" in j:
            j = j.split(":")[2]
            all_tokens.append(j)
        else:
            all_tokens.append(j)
 
    return all_tokens

class Functions:
  

  
  def get_full_token(token:str):
    filename = "./tokens.txt"
    all_tokens = get_all_tokens(filename)
    all_tokens_full = open(filename, "r").read().splitlines()
    index = all_tokens.index(token)
    return all_tokens_full[index]
  
  def get_session():
    try:
      session = tls_client.Session(
          client_identifier='okhttp4_android_7',
          ja3_string=random.choice(
              '771,4866-4867-4865-103-49200-49187-158-49188-49161-49171-61-49195-49199-156-60-49192-51-53-49172-49191-52392-49162-107-52394-49196-159-47-57-157-52393-255,0-11-10-35-16-22-23-13-43-45-51-21,29-23-30-25-24,0-1-2'
          ),
          h2_settings={
              "HEADER_TABLE_SIZE": 65536,
              "MAX_CONCURRENT_STREAMS": 1000,
              "INITIAL_WINDOW_SIZE": 6291456,
              "MAX_HEADER_LIST_SIZE": 262144
          },
          h2_settings_order=[
              "HEADER_TABLE_SIZE", "MAX_CONCURRENT_STREAMS",
              "INITIAL_WINDOW_SIZE", "MAX_HEADER_LIST_SIZE"
          ],
          supported_signature_algorithms=[
              "ECDSAWithP256AndSHA256",
              "PSSWithSHA256",
              "PKCS1WithSHA256",
              "ECDSAWithP384AndSHA384",
              "PSSWithSHA384",
              "PKCS1WithSHA384",
              "PSSWithSHA512",
              "PKCS1WithSHA512",
          ],
          supported_versions=["GREASE", "1.3", "1.2"],
          key_share_curves=["GREASE", "X25519"],
          cert_compression_algo="brotli",
          pseudo_header_order=[":method", ":authority", ":scheme", ":path"],
          connection_flow=15663105,
          header_order=[
              "accept", "user-agent", "accept-encoding", "accept-language"
          ])
      return session
    except:
      pass

  def get_cookies(session):
    try:
      r = session.get(f'https://discord.com/api/v9/login/')
      cookie1 = r.headers['Set-Cookie'][0]
      cookie2 = r.headers['Set-Cookie'][1]
      cookie3 = r.headers['Set-Cookie'][2]
    except:
      cookie1 = '1b427ed0d18d11edbebe91d030d1b835'
      cookie2 = '1b427ed1d18d11edbebe91d030d1b8357f3469a0fed7b719c0dd5cd01fa8a579b2d10082cb94c17f4a6c209d89efed49'
      cookie3 = 'f00abacc9acef85bb8d32a97317424ea77c7e833'
    return cookie1, cookie2, cookie3

  def main(self, tokstock, idd):
    with open(self.tokstock, 'r') as file:
      tokens = file.read().splitlines()
      token = random.choice(tokens)

    session = Functions.get_session()
    # proxy = Main.get_proxy()
    # proxies = Main.get_proxy()
    cookie1, cookie2, cookie3 = Functions.get_cookies(session)
    #user = Main.make_token_id(token)
    headers = {
        'authority': 'discord.com',
        'accept': '*/*',
        'user-agent': user_agent.generate_user_agent(),
        'accept-language': 'en-US,en;q=0.9',
        'authorization': token,
        'content-type': 'application/json',
        'origin': 'https://discord.com',
        'referer': f'https://discord.com/channels/@me/{self.idd}',
        'sec-ch-ua':
        '"Not/A)Brand";v="99", "Microsoft Edge";v="115", "Chromium";v="115"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'x-context-properties': 'eyJsb2NhdGlvbiI6IkNvbnRleHRNZW51In0=',
        'x-debug-options': 'bugReporterEnabled',
        'x-discord-locale': 'en-US',
        'x-discord-timezone': 'America/New_York',
        'x-super-properties':
        'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExNS4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMTUuMC4xOTAxLjIwMyIsImJyb3dzZXJfdmVyc2lvbiI6IjExNS4wLjAuMCIsIm9zX3ZlcnNpb24iOiIxMCIsInJlZmVycmVyIjoiaHR0cHM6Ly93d3cuYmluZy5jb20vIiwicmVmZXJyaW5nX2RvbWFpbiI6Ind3dy5iaW5nLmNvbSIsInNlYXJjaF9lbmdpbmUiOiJiaW5nIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjIyMDkyNywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=',
        'Cookie': f'{cookie1}; {cookie2}; {cookie3};',
    }
    json_data = {}
    response = session.put(
        F'https://discord.com/api/v9/users/@me/relationships/{self.idd}',
        headers=headers,
        json=json_data,
    )
    print(response.status_code)

  def memberadder(self):
    delay = random.uniform(2, 46)
    time.sleep(delay)
  tokens = get_all_tokens("./tokens.txt")
    line = Functions.get_full_token tokens
    idd = line[0]
    tokenn = line[1]
    data = {
        "access_token": tokenn,
    }
    headers = {
        "Authorization": f"Bot {self.tkn}",
        'Content-Type': 'application/json'
    }
    response = requests.put(
        f'{self.apiendpoint}/guilds/{self.serverid}/members/{idd}',
        headers=headers,
        json=data)
    # print(response.json())
    print(response.json())
    if response.status_code == 201:
      if "joined" not in response.text:
        #     already_joined_count += 1
        pass
      else:
        #     success_count += 1
        pass
    if response.status_code in (200, 204):
      pass
      #     pass
      #     already_joined_count += 1
    elif response.status_code == 429:
      delay = random.uniform(20, 35)
      time.sleep(delay)
      Functions.memberadder(self)
      pass
    elif response.status_code == 403:
      #     botnot +=1
      pass
    else:
      #     failed_count += 1
      pass

  def joinn(self, tokstock, invite):  # tokstock, invite

    # delay = random.uniform(7, 26)
    # time.sleep(delay)
    try:
      with open(self.tokstock, 'r') as file:
        tokens = get_all_tokens("input/tokens.txt")
        token = random.choice(tokens)

    except:
      print('Nothing Is In tokens.txt')
      exit()

    session = Functions.get_session()
    cookie1, cookie2, cookie3 = Functions.get_cookies(session)
    headers = {
        'User-Agent':
        user_agent.generate_user_agent(),
        'Cookie':
        f'{cookie1}; {cookie2}; {cookie3};',
        'authority':
        'discord.com',
        'accept':
        '*/*',
        'accept-language':
        'en-US,en;q=0.9',
        'authorization':
        token,
        'content-type':
        'application/json',
        'origin':
        'https://discord.com',
        'referer':
        'https://discord.com/channels/@me',
        'sec-ch-ua':
        '"Chromium";v="116", "Not)A;Brand";v="24", "Microsoft Edge";v="116"',
        'sec-ch-ua-mobile':
        '?0',
        'sec-ch-ua-platform':
        '"Windows"',
        'sec-fetch-dest':
        'empty',
        'sec-fetch-mode':
        'cors',
        'sec-fetch-site':
        'same-origin',
        'x-context-properties':
        'eyJsb2NhdGlvbiI6IkpvaW4gR3VpbGQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6IjY2MDk5NTcxMzQ1ODYzNDgwOCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI3MzU5NjE0NDgwNzI3NDEwMjgiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjV9',
        'x-debug-options':
        'bugReporterEnabled',
        'x-discord-locale':
        'en-US',
        'x-discord-timezone':
        'America/New_York',
        'x-super-properties':
        'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExNi4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMTYuMC4xOTM4Ljc2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTE2LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiJodHRwczovL3d3dy5iaW5nLmNvbS8iLCJyZWZlcnJpbmdfZG9tYWluIjoid3d3LmJpbmcuY29tIiwic2VhcmNoX2VuZ2luZSI6ImJpbmciLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MjI3NTU5LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
    }

    json_data = {"session_id": uuid.uuid4().hex}
    response = session.post(
        f'https://discord.com/api/v9/invites/{self.invite}',
        headers=headers,
        json=json_data)
    print(response.status_code)


class Discord_Bot:
  bot = None

  def __init__(self) -> None:

    self.blistedservids = ['']
    self.bot_token = 'MTE2ODk3ODYyMzI0NDUzMzkxMQ.GoMOBJ.i69-m1R1-CNUy4--czKO0uHqT8ewJRxtrcH-N8'
    self.channelid = '1168978291919704104'
    self.bot_prefix = '!'
    self.cooldown = commands.CooldownMapping.from_cooldown(
        1, 20, commands.BucketType.user)
    self.used_server_ids = {}
    self.used_userids = {}
    self.user_codes = {}
    self.blacklistedusers = ['']
    self.serveridjoin = 'stock.txt'
    self.tokstock = 'tokens.txt'
    self.guilds_to_keep = [1108039441924239420]
    self.allowed_roles = ["Owner", "Staff", "Moderator", "*"]

    self.webhook = 'https://discord.com/api/webhooks/1152035141846319224/JuTLlzcZcZ8EZZN0yeSmQaNGowjcoBHbMtC5zPYjY9kXany08d-EMa-fue4MiKn9BqFW'
    self.whitelist = set()
    self.blacklist = set()
    self.blacklistt = set()
    self.whitelistt = set()
    self.blacklisttt = set()
    self.whitelisttt = set()

    self.apiendpoint = 'https://canary.discord.com/api/v9'
    self.tkn = ""
    self.client_id = '1168978623244533911'
    self.client_secret = "cfUgG3dWoJ2rl4YFnjOMq8_c4VI8N3Mi"
    self.roles = {
        "Extra": 500,
        "Head Admin": 60,
        "Admin": 35,
        "Moderator": 30,
        "Staff": 25,
        "Premium": 40,
        "Diamond": 30,
        "Gold": 25,
        "Silver": 15,
        "Bronze": 10,
        "Members": 5
    }
    self.rolesfriends = {
        #"Head Admin": 60,
        #"Admin": 40,
        "Moderator": 30,
        "Staff": 20,
        "Premium": 35,
        "Diamond": 30,
        "Gold": 25,
        "Silver": 20,
        "Bronze": 15,
        "Members": 5
    }
    self.njoinam = {
        #"Head Admin": 60,
        #"Admin": 40,
        "Moderator": 5,
        "Staff": 5,
        "Premium": 3,
        "Diamond": 3,
        "Gold": 2,
        "Silver": 2,
        "Bronze": 1,
        "Members": 1
    }
    os.system("cls")
    self.run_bot()

  def commands(self):

    @self.bot.command()
    async def add(ctx):
        class SimpleView(discord.ui.View):
            def __init__(self):
                super().__init__(timeout=30)  # times out after 30 seconds
                button = discord.ui.Button(label='Add bot', style=discord.ButtonStyle.url, url='https://discord.com/api/oauth2/authorize?client_id=1167488526309408910&permissions=8&scope=bot')
                self.add_item(button)

        view = SimpleView() 
        await ctx.send(view=view)

    @self.bot.event
    async def on_ready():

      await self.bot.change_presence(activity=discord.Game(name="/membersv1"))
      pass

    class Threads():
      pass

    @self.bot.command(name="tokstockset", description="Set The Stock File.")
    async def tokstockset(ctx, filename):
      user_roles = [role.name for role in ctx.author.roles]
      if any(role in self.allowed_roles for role in user_roles):
        try:
          with open(filename, 'r') as file:
            file.read()

        except:
          embed = discord.Embed(title='**Error Setting**', color=0x0000FF)
          #     embed.set_author(name="membersv1", icon_url="https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&")
          embed.set_thumbnail(url="")
          embed.add_field(name="**Stock**",
                          value=f"Couldnt Find That File",
                          inline=False)
          embed.set_footer(
              text="discord.gg/membersv1 - andree4real eintommy",
              icon_url=
              "https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&"
          )
          await ctx.send(embed=embed)
          return

        self.tokstock = filename

        embed = discord.Embed(title='**Set**', color=0x0000FF)
        #     embed.set_author(name="membersv1", icon_url="https://images-ext-1.discordapp.net/external/2NAooU9gVTjbL1s_V6mVstZuyrVfaND6TwxXwzPJrYQ/%3Fsize%3D1024/https/cdn.discordapp.com/icons/1147749932757950514/7e7b0dc21cc38589daf1d46eda38f153.png?width=651&height=651")
        embed.set_thumbnail(
            url=
            "https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&"
        )
        embed.add_field(name="**Stock**",
                        value=f"stock File Set To {self.serveridjoin}",
                        inline=False)
        embed.set_footer(
            text="andree4real ",
            icon_url=
            "https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&"
        )
        await ctx.send(embed=embed)

    @self.bot.command(name="setstock", description="Set The Stock File.")
    async def setstock(ctx, filename):
      user_roles = [role.name for role in ctx.author.roles]
      if any(role in self.allowed_roles for role in user_roles):
        try:
          with open(filename, 'r') as file:
            file.read()

        except:
          embed = discord.Embed(title='**Error Setting**', color=0x0000FF)
          #     embed.set_author(name="membersv1", icon_url="https://images-ext-1.discordapp.net/external/2NAooU9gVTjbL1s_V6mVstZuyrVfaND6TwxXwzPJrYQ/%3Fsize%3D1024/https/cdn.discordapp.com/icons/1147749932757950514/7e7b0dc21cc38589daf1d46eda38f153.png?width=651&height=651")
          embed.set_thumbnail(
              url=
              "https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&"
          )
          embed.add_field(name="**Stock**",
                          value=f"Couldnt Find That File",
                          inline=False)
          embed.set_footer(
              text="Powered by discord.gg/membersv1 - andree4real eintommy",
              icon_url=
              "https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&"
          )
          await ctx.send(embed=embed)
          return

        self.serveridjoin = filename

        embed = discord.Embed(title='**Set**', color=0x0000FF)
        #     embed.set_author(name="membersv1", icon_url="https://images-ext-1.discordapp.net/external/2NAooU9gVTjbL1s_V6mVstZuyrVfaND6TwxXwzPJrYQ/%3Fsize%3D1024/https/cdn.discordapp.com/icons/1147749932757950514/7e7b0dc21cc38589daf1d46eda38f153.png?width=651&height=651")
        embed.set_thumbnail(
            url=
            "https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&"
        )
        embed.add_field(name="**Stock**",
                        value=f"stock File Set To {self.serveridjoin}",
                        inline=False)
        embed.set_footer(
            text="andree4real ",
            icon_url=
            "https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&"
        )
        await ctx.send(embed=embed)

    @self.bot.command(name="help", description="Get all commands.")
    async def help(ctx):
      embed = discord.Embed(title='.gg/membersv1',
                            description=f'__Commands__\n',
                            color=0x0000FF)
      embed.add_field(name="!join (serverid)",
                      value="Mass Join Any Server.",
                      inline=True)
      embed.add_field(name="!friend (user id)",
                      value="Mass Spam Any User ID.",
                      inline=True)
      embed.add_field(name="!njoin (server code)",
                      value="Mass Spam Any User ID.",
                      inline=True)
      embed.add_field(name="!stock", value="Join Stock Amount", inline=True)
      embed.add_field(name="!bug <reason>", value="Bug Rep", inline=True)
      embed.add_field(name="Trivia",
                      value="You Can Find This At <#1147755578278543410>",
                      inline=True)
      embed.add_field(name="Gamble",
                      value="You Can Find This At <#1147755561149010022>",
                      inline=True)
      # embed.add_field(name="Guess Song", value="You Can Find This At <#1147755590047768646>", inline=True)
      embed.set_footer(
          text="andree4real ",
          icon_url=
          "https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&"
      )
      await ctx.send(embed=embed)

    @self.bot.command(name="adminpanel", description="Get all commands.")
    async def adminpanel(ctx):
      embed = discord.Embed(title='Discord Members',
                            description=f'__Commands__\n',
                            color=0x0000FF)
      embed.add_field(name="!join (serverid)",
                      value="Mass Join Any Server.",
                      inline=True)
      embed.add_field(name="!friend (user id)",
                      value="Mass Spam Any User ID.",
                      inline=True)
      embed.add_field(name="!njoin (server code)",
                      value="Mass Spam Any User ID.",
                      inline=True)
      embed.add_field(name="!stock", value="Join Stock Amount", inline=True)
      embed.add_field(name="!leave", value="Join Stock Amount", inline=True)
      embed.add_field(name="!blacklistserverid <serverid> ",
                      value="Blacklist A ID",
                      inline=True)
      embed.add_field(name="!whitelistserverid <serverid> ",
                      value="Whitelist A ID",
                      inline=True)
      embed.add_field(name="!whitelistuserid <user> ",
                      value="Whitelist A ID",
                      inline=True)
      embed.add_field(name="!blacklistuserid <user> ",
                      value="Whitelist A ID",
                      inline=True)
      embed.add_field(name="!setstock <filename> ",
                      value="Switch The File / Go To Backup.",
                      inline=True)
      embed.add_field(name="!tokstockset <filename> ",
                      value="Switch The File / Backup.",
                      inline=True)
      # embed.add_field(name="!online", value="Start Onliner.", inline=True)
      embed.add_field(name="Trivia",
                      value="You Can Find This At <#1147755578278543410>",
                      inline=True)
      embed.add_field(name="Gamble",
                      value="You Can Find This At <#1147755561149010022>",
                      inline=True)
      # embed.add_field(name="Guess Song", value="You Can Find This At <#1147755590047768646>", inline=True)
      embed.set_footer(
          text="andree4real ",
          icon_url=
          "https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&"
      )
      await ctx.send(embed=embed)

    @self.bot.command(name="whitelistuserid", description="Whitelist A User.")
    async def whitelist(ctx, userid: int):
      user_roles = [role.name for role in ctx.author.roles]
      if any(role in self.allowed_roles for role in user_roles):
        if userid in self.blacklistt:
          payload = {
              "embeds": [{
                  "title":
                  "**User Did Whitelistuserid CMD**",
                  "color":
                  10992607,
                  "thumbnail": {
                      "url":
                      "https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&"
                  },
                  "fields": [{
                      "name": "**Whitelisted ID**",
                      "value":
                      f"User ID: ``{ctx.author}``\nUser Did Whitelist Command``",
                      "inline": False
                  }],
                  "footer": {
                      "text":
                      "Powered by discord.gg/membersv1 - andree4real eintommy",
                      "icon_url":
                      "https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&"
                  }
              }]
          }

          response = requests.post(self.webhook, json=payload)
          self.blacklistt.remove(userid)
          embed = discord.Embed(description="**Whitelisted**", color=0x0000FF)
          # embed.set_author(name="membersv1", icon_url="https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&")
          embed.set_thumbnail(
              url=
              "https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&"
          )
          embed.add_field(name="**Whitelisted**",
                          value=f"You Have Whitelisted: {userid}",
                          inline=False)
          embed.set_footer(
              text="andree4real ",
              icon_url=
              "https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&"
          )
          await ctx.send(embed=embed)
        else:
          embed = discord.Embed(description="*Error*", color=0x0000FF)
          # embed.set_author(name="membersv1", icon_url="https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&")
          embed.set_thumbnail(
              url=
              "https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&"
          )
          embed.add_field(name="**Whitelist Error**",
                          value=f"User ID Is Not Blacklisted: {userid}",
                          inline=False)
          embed.set_footer(
              text="andree4real ",
              icon_url=
              "https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&"
          )
          await ctx.send(embed=embed)
      else:
        #embed=discord.Embed(description="*Error*", color=0x0000FF)
        embed = discord.Embed(title='**Error**', color=0x0000FF)
        # embed.set_author(name="membersv1", icon_url="https://images-ext-1.discordapp.net/external/2NAooU9gVTjbL1s_V6mVstZuyrVfaND6TwxXwzPJrYQ/%3Fsize%3D1024/https/cdn.discordapp.com/icons/1147749932757950514/7e7b0dc21cc38589daf1d46eda38f153.png?width=651&height=651")
        embed.set_thumbnail(
            url=
            "https://media.discordapp.net/attachments/1158946205120872488/1158952389324324894/pb.png?ex=651e1e05&is=651ccc85&hm=d5eb4b97099b5a674c5144d8&"
        )
        embed.add_field(name="**Missing Perms.**",
                        value=f"Only Managers & Owners Can Do This CMD.",
                        inline=False)
        embed.set_footer(
            text="andree4real ",
            icon_url=
            "https://media.discordapp.net/attachments/1158946205120872488/1158952389324324894/pb.png?ex=651e1e05&is=651ccc85&hm=d5eb4b97099b5a674c5144d8&"
        )
        await ctx.send(embed=embed)

    @self.bot.command(name="blacklistuserid", description="Blacklist A User.")
    async def blacklist(ctx, userid: int):

      user_roles = [role.name for role in ctx.author.roles]
      if any(role in self.allowed_roles for role in user_roles):
        payload = {
            "embeds": [{
                "title":
                "**User Did Blacklisteruserid CMD**",
                "color":
                10992607,
                "thumbnail": {
                    "url":
                    "https://media.discordapp.net/attachments/1158946205120872488/1158952389324324894/pb.png?ex=651e1e05&is=651ccc85&hm=d5eb4b97099b5a674c5144d8&"
                },
                "fields": [{
                    "name": "**Blacklisted ID**",
                    "value":
                    f"User ID: ``{ctx.author}``\nUser Did Blacklistuserid Command``",
                    "inline": False
                }],
                "footer": {
                    "text":
                    "andree4real ",
                    "icon_url":
                    "https://media.discordapp.net/attachments/1158946205120872488/1158952389324324894/pb.png?ex=651e1e05&is=651ccc85&hm=d5eb4b97099b5a674c5144d8&"
                }
            }]
        }

        response = requests.post(self.webhook, json=payload)
        self.blacklistt.add(userid)
        embed = discord.Embed(description="**Blacklisted**", color=0x0000FF)
        # embed.set_author(name="membersv1", icon_url="https://media.discordapp.net/attachments/1158946205120872488/1158952389324324894/pb.png?ex=651e1e05&is=651ccc85&hm=d5eb4b97099b5a674c5144d8&")
        embed.set_thumbnail(
            url=
            "https://media.discordapp.net/attachments/1158946205120872488/1158952389324324894/pb.png?ex=651e1e05&is=651ccc85&hm=d5eb4b97099b5a674c5144d8&"
        )
        embed.add_field(name="**Blacklisted**",
                        value=f"USER ID Has Been Blacklisted: {userid}",
                        inline=False)
        embed.set_footer(
            text="andree4real ",
            icon_url=
            "https://media.discordapp.net/attachments/1158946205120872488/1158952389324324894/pb.png?ex=651e1e05&is=651ccc85&hm=d5eb4b97099b5a674c5144d8&"
        )
        await ctx.send(embed=embed)
      else:
        #embed=discord.Embed(description="**Error**", color=0x0000FF)
        embed = discord.Embed(title='**Error**', color=0x0000FF)
        # embed.set_author(name="membersv1", icon_url="https://media.discordapp.net/attachments/1158946205120872488/1158952389324324894/pb.png?ex=651e1e05&is=651ccc85&hm=d5eb4b97099b5a674c5144d8&")
        embed.set_thumbnail(
            url=
            "https://media.discordapp.net/attachments/1158946205120872488/1158952389324324894/pb.png?ex=651e1e05&is=651ccc85&hm=d5eb4b97099b5a674c5144d8&"
        )
        embed.add_field(name="**Missing Perms.**",
                        value=f"Only Managers & Owners Can Do This CMD.",
                        inline=False)
        embed.set_footer(
            text="andree4real ",
            icon_url=
            "https://media.discordapp.net/attachments/1158946205120872488/1158952389324324894/pb.png?ex=651e1e05&is=651ccc85&hm=d5eb4b97099b5a674c5144d8&"
        )
        await ctx.send(embed=embed)

    @self.bot.command(name="whitelistserverid",
                      description="Whitelist A User.")
    async def whitelist(ctx, serverid: int):
      user_roles = [role.name for role in ctx.author.roles]
      if any(role in self.allowed_roles for role in user_roles):
        if serverid in self.blacklist:
          payload = {
              "embeds": [{
                  "title":
                  "**User Did Whitelistserverid Command**",
                  "color":
                  10992607,
                  "thumbnail": {
                      "url":
                      "https://media.discordapp.net/attachments/1158946205120872488/1158952389324324894/pb.png?ex=651e1e05&is=651ccc85&hm=d5eb4b97099b5a674c5144d8&"
                  },
                  "fields": [{
                      "name": "**User**",
                      "value":
                      f"User ID: ``{ctx.author}``\nUser Did Whitelist Server ID Command``",
                      "inline": False
                  }],
                  "footer": {
                      "text":
                      "andree4real ",
                      "icon_url":
                      "https://media.discordapp.net/attachments/1158946205120872488/1158952389324324894/pb.png?ex=651e1e05&is=651ccc85&hm=d5eb4b97099b5a674c5144d8&"
                  }
              }]
          }

          response = requests.post(self.webhook, json=payload)
          self.blacklist.remove(serverid)
          embed = discord.Embed(description="**Whitelisted**", color=0x0000FF)
          # embed.set_author(name="membersv1", icon_url="https://media.discordapp.net/attachments/1158946205120872488/1158952389324324894/pb.png?ex=651e1e05&is=651ccc85&hm=d5eb4b97099b5a674c5144d8&")
          embed.set_thumbnail(
              url=
              "https://media.discordapp.net/attachments/1158946205120872488/1158952389324324894/pb.png?ex=651e1e05&is=651ccc85&hm=d5eb4b97099b5a674c5144d8&"
          )
          embed.add_field(name="**Whitelisted**",
                          value=f"You Have Whitelisted: {serverid}",
                          inline=False)
          embed.set_footer(
              text="andree4real ",
              icon_url=
              "https://media.discordapp.net/attachments/1158946205120872488/1158952389324324894/pb.png?ex=651e1e05&is=651ccc85&hm=d5eb4b97099b5a674c5144d8&"
          )
          await ctx.send(embed=embed)
        else:
          embed = discord.Embed(description="*Error*", color=0x0000FF)
          # embed.set_author(name="membersv1", icon_url="https://media.discordapp.net/attachments/1158946205120872488/1158952389324324894/pb.png?ex=651e1e05&is=651ccc85&hm=d5eb4b97099b5a674c5144d8&")
          embed.set_thumbnail(
              url=
              "https://media.discordapp.net/attachments/1158946205120872488/1158952389324324894/pb.png?ex=651e1e05&is=651ccc85&hm=d5eb4b97099b5a674c5144d8&"
          )
          embed.add_field(name="**Whitelist Error**",
                          value=f"Server ID Is Not Blacklisted: {serverid}",
                          inline=False)
          embed.set_footer(
              text="andree4real ",
              icon_url=
              "https://media.discordapp.net/attachments/1158946205120872488/1158952389324324894/pb.png?ex=651e1e05&is=651ccc85&hm=d5eb4b97099b5a674c5144d8&"
          )
          await ctx.send(embed=embed)
      else:
        #embed=discord.Embed(description="*Error*", color=0x0000FF)
        embed = discord.Embed(title='**Error**', color=0x0000FF)
        # embed.set_author(name="membersv1", icon_url="https://media.discordapp.net/attachments/1158946205120872488/1158952389324324894/pb.png?ex=651e1e05&is=651ccc85&hm=d5eb4b97099b5a674c5144d8&")
        embed.set_thumbnail(
            url=
            "https://media.discordapp.net/attachments/1158946205120872488/1158952389324324894/pb.png?ex=651e1e05&is=651ccc85&hm=d5eb4b97099b5a674c5144d8&"
        )
        embed.add_field(name="**Missing Perms.**",
                        value=f"Only Managers & Owners Can Do This CMD.",
                        inline=False)
        embed.set_footer(
            text="andree4real ",
            icon_url=
            "https://media.discordapp.net/attachments/1158946205120872488/1158952389324324894/pb.png?ex=651e1e05&is=651ccc85&hm=d5eb4b97099b5a674c5144d8&"
        )
        await ctx.send(embed=embed)

    @self.bot.command(name="blacklistserverid",
                      description="Blacklist A User.")
    async def blacklist(ctx, serverid: int):
      user_roles = [role.name for role in ctx.author.roles]
      if any(role in self.allowed_roles for role in user_roles):
        payload = {
            "embeds": [{
                "title":
                "**Blacklistserverid Command.**",
                "color":
                10992607,
                "thumbnail": {
                    "url":
                    "https://media.discordapp.net/attachments/1158946205120872488/1158952389324324894/pb.png?ex=651e1e05&is=651ccc85&hm=d5eb4b97099b5a674c5144d8&"
                },
                "fields": [{
                    "name": "**Blacklisted ID**",
                    "value":
                    f"User ID: ``{ctx.author}``\nUser Did Blacklistserverid Command``",
                    "inline": False
                }],
                "footer": {
                    "text":
                    "andree4real ",
                    "icon_url":
                    "https://media.discordapp.net/attachments/1158946205120872488/1158952389324324894/pb.png?ex=651e1e05&is=651ccc85&hm=d5eb4b97099b5a674c5144d8&"
                }
            }]
        }

        response = requests.post(self.webhook, json=payload)
        self.blacklist.add(serverid)
        embed = discord.Embed(description="**Blacklisted**", color=0x0000FF)
        # embed.set_author(name="membersv1", icon_url="https://media.discordapp.net/attachments/1158946205120872488/1158952389324324894/pb.png?ex=651e1e05&is=651ccc85&hm=d5eb4b97099b5a674c5144d8&")
        embed.set_thumbnail(
            url=
            "https://media.discordapp.net/attachments/1158946205120872488/1158952389324324894/pb.png?ex=651e1e05&is=651ccc85&hm=d5eb4b97099b5a674c5144d8&"
        )
        embed.add_field(name="**Blacklisted**",
                        value=f"Server ID Has Been Blacklisted: {serverid}",
                        inline=False)
        embed.set_footer(
            text="andree4real ",
            icon_url=
            "https://media.discordapp.net/attachments/1158946205120872488/1158952389324324894/pb.png?ex=651e1e05&is=651ccc85&hm=d5eb4b97099b5a674c5144d8&"
        )
        await ctx.send(embed=embed)
      else:
        #embed=discord.Embed(description="**Error**", color=0x0000FF)
        embed = discord.Embed(title='**Error**', color=0x0000FF)
        # embed.set_author(name="membersv1", icon_url="https://media.discordapp.net/attachments/1158946205120872488/1158952389324324894/pb.png?ex=651e1e05&is=651ccc85&hm=d5eb4b97099b5a674c5144d8&")
        embed.set_thumbnail(
            url=
            "https://media.discordapp.net/attachments/1158946205120872488/1158952389324324894/pb.png?ex=651e1e05&is=651ccc85&hm=d5eb4b97099b5a674c5144d8&"
        )
        embed.add_field(name="**Missing Perms.**",
                        value=f"Only Managers & Owners Can Do This CMD.",
                        inline=False)
        embed.set_footer(
            text="Powered by discord.gg/membersv1 - andree4real eintommy",
            icon_url=
            "https://images-ext-1.discordapp.net/external/2NAooU9gVTjbL1s_V6mVstZuyrVfaND6TwxXwzPJrYQ/%3Fsize%3D1024/https/cdn.discordapp.com/icons/1147749932757950514/7e7b0dc21cc38589daf1d46eda38f153.png?width=651&height=651"
        )
        await ctx.send(embed=embed)

    @self.bot.command(name="stock", description="Check tokens stock.")
    async def stock(ctx):
      try:
        with open(self.serveridjoin, 'r') as file:
          authamount = len(file.readlines())
        with open(self.tokstock, 'r') as file:
          toam = len(file.readlines())
        #     embed=discord.Embed(description="**Stock**", color=0x0000FF)
        embed = discord.Embed(title='**Stock**', color=0x0000FF)
        #     embed.set_author(name="membersv1", icon_url="https://images-ext-1.discordapp.net/external/2NAooU9gVTjbL1s_V6mVstZuyrVfaND6TwxXwzPJrYQ/%3Fsize%3D1024/https/cdn.discordapp.com/icons/1147749932757950514/7e7b0dc21cc38589daf1d46eda38f153.png?width=651&height=651")
        embed.set_thumbnail(
            url=
            "https://images-ext-1.discordapp.net/external/2NAooU9gVTjbL1s_V6mVstZuyrVfaND6TwxXwzPJrYQ/%3Fsize%3D1024/https/cdn.discordapp.com/icons/1147749932757950514/7e7b0dc21cc38589daf1d46eda38f153.png?width=651&height=651"
        )
        embed.add_field(name="**Stock**",
                        value=f"Stock Amount {authamount}\nTokens: {toam}",
                        inline=False)
        embed.set_footer(
            text="Powered by discord.gg/membersv1 - andree4real eintommy",
            icon_url=
            "https://images-ext-1.discordapp.net/external/2NAooU9gVTjbL1s_V6mVstZuyrVfaND6TwxXwzPJrYQ/%3Fsize%3D1024/https/cdn.discordapp.com/icons/1147749932757950514/7e7b0dc21cc38589daf1d46eda38f153.png?width=651&height=651"
        )
        await ctx.send(embed=embed)
      except FileNotFoundError:
        error_embed = discord.Embed(title='**Unknown Error**', color=0xFF0000)
        error_embed.set_thumbnail(
            url=
            "https://images-ext-1.discordapp.net/external/2NAooU9gVTjbL1s_V6mVstZuyrVfaND6TwxXwzPJrYQ/%3Fsize%3D1024/https/cdn.discordapp.com/icons/1147749932757950514/7e7b0dc21cc38589daf1d46eda38f153.png?width=651&height=651"
        )
        error_embed.add_field(name="**Error Message**",
                              value=str(),
                              inline=False)
        error_embed.set_footer(
            text="Powered by discord.gg/membersv1 - andree4real eintommy",
            icon_url=
            "https://images-ext-1.discordapp.net/external/2NAooU9gVTjbL1s_V6mVstZuyrVfaND6TwxXwzPJrYQ/%3Fsize%3D1024/https/cdn.discordapp.com/icons/1147749932757950514/7e7b0dc21cc38589daf1d46eda38f153.png?width=651&height=651"
        )
        await ctx.send(embed=error_embed)

    @self.bot.command(name="njoin", description="Send Mass Amounts Of Joins")
    async def njoin(ctx, servercode: str):
      try:
        if servercode is None:
          #embed=discord.Embed(description="*Error*", color=0x0000FF)
          embed = discord.Embed(title='**Error**', color=0x0000FF)
          # embed.set_author(name="membersv1", icon_url="https://images-ext-1.discordapp.net/external/2NAooU9gVTjbL1s_V6mVstZuyrVfaND6TwxXwzPJrYQ/%3Fsize%3D1024/https/cdn.discordapp.com/icons/1147749932757950514/7e7b0dc21cc38589daf1d46eda38f153.png?width=651&height=651")
          embed.set_thumbnail(
              url=
              "https://images-ext-1.discordapp.net/external/2NAooU9gVTjbL1s_V6mVstZuyrVfaND6TwxXwzPJrYQ/%3Fsize%3D1024/https/cdn.discordapp.com/icons/1147749932757950514/7e7b0dc21cc38589daf1d46eda38f153.png?width=651&height=651"
          )
          embed.add_field(name="**Args**",
                          value="Your Missing Required Args. Exa: !njoin Code",
                          inline=False)
          embed.set_footer(
              text="Powered by discord.gg/membersv1 - andree4real eintommy",
              icon_url=
              "https://images-ext-1.discordapp.net/external/2NAooU9gVTjbL1s_V6mVstZuyrVfaND6TwxXwzPJrYQ/%3Fsize%3D1024/https/cdn.discordapp.com/icons/1147749932757950514/7e7b0dc21cc38589daf1d46eda38f153.png?width=651&height=651"
          )
          await ctx.send(embed=embed)

          payload = {
              "embeds": [{
                  "title":
                  "**Error**",
                  "color":
                  10992607,
                  "thumbnail": {
                      "url":
                      "https://images-ext-1.discordapp.net/external/2NAooU9gVTjbL1s_V6mVstZuyrVfaND6TwxXwzPJrYQ/%3Fsize%3D1024/https://cdn.discordapp.com/icons/1147749932757950514/7e7b0dc21cc38589daf1d46eda38f153.png?width=651&height=651"
                  },
                  "fields": [{
                      "name": "**Args**",
                      "value":
                      f"User ID: ``{ctx.author}``\nIs Dumbass: ``Yes``\nReason: ``Forgot The Fucking Args``",
                      "inline": False
                  }],
                  "footer": {
                      "text":
                      "Powered by discord.gg/membersv1 - andree4real eintommy",
                      "icon_url":
                      "https://images-ext-1.discordapp.net/external/2NAooU9gVTjbL1s_V6mVstZuyrVfaND6TwxXwzPJrYQ/%3Fsize%3D1024/https://cdn.discordapp.com/icons/1147749932757950514/7e7b0dc21cc38589daf1d46eda38f153.png?width=651&height=651"
                  }
              }]
          }

          response = requests.post(self.webhook, json=payload)

          return

        if ctx.channel.id != int(self.channelid):

          #embed=discord.Embed(description="*Error*", color=0x0000FF)
          embed = discord.Embed(title='**Error**', color=0x0000FF)
          # embed.set_author(icon_url="https://images-ext-1.discordapp.net/external/2NAooU9gVTjbL1s_V6mVstZuyrVfaND6TwxXwzPJrYQ/%3Fsize%3D1024/https/cdn.discordapp.com/icons/1147749932757950514/7e7b0dc21cc38589daf1d46eda38f153.png?width=651&height=651")
          embed.set_thumbnail(
              url=
              "https://images-ext-1.discordapp.net/external/2NAooU9gVTjbL1s_V6mVstZuyrVfaND6TwxXwzPJrYQ/%3Fsize%3D1024/https/cdn.discordapp.com/icons/1147749932757950514/7e7b0dc21cc38589daf1d46eda38f153.png?width=651&height=651"
          )
          # embed.add_field(value=f"Please Do The Command In The Right Channel.", inline=False)
          embed.add_field(name="**Channel Error**",
                          value=f"Please Do The Command In The Right Channel.",
                          inline=False)
          embed.set_footer(
              text="Powered by discord.gg/membersv1 - andree4real eintommy",
              icon_url=
              "https://images-ext-1.discordapp.net/external/2NAooU9gVTjbL1s_V6mVstZuyrVfaND6TwxXwzPJrYQ/%3Fsize%3D1024/https/cdn.discordapp.com/icons/1147749932757950514/7e7b0dc21cc38589daf1d46eda38f153.png?width=651&height=651"
          )
          await ctx.send(embed=embed)
          return

        bucket = self.cooldown.get_bucket(ctx.message)
        remaining_cooldown = bucket.update_rate_limit()
        if remaining_cooldown and remaining_cooldown > 0:

          #     embed=discord.Embed(description="*Error*", color=0x0000FF)
          embed = discord.Embed(title='**Error**', color=0x0000FF)
          #     embed.set_author(icon_url="https://images-ext-1.discordapp.net/external/2NAooU9gVTjbL1s_V6mVstZuyrVfaND6TwxXwzPJrYQ/%3Fsize%3D1024/https/cdn.discordapp.com/icons/1147749932757950514/7e7b0dc21cc38589daf1d46eda38f153.png?width=651&height=651")
          embed.set_thumbnail(
              url=
              "https://images-ext-1.discordapp.net/external/2NAooU9gVTjbL1s_V6mVstZuyrVfaND6TwxXwzPJrYQ/%3Fsize%3D1024/https/cdn.discordapp.com/icons/1147749932757950514/7e7b0dc21cc38589daf1d46eda38f153.png?width=651&height=651"
          )
          embed.add_field(
              name="**Cooldown**",
              value=f"You Are On Cooldown: ``{remaining_cooldown:.2f}``",
              inline=False)
          embed.set_footer(
              text="Powered by discord.gg/membersv1 - andree4real eintommy",
              icon_url=
              "https://images-ext-1.discordapp.net/external/2NAooU9gVTjbL1s_V6mVstZuyrVfaND6TwxXwzPJrYQ/%3Fsize%3D1024/https/cdn.discordapp.com/icons/1147749932757950514/7e7b0dc21cc38589daf1d46eda38f153.png?width=651&height=651"
          )
          await ctx.send(embed=embed)
          return

        user = ctx.author
        if servercode in self.user_codes:
          if self.user_codes[servercode] != user.id:
            #     embed=discord.Embed(description="*Error*", color=0x0000FF)
            embed = discord.Embed(title='**Error**', color=0x0000FF)
            #     embed.set_author(name="membersv1", icon_url="https://images-ext-1.discordapp.net/external/2NAooU9gVTjbL1s_V6mVstZuyrVfaND6TwxXwzPJrYQ/%3Fsize%3D1024/https/cdn.discordapp.com/icons/1147749932757950514/7e7b0dc21cc38589daf1d46eda38f153.png?width=651&height=651")
            embed.set_thumbnail(
                url=
                "https://images-ext-1.discordapp.net/external/2NAooU9gVTjbL1s_V6mVstZuyrVfaND6TwxXwzPJrYQ/%3Fsize%3D1024/https/cdn.discordapp.com/icons/1147749932757950514/7e7b0dc21cc38589daf1d46eda38f153.png?width=651&height=651"
            )
            embed.add_field(
                name="**Error**",
                value=
                f"`{servercode}`: Has Been Used By a Different User Already.",
                inline=False)
            embed.set_footer(
                text="Powered by discord.gg/membersv1 - andree4real eintommy",
                icon_url=
                "https://images-ext-1.discordapp.net/external/2NAooU9gVTjbL1s_V6mVstZuyrVfaND6TwxXwzPJrYQ/%3Fsize%3D1024/https/cdn.discordapp.com/icons/1147749932757950514/7e7b0dc21cc38589daf1d46eda38f153.png?width=651&height=651"
            )
            await ctx.send(embed=embed)

            payload = {
                "embeds": [{
                    "title":
                    "**Error**",
                    "color":
                    10992607,
                    "thumbnail": {
                        "url":
                        "https://images-ext-1.discordapp.net/external/2NAooU9gVTjbL1s_V6mVstZuyrVfaND6TwxXwzPJrYQ/%3Fsize%3D1024/https/cdn.discordapp.com/icons/1147749932757950514/7e7b0dc21cc38589daf1d46eda38f153.png?width=651&height=651"
                    },
                    "fields": [{
                        "name": "**ID**",
                        "value":
                        f"User ID: ``{ctx.author}``\nReason: ``User ID Is Alting The Server Code: {servercode}``",
                        "inline": False
                    }],
                    "footer": {
                        "text":
                        "Powered by discord.gg/membersv1 - andree4real eintommy",
                        "icon_url":
                        "https://images-ext-1.discordapp.net/external/2NAooU9gVTjbL1s_V6mVstZuyrVfaND6TwxXwzPJrYQ/%3Fsize%3D1024/https/cdn.discordapp.com/icons/1147749932757950514/7e7b0dc21cc38589daf1d46eda38f153.png?width=651&height=651"
                    }
                }]
            }

            response = requests.post(self.webhook, json=payload)
            return

        self.user_codes[servercode] = user.id

        user_roles = [role.name for role in ctx.author.roles]
        selected_role = None
        for role in user_roles:
          if role in self.njoinam:
            if selected_role is None or self.njoinam[role] > self.njoinam[
                selected_role]:
              selected_role = role

        if selected_role is None:
          return
        self.a = self.njoinam[selected_role]
        invite = servercode

        for i in range(int(self.a)):

          self.invite = invite
          threading.Thread(target=Functions.joinn,args=(self, self.tokstock, invite)).start()

        payload = {
            "embeds": [{
                "title":
                "**Success**",
                "color":
                10992607,
                "thumbnail": {
                    "url":
                    "https://images-ext-1.discordapp.net/external/2NAooU9gVTjbL1s_V6mVstZuyrVfaND6TwxXwzPJrYQ/%3Fsize%3D1024/https/cdn.discordapp.com/icons/1147749932757950514/7e7b0dc21cc38589daf1d46eda38f153.png?width=651&height=651"
                },
                "fields": [{
                    "name": "**Success**",
                    "value":
                    f"User ID: ``{ctx.author}``\nReason: ``Sent Members To {servercode}``",
                    "inline": False
                }],
                "footer": {
                    "text":
                    "Powered by discord.gg/membersv1 - andree4real eintommy",
                    "icon_url":
                    "https://images-ext-1.discordapp.net/external/2NAooU9gVTjbL1s_V6mVstZuyrVfaND6TwxXwzPJrYQ/%3Fsize%3D1024/https/cdn.discordapp.com/icons/1147749932757950514/7e7b0dc21cc38589daf1d46eda38f153.png?width=651&height=651"
                }
            }]
        }

        response = requests.post(self.webhook, json=payload)
        embed = discord.Embed(title="**Result**", color=discord.Color.blue())

        embed = discord.Embed(title='**Success**', color=0x0000FF)
        #     embed.set_author(name="membersv1", icon_url="https://images-ext-1.discordapp.net/external/2NAooU9gVTjbL1s_V6mVstZuyrVfaND6TwxXwzPJrYQ/%3Fsize%3D1024/https/cdn.discordapp.com/icons/1147749932757950514/7e7b0dc21cc38589daf1d46eda38f153.png?width=651&height=651")
        embed.set_thumbnail(
            url=
            "https://images-ext-1.discordapp.net/external/2NAooU9gVTjbL1s_V6mVstZuyrVfaND6TwxXwzPJrYQ/%3Fsize%3D1024/https/cdn.discordapp.com/icons/1147749932757950514/7e7b0dc21cc38589daf1d46eda38f153.png?width=651&height=651"
        )
        embed.add_field(name="**Results(Not Sure)**",
                        value=f"Sending `{self.a}` Joins To ``{servercode}``",
                        inline=False)

        embed.set_footer(
            text="Powered by discord.gg/membersv1 - andree4real eintommy",
            icon_url=
            "https://images-ext-1.discordapp.net/external/2NAooU9gVTjbL1s_V6mVstZuyrVfaND6TwxXwzPJrYQ/%3Fsize%3D1024/https/cdn.discordapp.com/icons/1147749932757950514/7e7b0dc21cc38589daf1d46eda38f153.png?width=651&height=651"
        )
        await ctx.send(embed=embed)

      except Exception as e:
        error_embed = discord.Embed(title='**Unknown Error**', color=0xFF0000)
        error_embed.set_thumbnail(
            url=
            "https://images-ext-1.discordapp.net/external/2NAooU9gVTjbL1s_V6mVstZuyrVfaND6TwxXwzPJrYQ/%3Fsize%3D1024/https/cdn.discordapp.com/icons/1147749932757950514/7e7b0dc21cc38589daf1d46eda38f153.png?width=651&height=651"
        )
        error_embed.add_field(name="**Error Message**",
                              value=str(e),
                              inline=False)
        error_embed.set_footer(
            text="Powered by discord.gg/membersv1 - andree4real eintommy",
            icon_url=
            "https://images-ext-1.discordapp.net/external/2NAooU9gVTjbL1s_V6mVstZuyrVfaND6TwxXwzPJrYQ/%3Fsize%3D1024/https/cdn.discordapp.com/icons/1147749932757950514/7e7b0dc21cc38589daf1d46eda38f153.png?width=651&height=651"
        )
        await ctx.send(embed=error_embed)

    @self.bot.command(name="friend",
                      description="Send Mass Amounts Of Friends")
    async def friend(ctx, idd: int = None):
      try:
        threads = []

        if idd is None:
          #embed=discord.Embed(description="*Error*", color=0x0000FF)
          embed = discord.Embed(title='**Error**', color=0x0000FF)
          # embed.set_author(name="membersv1", icon_url="https://images-ext-1.discordapp.net/external/2NAooU9gVTjbL1s_V6mVstZuyrVfaND6TwxXwzPJrYQ/%3Fsize%3D1024/https/cdn.discordapp.com/icons/1147749932757950514/7e7b0dc21cc38589daf1d46eda38f153.png?width=651&height=651")
          embed.set_thumbnail(
              url=
              "https://images-ext-1.discordapp.net/external/2NAooU9gVTjbL1s_V6mVstZuyrVfaND6TwxXwzPJrYQ/%3Fsize%3D1024/https/cdn.discordapp.com/icons/1147749932757950514/7e7b0dc21cc38589daf1d46eda38f153.png?width=651&height=651"
          )
          embed.add_field(
              name="**Args**",
              value=
              "Your Missing Required Args. Exa: !friend 1062700266157264936",
              inline=False)
          embed.set_footer(
              text="Powered by discord.gg/membersv1 - andree4real eintommy",
              icon_url=
              "https://images-ext-1.discordapp.net/external/2NAooU9gVTjbL1s_V6mVstZuyrVfaND6TwxXwzPJrYQ/%3Fsize%3D1024/https/cdn.discordapp.com/icons/1147749932757950514/7e7b0dc21cc38589daf1d46eda38f153.png?width=651&height=651"
          )
          await ctx.send(embed=embed)

          payload = {
              "embeds": [{
                  "title":
                  "**Error**",
                  "color":
                  10992607,
                  "thumbnail": {
                      "url":
                      "https://images-ext-1.discordapp.net/external/2NAooU9gVTjbL1s_V6mVstZuyrVfaND6TwxXwzPJrYQ/%3Fsize%3D1024/https/cdn.discordapp.com/icons/1147749932757950514/7e7b0dc21cc38589daf1d46eda38f153.png?width=651&height=651"
                  },
                  "fields": [{
                      "name": "**Args**",
                      "value":
                      f"User ID: ``{ctx.author}``\nIs Dumbass: ``Yes``\nReason: ``Forgot The Fucking Args``",
                      "inline": False
                  }],
                  "footer": {
                      "text":
                      "Powered by discord.gg/membersv1 - andree4real eintommy",
                      "icon_url":
                      "https://images-ext-1.discordapp.net/external/2NAooU9gVTjbL1s_V6mVstZuyrVfaND6TwxXwzPJrYQ/%3Fsize%3D1024/https/cdn.discordapp.com/icons/1147749932757950514/7e7b0dc21cc38589daf1d46eda38f153.png?width=651&height=651"
                  }
              }]
          }

          response = requests.post(self.webhook, json=payload)

          return

        if ctx.channel.id != int(self.channelid):

          #embed=discord.Embed(description="*Error*", color=0x0000FF)
          embed = discord.Embed(title='**Error**', color=0x0000FF)
          # embed.set_author(icon_url="https://images-ext-1.discordapp.net/external/2NAooU9gVTjbL1s_V6mVstZuyrVfaND6TwxXwzPJrYQ/%3Fsize%3D1024/https/cdn.discordapp.com/icons/1147749932757950514/7e7b0dc21cc38589daf1d46eda38f153.png?width=651&height=651")
          embed.set_thumbnail(
              url=
              "https://images-ext-1.discordapp.net/external/2NAooU9gVTjbL1s_V6mVstZuyrVfaND6TwxXwzPJrYQ/%3Fsize%3D1024/https/cdn.discordapp.com/icons/1147749932757950514/7e7b0dc21cc38589daf1d46eda38f153.png?width=651&height=651"
          )
          # embed.add_field(value=f"Please Do The Command In The Right Channel.", inline=False)
          embed.add_field(name="**Channel Error**",
                          value=f"Please Do The Command In The Right Channel.",
                          inline=False)
          embed.set_footer(
              text="andree4real ",
              icon_url=
              "https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&"
          )
          await ctx.send(embed=embed)
          return

        if idd == self.blacklistedusers:
          #     embed=discord.Embed(description="*Error*", color=0x0000FF)
          embed = discord.Embed(title='**Error**', color=0x0000FF)
          #     embed.set_author(name="membersv1", icon_url="https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&")
          embed.set_thumbnail(
              url=
              "https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&"
          )
          embed.add_field(name="**User ID**",
                          value=f"User ID Is Blacklisted.",
                          inline=False)
          embed.set_footer(
              text="andree4real ",
              icon_url=
              "https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&"
          )
          await ctx.send(embed=embed)

          payload = {
              "embeds": [{
                  "title":
                  "**Error**",
                  "color":
                  10992607,
                  "thumbnail": {
                      "url":
                      "https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&"
                  },
                  "fields": [{
                      "name": "**Blacklisted**",
                      "value":
                      f"User ID: ``{ctx.author}``\nIs Dumbass: ``Yes``\nReason: ``User ID Is Blacklisted``",
                      "inline": False
                  }],
                  "footer": {
                      "text":
                      "andree4real ",
                      "icon_url":
                      "https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&"
                  }
              }]
          }

          response = requests.post(self.webhook, json=payload)
          return

        bucket = self.cooldown.get_bucket(ctx.message)
        remaining_cooldown = bucket.update_rate_limit()
        if remaining_cooldown and remaining_cooldown > 0:

          #     embed=discord.Embed(description="*Error*", color=0x0000FF)
          embed = discord.Embed(title='**Error**', color=0x0000FF)
          #     embed.set_author(icon_url="https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&")
          embed.set_thumbnail(
              url=
              "https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&"
          )
          embed.add_field(
              name="**Cooldown**",
              value=f"You Are On Cooldown: ``{remaining_cooldown:.2f}``",
              inline=False)
          embed.set_footer(
              text="andree4real ",
              icon_url=
              "https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&"
          )
          await ctx.send(embed=embed)
          return

        user = ctx.author
        if idd in self.used_userids:
          if self.used_userids[idd] != user.id:
            #     embed=discord.Embed(description="*Error*", color=0x0000FF)
            embed = discord.Embed(title='**Error**', color=0x0000FF)
            #     embed.set_author(name="membersv1", icon_url="https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&")
            embed.set_thumbnail(
                url=
                "https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&"
            )
            embed.add_field(
                name="**Error**",
                value=f"`{idd}`: Has Been Used By a Different User ID Already.",
                inline=False)
            embed.set_footer(
                text="andree4real ",
                icon_url=
                "https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&"
            )
            await ctx.send(embed=embed)
            payload = {
                "embeds": [{
                    "title":
                    "**Error**",
                    "color":
                    10992607,
                    "thumbnail": {
                        "url":
                        "https://images-ext-1.discordapp.net/external/2NAooU9gVTjbL1s_V6mVstZuyrVfaND6TwxXwzPJrYQ/%3Fsize%3D1024/https/cdn.discordapp.com/icons/1147749932757950514/7e7b0dc21cc38589daf1d46eda38f153.png?width=651&height=651"
                    },
                    "fields": [{
                        "name": "**Alting**",
                        "value":
                        f"User ID: ``{ctx.author}``\nIs Dumbass: ``Yes``\nReason: ``{idd} Has Been Used By a Different User``",
                        "inline": False
                    }],
                    "footer": {
                        "text":
                        "andree4real ",
                        "icon_url":
                        "https://images-ext-1.discordapp.net/external/2NAooU9gVTjbL1s_V6mVstZuyrVfaND6TwxXwzPJrYQ/%3Fsize%3D1024/https/cdn.discordapp.com/icons/1147749932757950514/7e7b0dc21cc38589daf1d46eda38f153.png?width=651&height=651"
                    }
                }]
            }

            response = requests.post(self.webhook, json=payload)
            return

        self.used_userids[idd] = user.id
        # botnot = 0
        user_roles = [role.name for role in ctx.author.roles]
        selected_role = None
        for role in user_roles:
          if role in self.rolesfriends:
            if selected_role is None or self.rolesfriends[
                role] > self.rolesfriends[selected_role]:
              selected_role = role

        if selected_role is None:
          return
        self.a = self.rolesfriends[selected_role]
        self.idd = idd

        for i in range(int(self.a)):
          time.sleep(0.01)
          self.idd = idd
          threading.Thread(target=Functions.main,
                           args=(self, self.tokstock, idd)).start()

        payload = {
            "embeds": [{
                "title":
                "**Success**",
                "color":
                10992607,
                "thumbnail": {
                    "url":
                    "https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&"
                },
                "fields": [{
                    "name": "**Success**",
                    "value":
                    f"User ID: ``{ctx.author}``\nIs Dumbass: ``No``\nReason: ``{idd} Has Been Sent Friend Rqs``",
                    "inline": False
                }],
                "footer": {
                    "text":
                    "andree4real ",
                    "icon_url":
                    "https://images-ext-1.discordapp.net/external/2NAooU9gVTjbL1s_V6mVstZuyrVfaND6TwxXwzPJrYQ/%3Fsize%3D1024/https/cdn.discordapp.com/icons/1147749932757950514/7e7b0dc21cc38589daf1d46eda38f153.png?width=651&height=651"
                }
            }]
        }

        response = requests.post(self.webhook, json=payload)
        embed = discord.Embed(title="**Result**", color=discord.Color.blue())

        embed = discord.Embed(title='**Success**', color=0x0000FF)
        #     embed.set_author(name="membersv1", icon_url="https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&")
        embed.set_thumbnail(
            url=
            "https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&"
        )
        embed.add_field(name="**Results(Not Sure)**",
                        value=f"Sending `{self.a}` Rqs To ``{idd}``",
                        inline=False)

        embed.set_footer(
            text="andree4real ",
            icon_url=
            "https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&"
        )
        await ctx.send(embed=embed)
      except Exception as e:
        error_embed = discord.Embed(title='**Unknown Error**', color=0xFF0000)
        error_embed.set_thumbnail(
            url=
            "https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&"
        )
        error_embed.add_field(name="**Error Message**",
                              value=str(e),
                              inline=False)
        error_embed.set_footer(
            text="andree4real ",
            icon_url=
            "https://images-ext-1.discordapp.net/external/2NAooU9gVTjbL1s_V6mVstZuyrVfaND6TwxXwzPJrYQ/%3Fsize%3D1024/https/cdn.discordapp.com/icons/1147749932757950514/7e7b0dc21cc38589daf1d46eda38f153.png?width=651&height=651"
        )
        await ctx.send(embed=error_embed)

    @self.bot.command(name="join", description="Send Discord Members")
    async def join(ctx, serverid: int = None):
      userid = ctx.author.id
      if serverid in self.blacklist and serverid not in self.whitelist:
        #embed=discord.Embed(description="*Error*", color=0x0000FF)
        embed = discord.Embed(title='**Error**', color=0x0000FF)
        # embed.set_author(name="membersv1", icon_url="https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&")
        embed.set_thumbnail(
            url=
            "https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&"
        )
        embed.add_field(
            name="**Blacklisted**",
            value=f"A Owner Or Manager Blacklisted Your ID: {serverid}",
            inline=False)
        embed.set_footer(
            text="andree4real ",
            icon_url=
            "https://images-ext-1.discordapp.net/external/2NAooU9gVTjbL1s_V6mVstZuyrVfaND6TwxXwzPJrYQ/%3Fsize%3D1024/https/cdn.discordapp.com/icons/1147749932757950514/7e7b0dc21cc38589daf1d46eda38f153.png?width=651&height=651"
        )
        await ctx.send(embed=embed)
        payload = {
            "embeds": [{
                "title":
                "**Error**",
                "color":
                10992607,
                "thumbnail": {
                    "url":
                    "https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&"
                },
                "fields": [{
                    "name": "**Blacklisted ID**",
                    "value":
                    f"User ID: ``{ctx.author}``\nIs Dumbass: ``No, Hes A Retart``\nReason: ``Server ID Is Blacklisted``",
                    "inline": False
                }],
                "footer": {
                    "text":
                    "andree4real ",
                    "icon_url":
                    "https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&"
                }
            }]
        }

        response = requests.post(self.webhook, json=payload)

        return

      if userid in self.blacklistt and userid not in self.whitelistt:
        #embed=discord.Embed(description="*Error*", color=0x0000FF)
        embed = discord.Embed(title='**Error**', color=0x0000FF)
        # embed.set_author(name="membersv1", icon_url="https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&")
        embed.set_thumbnail(
            url=
            "https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&"
        )
        embed.add_field(
            name="**Blacklisted**",
            value=f"A Owner Or Manager Blacklisted Your ID: {userid}",
            inline=False)
        embed.set_footer(
            text="andree4real ",
            icon_url=
            "https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&"
        )
        await ctx.send(embed=embed)

        payload = {
            "embeds": [{
                "title":
                "**Error**",
                "color":
                10992607,
                "thumbnail": {
                    "url":
                    "https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&"
                },
                "fields": [{
                    "name": "**Blacklisted ID**",
                    "value":
                    f"User ID: ``{ctx.author}``\nIs Dumbass: ``No, Hes A Retart``\nReason: ``User ID Is Blacklisted``",
                    "inline": False
                }],
                "footer": {
                    "text":
                    "andree4real ",
                    "icon_url":
                    "https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&"
                }
            }]
        }

        response = requests.post(self.webhook, json=payload)

        return

      threads = []

      if serverid is None:
        #embed=discord.Embed(description="*Error*", color=0x0000FF)
        embed = discord.Embed(title='**Error**', color=0x0000FF)
        # embed.set_author(name="membersv1", icon_url="https://images-ext-1.discordapp.net/external/2NAooU9gVTjbL1s_V6mVstZuyrVfaND6TwxXwzPJrYQ/%3Fsize%3D1024/https/cdn.discordapp.com/icons/1147749932757950514/7e7b0dc21cc38589daf1d46eda38f153.png?width=651&height=651")
        embed.set_thumbnail(
            url=
            "https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&"
        )
        embed.add_field(name="**Args**",
                        value="Your Missing Required Args. Exa: !join 1234",
                        inline=False)
        embed.set_footer(
            text="andree4real ",
            icon_url=
            "https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&"
        )
        await ctx.send(embed=embed)
        payload = {
            "embeds": [{
                "title":
                "**Error**",
                "color":
                10992607,
                "thumbnail": {
                    "url":
                    "https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&"
                },
                "fields": [{
                    "name": "**Args**",
                    "value":
                    f"User ID: ``{ctx.author}``\nIs Dumbass: ``Yes``\nReason: ``Forgot The Fucking Args``",
                    "inline": False
                }],
                "footer": {
                    "text":
                    "andree4real ",
                    "icon_url":
                    "https://images-ext-1.discordapp.net/external/2NAooU9gVTjbL1s_V6mVstZuyrVfaND6TwxXwzPJrYQ/%3Fsize%3D1024/https/cdn.discordapp.com/icons/1147749932757950514/7e7b0dc21cc38589daf1d46eda38f153.png?width=651&height=651"
                }
            }]
        }

        response = requests.post(self.webhook, json=payload)

        return

      if ctx.channel.id != int(self.channelid):

        #embed=discord.Embed(description="*Error*", color=0x0000FF)
        embed = discord.Embed(title='**Error**', color=0x0000FF)
        # embed.set_author(icon_url="https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&")
        embed.set_thumbnail(
            url=
            "https://images-ext-1.discordapp.net/external/2NAooU9gVTjbL1s_V6mVstZuyrVfaND6TwxXwzPJrYQ/%3Fsize%3D1024/https/cdn.discordapp.com/icons/1147749932757950514/7e7b0dc21cc38589daf1d46eda38f153.png?width=651&height=651"
        )
        # embed.add_field(value=f"Please Do The Command In The Right Channel.", inline=False)
        embed.add_field(name="**Channel Error**",
                        value=f"Please Do The Command In The Right Channel.",
                        inline=False)
        embed.set_footer(
            text="andree4real ",
            icon_url=
            "https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&"
        )
        await ctx.send(embed=embed)
        return

      bucket = self.cooldown.get_bucket(ctx.message)
      remaining_cooldown = bucket.update_rate_limit()
      if remaining_cooldown and remaining_cooldown > 0:

        #     embed=discord.Embed(description="*Error*", color=0x0000FF)
        embed = discord.Embed(title='**Error**', color=0x0000FF)
        #     embed.set_author(icon_url="https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&")
        embed.set_thumbnail(
            url=
            "https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&"
        )
        embed.add_field(
            name="**Cooldown**",
            value=f"You Are On Cooldown: ``{remaining_cooldown:.2f}``",
            inline=False)
        embed.set_footer(
            text="andree4real ",
            icon_url=
            "https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&"
        )
        await ctx.send(embed=embed)
        return

      if serverid == self.blistedservids:
        #     embed=discord.Embed(description="*Error*", color=0x0000FF)
        embed = discord.Embed(title='**Error**', color=0x0000FF)
        #     embed.set_author(name="membersv1", icon_url="https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&")
        embed.set_thumbnail(
            url=
            "https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&"
        )
        embed.add_field(name="**membersv1 id**",
                        value=f"membersv1 Is Blacklisted. Try Your Own Server.",
                        inline=False)
        embed.set_footer(
            text="andree4real ",
            icon_url=
            "https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&"
        )
        await ctx.send(embed=embed)

        payload = {
            "embeds": [{
                "title":
                "**Error**",
                "color":
                10992607,
                "thumbnail": {
                    "url":
                    "https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&"
                },
                "fields": [{
                    "name": "**Blacklisted ID**",
                    "value":
                    f"User ID: ``{ctx.author}``\nIs Dumbass: ``No, Hes A Retart``\nReason: ``Server ID Is Blacklisted``",
                    "inline": False
                }],
                "footer": {
                    "text":
                    "andree4real ",
                    "icon_url":
                    "https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&"
                }
            }]
        }

        response = requests.post(self.webhook, json=payload)

        return

      server = self.bot.get_guild(serverid)
      if server:
        print('in server: yes')
        pass
      else:
        #     await ctx.send('No, I am not in that server.')
        embed = discord.Embed(description="*Error*", color=0x0000FF)
        embed = discord.Embed(title='**Error**', color=0x0000FF)
        #     embed.set_author(icon_url="https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&")
        embed.set_thumbnail(
            url=
            "https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&"
        )
        embed.add_field(name="**Bot Error**",
                        value="Please Invite The Bot. <#1147751347253428335>",
                        inline=False)
        embed.set_footer(
            text="andree4real ",
            icon_url=
            "https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&"
        )
        await ctx.send(embed=embed)

        payload = {
            "embeds": [{
                "title":
                "**Error**",
                "color":
                10992607,
                "thumbnail": {
                    "url":
                    "https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&"
                },
                "fields": [{
                    "name": "**Bot**",
                    "value":
                    f"User ID: ``{ctx.author}``\nIs Dumbass: ``No``\nReason: ``Bot Is Not In The Server``",
                    "inline": False
                }],
                "footer": {
                    "text":
                    "andree4real ",
                    "icon_url":
                    "https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&"
                }
            }]
        }
        response = requests.post(self.webhook, json=payload)

        return

      user = ctx.author
      if serverid in self.used_server_ids:
        if self.used_server_ids[serverid] != user.id:
          #     embed=discord.Embed(description="*Error*", color=0x0000FF)
          embed = discord.Embed(title='**Error**', color=0x0000FF)
          #     embed.set_author(name="membersv1", icon_url="https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&")
          embed.set_thumbnail(
              url=
              "https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&"
          )
          embed.add_field(
              name="**Error**",
              value=
              f"`{serverid}`: Has Been Used By a Different User ID Already.",
              inline=False)
          embed.set_footer(
              text="andree4real ",
              icon_url=
              "https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&"
          )
          await ctx.send(embed=embed)
          payload = {
              "embeds": [{
                  "title":
                  "**Error**",
                  "color":
                  10992607,
                  "thumbnail": {
                      "url":
                      "https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&"
                  },
                  "fields": [{
                      "name": "**ID**",
                      "value":
                      f"User ID: ``{ctx.author}``\nReason: ``User ID Is Alting The Server ID: {serverid}``",
                      "inline": False
                  }],
                  "footer": {
                      "text":
                      "andree4real ",
                      "icon_url":
                      "https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&"
                  }
              }]
          }

          response = requests.post(self.webhook, json=payload)

          return

      self.used_server_ids[serverid] = user.id
      # botnot = 0
      user_roles = [role.name for role in ctx.author.roles]
      selected_role = None
      for role in user_roles:
        if role in self.roles:
          if selected_role is None or self.roles[role] > self.roles[
              selected_role]:
            selected_role = role

      if selected_role is None:
        return
      self.a = self.roles[selected_role]
      self.aa = self.a + random.randint(1, 3)

      for i in range(int(self.aa)):
        self.serverid = serverid
        time.sleep(0.05)
        threading.Thread(target=Functions.memberadder, args=(self, )).start()

      embed = discord.Embed(title="**Result**", color=discord.Color.blue())

      embed = discord.Embed(title='**Success**', color=0x0000FF)
      #     embed.set_author(name="membersv1", icon_url="https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&")
      embed.set_thumbnail(
          url=
          "https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&"
      )
      embed.add_field(name="**Sending Members**",
                      value=f"Sending `{self.aa}` Members To ``{serverid}``",
                      inline=False)

      embed.set_footer(
          text="andree4real ",
          icon_url=
          "https://cdn.discordapp.com/attachments/1168665376842862712/1168677514001010749/Nuovo_progetto_1.png?ex=6552a2c0&is=65402dc0&hm=d1aea1ef49460457e34f16e62840383109dc35c9054014a5a87504ab086b0b00&"
      )
      await ctx.send(embed=embed)

      payload = {
          "embeds": [{
              "title":
              "**Success**",
              "color":
              10992607,
              "thumbnail": {
                  "url":
                  "https://images-ext-1.discordapp.net/external/2NAooU9gVTjbL1s_V6mVstZuyrVfaND6TwxXwzPJrYQ/%3Fsize%3D1024/https/cdn.discordapp.com/icons/1147749932757950514/7e7b0dc21cc38589daf1d46eda38f153.png?width=651&height=651"
              },
              "fields": [{
                  "name": "**Sending**",
                  "value":
                  f"User ID: ``{ctx.author}``\nIs Dumbass: ``No``\nReason: `Sending Members To {serverid}``",
                  "inline": False
              }],
              "footer": {
                  "text":
                  "Powered by discord.gg/membersv1 - andree4real eintommy",
                  "icon_url":
                  "https://images-ext-1.discordapp.net/external/2NAooU9gVTjbL1s_V6mVstZuyrVfaND6TwxXwzPJrYQ/%3Fsize%3D1024/https/cdn.discordapp.com/icons/1147749932757950514/7e7b0dc21cc38589daf1d46eda38f153.png?width=651&height=651"
              }
          }]
      }
      response = requests.post(self.webhook, json=payload)

      return

    @self.bot.command(name="bug", description="bug")
    async def bug(ctx, bug: str):
      embed = discord.Embed(title='**Bug**', color=0x0000FF)
      #     embed.set_author(name="membersv1", icon_url="https://images-ext-1.discordapp.net/external/2NAooU9gVTjbL1s_V6mVstZuyrVfaND6TwxXwzPJrYQ/%3Fsize%3D1024/https/cdn.discordapp.com/icons/1147749932757950514/7e7b0dc21cc38589daf1d46eda38f153.png?width=651&height=651")
      embed.set_thumbnail(
          url=
          "https://images-ext-1.discordapp.net/external/2NAooU9gVTjbL1s_V6mVstZuyrVfaND6TwxXwzPJrYQ/%3Fsize%3D1024/https/cdn.discordapp.com/icons/1147749932757950514/7e7b0dc21cc38589daf1d46eda38f153.png?width=651&height=651"
      )
      embed.add_field(name="**Bug**",
                      value=f"Bug Reported, Exclude Will Fix Shortly!",
                      inline=False)

      embed.set_footer(
          text="Powered by discord.gg/membersv1 - andree4real eintommy",
          icon_url=
          "https://images-ext-1.discordapp.net/external/2NAooU9gVTjbL1s_V6mVstZuyrVfaND6TwxXwzPJrYQ/%3Fsize%3D1024/https/cdn.discordapp.com/icons/1147749932757950514/7e7b0dc21cc38589daf1d46eda38f153.png?width=651&height=651"
      )
      await ctx.send(embed=embed)

      payload = {
          "embeds": [{
              "title":
              "**Bug Reported**",
              "color":
              10992607,
              "thumbnail": {
                  "url":
                  "https://images-ext-1.discordapp.net/external/2NAooU9gVTjbL1s_V6mVstZuyrVfaND6TwxXwzPJrYQ/%3Fsize%3D1024/https://cdn.discordapp.com/icons/1147749932757950514/7e7b0dc21cc38589daf1d46eda38f153.png?width=651&height=651"
              },
              "fields": [{
                  "name": "**Blacklisted ID**",
                  "value":
                  f"Bug Report Logs\nUser ID: ``{ctx.author}``\nReason: ``{bug}``",
                  "inline": False
              }],
              "footer": {
                  "text":
                  "Powered by discord.gg/membersv1 - andree4real eintommy",
                  "icon_url":
                  "https://images-ext-1.discordapp.net/external/2NAooU9gVTjbL1s_V6mVstZuyrVfaND6TwxXwzPJrYQ/%3Fsize%3D1024/https://cdn.discordapp.com/icons/1147749932757950514/7e7b0dc21cc38589daf1d46eda38f153.png?width=651&height=651"
              }
          }]
      }
      response = requests.post(self.webhook, json=payload)

      return

    @self.bot.command(name="servers", description="Check server amount.")
    async def servers(ctx):
      num_servers = len(self.bot.guilds)
      if num_servers == 100:
        embed = discord.Embed(title='**Oops**', color=0x0000FF)
        #     embed.set_author(name="membersv1", icon_url="https://images-ext-1.discordapp.net/external/2NAooU9gVTjbL1s_V6mVstZuyrVfaND6TwxXwzPJrYQ/%3Fsize%3D1024/https/cdn.discordapp.com/icons/1147749932757950514/7e7b0dc21cc38589daf1d46eda38f153.png?width=651&height=651")
        embed.set_thumbnail(
            url=
            "https://images-ext-1.discordapp.net/external/2NAooU9gVTjbL1s_V6mVstZuyrVfaND6TwxXwzPJrYQ/%3Fsize%3D1024/https/cdn.discordapp.com/icons/1147749932757950514/7e7b0dc21cc38589daf1d46eda38f153.png?width=651&height=651"
        )
        embed.add_field(
            name="**Amount**",
            value=
            f"This Bot Is At The Max Servers Of 100. Ping Exclude Or Staff To Clear.",
            inline=False)

        embed.set_footer(
            text="Powered by discord.gg/membersv1 - andree4real eintommy",
            icon_url=
            "https://images-ext-1.discordapp.net/external/2NAooU9gVTjbL1s_V6mVstZuyrVfaND6TwxXwzPJrYQ/%3Fsize%3D1024/https/cdn.discordapp.com/icons/1147749932757950514/7e7b0dc21cc38589daf1d46eda38f153.png?width=651&height=651"
        )
        await ctx.send(embed=embed)
        return

      embed = discord.Embed(title='**Servers**', color=0x0000FF)
      #     embed.set_author(name="membersv1", icon_url="https://images-ext-1.discordapp.net/external/2NAooU9gVTjbL1s_V6mVstZuyrVfaND6TwxXwzPJrYQ/%3Fsize%3D1024/https/cdn.discordapp.com/icons/1147749932757950514/7e7b0dc21cc38589daf1d46eda38f153.png?width=651&height=651")
      embed.set_thumbnail(
          url=
          "https://images-ext-1.discordapp.net/external/2NAooU9gVTjbL1s_V6mVstZuyrVfaND6TwxXwzPJrYQ/%3Fsize%3D1024/https/cdn.discordapp.com/icons/1147749932757950514/7e7b0dc21cc38589daf1d46eda38f153.png?width=651&height=651"
      )
      embed.add_field(name="**Amount**",
                      value=f"This Bot is At {num_servers} Servers.",
                      inline=False)

      embed.set_footer(
          text="Powered by discord.gg/membersv1 - andree4real eintommy",
          icon_url=
          "https://images-ext-1.discordapp.net/external/2NAooU9gVTjbL1s_V6mVstZuyrVfaND6TwxXwzPJrYQ/%3Fsize%3D1024/https/cdn.discordapp.com/icons/1147749932757950514/7e7b0dc21cc38589daf1d46eda38f153.png?width=651&height=651"
      )
      await ctx.send(embed=embed)

    @self.bot.command(name="leave", description="Mass leave servers.")
    async def leave(ctx):
      user_roles = [role.name for role in ctx.author.roles]
      if any(role in self.allowed_roles for role in user_roles):
        embed = discord.Embed(title='**Servers**', color=0x0000FF)
        #     embed.set_author(name="membersv1", icon_url="https://images-ext-1.discordapp.net/external/2NAooU9gVTjbL1s_V6mVstZuyrVfaND6TwxXwzPJrYQ/%3Fsize%3D1024/https/cdn.discordapp.com/icons/1147749932757950514/7e7b0dc21cc38589daf1d46eda38f153.png?width=651&height=651")
        embed.set_thumbnail(
            url=
            "https://images-ext-1.discordapp.net/external/2NAooU9gVTjbL1s_V6mVstZuyrVfaND6TwxXwzPJrYQ/%3Fsize%3D1024/https/cdn.discordapp.com/icons/1147749932757950514/7e7b0dc21cc38589daf1d46eda38f153.png?width=651&height=651"
        )
        embed.add_field(name="**Leaving**",
                        value=f"Leaving All Servers",
                        inline=False)

        embed.set_footer(
            text="Powered by discord.gg/membersv1 - andree4real eintommy",
            icon_url=
            "https://images-ext-1.discordapp.net/external/2NAooU9gVTjbL1s_V6mVstZuyrVfaND6TwxXwzPJrYQ/%3Fsize%3D1024/https/cdn.discordapp.com/icons/1147749932757950514/7e7b0dc21cc38589daf1d46eda38f153.png?width=651&height=651"
        )
        await ctx.send(embed=embed)

        payload = {
            "embeds": [{
                "title":
                "**Leave CMD**",
                "color":
                10992607,
                "thumbnail": {
                    "url":
                    "https://images-ext-1.discordapp.net/external/2NAooU9gVTjbL1s_V6mVstZuyrVfaND6TwxXwzPJrYQ/%3Fsize%3D1024/https://cdn.discordapp.com/icons/1147749932757950514/7e7b0dc21cc38589daf1d46eda38f153.png?width=651&height=651"
                },
                "fields": [{
                    "name": "**Blacklisted ID**",
                    "value":
                    f"User ID: ``{ctx.author}``\nUser Did Leave Command``",
                    "inline": False
                }],
                "footer": {
                    "text":
                    "Powered by discord.gg/membersv1 - andree4real eintommy",
                    "icon_url":
                    "https://images-ext-1.discordapp.net/external/2NAooU9gVTjbL1s_V6mVstZuyrVfaND6TwxXwzPJrYQ/%3Fsize%3D1024/https://cdn.discordapp.com/icons/1147749932757950514/7e7b0dc21cc38589daf1d46eda38f153.png?width=651&height=651"
                }
            }]
        }

        response = requests.post(self.webhook, json=payload)

        for guild in self.bot.guilds:
          if guild.id not in self.guilds_to_keep:
            await guild.leave()
        else:
          pass
   

  def run_bot(self):
    intents = discord.Intents.default()
    intents.typing = True
    intents.presences = True
    intents.message_content = True

    self.bot = commands.Bot(command_prefix=self.bot_prefix,
                            help_command=None,
                            intents=intents)
    
    self.commands()
    self.bot.run(self.bot_token)


if __name__ == "__main__":
  Discord_Bot()

#     bot.run(tkn)

# HERE IS EXTRA CODE, FOR CAPTCHA ADDING

# def generate_code():
#    characters = string.ascii_letters + string.digits
#    code = ''.join(random.choice(characters) for _ in range(3))
#    return code

#    code = generate_code()
#    user_codes[ctx.author.id] = code
#
#    # Send the code to the user
#    embed = discord.Embed(
#        title="**Security**",
#        description=f"Enter The Code {ctx.author.mention}: ``{code}``",
#        color=discord.Color.blue()
#    )
#    embed.set_footer(text="Powered by Discord.gg/membersv1 - andree4real eintommy")
#    await ctx.send(embed=embed)
#
#   # Wait for the user's response
#    def check(msg):
#        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content == code
#
#    try:
#        await bot.wait_for('message', check=check, timeout=60)
#    except TimeoutError:
#        # If the user doesn't respond in time
#        embed = discord.Embed(
#            title="**Timeout**",
#            description=f"You Reached Time Limit. Try Again In 2 Minutes",
#            color=discord.Color.blue()
#        )
#        embed.set_footer(text="Powered by Discord.gg/membersv1 - andree4real eintommy")
#        await ctx.send(embed=embed)
#        return

# HERE IS A EXAMPLE OF A QUEUE SYSTEM
# YOU HAVE TO DO SOME EDITING FOR IT TO WORK.

#        queue = []

#            queue.append(ctx.author)
#            await asyncio.sleep(30)
#            if ctx.author in queue:
#                queue.remove(ctx.author)
