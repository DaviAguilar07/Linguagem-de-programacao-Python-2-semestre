# Descobrindo as informações da API
import pandas as pd

df_selic = pd.read_json(
    "https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json"
    "&dataInicial=01/01/2023&dataFinal=31/12/2024"
)
print(df_selic.info())

# Inserindo duas colunas (data e responsável) na tabela que a API forneceu
from datetime import date 
from datetime import datetime as dt

data_extraçao = date.today()
df_selic['data'] = data_extraçao
df_selic['responsável'] = "Autor"
print(df_selic.info())
print(df_selic.head())

# Pegando os valores da posição 0
df_selic.loc[0]

# Pegando os valores de forma boolena (analisa a condição e imprime true ou false)
df_selic.loc['valor'] > 0.0005
