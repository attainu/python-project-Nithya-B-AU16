import sys
import colorama
from colorama import Fore, Style
import os.path
from os import path
from os import system
from manageparkinglot import cl_manageparkinglot  
from display_commands import cl_listofcommands
from parking import cl_parking
from report import cl_report
command=' '

def fn_process(command_params):
    command_with_params = command_params.strip().split(' ')
    command= command_with_params[0].lower()     
    #print (command.upper())
# check status 
    if command   == 'status' :
        print (command.upper())      
        r=cl_report()  
        r.fn_status()

# exit from intractive command mode    
    elif command =='exit':
        print(Fore.GREEN + "Thank you")
        exit()
# new lot creation 
    elif command =='new_parking_lot':
        if len(command_with_params)<2:
            print (Fore.RED + 'Please provide capacity of the new paring lot')
        else:
            print (command.upper() +" "+ command_with_params[1]) 
            m=cl_manageparkinglot()
            _=m.fn_createparkinglot(command_with_params[1])
# to parking
    elif command =='parking':
        
        if len(command_with_params)<3:
            print (Fore.RED + 'Please provide command with Reg Number and Car Colour')
        else:
            print (command.upper() +" "+ command_with_params[1].upper()+ " " +command_with_params[2].upper())
            park=cl_parking()    
            _=park.fn_createparking(command_with_params[1].upper(),command_with_params[2].upper())
# leave from parking 

    elif command =='leave':

        if len(command_with_params)<3:
            print (Fore.RED + 'Please provide parking lot number and slot number')
        else:
            print (command.upper() +" "+ command_with_params[1]+ " " +command_with_params[2])
            park=cl_parking()
            _=park.fn_leaveparking(command_with_params[1],command_with_params[2])
# get parking details by colour 
    elif command =='getdetailsbycolour':

        if len(command_with_params)<2:
            print (Fore.RED + 'Please provide command with colour of the car')
        else:
            print (command.upper() +" "+ command_with_params[1].upper()) 
            r=cl_report()
            _=r.fn_getdetailsbycolor(command_with_params[1].upper())        
    
# get parking details by reg number
    elif command =='getdetailsbyregnumber':
        if len(command_with_params)<2:
            print (Fore.RED + 'Please provide command with Reg Number of the car')
        else:
            print (command.upper() +" "+ command_with_params[1].upper()) 
            r=cl_report()
            _=r.fn_getdetailsbyregnumber(command_with_params[1].upper())  

# get parking avaiablity on entire parking area
    elif command =='getavailablity':
        print (command.upper())
        r=cl_report()
        r.fn_availablity()  

    else: 
        if len(command)>1:
            print(Fore.RED + "Invalid command")
        l=cl_listofcommands()
        l.fn_menu()

if len(sys.argv) == 1:
    _ = system('cls') 
    fn_process(' ')
    while True:
        Cline = input()
        _ = system('cls') 
# read input file        
        if os.path.isfile(Cline):
           file1 = open(Cline).read().splitlines()
          # Lines = file1.readlines()
           for Fline in file1:
               #print(Fline)
               fn_process(Fline)
        else:
           fn_process(Cline)

if __name__==__main__:
    fn_process(' ')