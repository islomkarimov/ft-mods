from .. import loader, utils
from asyncio import sleep

class ArtMod(loader.Module):
	strings = {"name": "TxtArt"}

	async def helpartcmd(self,message):
		await message.edit('''***ЗВЕРУШКИ***

.cat - котик
.bear - медведь
.dog1- собака 1 вариант
.dog2 - собака 2 вариант
.pig - свинка
.sheep - овечка
.mk - обезьянка
.bird - птичка
.kit - кит
.gus - гусеница
.trollface - тролл морда

***ЛЮБОВЬ***

.heart - сердечко
.kiss - KISS
.iu - I ❤️ U
.lovebus - автобус с надписью love
.mhearts - много сердец

***ПЕРСОНАЖИ***

.bart - Барт Симпсон
.homer - Гомер Симпсон
.bob - Губка Боб
.bender - Бендер
.droid - Android

***С АНИМАЦИЕЙ***

.animiu - I ❤️ U (с аним.)
.animgus - гусеница (с аним.)
.animkiss - KISS (с аним.)

by islom ''')
	
	#ЗВЕРУШКИ
	
	async def trollfacecmd(self,message):
		await message.edit('''░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄
░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄
░░░█░░░▒▒▒▒▒▒░░░░░░░░▒▒▒░░█
░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░█
░▀▒▄▄▄▒░█▀▀▀▀▄▄█░░░██▄▄█░░░█
█▒█▒▄░▀▄▄▄▀░░░░░░░░█░░░▒▒▒▒▒█
█▒█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄▒█
░█▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█
░░█░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█
░░░█░░██░░▀█▄▄▄█▄▄█▄████░█
░░░░█░░░▀▀▄░█░░░█░███████░█
░░░░░▀▄░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█
░░░░░░░▀▄▄░▒▒▒▒░░░░░░░░░░█
░░░░░░░░░░▀▀▄▄░▒▒▒▒▒▒▒▒▒▒░█
░░░░░░░░░░░░░░▀▄▄▄▄▄░░░░░█''')

	async def catcmd(self,message):
		await message.edit('''╭━━━╮┈┈╱╲┈┈┈╱╲
┃╭━━╯┈┈▏▔▔▔▔▔▕
┃╰━━━━━▏╭▆┊╭▆▕
╰┫╯╯╯╯╯▏╰╯▼╰╯▕
┈┃╯╯╯╯╯▏╰━┻━╯▕
┈╰┓┏┳━┓┏┳┳━━━╯
┈┈┃┃┃┈┃┃┃┃┈┈┈┈
┈┈┗┻┛┈┗┛┗┛┈┈┈┈''')

	async def bearcmd(self,message):
		await message.edit('''┈┈╭━╱▔▔▔▔╲━╮┈┈┈
┈┈╰╱╭▅╮╭▅╮╲╯┈┈┈
╳┈┈▏╰┈▅▅┈╯▕┈┈┈┈
┈┈┈╲┈╰━━╯┈╱┈┈╳┈
┈┈┈╱╱▔╲╱▔╲╲┈┈┈┈
┈╭━╮▔▏┊┊▕▔╭━╮┈╳
┈┃┊┣▔╲┊┊╱▔┫┊┃┈┈
┈╰━━━━╲╱━━━━╯┈╳''')

	async def dog1cmd(self,message):
		await message.edit('''┈╭━━━━━━━━━━━╮┈ 
╭╯┈╭━━╮┈╭━━╮┈╰╮ 
┃┈┃┃╭╮┃┈┃╭╮┃┃┈┃ 
┃┈┃┻┻┻┛┈┗┻┻┻┃┈┃ 
┃┈┃╭╮┈◢▇◣┈╭╮┃┈┃ 
╰┳╯┃╰━━┳┳┳╯┃╰┳╯ 
┈┃┈╰━━━┫┃┣━╯┈┃┈ 
┈┃┈┈┈┈┈╰━╯┈┈┈┃┈
''')

	async def dog2cmd(self,message):
		await message.edit('''╱▏┈┈┈┈┈┈▕╲▕╲┈┈┈
▏▏┈┈┈┈┈┈▕▏▔▔╲┈┈
▏╲┈┈┈┈┈┈╱┈▔┈▔╲┈
╲▏▔▔▔▔▔▔╯╯╰┳━━▀
┈▏╯╯╯╯╯╯╯╯╱┃┈┈┈
┈┃┏┳┳━━━┫┣┳┃┈┈┈
┈┃┃┃┃┈┈┈┃┃┃┃┈┈┈
┈┗┛┗┛┈┈┈┗┛┗┛┈┈┈
''')

	async def pigcmd(self,message):
		await message.edit('''┈┏━╮╭━┓┈╭━━━━╮
┈┃┏┗┛┓┃╭┫ⓞⓘⓝⓚ┃
┈╰┓▋▋┏╯╯╰━━━━╯
╭━┻╮╲┗━━━━╮╭╮┈
┃▎▎┃╲╲╲╲╲╲┣━╯┈
╰━┳┻▅╯╲╲╲╲┃┈┈┈
┈┈╰━┳┓┏┳┓┏╯┈┈┈
┈┈┈┈┗┻┛┗┻┛┈┈┈┈
''')

	async def sheepcmd(self,message):
		await message.edit('''▕▔▔╲╱▔▔▔╲╱▔▔▏
┈╲＿╱╰╮┈╭╯╲＿╱
┈┈┈▏▉╮┈╭▉▕
┈┈╱╲╰╰┊╯╯╱╲
┈╱╰▕╰╰┳╯╯▏╯╲
▕╰╰╰╲╰┻╯╱╯╯╯▏
▕╰╰╰╰▔▔▔╯╯╯╯▏
▕╰╰╰╰╰╮╭╯╯╯╯▏
┈╲╭╮┈╰╮╭╯╭╮╱
┈┈┫┣╭━━━╮┫┃
┈┈┃┃┃┈┈┈┃┃┃
┈┈┗┛┛┈┈┈┗┗┛
''')

	async def mkcmd(self,message):
		await message.edit('''┊┊┊╱▔▔▔▔▔╲┊┊┊┊┊
┊┊╱┈┈╱▔╲╲╲▏┊┊┊┊
┊╱┈╭━━╱▔▔▔▔╲━━╮
┊▏┈┃▔▔▏╭▅╭▅▕▔▔┃
┊▏┈╰━╱┈╭┳┳╮┳╲━╯
┊╲┈┈╲▏╭━━━━╯▕┊┊
┊┊╲┈┈╲▂▂▂▂▂▂╱▔╲
''')

	async def birdcmd(self,message):
		await message.edit('''┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈
┈╭━━━━━╮┈┈┈┈┈┈┈┈
┈╰┳━━━━╰╮╭━╮┈┈┈┈
┈┈╰┳━━━━┣╯▊╲┈┈┈┈
┈┈┈╰━┳━━╯╰╱▔┈┈┈┈
┈┈┈┈┈╰━┳┳╯┈┈┈┈┈┈
━━━━━━━┻┻━━━━━━━''')

	async def kitcmd(self,message):
		await message.edit('''┊┊┊┊┊╭╭╭╮╮╮┊┊┊┊ 
┊┊┊┊┊╰╰╲╱╯╯┊┊┊┊ 
┊┏╮╭┓╭━━━━━━╮┊┊ 
┊╰╮╭╯┃┈┈┈┈┈┈┃┊┊ 
┊┊┃╰━╯┈┈╰╯┈┈┃┊┊ 
┊┊┃┈┈┈┈┈┈┈╰━┫┊┊ 
╲╱╲╱╲╱╲╱╲╱╲╱╲╱╲

''')

	async def guscmd(self,message):
		await message.edit('''. .╚⊙ ⊙╝..
╚═███═╝
.╚═███═╝
..╚═███═╝
...╚═███═╝
...╚═███═╝
..╚═███═╝
.╚═███═╝
╚═███═╝
╚═███═╝
.╚═███═╝
..╚═███═╝
...╚═███═╝
...╚═███═╝
..╚═███═╝
.╚═███═╝
╚═███═╝
╚═███═╝
.╚═███═╝
..╚═███═╝
...╚═███═╝
.... ╚═█═╝
''')


	#ЛЮБОВЬ *1000-7*

	async def heartcmd(self,message):
		await message.edit('''_____$$$$_________$$$$
___$$$$$$$$_____$$$$$$$$
_$$$$$$$$$$$$_$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$
_$$$$$$$$$$$$$$$$$$$$$$$$$
__$$$$$$$$$$$$$$$$$$$$$$$
____$$$$$$$$$$$$$$$$$$$
_______$$$$$$$$$$$$$
__________$$$$$$$
____________$$$
_____________$''')

	async def kisscmd(self,message):
		await message.edit('''▄▀▀▄▄▀▀▀▄
█▌▐██▌▄██
█▌▐█▌▄███
█▌▐▌▄████
█▌░▐█████
█▌▐▌▀████
█▌▐█▌▀███
█▌▐██▌▀██
▀▄▄▀▀▄▄▄▀

▄▄▄▀▀▄▄▄▄▄
██████████
███▌▐█████
███▌▐█████
███▌▐█████
███▌▐█████
███▌▐█████
███▌▐█████
▀▀▀▄▄▀▀▀▀▀

▄▄▄▄▄▄▄▄▄▄
███▀▀▀▀███
██▌░▐▄▄▐██
██▌░▐█████
██▌░▀▀▀▐██
██▀▀█▌░▐██
██▌▐█▌░▐██
██▌▐▀▀░▐██
███▄▄▄▄███

▄▄▄▄▄▄▄▄▄▄
███▀▀▀▀███
██▌░▐▄▄▐██
██▌░▐█████
██▌░▀▀▀▐██
██▀▀█▌░▐██
██▌▐█▌░▐██
██▌▐▀▀░▐██
███▄▄▄▄███
''')

	async def iucmd(self,message):
		await message.edit('''111111111111111111111111111
1_________________________1
1_________________________1
1_______¶¶¶¶¶¶¶¶¶¶________1
1_________¶¶¶¶¶¶__________1
1_________¶¶¶¶¶¶__________1
1_________¶¶¶¶¶¶__________1
1_________¶¶¶¶¶¶__________1
1_________¶¶¶¶¶¶__________1
1_________¶¶¶¶¶¶__________1
1_________¶¶¶¶¶¶__________1
1_________¶¶¶¶¶¶__________1
1_________¶¶¶¶¶¶__________1
1_______¶¶¶¶¶¶¶¶¶¶________1
1_________________________1
1_________________________1
1____¶¶¶¶¶_______¶¶¶¶¶____1
1__¶¶¶¶¶¶¶¶¶___¶¶¶¶¶¶¶¶¶__1
1_¶¶¶¶¶¶¶¶¶¶¶_¶¶¶¶¶¶¶¶¶¶¶_1
1_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_1
1__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__1 
1____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶____1
1______¶¶¶¶¶¶¶¶¶¶¶¶¶______1
1________¶¶¶¶¶¶¶¶¶________1
1_________¶¶¶¶¶¶¶_________1
1__________¶¶¶¶¶__________1
1___________¶¶¶___________1 
1____________¶____________1
1_________________________1
1_________________________1
1_¶¶¶¶¶¶¶¶¶_____¶¶¶¶¶¶¶¶¶_1
1___¶¶¶¶¶_________¶¶¶¶¶___1
1___¶¶¶¶¶_________¶¶¶¶¶___1
1___¶¶¶¶¶_________¶¶¶¶¶___1
1___¶¶¶¶¶_________¶¶¶¶¶___1
1___¶¶¶¶¶_________¶¶¶¶¶___1
1___¶¶¶¶¶_________¶¶¶¶¶___1
1___¶¶¶¶¶_________¶¶¶¶¶___1
1___¶¶¶¶¶¶_______¶¶¶¶¶¶___1
1____¶¶¶¶¶¶_____¶¶¶¶¶¶____1
1______¶¶¶¶¶¶¶¶¶¶¶¶¶______1
1________¶¶¶¶¶¶¶¶¶________1
1_________________________1
111111111111111111111111111
''')

	async def lovebuscmd(self,message):
		await message.edit('''┈╱▔▔▔▔▔▔▔▔╲┈┈┈┈ 
╱▔▔▔▔▔▔▔▔╲╱┈┈┈┈
▏┳╱╭╮┓┏┏┓▕╱▔▔╲┈
▏┃╱┃┃┃┃┣▏▕▔▔╲╱▏
▏┻┛╰╯╰╯┗┛▕▕▉▕╱╲
▇▇▇▇▇▇▇▇▇▇▔▔▔╲▕
▇▇╱▔╲▇▇▇▇▇╱▔╲▕╱
┈┈╲▂╱┈┈┈┈┈╲▂╱▔┈
''')

	async def mheartscmd(self,message):
		await message.edit('''_$$$_$$$
$$$$$$$$$
$$$$$$$$$
_$$$$$$$
__$$$$$___$$_$$
___$$$___$$$$$$$
____$____$$$$$$$
__________$$$$$
___$_$_____$$$
__$$$$$_____$
__$$$$$
___$$$
____$
____o
_____o
_______o
________o
________ o
______$$$_$$$
_____$$$$$$$$$
_____$$$$$$$$$
______$$$$$$$
_______$$$$$
________$$$
_________$
_________o
__________o
___________ o
__________$$_$$
_________$$$$$$$
_________$$$$$$$
__________$$$$$
___________$$$
____________$
____________o
__________ o
________ o
______ o
_____o
____$_$
___$$$$$
___$$$$$
____$$$
_____$
''')


	#ПЕРСЫ

	async def bartcmd(self,message):
		await message.edit('''_____________¶____¶ 
_________¶_¶¶¶¶¶¶¶¶¶¶ 
_____¶¶¶¶¶¶¶_________¶ 
___¶¶¶¶¶_____________¶ 
___¶_________________¶ 
____¶________________¶¶ 
____¶¶________________¶ 
_____¶________________¶¶ 
_____¶¶_______¶¶¶____¶¶¶ 
______¶_____¶¶___¶¶_¶___¶ 
______¶_____¶¶_____¶____¶ 
______¶¶____¶______¶¶¶¶¶¶¶ 
_______¶____¶¶__¶¶¶_____¶¶ 
______¶¶¶¶____¶¶¶¶_____¶¶ 
______¶¶¶_______________¶¶ 
_______¶¶¶______________¶¶ 
________¶_____¶¶¶¶¶¶¶¶¶¶¶ 
_______¶¶_______¶¶¶¶¶ 
______¶¶¶¶¶_____¶ 
___¶¶¶¶__¶¶¶¶¶¶¶¶ 
__¶¶____¶¶_____¶¶ 
_¶¶_____¶¶______¶¶ 
¶¶______¶¶_______¶¶ 
_¶¶¶¶¶___¶¶______¶¶ 
_¶__¶¶¶¶¶¶_______¶¶ 
¶¶____¶___________¶¶ 
¶____¶¶__________¶¶¶ 
¶____¶¶____________¶ 
¶_____¶___________¶¶¶ 
¶_____¶¶¶¶¶¶¶¶¶¶¶¶¶_¶ 
¶______¶_________¶___¶ 
¶¶¶¶__¶__________¶_¶¶¶ 
_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ 
___¶¶¶¶¶¶¶¶¶____¶ 
___¶¶___¶__¶____¶ 
___¶____¶__¶____¶ 
___¶¶___¶__¶____¶¶ 
__¶_______¶¶¶¶¶¶¶¶¶¶ 
_¶¶¶¶¶¶¶¶¶¶¶__¶¶¶¶¶¶¶ 
_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
''')

	async def homercmd(self,message):
		await message.edit('''┈┈┈╭━━━━━╮┈┈┈┈┈
┈┈┈┃┊┊┊┊┊┃┈┈┈┈┈
┈┈┈┃┊┊╭━╮┻╮┈┈┈┈
┈┈┈╱╲┊┃▋┃▋┃┈┈┈┈
┈┈╭┻┊┊╰━┻━╮┈┈┈┈
┈┈╰┳┊╭━━━┳╯┈┈┈┈
┈┈┈┃┊┃╰━━┫┈HOMER
┈┈┈┈┈┈┏━┓┈┈┈┈┈┈
''')

	async def bobcmd(self,message):
		await message.edit('''┈┈╱▔▔▔▔▔▔▔▔▔▔▔▏ 
┈╱╭▏╮╭┻┻╮╭┻┻╮╭▏ 
▕╮╰▏╯┃╭╮┃┃╭╮┃╰▏ 
▕╯┈▏┈┗┻┻┛┗┻┻┻╮▏ 
▕╭╮▏╮┈┈┈┈┏━━━╯▏
▕╰╯▏╯╰┳┳┳┳┳┳╯╭▏ 
▕┈╭▏╭╮┃┗┛┗┛┃┈╰▏ 
▕┈╰▏╰╯╰━━━━╯┈┈▏
''')

	async def bendercmd(self,message):
		await message.edit('''____________¶¶¶
___________¶___¶
____________¶¶¶
____________¶_¶
____________¶_¶
__________¶¶¶_¶¶¶
________¶¶__¶¶¶__¶¶¶
______¶¶__¶¶¶¶¶¶¶___¶
_____¶_______________¶
____¶_________________¶
____¶_________________¶
____¶_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
____¶____¶_______________¶
____¶____¶___¶¶¶¶¶¶¶¶¶¶¶¶¶
____¶___¶___¶___________¶¶¶
____¶___¶___¶_¶¶¶___¶¶¶__¶¶
____¶___¶___¶_¶¶¶___¶¶¶__¶¶
____¶___¶___¶___________¶¶¶
____¶____¶___¶¶¶¶¶¶¶¶¶¶¶¶¶
____¶_____¶¶¶¶¶¶¶¶¶¶¶¶¶¶
____¶_________________¶
____¶____¶¶¶¶¶¶¶¶¶¶¶¶¶¶
____¶___¶__¶__¶__¶__¶
____¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶
____¶__¶___¶__¶__¶__¶
____¶___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
___¶¶¶_________________¶¶¶
''')

	async def droidcmd(self,message):
		await message.edit('''┈┈┈╲┈┈┈┈╱
┈┈┈╱▔▔▔▔╲
┈┈┃┈▇┈┈▇┈┃
╭╮┣━━━━━━┫╭╮
┃┃┃┈┈┈┈┈┈┃┃┃
╰╯┃┈┈┈┈┈┈┃╰╯
┈┈╰┓┏━━┓┏╯
┈┈┈╰╯┈┈╰╯
''')
	

	#ANIMATION

	async def animiucmd(self,message):
		await message.edit('''111111111111111111111111111
1_________________________1
1_________________________1
1_______¶¶¶¶¶¶¶¶¶¶________1
1_________¶¶¶¶¶¶__________1''')
		await sleep(0.4)

		await message.edit('''111111111111111111111111111
1_________________________1
1_________________________1
1_______¶¶¶¶¶¶¶¶¶¶________1
1_________¶¶¶¶¶¶__________1
1_________¶¶¶¶¶¶__________1
1_________¶¶¶¶¶¶__________1
1_________¶¶¶¶¶¶__________1
1_________¶¶¶¶¶¶__________1
1_________¶¶¶¶¶¶__________1
1_________¶¶¶¶¶¶__________1''')
		await sleep(0.4)

		await message.edit('''111111111111111111111111111
1_________________________1
1_________________________1
1_______¶¶¶¶¶¶¶¶¶¶________1
1_________¶¶¶¶¶¶__________1
1_________¶¶¶¶¶¶__________1
1_________¶¶¶¶¶¶__________1
1_________¶¶¶¶¶¶__________1
1_________¶¶¶¶¶¶__________1
1_________¶¶¶¶¶¶__________1
1_________¶¶¶¶¶¶__________1
1_________¶¶¶¶¶¶__________1
1_________¶¶¶¶¶¶__________1
1_______¶¶¶¶¶¶¶¶¶¶________1
1_________________________1''')
		await sleep(0.4)


		await message.edit('''111111111111111111111111111
1_________________________1
1_________________________1
1_______¶¶¶¶¶¶¶¶¶¶________1
1_________¶¶¶¶¶¶__________1
1_________¶¶¶¶¶¶__________1
1_________¶¶¶¶¶¶__________1
1_________¶¶¶¶¶¶__________1
1_________¶¶¶¶¶¶__________1
1_________¶¶¶¶¶¶__________1
1_________¶¶¶¶¶¶__________1
1_________¶¶¶¶¶¶__________1
1_________¶¶¶¶¶¶__________1
1_______¶¶¶¶¶¶¶¶¶¶________1
1_________________________1
1_________________________1
1____¶¶¶¶¶_______¶¶¶¶¶____1
1__¶¶¶¶¶¶¶¶¶___¶¶¶¶¶¶¶¶¶__1
1_¶¶¶¶¶¶¶¶¶¶¶_¶¶¶¶¶¶¶¶¶¶¶_1
1_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_1
1__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__1
1____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶____1
1______¶¶¶¶¶¶¶¶¶¶¶¶¶______1
1________¶¶¶¶¶¶¶¶¶________1
1_________¶¶¶¶¶¶¶_________1
1__________¶¶¶¶¶__________1''')
		await sleep(0.4)

		await message.edit('''111111111111111111111111111
1_________________________1
1_________________________1
1_______¶¶¶¶¶¶¶¶¶¶________1
1_________¶¶¶¶¶¶__________1
1_________¶¶¶¶¶¶__________1
1_________¶¶¶¶¶¶__________1
1_________¶¶¶¶¶¶__________1
1_________¶¶¶¶¶¶__________1
1_________¶¶¶¶¶¶__________1
1_________¶¶¶¶¶¶__________1
1_________¶¶¶¶¶¶__________1
1_________¶¶¶¶¶¶__________1
1_______¶¶¶¶¶¶¶¶¶¶________1
1_________________________1
1_________________________1
1____¶¶¶¶¶_______¶¶¶¶¶____1
1__¶¶¶¶¶¶¶¶¶___¶¶¶¶¶¶¶¶¶__1
1_¶¶¶¶¶¶¶¶¶¶¶_¶¶¶¶¶¶¶¶¶¶¶_1
1_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_1
1__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__1
1____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶____1
1______¶¶¶¶¶¶¶¶¶¶¶¶¶______1
1________¶¶¶¶¶¶¶¶¶________1
1_________¶¶¶¶¶¶¶_________1
1__________¶¶¶¶¶__________1
1____________¶____________1
1_________________________1
1_________________________1
1_¶¶¶¶¶¶¶¶¶_____¶¶¶¶¶¶¶¶¶_1
1___¶¶¶¶¶_________¶¶¶¶¶___1''')
		await sleep(0.4)

		await message.edit('''111111111111111111111111111
1_________________________1
1_________________________1
1_______¶¶¶¶¶¶¶¶¶¶________1
1_________¶¶¶¶¶¶__________1
1_________¶¶¶¶¶¶__________1
1_________¶¶¶¶¶¶__________1
1_________¶¶¶¶¶¶__________1
1_________¶¶¶¶¶¶__________1
1_________¶¶¶¶¶¶__________1
1_________¶¶¶¶¶¶__________1
1_________¶¶¶¶¶¶__________1
1_________¶¶¶¶¶¶__________1
1_______¶¶¶¶¶¶¶¶¶¶________1
1_________________________1
1_________________________1
1____¶¶¶¶¶_______¶¶¶¶¶____1
1__¶¶¶¶¶¶¶¶¶___¶¶¶¶¶¶¶¶¶__1
1_¶¶¶¶¶¶¶¶¶¶¶_¶¶¶¶¶¶¶¶¶¶¶_1
1_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_1
1__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__1
1____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶____1
1______¶¶¶¶¶¶¶¶¶¶¶¶¶______1
1________¶¶¶¶¶¶¶¶¶________1
1_________¶¶¶¶¶¶¶_________1
1__________¶¶¶¶¶__________1
1____________¶____________1
1_________________________1
1_________________________1
1_¶¶¶¶¶¶¶¶¶_____¶¶¶¶¶¶¶¶¶_1
1___¶¶¶¶¶_________¶¶¶¶¶___1
1___¶¶¶¶¶_________¶¶¶¶¶___1
1___¶¶¶¶¶_________¶¶¶¶¶___1
1___¶¶¶¶¶_________¶¶¶¶¶___1
1___¶¶¶¶¶_________¶¶¶¶¶___1
1___¶¶¶¶¶_________¶¶¶¶¶___1
1___¶¶¶¶¶_________¶¶¶¶¶___1
''')
		await sleep(0.4)

		await message.edit('''111111111111111111111111111
1_________________________1
1_________________________1
1_______¶¶¶¶¶¶¶¶¶¶________1
1_________¶¶¶¶¶¶__________1
1_________¶¶¶¶¶¶__________1
1_________¶¶¶¶¶¶__________1
1_________¶¶¶¶¶¶__________1
1_________¶¶¶¶¶¶__________1
1_________¶¶¶¶¶¶__________1
1_________¶¶¶¶¶¶__________1
1_________¶¶¶¶¶¶__________1
1_________¶¶¶¶¶¶__________1
1_______¶¶¶¶¶¶¶¶¶¶________1
1_________________________1
1_________________________1
1____¶¶¶¶¶_______¶¶¶¶¶____1
1__¶¶¶¶¶¶¶¶¶___¶¶¶¶¶¶¶¶¶__1
1_¶¶¶¶¶¶¶¶¶¶¶_¶¶¶¶¶¶¶¶¶¶¶_1
1_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_1
1__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__1
1____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶____1
1______¶¶¶¶¶¶¶¶¶¶¶¶¶______1
1________¶¶¶¶¶¶¶¶¶________1
1_________¶¶¶¶¶¶¶_________1
1__________¶¶¶¶¶__________1
1____________¶____________1
1_________________________1
1_________________________1
1_¶¶¶¶¶¶¶¶¶_____¶¶¶¶¶¶¶¶¶_1
1___¶¶¶¶¶_________¶¶¶¶¶___1
1___¶¶¶¶¶_________¶¶¶¶¶___1
1___¶¶¶¶¶_________¶¶¶¶¶___1
1___¶¶¶¶¶_________¶¶¶¶¶___1
1___¶¶¶¶¶_________¶¶¶¶¶___1
1___¶¶¶¶¶_________¶¶¶¶¶___1
1___¶¶¶¶¶_________¶¶¶¶¶___1 
1___¶¶¶¶¶_________¶¶¶¶¶___1
1___¶¶¶¶¶¶_______¶¶¶¶¶¶___1
1____¶¶¶¶¶¶_____¶¶¶¶¶¶____1
1______¶¶¶¶¶¶¶¶¶¶¶¶¶______1
1________¶¶¶¶¶¶¶¶¶________1
1_________________________1
111111111111111111111111111
''')
		await sleep(0.4)


	async def animguscmd(self,message):
		await message.edit('''. .╚⊙ ⊙╝..
╚═███═╝
.╚═███═╝
..╚═███═╝''')
		await sleep(0.4)

		await message.edit('''. .╚⊙ ⊙╝..
╚═███═╝
.╚═███═╝
..╚═███═╝
...╚═███═╝
...╚═███═╝
..╚═███═╝
.╚═███═╝''')
		await sleep(0.4)

		await message.edit('''. .╚⊙ ⊙╝..
╚═███═╝
.╚═███═╝
..╚═███═╝
...╚═███═╝
...╚═███═╝
..╚═███═╝
.╚═███═╝
╚═███═╝
╚═███═╝
.╚═███═╝
..╚═███═╝''')
		await sleep(0.4)

		await message.edit('''. .╚⊙ ⊙╝..
╚═███═╝
.╚═███═╝
..╚═███═╝
...╚═███═╝
...╚═███═╝
..╚═███═╝
.╚═███═╝
╚═███═╝
╚═███═╝
.╚═███═╝
..╚═███═╝
...╚═███═╝
...╚═███═╝
..╚═███═╝
.╚═███═╝''')
		await sleep(0.4)

		await message.edit('''. .╚⊙ ⊙╝..
╚═███═╝
.╚═███═╝
..╚═███═╝
...╚═███═╝
...╚═███═╝
..╚═███═╝
.╚═███═╝
╚═███═╝
╚═███═╝
.╚═███═╝
..╚═███═╝
...╚═███═╝
...╚═███═╝
..╚═███═╝
.╚═███═╝
..╚═███═╝
...╚═███═╝
.... ╚═█═╝''')
		await sleep(0.4)



	async def animkisscmd(self,message):
		await message.edit('''▄▀▀▄▄▀▀▀▄
█▌▐██▌▄██
█▌▐█▌▄███
█▌▐▌▄████
█▌░▐█████
█▌▐▌▀████
█▌▐█▌▀███
█▌▐██▌▀██
▀▄▄▀▀▄▄▄▀''')
		await sleep(1)

		await message.edit('''▄▀▀▄▄▀▀▀▄
█▌▐██▌▄██
█▌▐█▌▄███
█▌▐▌▄████
█▌░▐█████
█▌▐▌▀████
█▌▐█▌▀███
█▌▐██▌▀██
▀▄▄▀▀▄▄▄▀

▄▄▄▀▀▄▄▄▄▄
██████████
███▌▐█████
███▌▐█████
███▌▐█████
███▌▐█████
███▌▐█████
███▌▐█████
▀▀▀▄▄▀▀▀▀▀''')
		await sleep(1)

		await message.edit('''▄▀▀▄▄▀▀▀▄
█▌▐██▌▄██
█▌▐█▌▄███
█▌▐▌▄████
█▌░▐█████
█▌▐▌▀████
█▌▐█▌▀███
█▌▐██▌▀██
▀▄▄▀▀▄▄▄▀

▄▄▄▀▀▄▄▄▄▄
██████████
███▌▐█████
███▌▐█████
███▌▐█████
███▌▐█████
███▌▐█████
███▌▐█████
▀▀▀▄▄▀▀▀▀▀

▄▄▄▄▄▄▄▄▄▄
███▀▀▀▀███
██▌░▐▄▄▐██
██▌░▐█████
██▌░▀▀▀▐██
██▀▀█▌░▐██
██▌▐█▌░▐██
██▌▐▀▀░▐██
███▄▄▄▄███''')
		await sleep(1)

		await message.edit('''▄▀▀▄▄▀▀▀▄
█▌▐██▌▄██
█▌▐█▌▄███
█▌▐▌▄████
█▌░▐█████
█▌▐▌▀████
█▌▐█▌▀███
█▌▐██▌▀██
▀▄▄▀▀▄▄▄▀

▄▄▄▀▀▄▄▄▄▄
██████████
███▌▐█████
███▌▐█████
███▌▐█████
███▌▐█████
███▌▐█████
███▌▐█████
▀▀▀▄▄▀▀▀▀▀

▄▄▄▄▄▄▄▄▄▄
███▀▀▀▀███
██▌░▐▄▄▐██
██▌░▐█████
██▌░▀▀▀▐██
██▀▀█▌░▐██
██▌▐█▌░▐██
██▌▐▀▀░▐██
███▄▄▄▄███

▄▄▄▄▄▄▄▄▄▄
███▀▀▀▀███
██▌░▐▄▄▐██
██▌░▐█████
██▌░▀▀▀▐██
██▀▀█▌░▐██
██▌▐█▌░▐██
██▌▐▀▀░▐██
███▄▄▄▄███''')
		await sleep(1)
