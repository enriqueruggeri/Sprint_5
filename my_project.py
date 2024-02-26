# Cargamos todas las librerías que ocuparemos en el proyecto:
import pandas as pd  # importamos las librerías de pandas
# importamos las librerías pyplot de Matplotlib
from matplotlib import pyplot as plt
# importamos la librerías de NumPy, se usa para funciones matemáticas complejas
import numpy as np
# importamos el módulo stats de la librería SciPy.
from scipy import stats as st
import seaborn as sns  # importamos la librería Seaborn para realizar unos gráficos
# cargamos el DataFrame
vehicules = pd.read_csv(
    '/Users/eruggeri/Pythons_Projects/Sprint_5/vehicles_us.csv')
vehicules.info()
