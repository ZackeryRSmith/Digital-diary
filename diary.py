#!/usr/bin/python3

from os import system
from os.path import exists
from os import name as op_sys
from datetime import datetime
from sys import exit

def clear():
    if op_sys == 'nt': system('cls')
    else: system('clear')

def linux_setup():
    system('mkdir .software/files .software/diary .software/info .software/pass .software/log')
    input('[+] Setup done [+]\npress enter to continue...')
    login()


def win_setup():
    system('mkdir software/files software/diary software/info software/pass software/log')
    system('attrib +h software')
    input('[+] Setup done [+]\npress enter to continue...'); login()

def login():
    clear()
    print('\n[+] Login [+]')
    if exists('.software/log/a'):
        if input()==open('.software/log/a','r').read(): main()
        else: input('[!] Invalid password [!]\npress enter to continue...'); login()
    else:
        open('.software/log/a','w').write(input('\n[+] Create a password to proceed [+]'))
        input('[+] Password created [+]\npress enter to continue..'); login()

def main():
    # TODO: Add help option
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
    if   task=='1' : write_diary()
    elif task=='2' : read_diary()
    elif task=='3' : add_files()
    elif task=='4' : ppl_info()
    elif task=='5' : passwords()
    elif task=='6' : search()
    elif task=='7' : 
        open('.software/log/a','w').write(input('\n[+] Enter new password [+] '))
        input('[+] Password updated [+]\npress enter to continue'); main()
    #elif task=='8': program_help()
    elif task=='9' : exit()
    else: input('[!] Invalid option [!]\npress enter to continue'); main()

def write_diary():#completed,working
    clear()
    print( '''
[+] Start writing from here
[+] Date and time will be added automatically
print('[+] To clear the screen, type "!c" on a new line')
print('[+] To stop writing, type "!e" on a new line')
           ''')

    lst=[]
    date_today=str(datetime.today())[:10]
    time_at_the_start_of_writing=str(datetime.today())[11:19]  # Bad variable naming.

    while True:
        data=input()
        if data=='!e':
            print('\n[+] File ended [+]')
            lst.append('\n')
            lst.insert(0,time_at_the_start_of_writing+'\n')
            open('.software/diary/'+date_today,'a').writelines(lst)
            
            input('[+] Data added successfully [+]\npress enter to continue..')
            main(); break
        
        elif data=='!c': clear()
        elif data=='': lst.append('\n')
        else: lst.append(data)

def add_files():
    clear()
    task=input('\n[+] Add files or view files? [+] (add/view/delete) ')
    
    if task=='add':
        path=input('[+] Enter the path to the file [+] ')
        
        if exists(path):
            command=''.join(['cp ',path,' software/files/'])
            system(f'cp {command}software/files/')
            input('[+] Files added successfully [+]\npress enter to continue...')
            main()
        else:
            input('[!] File not found [!]\npress enter to continue...')
            main()

    elif task=='view':
        while True:
            search=input('[+] Enter the name of the file, or type "list" to see all files, !e to exit [+] ')
            if search=='list':
                system('ls .software/files')
                input('press enter to continue...')
            elif search=='!e': main()
            elif search!='list':
                if exists('.software/files/'+search):
                    system('firefox --private-window .software/files/'+search)
                    input('press enter to continue...')
                    main()
                else: print('[!] File not found [!]')

    elif task=='delete':
        a=input('[+] Enter the file name to delete [+] ')
        if exists('.software/files/'+a):
            system('rm software/files/'+a)
            input('[+] File deleted successfully [+]\npress enter to continue...')
            main()
        else:
            input('[+] File not found [+]\npress enter to continue...')
            main()
    else:
        input('[!] Invalid option [!]\npress enter to continue...')
        add_files()

