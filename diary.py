#!/usr/bin/python3

from os import system
from os.path import exists
from datetime import datetime
from sys import exit
from platform import system as op_sys
#from cryptography.fernet import Fernet

#key=b'QP0F9hkybntvrxd5GWWwniUHvBeMydSQ5Lyy_cmfAHE='

#software - root folders
#files,diary,info,pass,log - child folders
#system('color b')

def clear():
    if op_sys() != 'Linux':
	system('cls')
    else:
	system('clear')

def linux_setup():
    system('mkdir .software/files')
    system('mkdir .software/diary')
    system('mkdir .software/info')
    system('mkdir .software/pass')
    system('mkdir .software/log')
    print('[+] Setup done [+]')
    input('press enter to continue')
    login()


def win_setup():#completed, working
    system('mkdir software/files')
    system('mkdir software/diary')
    system('mkdir software/info')
    system('mkdir software/pass')
    system('mkdir software/log')
    system('attrib +h software')
    print('[+] Setup done [+]')
    input('press enter to continue')
    login()

#def login():#completed, working
    clear()
    print()
    print('[+] Login [+]')
    if exists('.software/log/a'):
        if input()==open('.software/log/a','r').read():
            main()
        else:
            print('[!] Invalid password [!]')
            input('press enter to continue')
            login()
    else:
        print()
        open('.software/log/a','w').write(input('[+] Create a password to procede [+]'))
        print('[+] Password created [+]')
        input('press enter to continue')
        login()

def main():#help option remaining
    print('''

    [1] Write Diary
    [2] Read Diary
    [3] Add/view files
    [4] Record people information
    [5] Save/view Passwords
    [6] Search Diary for a keyword
    [7] Change diary password
    [8] Help #option unavailable
    [9] Exit

    ''')

    task=input('[+] Enter option ')
    if task=='1':
        write_diary()
    elif task=='2':
        read_diary()
    elif task=='3':
        add_files()
    elif task=='4':
        ppl_info()
    elif task=='5':
        passwords()
    elif task=='6':
        search()
    elif task=='7':
        print()
        open('.software/log/a','w').write(input('[+] Enter new password [+] '))
        print('[+] Password updated [+]')
        input('press enter to continue')
        main()
    #elif task=='8':
        #program_help()
    elif task=='9':
        exit()
    else:
        print('[!] Invalid option [!]')
        input('press enter to continue')
        main()

def write_diary():#completed,working
    clear()
    print()
    print('[+] Start writing from here')
    print('[+] Date and time will be added automatically')
    #print('[+] To add inline attachments, type <file path>. Exapmle- The attachment can be found here, <C:\file.txt>')
    print('[+] To clear the screen, type "!c" on a new line')
    print('[+] To stop writing, type "!e" on a new line')
    print()

    lst=[]
    date_today=str(datetime.today())[:10]
    time_at_the_start_of_writing=str(datetime.today())[11:19]

    while True:
        data=input()
        if data=='!e':
            print()
            print('[+] File ended')
            lst.append('\n')
            lst.insert(0,time_at_the_start_of_writing+'\n')
            open('.software/diary/'+date_today,'a').writelines(lst)
            
            print('[+] Data added successfully')
            input('press enter to continue')
            main()
            break
        
        elif data=='!c':
            clear()

        elif data=='':
            lst.append('\n')
        
        else:
            lst.append(data)

def add_files():#completed,working
    clear()
    print()
    task=input('[+] Add files or view files? [+] (add/view/delete) ')
    
    if task=='add':
        loca=input('[+] Enter the location of the file [+] ')
        
        if exists(loca):
            command=''.join(['cp ',loca,' software/files/'])
            system(command)
            print('[+] Files added successfully')
            input('press enter to continue')
            main()
        else:
            print('[!] File not found [!]')
            input('press enter to continue')
            main()

    elif task=='view':
        while True:
            search=input('[+] Enter the name of the file, or type "list" to see all files, !e to exit [+] ')
            if search=='list':
                system('ls .software/files')
                input('press enter to continue')
            elif search=='!e':
                main()
            elif search!='list':
                if exists('.software/files/'+search):
                    system('firefox --private-window .software/files/'+search)
                    input('press enter to continue')
                    main()
                else:
                    print('[!] File not found [!]')

    elif task=='delete':
        a=input('[+] Enter the file name to delete [+] ')
        if exists('.software/files/'+a):
            system('rm software/files/'+a)
            print('[+] File deleted successfully [+]')
            input('press enter to continue')
            main()
        else:
            print('[+] File not found [+]')
            input('press enter to continue')
            main()
    else:
        print('[!] Invalid option [!]')
        input('press enter to continue')
        add_files()

