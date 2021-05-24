import pandas as pd

vehiculos = {'Marca': [''Toyota','Ford','Audi'],
        'Precio': [34000,56000,23000]
        }

df = pd.DataFrame(vehiculos, columns = ['Marca', 'Precio'])