def ppl_info():
    clear()
    task=input('\n[+] Add/modify/delete/view [+] (a/m/d/v)')

    if task=='a':
        name = input('[+] Enter name [+] ')
        DOB  = input('[+] Enter date of birth [+] ')
        IG   = input('[+] User on instagram? If yes enter ID, else leave blank [+]')
        FB   = input('[+] User on facebook? If yes enter ID, else leave blank [+]')
        PN   = input('[+] User on pinterest? If yes enter ID, else leave blank [+]')
        LN   = input('[+] User on linkedin? If yes enter ID, else leave blank [+]')
        SC   = input('[+] User on snapchat? If yes enter ID, else leave blank [+]')
        M    = input('[+] User on Mail? If yes enter ID, else leave blank [+]')
        PHN  = input('[+] Enter the phone number, else leave blank [+]')
        IP   = input('[+] Enter the IP address, else leave blank [+]')
        note = input('[+] Extra details, else leave blank [+]')
        
        lst=[
            'NAME: '          + name ,
            'DATE OF BIRTH: ' + DOB  ,
            'INSTAGRAM: '     + IG   ,
            'FACEBOOK: '      + FB   ,
            'PINTEREST: '     + PN   ,
            'LINKEDIN: '      + LN   ,
            'SNAPCHAT: '      + SC   ,
            'MAIL: '          + M    ,
            'PHONE NUMBER: '  + PHN  ,
            'IP ADDRESS: '    + IP   ,
            'NOTES: '         + note
        ]
        with open('.software/info/'+name,'w') as f:
            for i in lst: f.write(i+'\n')

        input('[+] Data added successfully [+]\npress enter to continue...')
        main()

    elif task=='m':
        name=input('[+] Enter the name to edit [+] ')

        if exists('.software/info/'+name):
            DOB  = input('[+] Edit date of birth leave blank to leave it unmodified [+] ')
            IG   = input('[+] Edit instagram? leave blank to leave it unmodified [+]')
            FB   = input('[+] Edit facebook? leave blank to leave it unmodified [+]')
            PN   = input('[+] Edit pinterest? leave blank to leave it unmodified [+]')
            LN   = input('[+] Edit linkedin? If yes enter ID, else leave blank [+]')
            SC   = input('[+] Edit snapchat? If yes enter ID, else leave blank [+]')
            M    = input('[+] Edit Mail? If yes enter ID, else leave blank [+]')
            PHN  = input('[+] Edit phone number leave blank to leave it unmodified [+]')
            IP   = input('[+] Edit IP address, else leave blank to leave it unmodified [+]')
            note = input('[+] Extra details, else leave blank to leave it unmodified [+]')

            lst=[
                'NAME: '          + name ,
                'DATE OF BIRTH: ' + DOB  ,
                'INSTAGRAM: '     + IG   ,
                'FACEBOOK: '      + FB   ,
                'PINTEREST: '     + PN   ,
                'LINKEDIN: '      + LN   ,
                'SNAPCHAT: '      + SC   ,
                'MAIL: '          + M    ,
                'PHONE NUMBER: '  + PHN  ,
                'IP ADDRESS: '    + IP   ,
                'NOTES: '         + note
            ]
            
            b=open('.software/info/'+name,'r').readlines()
            
            for i in lst:
                if i!='':
                    num=lst.index(i)
                    b.pop(num)
                    b.insert(num,i)
            
            with open('.software/info/'+name,'w') as f:
                for i in b: f.write(i+'\n')

            input('[+] Information edited successfully [+]\npress enter to continue...')
            main()

        else:
            input('[!] Name not found [!]\npress enter to continue...')
            main()

    elif task=='d':
        name=input('[+] Enter the name to delete [+] ')
        if exists('software/info/'+name):
            system('rm ".software/info/'+name+'"')
            input('[+] Deleted successfully [+]\npress enter to continue...')
            main()
        else:
            input('[!] Not found [!]\npress enter to continue...')
            main()
    
    elif task=='v':
        while True:
            name=input('[+] Enter the name to view stored information,type "all" to see all [+] ')
            if name=='all':
                system('ls .software/info/')
                input('press enter to continue')
            else:
                if exists('.software/info/'+name):
                    for i in open('.software/info/'+name).readlines(): print(i)
                    input('press enter to continue')
                    main()
                else:
                    input('[!] Name does not exist [!]\npress enter to continue...')
                    main()

