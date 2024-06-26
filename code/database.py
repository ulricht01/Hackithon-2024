import mariadb
import pandas as pd

def vytvor_db():
    config = {
        'user': 'root',
        'password': '123',
        'host': 'mariadb',
        #'host': 'localhost',
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
        #'host': 'localhost',
        'host': 'mariadb',
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
    
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS souradnice_mesta_ok (
                    obec VARCHAR(255),
                    kod_obce INT,
                    okres VARCHAR(255),
                    kod_okresu VARCHAR(255),
                    kraj VARCHAR(255),
                    kod_kraje VARCHAR(255),
                    psc INT,
                    latitude FLOAT,
                    longitude FLOAT
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

def top_5_strany():
    conn, cursor = napoj_do_db()
    cursor.execute("""
                    SELECT 
    cis_str.nazev_strany, 
    cis_str.zkratka_strany,
    sum(obc.hlasy)
        FROM 
            (SELECT 
                DISTINCT kstrana,
                hlasy
            FROM 
                volby_okres) AS obc
        LEFT JOIN 
            ciselnik_strany cis_str ON (obc.kstrana = cis_str.id)
        GROUP BY 
            1, 2
        ORDER BY 
            3 DESC
        LIMIT 5""")
    data = cursor.fetchall()
    conn.close()
    return data

def bottom_5_strany():
    conn, cursor = napoj_do_db()
    cursor.execute("""
                    SELECT  cis_str.nazev_strany, 
                            cis_str.zkratka_strany,
                            sum(obc.hlasy) as Celkem_hlasu
                    FROM volby_obce obc
                    LEFT JOIN ciselnik_strany cis_str on (obc.kstrana = cis_str.id)
                    WHERE typ_obec != "OBEC_S_MCMO" 
                    GROUP BY 1,2
                    ORDER BY 3 Asc
                    LIMIT 5""")
    data = cursor.fetchall()
    conn.close()
    return data

def min_prc_ucast():
    conn, cursor = napoj_do_db()
    cursor.execute("""
                    SELECT  distinct naz_obec, 
                            ucast_proc
                    FROM volby_obce obc
                    ORDER BY 2 Asc
                    LIMIT 5""")
    data = cursor.fetchall()
    conn.close()
    return data

def top_prc_ucast():
    conn, cursor = napoj_do_db()
    cursor.execute("""
                    SELECT  distinct naz_obec, 
                            ucast_proc
                    FROM volby_obce obc
                    ORDER BY 2 Desc
                    LIMIT 5""")
    data = cursor.fetchall()
    conn.close()
    return data

def obec_bez_vs_s_mcmo():
    conn, cursor = napoj_do_db()
    cursor.execute("""
                    SELECT TYP_OBEC, sum(PLATNE_HLASY) as plt FROM 
                   (SELECT DISTINCT NAZ_OBEC, TYP_OBEC, PLATNE_HLASY FROM `volby_obce` WHERE TYP_OBEC != "MCMO") as xxx 
                   GROUP by 1
                    """)
    data = cursor.fetchall()
    conn.close()
    return data


def obec_vs_mesto_prc_avg():
    conn, cursor = napoj_do_db()
    cursor.execute("""
                    SELECT  typ_obec, 
                            avg(ucast_proc) as celkem_hlasu
                    FROM volby_obce obc
                    WHERE typ_obec in ('OBEC_S_MCMO', 'OBEC_BEZ_MCMO')
                    GROUP BY 1
                    """)
    data = cursor.fetchall()
    conn.close()
    return data


def platne_vs_odevzdane_hlasy():
    conn, cursor = napoj_do_db()
    cursor.execute("""
                    SELECT  typ_obec,
                            sum(odevzdane_obalky-platne_hlasy) as rozdil
                    FROM (SELECT DISTINCT NAZ_OBEC, TYP_OBEC, PLATNE_HLASY, odevzdane_obalky FROM `volby_obce` WHERE TYP_OBEC != "MCMO") as xxx
                    group by 1
                    """)
    data = cursor.fetchall()
    conn.close()
    return data

def vydane_vs_ztracene_hlasy():
    conn, cursor = napoj_do_db()
    cursor.execute("""
                    SELECT  typ_obec,
                            sum(vydane_obalky-odevzdane_obalky) as rozdil
                    FROM (SELECT DISTINCT NAZ_OBEC, TYP_OBEC, vydane_obalky, odevzdane_obalky FROM `volby_obce` WHERE TYP_OBEC != "MCMO") as xxx
                    group by 1
                    """)
    data = cursor.fetchall()
    conn.close()
    return data

def data_pro_mapu():
    conn, cursor = napoj_do_db()
    cursor.execute("""
                    SELECT latitude, longitude, sum(hlasy) as hlasy
                    FROM souradnice_mesta_ok smo
                    inner JOIN (SELECT cis_obec, hlasy
                    FROM volby_obce WHERE typ_obec != ('MCMO')) as vol on (vol.cis_obec = smo.kod_obce)
                   GROUP BY 1,2
""")
    data = cursor.fetchall()
    conn.commit()
    return data
#vytvor_tabulky()
#nahraj_data('datafiles/ciselnik_obci.csv', ";")
#nahraj_data('datafiles/volby_obce.csv', ";")
#nahraj_data('datafiles/volby_okres.csv', ";")
#nahraj_data('datafiles/ciselnik_strany.csv', ";")
#vytvor_tabulky()
#nahraj_data('datafiles/souradnice_mesta_ok.csv', ";")

