import mariadb

def vytvor_db():
    config = {
        'user': 'root',
        'password': '123',
        #'host': 'mariadb',
        'host': 'localhost',
        'port': 3306
    }
    conn = mariadb.connect(**config)
    cursor = mariadb.Cursor(conn)
    cursor.execute("""
                   CREATE DATABASE IF NOT EXISTS hackithon_2024
                   """)
    cursor.close()
    conn.commit()

def napoj_do_db():
    config = {
        'user': 'root',
        'password': '123',
        'host': 'localhost',
        'port': 3306,
        'database': 'hackithon_2024'
    }
    conn = mariadb.connect(**config)
    cursor = mariadb.Cursor(conn)
    return conn, cursor

def vytvor_tabulky(datafile):
    conn, cursor = napoj_do_db()
    cursor.execute("""
                
                """)
