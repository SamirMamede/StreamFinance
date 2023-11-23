import streamlit as st
import pandas as pd
import pandas_datareader.data as web
import datetime as dt
import yfinance as yf

yf.pdr_override()
st.set_page_config(page_title='PandasFinance 🐼', layout="wide", initial_sidebar_state="auto")


st.title('PandasFinance 🐼')

end_date = dt.datetime.today()
start_date = dt.datetime(end_date.year-1, end_date.month, end_date.day)

dolar = web.get_data_yahoo('USDBRL=X', start=end_date, end=end_date)
euro = web.get_data_yahoo('EURBRL=X', start=end_date, end=end_date)

dolar = dolar.reset_index()
euro = euro.reset_index()

cotacao_dolar = round(dolar['Close'], 2)
cotacao_euro = round(euro['Close'], 2)


with st.container():

    coluna1, coluna2, coluna3 = st.columns(3)

    with coluna1:
        st.metric('Dólar', f'R$ {cotacao_dolar.to_string(index=False)}')
    with coluna2:
        st.metric('Euro', f'R$ {cotacao_euro.to_string(index=False)}')
    with coluna3:
        st.write('Bitcoin em desenvolvimento.')
    


with st.container():

    coluna4, coluna5, coluna6 = st.columns(3)

    with coluna4:
        ativo = st.selectbox('Selecione o ativo:', options=['PETR4.SA', 'GOAU4.SA', 'MGLU3.SA', 'HAPV3.SA', 'RAIZ4.SA', 'VALE3.SA', 'CSNA3.SA', 'BBDC4.SA', 'CIEL3.SA', 'GGBR4.SA'])
    with coluna5:
        data_inicial = st.date_input('Selecione a data inicial:', start_date)
    with coluna6:
        data_final = st.date_input('Selecione a data final:', end_date)


df = web.get_data_yahoo(ativo, start=data_inicial, end=data_final)
df.index = df.index.date

ultima_atualizacao = df.index.max()
primeira_cotacao = round(df.loc[df.index.min(), 'Adj Close'], 2)
ultima_cotacao = round(df.loc[df.index.max(), 'Adj Close'], 2)
menor_cotacao = round(df['Adj Close'].min(), 2)
maior_cotacao = round(df['Adj Close'].max(), 2)
variacao_cotacao = round(((ultima_cotacao - primeira_cotacao) / primeira_cotacao) * 100, 2)

with st.container():

    with coluna4:
        st.metric('Última cotação', f'R${ultima_cotacao:.2f}', f'{variacao_cotacao}%')
    with coluna5:
        st.metric('Menor cotação do período', f'R${menor_cotacao}')
    with coluna6:
        st.metric('Maior cotação do período', f'R${maior_cotacao}')

with st.container():

    coluna7, coluna8 = st.columns(2)

    with coluna7:
        st.dataframe(df, 1000, 330)
    with coluna8:
        st.area_chart(df[['Adj Close']])

with st.container():
    st.subheader(f'Volume de negociações do ativo {ativo}')
    st.line_chart(df[['Volume']])


#with st.container():
#    st.subheader('FIIs')
#    options_fiis = st.multiselect('Escolha os FIIs para comparar', ['VGIA11', 'VINO11', 'GALG11', 'GSFI11', 'VGHF11', 'MXRF11',
#                                                                  'KNCA11', 'BBPO11', 'GGRC11', 'MALL11', 'XPML11', 'BCFF11', 'KNRI11'])
