from bcb import sgs
import pandas as pd
import matplotlib.pyplot as plt
import requests

# Baixa dados do banco central dado código, data de início e data final
def baixar_dados_bcb(codigo_serie, data_inicio, data_final):
    url = f'https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo_serie}/dados?formato=json&dataInicial={data_inicio}&dataFinal={data_final}'
    response = requests.get(url)

    if response.status_code == 200:
        df = pd.read_json(url)
        df.set_index('data', inplace = True)
        df.index = pd.to_datetime(df.index, dayfirst= True)
        return df

    else:
        print(f"Erro ao baixar a série {codigo_serie}: {response.status_code}")
        return None

# Gráfico original
def plot_orig(time_series):
    org = plt.plot(time_series)

# Gráfico sazonalidade
def plot_sazonalidade(time_series):
    saz = plt.plot(time_series.diff())

# Gráfico média móvel
def plot_mediamovel(time_series):
    rolmean = time_series.rolling(12).mean()
    org = plt.plot(time_series, alpha = 0.5)
    tend = plt.plot(rolmean, color = 'r')
    plt.show(block=False)

def main():
    codigo_inflacao = 433
    codigo_metas_inflacao = 13521
    codigo_selic = 11

    inicio = '01/01/2015'
    fim = '31/12/2025'

    df_inflacao = baixar_dados_bcb(codigo_inflacao, inicio, fim)
    df_metas = baixar_dados_bcb(codigo_metas_inflacao, inicio, fim)
    df_selic = baixar_dados_bcb(codigo_selic, inicio, fim)

if(__name__ == '__main__'):
    main()
