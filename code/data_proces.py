import pandas as pd
import xml.etree.ElementTree as ET
import csv
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


import pandas as pd
import statsmodels.api as sm

# Načtení dat
file = pd.read_csv('datafiles/voleni_zavislost.csv', sep=";")

# Definice nezávislé a závislé proměnné
X = file['vek_volenych']  # Věk volených
y = file['pocet_hlasu']   # Počet hlasů

# Přidání konstanty pro konstantní člen v modelu
X = sm.add_constant(X)

# Vytvoření modelu a provedení regrese
model = sm.OLS(y, X).fit()

# Výpis výsledků regrese
print(model.summary())


# Function to parse the XML and extract relevant data
def parse_xml(file_path):
    # Parse the XML file
    tree = ET.parse(file_path)
    root = tree.getroot()
    ns = {'ns': 'http://www.w3.org/namespace/'}
    
    # Lists to store the data
    okres_data = []
    obec_data = []
    
    # Extract OKRES data
    for okres in root.findall('ns:OKRES', ns):
        okres_info = okres.attrib
        ucast_info = okres.find('ns:UCAST', ns).attrib
        
        # Combine OKRES and UCAST data
        okres_combined = {**okres_info, **ucast_info}
        
        # Extract HLASY_STRANA data for OKRES
        hlasy_strana = []
        for strana in okres.findall('ns:HLASY_STRANA', ns):
            strana_info = strana.attrib
            hlasy_strana.append({**okres_combined, **strana_info})
        
        okres_data.extend(hlasy_strana)
    
    # Extract OBEC data
    for obec in root.findall('ns:OBEC', ns):
        obec_info = obec.attrib
        ucast_info = obec.find('ns:UCAST', ns).attrib
        
        # Combine OBEC and UCAST data
        obec_combined = {**obec_info, **ucast_info}
        
        # Extract HLASY_STRANA data for OBEC
        hlasy_strana = []
        for strana in obec.findall('ns:HLASY_STRANA', ns):
            strana_info = strana.attrib
            hlasy_strana.append({**obec_combined, **strana_info})
        
        obec_data.extend(hlasy_strana)
    
    # Convert lists to DataFrames
    df_okres = pd.DataFrame(okres_data)
    df_obec = pd.DataFrame(obec_data)
    
    return df_okres, df_obec

# Parse the XML file and get DataFrames
#file_path = 'datafiles/vysledky_okres.xml'
#df_okres, df_obec = parse_xml(file_path)

#df_obec.to_csv('datafiles/volby_obce.csv', sep=";", index=False, encoding='utf-8')
#df_okres.to_csv('datafiles/volby_okres.csv', sep=";", index=False, encoding='utf-8')


#datafile = pd.read_excel('datafiles/ciselnik_strany.xlsx')

#datafile.to_csv('datafiles/ciselnik_strany.csv', sep=";", index=False)


#df = pd.read_csv('datafiles/ciselnik_obci.csv', encoding='utf-8')


#import pandas as pd
#import unicodedata

# Načtení dat
#file = pd.read_csv('datafiles/souradnice_mesta.csv', encoding='utf-8')

# Změna názvů sloupců na bez mezer a diakritiky
#new_columns = {column: unicodedata.normalize('NFKD', column).encode('ascii', 'ignore').decode('utf-8').replace(' ', '_').lower() for column in file.columns}
#file = file.rename(columns=new_columns)

# Výpis DataFrame s novými názvy sloupců
#print(file.head())

#file.to_csv('datafiles/souradnice_mesta_ok.csv', sep=";", index=False)

