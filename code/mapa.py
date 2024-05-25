import pandas as pd
import unicodedata

# Načtení dat
file = pd.read_csv('datafiles/souradnice_mesta.csv', encoding='utf-8')

# Změna názvů sloupců na bez mezer a diakritiky
new_columns = {column: unicodedata.normalize('NFKD', column).encode('ascii', 'ignore').decode('utf-8').replace(' ', '_').lower() for column in file.columns}
file = file.rename(columns=new_columns)

# Výpis DataFrame s novými názvy sloupců
print(file.head())

file.to_csv('datafiles/souradnice_mesta_ok.csv', sep=";", index=False)