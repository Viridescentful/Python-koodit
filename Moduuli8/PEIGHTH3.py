import mysql.connector
import geopy.distance
from geopy.distance import great_circle as GRC

yhteys = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="flight_game",
    user="Veikko",
    password="SQLTemp",
    autocommit=True
)

def hae_lentokentta(koodi):
    sql = f"SELECT name, latitude_deg, longitude_deg FROM airport WHERE ident = '{koodi}' group by type"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()

    return tulos


ensimmainenkentta = hae_lentokentta(str(input("Anna ensimmäinen ICAO: ")))
toinenkentta = hae_lentokentta(str(input("Anna ensimmäinen ICAO: ")))

distance = GRC((ensimmainenkentta[1], ensimmainenkentta[2]), (toinenkentta[1], toinenkentta[2])).km

print("Lentokenttien", ensimmainenkentta[0], "ja", toinenkentta[0], "välinen matka on:", round(distance, 0), "KM")