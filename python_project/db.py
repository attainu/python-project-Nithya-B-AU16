import os
import pyodbc

class cl_databaseconnect:

    def fn_getconnection(self):
        dbpath = os.getcwd()                                                                                                    
        dbpath=dbpath+r"\Database1.accdb"
        mainconn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ='+dbpath+';')
        return mainconn