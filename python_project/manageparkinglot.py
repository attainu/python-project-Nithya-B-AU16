from colorama import Fore, Style
from db import cl_databaseconnect
from report import cl_report
connn=cl_databaseconnect()
conn=connn.fn_getconnection()
    
class  cl_manageparkinglot:
# create new parking lot
    def fn_createparkinglot(self,slotcount):
        cursor = conn.cursor()
        
        cursor.execute('select max(lot_number)+1  from parking_lot')
        
        records = cursor.fetchall()

        for row in records:
            parkinglotnum=row[0]
        
        if parkinglotnum is None:
            parkinglotnum=1

        if parkinglotnum>=7 : 
            print (Fore.RED +"Maximum parking lots are allocated Parking" +Style.RESET_ALL)
            r=cl_report()
            r.fn_availablity()
            return True

        i=0
        while i < int(slotcount):
            i=i+1
            cursor = conn.cursor()
            cursor.execute("insert into parking_lot (lot_number,slot_number)values(" + str(parkinglotnum)+ ","+ str(i) +")")
            conn.commit()        
        print (Fore.YELLOW +"New parking lot "+ str(parkinglotnum) +" created with the capacity of " + str(slotcount) +Style.RESET_ALL)
        return True

