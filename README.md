# 🚗 Predição de Vendas de Veículos & Dashboard Analítico

## 📌 Sobre o Projeto
Este é um projeto completo de Ciência de Dados. O objetivo foi analisar uma base histórica de clientes de uma concessionária e desenvolver um modelo de Inteligência Artificial capaz de prever a probabilidade de compra de um novo veículo com base no perfil demográfico (Idade, Gênero e Salário Anual).

O projeto culmina em uma **Aplicação Web Interativa (Dashboard)** onde o time de Vendas e Marketing pode simular o perfil de novos visitantes (Lead Scoring).

## 🛠️ Tecnologias Utilizadas
* **Python:** Linguagem principal.
* **Pandas:** Limpeza, manipulação de dados e Feature Engineering.
* **Scikit-Learn:** Treinamento do modelo de Machine Learning (`RandomForestClassifier`).
* **Plotly:** Visualização de dados interativa.
* **Streamlit:** Criação do Dashboard web e deploy.

## 📊 Arquitetura e Funcionalidades
1. **Análise Exploratória e Tratamento:** Separação de idades e salários em faixas (bins) e conversão de variáveis categóricas (Gender) para numéricas.
2. **Machine Learning:** Modelo de classificação binária treinado para identificar padrões de compra.
3. **Simulador de Leads:** Interface na barra lateral onde é possível inserir dados de um novo potencial cliente e receber um "Alerta de Compra" ou "Perfil Frio" em tempo real.
4. **Fábrica de Gráficos:** Código modularizado separando regras de negócio (`graficos.py`) da interface visual (`app.py`).

## 🚀 Como executar o projeto localmente
1. Clone este repositório.
2. Instale as dependências executando: `pip install -r requirements.txt`
3. Navegue até a pasta Dashboard e rode o servidor web: `streamlit run app.py`

## 📊 Streamlit
Acesso ao dashboard: https://predicao-vendas-carros-utjqjhmcqchj4k4dug3mdb.streamlit.app/
