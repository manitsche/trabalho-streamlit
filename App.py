import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar o dataset
caminho = "./carros.csv"

try:
    df = pd.read_csv(caminho)
    st.title("Base de dados - Caracteristicas e preços de carros")
except FileNotFoundError:
    st.error(f"O arquivo não foi encontrado no caminho: {caminho}")

# Verificar as primeiras linhas do DataFrame se o arquivo foi carregado com sucesso
if 'df' in locals():
    # 'df' in locals() verifica se a chave 'df' (ou seja, o nome da variável) está presente no dicionário retornado por locals().
    # Isso indica se a variável df foi definida anteriormente no código.

    # st.write("Visualização dos dados:")
    # st.write(df.head())

    # Criar abas para as diferentes análises
    abas = st.tabs(["Análise de Preço", "Características Técnicas", "Análise por Fabricante"])

    # 1. Análise de Preço - Média de Preços por Modelo
    with abas[0]:
        st.subheader("Média de Preços por Modelo")
        
        media_preco_modelo = df.groupby('Model')['MSRP'].mean().sort_values(ascending=False).head(10)
        # Agrupa o DataFrame df com base nos valores da coluna Model.
        # Após o agrupamento, seleciona a coluna MSRP (Manufacturer's Suggested Retail Price ou "Preço Sugerido pelo Fabricante") para realizar operações apenas sobre esses valores.
        # Calcula a média do MSRP para cada grupo (ou seja, para cada modelo). Assim, obtem o preço médio de cada modelo presente na base de dados.
        # Ordena os valores resultantes em ordem decrescente, ou seja, do modelo com preço médio mais alto para o mais baixo.
        # Seleciona apenas os 10 primeiros valores dessa lista ordenada. Isso nos dá os 10 modelos com os preços médios mais altos.
        
        fig, ax = plt.subplots()
        # plt.subplots(): Esse comando cria uma nova figura (fig) e um conjunto de eixos (ax), que podem ser usados para criar gráficos. Ele é muito útil para organizar a área de plotagem e configurar múltiplos gráficos, mas aqui estapenas criando uma figura e um único conjunto de eixos, o que é suficiente para um gráfico simples.
        # fig: É um objeto Figure, que representa o contêiner de nível superior para todo o gráfico. Ele controla aspectos como o tamanho da figura, a resolução, e permite que você salve a figura inteira como uma imagem.
        # ax: É um objeto Axes, que representa a área onde os dados reais são plotados. Esse objeto oferece métodos e propriedades para customizar o gráfico, como definir títulos, rótulos dos eixos e personalizar a aparência do gráfico.

        media_preco_modelo.plot(kind='bar', ax=ax, color='skyblue')
        ax.set_title("Média de Preço (MSRP) por Modelo (Top 10)")
        ax.set_xlabel("Modelo") 
        ax.set_ylabel("Preço Médio (MSRP)")
        st.pyplot(fig)

    # 2. Características Técnicas - Transmissão
    with abas[1]:
        st.subheader("Transmissão")
        transmissao_counts = df['Transmission Type'].value_counts()
        
        fig, ax = plt.subplots()
        transmissao_counts.plot(kind='bar', ax=ax, color='lightgreen')
        ax.set_title("Distribuição dos Tipos de Transmissão")
        ax.set_xlabel("Tipo de Transmissão")
        ax.set_ylabel("Quantidade")
        st.pyplot(fig)

    # 3. Análise por Fabricante (Marca) - Comparação de Preços entre Fabricantes
    with abas[2]:
        st.subheader("Comparação de Preços entre Fabricantes")
        media_preco_fabricante = df.groupby('Make')['MSRP'].mean().sort_values(ascending=False).head(10)
        
        fig, ax = plt.subplots()
        media_preco_fabricante.plot(kind='bar', ax=ax, color='orange')
        ax.set_title("Média de Preço (MSRP) por Fabricante (Top 10)")
        ax.set_xlabel("Fabricante")
        ax.set_ylabel("Preço Médio (MSRP)")
        st.pyplot(fig)
else:
    st.error("Não foi possível carregar o DataFrame.")