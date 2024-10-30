import dash
import streamlit as st
import seaborn as sns
from sklearn import datasets

#carrega o dataset
df = sns.load_dataset('iris')


#faz o cabeçalho
st.title("Titulo")
st.write(df.head())

#sub cabeçalho
st.subheader(st.write("Estatisticas descritivas"))
st.write(df.describe())

#cos interativos
st.subheader(st.write("nome do sub cabeçalho"))
st.write("escreve mais coisas")
scatter_plot = sns.scatterplot(data=df, x='petal_length', y='petal_width', hue='species') #seaborn

st.pyplot(scatter_plot.figure)

#graficos interativos
st.subheader(st.write("nome do sub cabeçalho"))
st.write("escreve mais coisas")
hist_plot = sns.histplot(data=df, x='sepal_length', hue='species', multiple='stack') #seaborn

st.pyplot(hist_plot.figure)
