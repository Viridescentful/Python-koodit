import mysql.connector


yhteys = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    database="flight_game",
    user="Veikko",
    password="SQLTemp",
    autocommit=True
)

def hae_lentokentta(koodi):
    sql = f"SELECT type, count(type) FROM airport WHERE iso_country = '{koodi}' group by type"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    for tyyppi in tulos:
        print(tyyppi[0], "tyypi lentokenttiä on:", tyyppi[1])


hae_lentokentta(str(input("Anna Lokaali koodi: ")))
