from flask import Flask
from sqlalchemy import create_engine
import pyodbc

app = Flask(__name__)

@app.route('/')
def connection():
    Driver = "{ODBC Driver 17 for SQL Server}"
    Server = "pavelserver.mysql.database.azure.com"
    Port = 3306
    Database = "library"
    Uid = "thesquashedman"
    Pwd = "Mesoepic2"
    
    try:
        cnxn = pyodbc.connect(f'DRIVER={Driver};SERVER={Server};DATABASE={Database};Uid={Uid};Pwd={Pwd};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
        cursor = cnxn.cursor()
        cursor.execute(f"SELECT * FROM test where testvar LIKE '%1%';")

    for row in cursor:
        print('row = %r' % (row,))
    return "Connection to database successful"

