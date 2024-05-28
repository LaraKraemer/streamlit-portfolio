import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Ardit Sulce")
    content = """
    Hey there! I am Ardit. 
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me
"""
st.write(content2)

col3, empty_column, col4 = st.columns([1.5, 0.5, 1.5])

content_csv = pandas.read_csv("data.csv", sep=";" )

with col3:
    for index, row in content_csv[:10].iterrows():

        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")


with col4:
    for index, row in content_csv[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
