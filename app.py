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

    coluna1, coluna2, coluna3 =st.columns(3)

    with coluna1:
        ativo = st.selectbox('Selecione o ativo:', options=['PETR4.SA', 'GOAU4.SA', 'MGLU3.SA', 'HAPV3.SA', 'RAIZ4.SA', 'VALE3.SA', 'CSNA3.SA', 'BBDC4.SA', 'CIEL3.SA', 'GGBR4.SA'])
    with coluna2:
        data_inicial = st.date_input('Selecione a data inicial:', start_date)
    
    with coluna3:
        data_final = st.date_input('Selecione a data final:', end_date)


df = web.get_data_yahoo(ativo, start=data_inicial, end=data_final)
#dolar = web.get_data_yahoo('USDBRL=X', start=start_date, end=end_date)
#btc = web.get_data_yahoo('BTC-USD', start=start_date, end=end_date)

with st.container():
    st.dataframe(df.head(14), 1000, 500)