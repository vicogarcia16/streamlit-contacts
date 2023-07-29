import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def get_conexion():
    
    ps_connection = psycopg2.connect(user=os.getenv('USER'),
                                    password=os.getenv('PASSWORD'),
                                    host=os.getenv('HOST'),
                                    port=os.getenv('PORT'),
                                    database=os.getenv('DATABASE'))
    return ps_connection

def close_conexion(ps_connection):
    if ps_connection:
        ps_connection.close()
    
    