import streamlit as st
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    LINKEDIN_USERNAME: str = st.secrets["LINKEDIN_USERNAME"]
    LINKEDIN_PASSWORD: str = st.secrets["LINKEDIN_PASSWORD"]


settings = Settings()
