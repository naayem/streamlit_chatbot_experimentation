import streamlit as st
import numpy as np
import altair as alt
import pandas as pd

# App title
st.set_page_config(page_title="JAW Llama2 Chatbot 🦙")

with st.sidebar:
    st.title(' JAW Llama2 Chatbot 🦙')
    if 'REPLICATE_API_TOKEN' in st.secrets:
        st.write('Hello World !')
    else:
        st.write("Tu n'as pas de token vilain !")

    st.header('st.button')
    if st.button('say hello'):
        st.write('why hello?')
    else:
        st.write('goodbye')

st.header('st.write')  # Example 1

st.subheader('Hello there :wave:')

st.write('Hello, *World!* :mountain:')

# Example 2

st.write(1234)

# Example 3

df = pd.DataFrame({
     'première colonne': [1, 2, 3, 4],
     'deuxième colonne': [10, 20, 30, 40]
     })
st.write(df)

# Example 4

st.write('Ci-dessous se trouve un DataFrame :', df, 'Ci-dessus se trouve un DataFrame.')

# Example 5

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write("\n voila un graphe de altair", c, "C'est joli")

st.markdown('📖 Learn how to build this app in this [blog]\
(https://towardsdatascience.com/how-to-build-a-llama2-chatbot-with-streamlit-\
and-replicate-ai-2f8a8f2b9d3b) post.')

st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

st.caption('This is a string that explains something above.')
st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')

