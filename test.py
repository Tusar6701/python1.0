# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 11:13:35 2020
for IIEC Rise Python
@author: TUSHAR
"""
import pyttsx3 as py
import os
py.speak("Welcome to python OS")
py.speak("Do you wish to chat with me or choose from a menu? Or worse, EXIT???")
def choiceMenu():
    print("Do you want to (1)chat, (2)choose or (3)exit?")
    
    ch = input()
    if ch == "chat" or ch == '1':
        py.speak('How can I help u?')
        print("How can I help u?")
        
        p=funcChat()
        print(p)
        check(p)
        return 0
    elif ch == "choose" or ch == '2':
        p=funcMenu()
        
        check(p)
        return 0
    elif ch == "exit" or ch == "quit" or '3':
        py.speak("Ok, seeya!!!")
        print("Exitting the program!!!")
        return 1
    else:
        print("Wrong choice, please try again")
        choiceMenu()
        return 0
 
def contEx():
    print("Do you wish to (1)continue or (2)exit?")
    c=input()
    if c=='1' or c == 'continue':
        choiceMenu()
        return 0
    elif c=='2' or c == 'exit' or c == 'quit':
        py.speak("Ok, seeya!!!")
        print("Exitting the program!!!")
        
        return 1
    
def funcChat():
    
    
def funcMenu():
    
    #menu can be created
    print("\n")
    
    print("**********************************************")
    print("*                 MENU!!!                    *")
    print("**********************************************")
    print("*   1   *       GOOGLE CHROME                *")
    print("*   2   *       NOTEPAD++                    *")
    print("*   3   *       NOTEPAD                      *")
    print("*   4   *       WINDOWS MEDIA PLAYER         *")
    print("*   5   *       WHATSAPP DESKTOP             *")
    print("*   6   *       SPOTIFY                      *")
    print("*   7   *       VLC MEDIA PLAYER             *")
    print("*   8   *       COMMAND PROMPT AS ADMIN      *")
    print("*   9   *       FILE EXPLORER                *")
    print("*   10  *       SETTINGS                     *")
    print("*   11  *       START MENU                   *")
    print("*   12  *       RESTART                      *")
    print("**********************************************")
 
    print("\n")
    s = input("Enter your choice : ")
    return s

def check(p):
    if p == '1' : 
        py.speak('Opening google chrome')
        os.system("start chrome")
    elif p == '2' : 
        py.speak('opening notepad++')
        os.system("notepad++")
    elif p == '3' :
        py.speak('opening notepad')
        os.system("notepad")
    elif p == '4' : 
        py.speak('opening windows media player')
        os.system("wmplayer")
    elif p == '5' :
        py.speak('opening whatsapp for desktop')
        os.system("start whatsapp:")
    elif p == '6' : 
        py.speak('opening spotify')
        os.system("start spotify:")
    elif p == '7' :
        py.speak('opening vlc media player')
        os.system("vlc")
        
    elif p == '8' : 
        py.speak('opening command prompt as an administrator')
        os.system("start")
    elif p == '9' :
        py.speak('opening windows file explorer')
        os.system("explorer")
    elif p == '10' : 
        py.speak('opening Settings')
        os.system("start ms-settings:")
    elif p == '11' : 
        py.speak('opening start menu')
        os.system("C:/Users/KIIT/AppData/Roaming/Rainmeter/Addons/Tray/Start.exe")
    elif p == '12' : 
        choiceMenu()            
    else:
        py.speak('Oops!!! I am afraid, I dont support this feature yet')
        print("Not supported!!!")

i=choiceMenu()
while(i==0):
    #i=choiceMenu() 
    i=contEx()
    
