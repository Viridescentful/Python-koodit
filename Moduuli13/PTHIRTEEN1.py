from flask import Flask, request

app = Flask(__name__)
@app.route('/alkuluku/<teksti>')

def alkuluku(teksti): #127.0.0.1:3000/alkuluku/31
    isprime = True

    for i in range(2, int(teksti)):
        if int(teksti) % i == 0:
            isprime = False
            break

    vastaus = {
        "Number": teksti,
        "isPrime": isprime
    }

    return vastaus

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)