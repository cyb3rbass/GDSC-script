from art import *
import os
from termcolor import colored


my_art = text2art("GDSC - script !")
print(colored(my_art, "blue"))

print(colored("*for GDSC students!*\n\n-----------by: -----------\n - Yehia Abdelghafar\n - Rokayah Badran", "green"))
print("--------------------------\n\n")


print(colored("   |------Select------|", "blue"))

print("--------------------------")
print(colored("1 - Information gathering \n2 - exit", "yellow"))
print("--------------------------")

Se = input(colored("Select [1~2]: ", "yellow"))
print("--------------------------")



os.system('clear')
if(Se == '1'):

    my_art = text2art("OSINT tools")
    print(colored(my_art, "yellow"))
    print("- for GDSC students!")
    print("--------------------------")


    
    print(colored("1 - Maltego tool \n2 - Sherlock tool\n3 - User-recon tool\n", "yellow"))
    tool = input(colored("Select[1~3]:", "yellow"))

    if(tool == '1'):
        print("Opening...")
        os.system('clear')
        os.system("open maltego.desktop")


    elif(tool == '2'):
        os.system('clear')
        
        print("Opening...")
        
        my_art = text2art("Sherlock")
        print(my_art)
        print("---------------------------------------------")
        user = input("Please enter the user of the victim: ")
        os.system("python sherlock/sherlock " + user)
        print("---------------------------------------------")


    elif(tool == '3'):
        os.system('clear')
        print("Opening...")
        
        os.system("bash userrecon/userrecon.sh")








elif(Se == '2'):
    exit()
