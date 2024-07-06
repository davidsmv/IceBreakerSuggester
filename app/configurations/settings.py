import streamlit as st
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    LINKEDIN_USERNAME: str = st.secrets["LINKEDIN_USERNAME"]
    LINKEDIN_PASSWORD: str = st.secrets["LINKEDIN_PASSWORD"]
    CONSUMER_KEY: str = st.secrets["CONSUMER_KEY"]
    CONSUMER_SECRET: str = st.secrets["CONSUMER_SECRET"]
    ACCESS_TOKEN: str = st.secrets["ACCESS_TOKEN"]
    ACCESS_TOKEN_SECRET: str = st.secrets["ACCESS_TOKEN_SECRET"]


settings = Settings()
