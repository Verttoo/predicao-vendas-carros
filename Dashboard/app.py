from sklearn.ensemble import RandomForestClassifier
import streamlit as st
import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Graficos.graficos import gerar_grafico_idade, gerar_grafico_salario, gerar_grafico_calor

st.set_page_config(page_title="Dashboard Preditivo de Vendas", layout="wide")
st.title("🚗 Simulador de Público-Alvo e Dashboard")

diretorio_atual = os.path.dirname(os.path.abspath(__file__))

caminho_base = os.path.join(diretorio_atual, "..", "Bases", "base_pronta.csv")

@st.cache_resource 
def preparar_modelo_e_dados():
    df = pd.read_csv(caminho_base) 
    
    X = df[['Age', 'AnnualSalary','Gender_Numeric']]
    y = df['Purchased']
    modelo = RandomForestClassifier(random_state=42)
    modelo.fit(X, y)
    
    return df, modelo

df, modelo_producao = preparar_modelo_e_dados()

st.sidebar.header("🎯 Simulador de Novo Cliente")
st.sidebar.write("Insira os dados do visitante para prever a compra:")

input_idade = st.sidebar.number_input("Idade do Cliente:", min_value=18, max_value=100, value=30)
input_salario = st.sidebar.number_input("Salário Anual (R$):", min_value=0, value=50000, step=5000)
input_genero_texto = st.sidebar.selectbox("Gênero do Cliente:", ["Male", "Female"])

if st.sidebar.button("Analisar Cliente"):
    valor_genero = 1 if input_genero_texto == "Male" else 0
    novo_cliente = pd.DataFrame({
            'Age': [input_idade],
            'AnnualSalary': [input_salario],
            'Gender_Numeric': [valor_genero]
        })
    
    novo_cliente = novo_cliente[['Age', 'AnnualSalary', 'Gender_Numeric']]
    previsao = modelo_producao.predict(novo_cliente)[0]
    probabilidade = modelo_producao.predict_proba(novo_cliente)[0][1] * 100
    
    if previsao == 1:
        st.sidebar.success(f"**ALERTA DE COMPRA!** ({probabilidade:.1f}%)")
    else:
        st.sidebar.error(f"**PERFIL FRIO** ({probabilidade:.1f}%)")
st.markdown("### Análise Histórica da Base de Dados")

grafico_1 = gerar_grafico_idade(df)
grafico_2 = gerar_grafico_salario(df)
grafico_3 = gerar_grafico_calor(df)

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(grafico_1, use_container_width=True)

with col2:
    st.plotly_chart(grafico_2, use_container_width=True)

st.markdown("---")
st.plotly_chart(grafico_3, use_container_width=True)