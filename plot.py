# plots de dados do arquivo autos.csv

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('autos.csv', encoding='latin-1')

#print(df.head())
print(list(df))

# plot com a distribuição de veículos por ano de registro
plt.hist(df['yearOfRegistration'], bins=100, histtype='barstacked', rwidth=0.8)
plt.xlabel('Ano de registro')
plt.ylabel('Número de veículos')
plt.title('Distribuição de veículos por ano de registro')
plt.show()







