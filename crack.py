#!/usr/bin/python
import r2pipe


while(1):
    print("Hello, it's a crack from Ivanov A. O. and Khachatryan S. A.\n \nSelect what you want to do: \n")
    print("1) Crack cp\n")
    print("2) Crack tp\n")
    print("3) Crack game\n")
    print("4) Exit\n")

    c = int(input())

    if(c == 1):
        try:
            r1 = r2pipe.open('cp')
        except Exception:
            print("Can't find cp file! Please make sure, that cp file is in one folder with crack! \n")
        else:
            r1.cmd('oo+')  
            r1.cmd('s 0x00400b39')
            r1.cmd('wa jmp 0x400b45')
            r1.cmd('s 0x00400f99')
            r1.cmd('wa jmp 0x00401094')
            r1.cmd('s 0x00401094')
            r1.cmd('wa mov eax, 2')
            print('File cp is successfully cracked!\n')

    elif(c == 2):
        try:
            r2 = r2pipe.open('tp')
        except Exception:
            print("Can't find tp file! Please make sure, that tp file is in one folder with crack!\n")
        else:
            r2.cmd('oo+')
            r2.cmd('s 0x00400e21')
            r2.cmd('wa jmp 0x400e2d')
            r2.cmd('s 0x004013f2')
            r2.cmd('wa jmp 0x004013f4')
            r2.cmd('s 0x004013f4')
            r2.cmd('wa mov eax, 2')
            print('File tp is successfully cracked!\n')
    elif(c == 3):
        try:
            r3 = r2pipe.open('game')
        except Exception:
            print("Can't find game file! Please make sure, that game file is in one folder with crack!\n")
        else:
            r3.cmd('oo+')
            r3.cmd('s 0x00401cfe')
            r3.cmd('wa jmp 0x401d07')
            print('File game is successfully cracked!')
    elif(c == 4):
        break
    else:
        print('Wrong input! Please write number from 1 to 4!')


    
