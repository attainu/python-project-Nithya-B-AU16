from colorama import Fore, Style
import os.path
import os

class cl_listofcommands:

        def fn_menu(self):
# list of commands 
                print(Fore.MAGENTA + "WELCOME TO BANGALORE CAR PARKING")
                print(Fore.MAGENTA + "Valid command listed below")
                print(Fore.MAGENTA + "========================")
                print(Fore.CYAN + "STATUS" + Style.RESET_ALL +"                               To get the status of parkinglot")    
                print(Fore.CYAN + "NEW_PARKING_LOT" + Style.RESET_ALL +Fore.LIGHTGREEN_EX +" <slot count>" + Style.RESET_ALL +"         To create new parking lot with spcific slots")
                print(Fore.CYAN + "PARKING" + Style.RESET_ALL +Fore.LIGHTGREEN_EX +" <reg number> <car colour>" + Style.RESET_ALL +"    To get availabe parking space")    
                print(Fore.CYAN + "LEAVE" + Style.RESET_ALL +Fore.LIGHTGREEN_EX +" <lot number> <slot number>" + Style.RESET_ALL +"     To leave parking")    
                print(Fore.CYAN + "GETDETAILSBYCOLOUR" + Style.RESET_ALL +Fore.LIGHTGREEN_EX +" <car colour>" + Style.RESET_ALL +"      To get car parking details by colour" )    
                print(Fore.CYAN + "GETDETAILSBYREGNUMBER" + Style.RESET_ALL +Fore.LIGHTGREEN_EX +" <reg number>" + Style.RESET_ALL +"   To get car parking details by reg number ") 
                print(Fore.CYAN + "GETAVAILABLITY" + Style.RESET_ALL +"                       To check avaiablity ")   
                print(Fore.CYAN + "EXIT" + Style.RESET_ALL +"                                 To exit programe")  
