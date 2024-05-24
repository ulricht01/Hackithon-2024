import mariadb
import pandas as pd

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
        'database': 'hackithon_2024',
        'local_infile': True,
    }
    conn = mariadb.connect(**config)
    cursor = mariadb.Cursor(conn)
    return conn, cursor

def vytvor_tabulky():
    conn, cursor = napoj_do_db()
    cursor.execute(f"""
    CREATE TABLE IF NOT EXISTS ciselnik_obci (
        kodjaz VARCHAR(2),
        akrcis VARCHAR(5),
        kodcis VARCHAR(6),
        chodnota VARCHAR(50),
        zkrtext VARCHAR(50),
        text VARCHAR(50),
        admplod VARCHAR(20),
        admnepo VARCHAR(20),
        obec_ul ENUM("ano", "ne"),
        ob_ul_cor ENUM("ano", "ne"),
        sm_rozsah INT,
        sm_typ INT,
        kodobce_h INT,
        domin_cobc INT,
        porcobec_o INT
    );
    """)

    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS  volby_obce (
                    CIS_OBEC INT,
                    NAZ_OBEC VARCHAR(255),
                    TYP_OBEC VARCHAR(50),
                    OKRSKY_CELKEM INT,
                    OKRSKY_ZPRAC INT,
                    OKRSKY_ZPRAC_PROC FLOAT,
                    ZAPSANI_VOLICI INT,
                    VYDANE_OBALKY INT,
                    UCAST_PROC FLOAT,
                    ODEVZDANE_OBALKY INT,
                    PLATNE_HLASY INT,
                    PLATNE_HLASY_PROC FLOAT,
                    KSTRANA INT,
                    HLASY INT,
                    PROC_HLASU FLOAT
                );          """)


    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS  volby_okres (
                    NUTS_OKRES VARCHAR(10),
                    NAZ_OKRES VARCHAR(255),
                    OKRSKY_CELKEM INT,
                    OKRSKY_ZPRAC INT,
                    OKRSKY_ZPRAC_PROC FLOAT,
                    ZAPSANI_VOLICI INT,
                    VYDANE_OBALKY INT,
                    UCAST_PROC FLOAT,
                    ODEVZDANE_OBALKY INT,
                    PLATNE_HLASY INT,
                    PLATNE_HLASY_PROC FLOAT,
                    KSTRANA INT,
                    HLASY INT,
                    PROC_HLASU FLOAT
                );
                    """)
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS  ciselnik_strany (
                    id INT,
                    nazev_strany VARCHAR(40),
                    zkratka_strany VARCHAR(20)
                );
                    """)
    conn.commit()


def nahraj_data(datafile, sep):
    conn, cursor = napoj_do_db()
    cursor.execute(f"""
                    LOAD DATA LOCAL INFILE '{datafile}'
                    INTO TABLE {datafile[10:-4]}
                    FIELDS TERMINATED BY '{sep}'
                    ENCLOSED BY '"'
                    LINES TERMINATED BY '\n'
                    IGNORE 1 ROWS;
                """)
    conn.commit()

#vytvor_tabulky()
#nahraj_data('datafiles/ciselnik_obci.csv', ";")
#nahraj_data('datafiles/volby_obce.csv', ";")
#nahraj_data('datafiles/volby_okres.csv', ";")
#nahraj_data('datafiles/ciselnik_strany.csv', ";")


