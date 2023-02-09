import pandas as pd
from IPython.display import display

combustiveis_df = pd.read_excel("ca-2021-02.xlsx")

def main():
    filtraEtanolEMunicipio()

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

def filtraEtanolEMunicipio():
    # DataFrame.loc[] com múltiplas condições para filtragem
    # Quais são so preços do ETANOL na minha cidade
    ca_df = combustiveis_df[['Revenda', 'Municipio', 'Produto', 'Valor de Venda']]

    etanol_salvador_df = ca_df.loc[(ca_df['Produto'] == 'ETANOL') & (ca_df['Municipio'] == 'SALVADOR')]
    display(etanol_salvador_df.sort_values(by='Valor de Venda'))

def mediaCombustiveisBairroSp():
    # Qual a média de preços dos combustíveis GASOLINA e GASOLINA ADITIVADA do Bairro MOOCA em SÃO PAULO?
    display(combustiveis_df.loc[(combustiveis_df['Bairro'] == 'MOOCA') &
                                (combustiveis_df['Municipio'] == 'SAO PAULO') &
                                (combustiveis_df['Produto'].isin(["GASOLINA", "GASOLINA ADITIVADA"])),
                                ['Valor de Venda']].mean())

def mediaValorDeVendaPorCombustiveis():
    # Como mostrar média de valor de venda POR COMBUSTÍVEL no Brasil
    media_por_combustivel_df = ca_df[['Produto', 'Valor de Venda']].groupby(by='Produto').mean().round(2)
    display(media_por_combustivel_df)


if __name__ == '__main__':
    global ca_df
    global gas_df

    main()