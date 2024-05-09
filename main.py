import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st

# Configurando o estilo padrão dos gráficos
sns.set_style("whitegrid")


# Função para criar o gráfico de barras
def bar_chart():
    data = {"Categoria": ["A", "B", "C", "D"], "Valor": [23, 45, 56, 78]}
    df = pd.DataFrame(data)
    fig, ax = plt.subplots()
    sns.barplot(x="Categoria", y="Valor", data=df, ax=ax)
    ax.set_title("Gráfico de Barras")
    ax.set_xlabel("Categorias")
    ax.set_ylabel("Valores")
    st.pyplot(fig)


# Função para criar o gráfico de pizza
def pie_chart():
    labels = ["A", "B", "C", "D"]
    sizes = [15, 30, 45, 10]
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140)
    ax.axis("equal")
    ax.set_title("Gráfico de Pizza")
    st.pyplot(fig)


# Função para criar o gráfico de dispersão
def scatter_plot():
    np.random.seed(0)
    x = np.random.rand(50)
    y = np.random.rand(50)
    fig, ax = plt.subplots()
    ax.scatter(x, y)
    ax.set_title("Gráfico de Dispersão")
    ax.set_xlabel("Eixo X")
    ax.set_ylabel("Eixo Y")
    st.pyplot(fig)


# Função para criar o gráfico de correlação
def correlation_plot():
    df = pd.DataFrame(np.random.rand(10, 5), columns=["A", "B", "C", "D", "E"])
    fig, ax = plt.subplots()
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm", ax=ax)
    ax.set_title("Gráfico de Correlação")
    st.pyplot(fig)


# Função para criar o gráfico de contagem
def count_plot():
    data = {"Categoria": ["A", "B", "C", "D", "A", "B", "C", "D", "A", "B"], "Valor": [23, 45, 56, 78, 45, 56, 78, 23, 56, 78]}
    df = pd.DataFrame(data)
    fig, ax = plt.subplots()
    sns.countplot(x="Categoria", data=df, ax=ax)
    ax.set_title("Gráfico de Contagem")
    ax.set_xlabel("Categorias")
    ax.set_ylabel("Contagem")
    st.pyplot(fig)


# Função para criar o gráfico de frequência
def freq_plot():
    data = {"Categoria": ["A", "B", "C", "D", "A", "B", "C", "D", "A", "B"], "Valor": [23, 45, 56, 78, 45, 56, 78, 23, 56, 78]}
    df = pd.DataFrame(data)
    fig, ax = plt.subplots()
    sns.histplot(data=df, x="Categoria", ax=ax)
    ax.set_title("Gráfico de Frequência")
    ax.set_xlabel("Categorias")
    ax.set_ylabel("Frequência")
    st.pyplot(fig)


# Função para criar o gráfico de rosca
def donut_plot():
    labels = ["A", "B", "C", "D"]
    sizes = [15, 30, 45, 10]
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140)
    ax.axis("equal")
    ax.set_title("Gráfico de Rosca")
    # Adicionar um círculo branco no centro para criar um gráfico de rosca
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig.gca().add_artist(centre_circle)
    st.pyplot(fig)


# Função para criar o gráfico de caixa (boxplot)
def box_plot():
    data = {"Categoria": ["A", "B", "C", "D", "A", "B", "C", "D", "A", "B"], "Valor": [23, 45, 56, 78, 45, 56, 78, 23, 56, 78]}
    df = pd.DataFrame(data)
    fig, ax = plt.subplots()
    sns.boxplot(x="Categoria", y="Valor", data=df, ax=ax)
    ax.set_title("Gráfico de Caixa (Boxplot)")
    ax.set_xlabel("Categorias")
    ax.set_ylabel("Valores")
    st.pyplot(fig)


# Função para criar o gráfico de violino
def violin_plot():
    data = {"Categoria": ["A", "B", "C", "D", "A", "B", "C", "D", "A", "B"], "Valor": [23, 45, 56, 78, 45, 56, 78, 23, 56, 78]}
    df = pd.DataFrame(data)
    fig, ax = plt.subplots()
    sns.violinplot(x="Categoria", y="Valor", data=df, ax=ax)
    ax.set_title("Gráfico de Violino")
    ax.set_xlabel("Categorias")
    ax.set_ylabel("Valores")
    st.pyplot(fig)


# Função para criar o gráfico de barra empilhada
def stacked_bar_plot():
    data = {"Categoria": ["A", "B", "C", "D"], "Valor1": [23, 45, 56, 78], "Valor2": [12, 34, 67, 89]}
    df = pd.DataFrame(data)
    fig, ax = plt.subplots()
    df.plot(x="Categoria", kind="bar", stacked=True, ax=ax)
    ax.set_title("Gráfico de Barra Empilhada")
    ax.set_xlabel("Categorias")
    ax.set_ylabel("Valores")
    st.pyplot(fig)


# Título do aplicativo
st.title("Aplicativo de Gráficos")

# Botões para selecionar o tipo de gráfico
chart_type = st.sidebar.selectbox(
    "Selecione o tipo de gráfico:",
    [
        "Gráfico de Barras",
        "Gráfico de Pizza",
        "Gráfico de Dispersão",
        "Gráfico de Correlação",
        "Gráfico de Contagem",
        "Gráfico de Frequência",
        "Gráfico de Rosca",
        "Gráfico de Caixa (Boxplot)",
        "Gráfico de Violino",
        "Gráfico de Barra Empilhada",
    ],
)

# Executando a função correspondente ao botão selecionado
if chart_type == "Gráfico de Barras":
    bar_chart()
elif chart_type == "Gráfico de Pizza":
    pie_chart()
elif chart_type == "Gráfico de Dispersão":
    scatter_plot()
elif chart_type == "Gráfico de Correlação":
    correlation_plot()
elif chart_type == "Gráfico de Contagem":
    count_plot()
elif chart_type == "Gráfico de Frequência":
    freq_plot()
elif chart_type == "Gráfico de Rosca":
    donut_plot()
elif chart_type == "Gráfico de Caixa (Boxplot)":
    box_plot()
elif chart_type == "Gráfico de Violino":
    violin_plot()
elif chart_type == "Gráfico de Barra Empilhada":
    stacked_bar_plot()

