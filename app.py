from flask import Flask
from sqlalchemy import create_engine
import pyodbc

app = Flask(__name__)

@app.route('/')
def connection():
    
    
    
    server = 'tcp:paveldatabasewebapp.azurewebsites.net:3306' 
    database = 'library' 
    username = 'thesquashedman' 
    password = 'Mesoepic2'
    # ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    cursor.execute("SELECT * FROM test where testvar LIKE '%1%';")

    row = cursor.fetchone() 
    while row:
        print (row) 
        row = cursor.fetchone()
    return "Connection to database successful"