def ppl_info():#completed,working

    clear()
    print()
    task=input('[+] Add/modify/delete/view [+] (a/m/d/v)')

    if task=='a':
        name=input('[+] Enter name [+] ')
        DOB=input('[+] Enter date of birth [+] ')
        IG=input('[+] User on instagram? If yes enter ID, else leave blank [+]')
        FB=input('[+] User on facebook? If yes enter ID, else leave blank [+]')
        PN=input('[+] User on pinterest? If yes enter ID, else leave blank [+]')
        LN=input('[+] User on linkedin? If yes enter ID, else leave blank [+]')
        SC=input('[+] User on snapchat? If yes enter ID, else leave blank [+]')
        M=input('[+] User on Mail? If yes enter ID, else leave blank [+]')
        PHN=input('[+] Enter the phone number, else leave blank [+]')
        IP=input('[+] Enter the IP address, else leave blank [+]')
        note=input('[+] Extra details, else leave blank [+]')
        
        lst=['NAME: '+name,'DATE OF BIRTH: '+DOB,'INSTAGRAM: '+IG,'FACEBOOK: '+FB,'PINTEREST: '+PN,'LINKEDIN: '+LN,'SNAPCHAT: '+SC,'MAIL: '+M,'PHONE NUMBER: '+PHN,'IP ADDRESS: '+IP,'NOTES: '+note]
        a=open('.software/info/'+name,'w')
        for i in lst:
            a.write(i+'\n')
        a.close()

        print('[+] Data added successfully [+]')
        input('press enter to continue')
        main()

    elif task=='m':
        name=input('[+] Enter the name to edit [+] ')

        if exists('.software/info/'+name):
            DOB=input('[+] Edit date of birth leave blank to leave it unmodified [+] ')
            IG=input('[+] Edit instagram? leave blank to leave it unmodified [+]')
            FB=input('[+] Edit facebook? leave blank to leave it unmodified [+]')
            PN=input('[+] Edit pinterest? leave blank to leave it unmodified [+]')
            LN=input('[+] Edit linkedin? If yes enter ID, else leave blank [+]')
            SC=input('[+] Edit snapchat? If yes enter ID, else leave blank [+]')
            M=input('[+] Edit Mail? If yes enter ID, else leave blank [+]')
            PHN=input('[+] Edit phone number leave blank to leave it unmodified [+]')
            IP=input('[+] Edit IP address, else leave blank to leave it unmodified [+]')
            note=input('[+] Extra details, else leave blank to leave it unmodified [+]')

            lst=['NAME: '+name,'DATE OF BIRTH: '+DOB,'INSTAGRAM: '+IG,'FACEBOOK: '+FB,'PINTEREST: '+PN,'LINKEDIN: '+LN,'SNAPCHAT: '+SC,'MAIL: '+M,'PHONE NUMBER: '+PHN,'IP ADDRESS: '+IP,'NOTES: '+note]
            
            b=open('.software/info/'+name,'r').readlines()
            
            for i in lst:
                if i!='':
                    num=lst.index(i)
                    b.pop(num)
                    b.insert(num,i)
            
            a=open('.software/info/'+name,'w')
            for i in b:
                a.write(i+'\n')
            a.close()

            print('[+] Information edited successfully')
            input('press enter to continue')
            main()

        else:
            print('[!] Name not found [!]')
            input('press enter to continue')
            main()

    elif task=='d':
        name=input('[+] Enter the name to delete [+] ')
        if exists('software/info/'+name):
            system('rm ".software/info/'+name+'"')
            print('[+] Deleted successfully [+]')
            input('press enter to continue')
            main()
        else:
            print('[!] Not found [!]')
            input('press enter to continue')
            main()
    
    elif task=='v':
        while True:
            name=input('[+] Enter the name to view stored information,type "all" to see all [+] ')
            if name=='all':
                system('ls .software/info/')
                input('press enter to continue')
            else:
                if exists('.software/info/'+name):
                    for i in open('.software/info/'+name).readlines():
                        print(i)
                    input('press enter to continue')
                    main()
                else:
                    print('[!] Name does not exist [!]')
                    input('press enter to continue')
                    main()

