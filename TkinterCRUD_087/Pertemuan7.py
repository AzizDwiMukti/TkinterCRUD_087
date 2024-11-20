import sqlite3
con = sqlite3.connect("tutorial.db")
cur = con.cursor()
_title=input("Masukan nama Movie: ")
_year=input("Masukan tahun release: ")
_rating=input("Masukan rating Movienya: ")
cur.execute("""
            INSERT INTO movie VALUES
            ('{}',{},{})
            """.format(_title,_year,_rating))
con.commit()