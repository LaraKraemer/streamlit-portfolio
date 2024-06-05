"""This module downloads streamlit library"""
import streamlit as st
import pandas
from src.send_email import send_email

df = pandas.read_csv("topics.csv")

st.header("Contact Me")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")
    option = st.selectbox(
        'What topic do you want to discuss?',
        df["topic"])
    raw_message = st.text_area("Your message")
    message = f"""\
Subject: New Email from {user_email}

From: {user_email}
{raw_message}
"""

    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Your email was sent successfully")
