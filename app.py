from flask import Flask
from sqlalchemy import create_engine
import pyodbc

app = Flask(__name__)

@app.route('/')
def connection():
    
    
    
    cnxn = pyodbc.connect('DRIVER={Devart ODBC Driver for SQL Server};Server=pavelserver.mysql.database.azure.com;Database=library;Port=3306;User ID=thesquashedman;Password=Mesoepic2')
    cursor = cnxn.cursor()
    cursor.execute("SELECT * FROM test where testvar LIKE '%1%';")

    row = cursor.fetchone() 
    while row:
        print (row) 
        row = cursor.fetchone()
    return "Connection to database successful"

