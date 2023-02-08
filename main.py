import pandas as pd
from IPython.display import display

combustiveis_df = pd.read_excel("ca-2021-02.xlsx")

def main():
    filtrandoESelecinandoMinhasColunas()

# Usa o print para ver o dataframe!
def usandoPrint():
    print(combustiveis_df)

# Usa o Display para ver o dataframe!
def usandoDisplay():
    display(combustiveis_df)

#Exibe as primeiras 5 linhas!
def exibeCincoLinhas():
    display(combustiveis_df.head())

#Exibe as primeiras 15 linhas!
def exibeQuinzeLinhas():
    display(combustiveis_df.head(15))

# Comandos Dataframe.shape e Dataframe.describe()
def comandoShape():
    # mostra o número de linhas e colunas (linhas, colunas)
    print(combustiveis_df.shape)

    #só as linhas
    print(combustiveis_df.shape[0])

# describe() mostra estatísticas "mais básicas" que a gente precisa
def comandoDescribe():
    print(combustiveis_df.describe())

# Quais são as colunas e que tipo de dados cada um tem...
def infos():
    print(combustiveis_df.info())

# filtrar apenas por uma coluna
def filtraPorColuna():
    display(combustiveis_df['Revenda'])

# Aqui criamos um novo dataframe apenas com as colunas que eu quero...
def filtrandoESelecinandoMinhasColunas():
    ca_df = combustiveis_df[['Revenda', 'Municipio', 'Produto', 'Valor de Venda']]
    display(ca_df)

def exibeAQuartaLinha():
    # Exibe a 4a. linha.
    display(ca_df.loc[3])
    # Exibir da 10a. linha até a 20a. linha
    display(ca_df.loc[9:19])

def filtrandoSomenteGasolina():
    # Criar um Dataframe gas_df contendo
    # apenas as 4 colunas (Revenda, Municipio, Produto, Valor de Venda)
    # somente com combustível sendo GASOLINA.
    gas_df = ca_df.loc[ca_df['Produto'] == 'GASOLINA']
    display(gas_df)

    display(gas_df['Valor de Venda'].max())

def exibeInfosGasolinaMaisCara():
    # Exibir qual é o posto e munícipio da gasolina mais cara do país?
    display(gas_df[['Revenda', 'Municipio', 'Valor de Venda']].max())


if __name__ == '__main__':
    global ca_df
    global gas_df

    main()