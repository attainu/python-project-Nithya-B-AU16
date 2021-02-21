from colorama import Fore, Style
from db import cl_databaseconnect
connn=cl_databaseconnect()
conn=connn.fn_getconnection()

class cl_report:
# check status 
    def fn_status(self):
        
        cursor = conn.cursor()
        cursor.execute('select * from parking_lot where reg_number is not null')

        records = cursor.fetchall()
        print(Fore.YELLOW +"Lot No.".ljust(10,' ')+"Slot No.".ljust(10,' ')+ "Reg Num".ljust(20,' ') + "Colour".ljust(10,' '))
        print(Fore.YELLOW +"".ljust(9,'=')+" ".ljust(10,'=')+" ".ljust(20,'=')+" ".ljust(10,'=') + Style.RESET_ALL)
        for row in records:
            print(str(row[0]).ljust(10,' ')+str(row[1]).ljust(10,' ')+row[2].ljust(20,' ')+row[3].ljust(10,' ')+""+Style.RESET_ALL)
        
# check free space in parking lot     
    def fn_availablity(self):
        cursor = conn.cursor()
        cursor.execute('select lot_number,slot_number from parking_lot where reg_number is null')
        records = cursor.fetchall()
        
        if not records:
            print(Fore.RED + "No Parking space Available" +Style.RESET_ALL)
            
        for row in records:
            print(Fore.YELLOW +"Parking space Available at Lot number: " + str(row[0])+" Slot Number: "+str(row[1]) +Style.RESET_ALL)


# get details by colour

    def fn_getdetailsbycolor(self,carcolour):
        cursor = conn.cursor()
        cursor.execute("select lot_number,slot_number,reg_number,car_colour from parking_lot where car_colour='"+carcolour+"'")
        records = cursor.fetchall()

        if not records:
            print(Fore.RED + "No car parked with "+  carcolour +" colour" +Style.RESET_ALL)

        for row in records:
            parkinglotnum=row[0]
            parkingslotnum=row[1]
            regnum=row[2]
            print (Fore.YELLOW +"Lot number :"+ str(parkinglotnum) +" Slot Number : "+  str(parkingslotnum) +" Reg Number : "+  str(regnum) +"" +Style.RESET_ALL)
        return True

# get details by reg number
    def fn_getdetailsbyregnumber(self,regnumber):
        cursor = conn.cursor()
        cursor.execute("select lot_number,slot_number,reg_number,car_colour from parking_lot where reg_number='"+regnumber+"'")
        records = cursor.fetchall()

        if not records:
            print(Fore.RED + regnumber + " Reg number not found " +Style.RESET_ALL)

        for row in records:
            parkinglotnum=row[0]
            parkingslotnum=row[1]
            print (Fore.YELLOW +"Lot number :"+ str(parkinglotnum) +" Slot Number : "+  str(parkingslotnum) +"" +Style.RESET_ALL)
        return True 