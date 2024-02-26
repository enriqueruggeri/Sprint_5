# Cargamos todas las librerías que ocuparemos en el proyecto:
import pandas as pd  # importamos las librerías de pandas
vehicules = pd.read_csv(
    '/Users/eruggeri/Pythons_Projects/Sprint_5/vehicles_us.csv')
vehicules.info()
print('--------------')
print(vehicules.head())
print('--------------')