def passwords():#completed,working

    clear()
    print()
    print('''
    [1] Enter passwords
    [2] View passwords
    [3] Delete passwords
    
    ''')
    task=input('[+] ')

    if task=='1':
        username=input('[+] Enter username [+] ')
        password=input('[+] Enter password [+] ')
        name=input('[+] Name of the credentials [+]')
        open('.software/pass/'+name,'w').writelines(['USERNAME:'+username,'\nPASSWORD: '+password])
        print('[+] Credentials added successfully [+]')
        input('press enter to continue')
        main()
    
    if task=='2':
        while True:
            name=input('[+] Enter the name of the credentials, type "all" to see all names [+] ')
        
            if name=="all":
                system('ls .software/pass/')
                input('press enter to continue')
            elif exists('software/pass/'+name):
                for i in open('.software/pass/'+name).readlines():
                    print(i)
                input('press enter to continue')
                main()
            else:
                print('[!] Name does not exist [!]')
                input('press enter to continue')
                main()
    
    if task=='3':
        name=input('[+] Enter the credential name to delete [+] ')
        if exists('.software/pass/'+name):
            system('rm .software/pass/'+name)
            print('[+] Credential deleted successfully [+]]')
            input('press enter to continue')
            main()
        else:
            print('[!] Credential name not found [!]')
            input('press enter to continue')
            main()

def search():#completed,working

    clear()
    print()
    search=input('[+] Enter the keyword to search [+] ')
    system('ls .software/diary>a')
    found=[]

    print('[+] Searching for '+search+'...')
    print('[+] This might take some time [+]')
    print()

    for i in open('a').read().split('\n'):
        if i!='':
            if search.lower() in open('.software/diary/'+i).read().lower():
                found.append(i)
        else:
            break
    system('rm a')
    print('[+] The word "'+search+'" was used on the dates shown below [+]')
    if len(found)!=0:
        for i in found:
                print(i)
    else:
        print('[!] Word not found [!]')
        input('press enter to continue')
        main()
    
    while True:
        print('''
[1] Read one of them
[2] Read all, export data to text file
[3] Exit
        ''')
        a=input('[+] ')

        if a=='1':
            inp=input('[+] Enter the date [+] ')
            if inp in found:
                for i in open('.software/diary/'+inp).readlines():
                    print(i)
                a=input('[+] Export data to text file? [+] (y/n) ')
                if a=='y':
                    system('cp .software/diary/'+inp+' '+input('[+] Enter location to export the file [+] '+'.txt'))
                    print('[+] File exported [+]')
                    input('press enter to continue')
                    main()
                elif a=='n':
                    pass
                else:
                    print('[+] Invalid, defaulting to option no [+]')
                    input('press enter to continue')
                    main()
            else:
                print('[+] Please enter the date from the list [+]')
                input('press enter to continue')

        elif a=='2':
            print('[+] Exporting data to tar zip file...')
            for i in found:
                system('if not exist /tmp/diary/ mkdir /tmp/diary/')
                system('cp .software/diary/'+i+' /tmp/diary/'+i+'.txt')
            system('tar -cf diary_search_results.tar /tmp/diary')
            system('mv diary_search_results.tar '+input('[+] Enter the location to export the file [+] '))
            system('rmdir /tmp/diary /s /q')
            print('[+] File copied to specified directory [+]')
            input('press enter to continue')
            main()

        elif a=='3':
            main()

        else:
            print('[!] Invalid Option [!]')
            input('press enter to continue')

def read_diary():#completed,working
    clear()
    print()
    print('''
    [1] Read diary of specific date
    [2] Read complete diary, export diary to tar file
    [3] Exit
    ''')

    a=input('[+] ')
    if a=='1':
        a=input('[+] Enter the date, ex-2022-01-24 [+]')
        if exists('.software/diary/'+a):
            for i in open('.software/diary/'+a).readlines():
                print(i)
            if input('[+] Export diary to text file? [+] (y/n) ')=='y':
                system('cp software/diary/'+a+' '+input('[+] Enter the complete location to export file with / [+]')+a+'.txt')
                print('[+] File exported successfully [+]')
                input('press enter to continue')
                main()
            else:
                main()
        else:
            print('[+] Doesnt exist, maybe diary wasnt written on '+a)
            input('press enter to continue')
            main()
    elif a=='2':
             system('tar -cf diary.tar .software/diary')
             system('mv diary.tar '+input('[+] Enter the location to export file [+]'))
             print('[+] Diary exported successfully [+]')
             input('press enter to continue')
             main()
    elif a=='3':
        main()
    else:
        print('[!] Invalid option [!]')
        input('press enter to continue')
        read_diary()

if exists('.software'):
    main()
else:
    setup()
