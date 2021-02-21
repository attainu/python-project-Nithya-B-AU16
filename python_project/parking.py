from colorama import Fore, Style
from db import cl_databaseconnect
connn=cl_databaseconnect()
conn=connn.fn_getconnection()
    
class cl_parking:
    # parking 
    
    def fn_createparking(self,reg_number,colour):
        
        cursor = conn.cursor()
        parkinglotnum=0
# check the reg number alrady exist in ther parking lot
        cursor.execute("select count(*) from parking_lot where reg_number='"+reg_number+"'")
        records = cursor.fetchall()
        for row in records:
            regnumstat=row[0]
        
        if regnumstat>0:
            print(Fore.RED +"Reg number already parked, Please check the number" +Style.RESET_ALL)
            return False
        
        cursor = conn.cursor()
        parkinglotnum=0
        cursor.execute('select min(lot_number),min(slot_number) from parking_lot where reg_number is null and lot_number=(select min(lot_number) from  parking_lot where  reg_number is null )')
        
        records = cursor.fetchall()
        parkinglotnum=''
        parkingslotnum=''
        for row in records:
            parkinglotnum=row[0]
            parkingslotnum=row[1]

        if parkingslotnum =='' or parkingslotnum is None:
            print (Fore.RED +"No Parking lots are available" +Style.RESET_ALL)
            return False
        else:    
            cursor = conn.cursor()
            cursor.execute("update parking_lot set reg_number='" + reg_number +"',car_colour='" + colour +"' where lot_number=" + str(parkinglotnum)+ " and slot_number="+str(parkingslotnum))
            conn.commit()
            print (Fore.YELLOW +"Parking space allocated at Lot number :"+ str(parkinglotnum) +" Slot Number : "+  str(parkingslotnum) +""+Style.RESET_ALL )
        return True

# Leave 

    def fn_leaveparking(self,parkinglotnum,parkingslotnum):
        
        cursor = conn.cursor()
        cursor.execute('select reg_number from parking_lot where lot_number='+ str(parkinglotnum) + ' and slot_number='+ str(parkingslotnum))
        
        records = cursor.fetchall()
        chkreg=''
        for row in records:
            chkreg=row[0]

        if chkreg =='' or chkreg is None:
            print (Fore.RED +"Parking space is already Free" + Style.RESET_ALL)
            return False

        cursor = conn.cursor()
        cursor.execute("update parking_lot set reg_number=null,car_colour=null  where lot_number=" + str(parkinglotnum)+ " and slot_number="+str(parkingslotnum))
        conn.commit()
        print (Fore.YELLOW +"Parking space freed at Lot number :"+ str(parkinglotnum) +" Slot Number : "+  str(parkingslotnum) +"" + Style.RESET_ALL)
        return True