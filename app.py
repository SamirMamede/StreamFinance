import streamlit as st
import pandas as pd
import pandas_datareader.data as web
import datetime as dt
import yfinance as yf

yf.pdr_override()
st.set_page_config(page_title='Stream Finance', layout="wide", initial_sidebar_state="auto")


st.title('Stream Finance')

end_date = dt.datetime.today()
start_date = dt.datetime(end_date.year-1, end_date.month, end_date.day)

with st.container():

    coluna1, coluna2, coluna3 = st.columns(3)

    with coluna1:
        ativo = st.selectbox('Selecione o ativo:', options=['PETR4.SA', 'GOAU4.SA', 'MGLU3.SA', 'HAPV3.SA', 'RAIZ4.SA', 'VALE3.SA', 'CSNA3.SA', 'BBDC4.SA', 'CIEL3.SA', 'GGBR4.SA'])
    with coluna2:
        data_inicial = st.date_input('Selecione a data inicial:', start_date)
    
    with coluna3:
        data_final = st.date_input('Selecione a data final:', end_date)


df = web.get_data_yahoo(ativo, start=data_inicial, end=data_final)
df.index = df.index.date
#dolar = web.get_data_yahoo('USDBRL=X', start=start_date, end=end_date)
#btc = web.get_data_yahoo('BTC-USD', start=start_date, end=end_date)

ultima_atualizacao = df.index.max()
primeira_cotacao = round(df.loc[df.index.min(), 'Adj Close'], 2)
ultima_cotacao = round(df.loc[df.index.max(), 'Adj Close'], 2)
menor_cotacao = round(df['Adj Close'].min(), 2)
maior_cotacao = round(df['Adj Close'].max(), 2)
variacao_cotacao = round(((ultima_cotacao - primeira_cotacao) / primeira_cotacao) * 100, 2)

with st.container():

    with coluna1:
        st.metric('Última cotação', f'R${ultima_cotacao:.2f}', f'{variacao_cotacao}%')
    with coluna2:
        st.metric('Menor cotação do período', f'R${menor_cotacao}')
    with coluna3:
        st.metric('Maior cotação do período', f'R${maior_cotacao}')

with st.container():

    coluna4, coluna5 = st.columns(2)

    with coluna4:
        st.dataframe(df, 1000, 330)
    with coluna5:
        st.area_chart(df[['Adj Close']])

with st.container():
    st.line_chart(df[['High', 'Low']])