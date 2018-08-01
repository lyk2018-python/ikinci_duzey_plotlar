import sqlite3


with sqlite3.connect('vt.sqlite') as vt:
    im = vt.cursor()
    im.execute("""SELECT * FROM dolar""")
    all_data = im.fetchall()
    print(all_data)