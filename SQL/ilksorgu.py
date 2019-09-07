import sqlite3 as sql
# db = sql.connect(r"C:\Users\vektorel\Documents\GitHub\Python9\SQL\chinook.db")
# cur = db.cursor()
# filtre  = input("Sorgulamak istediğin seçenek")
# cur.execute("SELECT * FROM albums WHERE Title LIKE {}".format(filtre))
# liste =  cur.fetchall()
# for a,b,c  in liste:
#     print("{}-{}-{}".format(a,b,c))

def parcaEkle():
    try:
        parcaadi = input("Parçanın adını giriniz")
        sure = input("Süre giriniz")
        Boyut = input("Boyut giriniz")
        ucret = input("Ücret giriniz")
        sorgu = """
        INSERT INTO tracks (
                        Name,
                        AlbumId,
                        MediaTypeId,
                        GenreId,
                        Milliseconds,
                        Bytes,
                        UnitPrice
                    )
                    VALUES (
                        '{}',
                        348,
                        1,
                        26,
                        {},
                        {},
                        {}
                    )
        """.format(parcaadi,sure,Boyut,ucret)

        db = sql.connect(r"C:\Users\vektorel\Documents\GitHub\Python9\SQL\chinook.db")
        cur = db.cursor()
        cur.execute(sorgu)
        db.commit()
    except:
        pass
    finally:
        db.close()

# parcaEkle()
def albumListele():
    db = sql.connect(r"C:\Users\vektorel\Documents\GitHub\Python9\SQL\chinook.db")
    cur = db.cursor()
    filtre  = input("Sorgulamak istediğin seçenek")
    cur.execute("SELECT * FROM albums WHERE Title LIKE '{}'".format(filtre))
    liste =  cur.fetchall()
    for a,b,c  in liste:
        print("{}-{}-{}".format(a,b,c))
    
albumListele()
