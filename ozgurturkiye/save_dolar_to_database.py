import sqlite3
import time

def dolar_write(liste):
    with sqlite3.connect('vt.sqlite') as vt:
        im = vt.cursor()

        clean_liste = list(liste.values())
        now = time.time()
        clean_liste.append(now)

        im.execute("""CREATE TABLE IF NOT EXISTS dolar
            ("Döviz Kodu", "Birim", "Döviz Cinsi", "Döviz Alış", "Döviz Satış", "Efektif Alış", "zaman")""")

        im.execute("""INSERT INTO dolar VALUES 
            (?, ?, ?, ?, ?, ?, ?)""", clean_liste)

        vt.commit()