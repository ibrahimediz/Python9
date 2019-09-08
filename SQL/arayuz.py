import tkinter as tk
import sqlite3 as sql
def verigetir():
    db = sql.connect(r"C:\Users\vektorel\Documents\GitHub\Python9\SQL\chinook.db")
    cur = db.cursor()
    cur.execute("select * from artists WHERE ArtistId = 1")
    liste = cur.fetchall()
    return liste
pencere = tk.Tk()
pencere.geometry("200x300")
etiket = tk.Label()
etiket["text"] = verigetir()[0][1]
etiket.pack()

pencere.mainloop()