from flask import Flask, request
import mysql.connector
import json

yhteys = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        database="flight_game",
        user="Veikko",
        password="",
        autocommit=True
    )
app = Flask(__name__)
@app.route('/kenttä/<teksti>')

def kenttä(teksti): #127.0.0.1:3000/kenttä/EFHK
    def hae_lentokentta(koodi):
        sql = f"SELECT ident, name, municipality FROM airport WHERE ident = '{koodi}'"
        kursori = yhteys.cursor()
        kursori.execute(sql)
        tulos = kursori.fetchone()
        print(tulos)

        return tulos

    tiedot = hae_lentokentta(teksti)

    if tiedot != None:
        vastaus = {
            "ICAO": tiedot[0],
            "Name": tiedot[1],
            "Municipality": tiedot[2],
        }

        return vastaus
    else:
        return "Ei saatavilla olevaa lentokenttää"



if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)