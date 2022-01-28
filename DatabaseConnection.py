import mysql.connector

cursor = None
def __init__():
    LicenseNumberDB = mysql.connector.connect(
        host = "localhost",
        user = "cbn",
        password = "admin",
        database = "LicensePlates"
    )
    global cursor
    cursor = LicenseNumberDB.cursor()

def savePlate(LicenseNumber):
    pass
