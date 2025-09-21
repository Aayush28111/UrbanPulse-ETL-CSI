import pandas as pd
import datetime
from sqlalchemy import create_engine
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

MYSQL_USER = config["mysql"]["user"]
MYSQL_PASS = config["mysql"]["password"]
MYSQL_HOST = config["mysql"]["host"]
MYSQL_PORT = config["mysql"]["port"]
MYSQL_DB = config["mysql"]["database"]
CITY = config["settings"]["city"]

engine = create_engine(
    f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASS}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"
)

def normalize(val, max_val):
    return min(val / max_val, 1.0) if val is not None else 0

def main():
    print("Calculating CSI...")

    weather = pd.read_sql("SELECT * FROM weather_data ORDER BY id DESC LIMIT 1", engine)
    air = pd.read_sql("SELECT * FROM air_quality_data ORDER BY id DESC LIMIT 1", engine)
    traffic = pd.read_sql("SELECT * FROM traffic_data ORDER BY id DESC LIMIT 1", engine)
   
