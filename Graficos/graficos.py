import pandas as pd
import plotly.express as px

colors = ['#43ff00', '#269900', '#ffaa00', '#ff6600', '#cc2900']
colors_heat = ['#b3f0ff', '#ffffb3', '#ff6633', '#e62e00']


def gerar_grafico_idade(df):
    compradores = df[df['Purchased'] == 1]
    contagem_faixa_idade = compradores.groupby('faixa_idade', observed=False).size()

    fig_idade = px.bar(
        contagem_faixa_idade,
        x=contagem_faixa_idade.index,
        y=contagem_faixa_idade.values,
        title="Quantidade de Vendas por Faixa de Idade",
        color=contagem_faixa_idade.values,
        color_continuous_scale=colors[::-1],
        text_auto=True
    )
    
    fig_idade.update_xaxes(title_text='Faixa de Idade')
    fig_idade.update_yaxes(title_text='Quantidade de Vendas', showgrid=True, gridcolor='#E5E5E5', gridwidth=1, griddash='dot')
    fig_idade.update_traces(marker_line_color='#0d0d0d', textposition='outside', textfont_size=12, textangle=0)
    fig_idade.update_layout(plot_bgcolor='#bfbfbf', paper_bgcolor='#000000', font=dict(color='#f2f2f2'), margin=dict(l=10, r=10, t=60, b=10))
    
    return fig_idade

def gerar_grafico_salario(df):
    compradores = df[df['Purchased'] == 1]
    contagem_faixa_salario = compradores.groupby('faixa_salario', observed=False).size()

    fig_salario = px.bar(
        contagem_faixa_salario,
        x=contagem_faixa_salario.index,
        y=contagem_faixa_salario.values,
        title="Quantidade de Vendas por Faixa de Salario Anual",
        color=contagem_faixa_salario.values,
        color_continuous_scale=colors[::-1],
        text_auto=True
    )
    
    fig_salario.update_xaxes(title_text='Faixa de Salario Anual')
    fig_salario.update_yaxes(title_text='Quantidade de Vendas', showgrid=True, gridcolor='#E5E5E5', gridwidth=1, griddash='dot')
    fig_salario.update_traces(marker_line_color='#0d0d0d', textposition='outside', textfont_size=12, textangle=0)
    fig_salario.update_layout(plot_bgcolor='#bfbfbf', paper_bgcolor='#000000', font=dict(color='#f2f2f2'))
    
    return fig_salario

def gerar_grafico_calor(df):
    compradores = df[df['Purchased'] == 1]
    contagem = compradores.groupby(['faixa_idade', 'faixa_salario'], observed=False).size()
    porcentagem = (contagem / contagem.groupby(level='faixa_idade', observed=False).transform('sum')) * 100
    porcentagem_tratada = porcentagem.fillna(0).unstack()

    fig_calor = px.imshow(
        porcentagem_tratada,
        text_auto='.1f',
        color_continuous_scale=colors_heat,
        aspect='auto',
        title="Distribuição do Público-Alvo: Idade vs Salário (%)"
    )
    
    fig_calor.update_xaxes(title_text="Faixa Salarial")
    fig_calor.update_yaxes(title_text="Faixa de Idade")
    fig_calor.update_layout(margin=dict(l=20, r=20, t=50, b=20), paper_bgcolor='#000000', font=dict(color='#f2f2f2'))
    
    return fig_calor