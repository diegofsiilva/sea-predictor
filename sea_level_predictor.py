import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Carregar os dados
    data = pd.read_csv('epa-sea-level.csv')

    # Gráfico de dispersão
    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'])

    # Linha de tendência completa
    full_fit = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
    years_full = range(data['Year'].min(), 2051)
    sea_level_full = full_fit.intercept + full_fit.slope * pd.Series(years_full)
    plt.plot(years_full, sea_level_full, label='Trend: All Data')

    # isso aqui mostra a linha de tendência desde 2000
    recent_data = data[data['Year'] >= 2000]
    recent_fit = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
    years_recent = range(2000, 2051)
    sea_level_recent = recent_fit.intercept + recent_fit.slope * pd.Series(years_recent)
    plt.plot(years_recent, sea_level_recent, label='Trend: From 2000')

    # mostra os rótulos e títulos
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # pra salvar gráfico como img
    plt.savefig('sea_level_plot.png')
    return plt.gca()