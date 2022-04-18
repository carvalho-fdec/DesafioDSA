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

# boxplot para verificar a distribuição de preços por tipo de veículo
plt.boxplot(df['price'] , labels=df['vehicleType'])
plt.xlabel('Tipo de veículo')
plt.ylabel('Preço')
plt.title('Distribuição de preços por tipo de veículo')
plt.show()

# countplot para verificar a distribuição de veículos por tipo de veículo
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.title('Distribuição de veículos por tipo de veículo')
plt.xlabel('Tipo de veículo')
plt.ylabel('Número de veículos')
plt.xticks(rotation=90)
plt.subplot(1,2,2)
plt.title('Distribuição de veículos por tipo de veículo')
plt.xlabel('Tipo de veículo')
plt.ylabel('Número de veículos')
plt.xticks(rotation=90)
plt.show()