def passwords():
    clear()
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
        input('[+] Credentials added successfully [+]\npress enter to continue...')
        main()
    
    if task=='2':
        while True:
            name=input('[+] Enter the name of the credentials, type "all" to see all names [+] ')
        
            if name=="all":
                system('ls .software/pass/')
                input('press enter to continue')
            elif exists('software/pass/'+name):
                for i in open('.software/pass/'+name).readlines(): print(i)
                input('press enter to continue')
                main()
            else:
                input('[!] Name does not exsit [!]\npress enter to continue...')
                main()
    
    if task=='3':
        name=input('[+] Enter the credential name to delete [+] ')
        if exists('.software/pass/'+name):
            system('rm .software/pass/'+name)
            input('[+] Credential deleted successfully [+]\npress enter to continue...')
            main()
        else:
            input('[!] Credential name not found [!]\npress enter to continue...')
            main()

def search():
    clear()
    search=input('[+] Enter the keyword to search [+] ')
    system('ls .software/diary>a')
    found=[]

    print(f'[+] Searching for {search}...\n[+] This might take some time [+]')

    for i in open('a').read().split('\n'):
        if i!='' and search.lower() in open('.software/diary/'+i).read().lower(): found.append(i)
        else: break
    system('rm a')
    print('[+] The word "'+search+'" was used on the dates shown below [+]')
    if len(found)!=0:
        for i in found: print(i)
    else:
        input('[!] Word not found [!]\npress enter to continue...')
        main()
    
    while True:
        print('''
[1] Read one of them
[2] Read all, export data to text file
[3] Exit
        ''')
        if a := input('[+] ')=='1':
            inp=input('[+] Enter the date [+] ')
            if inp in found:
                for i in open('.software/diary/'+inp).readlines(): print(i)
                a=input('[+] Export data to text file? [+] (y/n) ')
                if a=='y':
                    system('cp .software/diary/'+inp+' '+input('[+] Enter location to export the file [+] '+'.txt'))
                    input('[+] File exported [+]\npress enter to continue...')
                    main()
                elif a=='n':
                    pass
                else:
                    input('[+] Invalid, defaulting to option no [+]\npress enter to continue...')
                    main()
            else:
                input('[+] Please enter the date from the list [+]\npress enter to continue...')

        elif a=='2':
            print('[+] Exporting data to tar zip file...')
            for i in found:
                system('if not exist /tmp/diary/ mkdir /tmp/diary/')
                system('cp .software/diary/'+i+' /tmp/diary/'+i+'.txt')
            system('tar -cf diary_search_results.tar /tmp/diary')
            system('mv diary_search_results.tar '+input('[+] Enter the location to export the file [+] '))
            system('rmdir /tmp/diary /s /q')
            input('[+] File copied to specified directory [+]\npress enter to continue...')
            main()

        elif a=='3':
            main()

        else:
            input('[!] Invalid Option [!]\npress enter to continue...')

def read_diary():
    clear()
    print('''
[1] Read diary of specific date
[2] Read complete diary, export diary to tar file
[3] Exit
          ''')

    if a:= input('[+] ') =='1':
        a=input('[+] Enter the date, ex-2022-01-24 [+]')
        if exists('.software/diary/'+a):
            for i in open('.software/diary/'+a).readlines(): print(i)
            if input('[+] Export diary to text file? [+] (y/n) ').lower()=='y':
                system('cp software/diary/'+a+' '+input('[+] Enter the complete location to export file with / [+]')+a+'.txt')
                input('[+] File exported successfully [+]\npress enter to continue...')
                main()
            else: main()
        else:
            input(f'[+] Doesnt exist, maybe diary wasnt written on {a}\npress enter to continue...')
            main()
    elif a=='2':
             system('tar -cf diary.tar .software/diary')
             system('mv diary.tar '+input('[+] Enter the location to export file [+]'))
             input('[+] Diary exported successfully [+]\npress enter to continue...')
             main()
    elif a=='3':main()
    else:
        input('[!] Invalid option [!]\npress enter to continue...')
        read_diary()

if exists('.software'):
    main()
else:
    if op_sys != "Linux":
        win_setup()
    else:
        linux_setup()
