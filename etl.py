import requests
import datetime
import random
import pandas as pd
from sqlalchemy import create_engine
import configparser

# --- Load config ---
config = configparser.ConfigParser()
config.read("config.ini")

MYSQL_USER = config["mysql"]["user"]
MYSQL_PASS = config["mysql"]["password"]
MYSQL_HOST = config["mysql"]["host"]
MYSQL_PORT = config["mysql"]["port"]
MYSQL_DB = config["mysql"]["database"]

OPENWEATHER_KEY = config["openweather"]["api_key"]
AQICN_KEY = config["aqicn"]["api_token"]

CITY = config["settings"]["city"]

# --- MySQL connection ---
engine = create_engine(
    f"mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASS}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"
)

# --- Weather API ---
def fetch_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_KEY}&units=metric"
    res = requests.get(url).json()
    return {
        "city": city,
        "temperature": res["main"]["temp"],
        "humidity": res["main"]["humidity"],
        "weather_desc": res["weather"][0]["description"],
        "ts": datetime.datetime.utcnow(),
    }

# --- AQI API ---
def fetch_air_quality(city):
    url = f"https://api.waqi.info/feed/{city}/?token={AQICN_KEY}"
    res = requests.get(url).json()
    if res["status"] == "ok":
        data = res["data"]
        return {
            "city": city,
            "aqi": data["aqi"],
            "pm25": data.get("iaqi", {}).get("pm25", {}).get("v", None),
            "pm10": data.get("iaqi", {}).get("pm10", {}).get("v", None),
            "ts": datetime.datetime.utcnow(),
        }
    return None

# --- Mock Traffic Data ---
def fetch_traffic(city):
    return {
        "city": city,
        "area": "Central",
        "congestion_score": random.uniform(0, 10),
        "ts": datetime.datetime.utcnow(),
    }

# --- Main ETL ---
def main():
    print("Fetching data...")

    weather = fetch_weather(CITY)
    air = fetch_air_quality(CITY)
    traffic = fetch_traffic(CITY)

    # Insert into MySQL
    pd.DataFrame([weather]).to_sql("weather_data", engine, if_exists="append", index=False)
    if air:
        pd.DataFrame([air]).to_sql("air_quality_data", engine, if_exists="append", index=False)
    pd.DataFrame([traffic]).to_sql("traffic_data", engine, if_exists="append", index=False)

    print("Data inserted successfully.")

if __name__ == "__main__":
    main()
