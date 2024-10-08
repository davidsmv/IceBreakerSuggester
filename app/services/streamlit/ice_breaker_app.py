import streamlit as st
from services.langchain.ice_breaker import IceBreaker


class IceBreakerApp:
    def __init__(self):
        if 'ice_breaker' not in st.session_state:
            st.session_state.ice_breaker = IceBreaker()

    def configure_header(self):
        st.set_page_config(layout='wide')

        st.image("app/services/streamlit/images/header.png",
                 use_column_width=True,
                 caption="Image generated by DALL-E, an AI image generation tool by OpenAI.")

        st.markdown("""
            <style>
            .title {
                text-align: center;
                font-size: 36px;
                font-weight: bold;
                margin-top: 20px;
                margin-bottom: 20px;
            }
            </style>
            <div class="title">IceBreaker Suggester</div>
            """, unsafe_allow_html=True)

        st.markdown("""
            ### About This App

            Welcome to my personal project! I'm [**David Martínez**](https://www.linkedin.com/in/davidsmv/), and this application showcases my skills in **web scraping**, **Streamlit**, and **LangChain** tools.

            #### Project Inspiration
            The concept for this project originated from the Udemy course [_"LangChain - Develop LLM Powered Applications with LangChain"_](https://www.udemy.com/course/langchain/?couponCode=LETSLEARNNOWPP) by Eden Marco. While the foundational idea is derived from this course, I've made several significant modifications to tailor it to my vision.
            Feel free to explore the original project on GitHub for comparison and further understanding: [Original Project by Eden Marco](https://github.com/emarco177/ice_breaker).
            ### Instructions
            The purpose of this project is to provide icebreaker suggestions based on the name and company of the person you specify. Please enter the person's name and company in the appropriate fields to receive the suggestions. **Remember!** If you do not fill in both fields, we will not be able to make suggestions for you.
            """)

    def configure_body(self, summary_and_facts, topics_of_interest, ice_breakers):
        summary_data = summary_and_facts["text"]
        summary = summary_data.summary
        facts = summary_data.facts
        twitter_alert = summary_data.twitter_alert
        final_message = summary_data.final_message

        topics_data = topics_of_interest["text"]
        topics = topics_data.topics_of_interest

        ice_breakers_data = ice_breakers["text"]
        ice_breaker_list = ice_breakers_data.ice_breakers

        st.title("Summary and Highlights")

        st.header("Summary")
        st.markdown(summary)

        st.header("Interesting Facts")
        for fact in facts:
            st.markdown(f"✅ {fact}")

        st.header("Ice Breakers")
        for breaker in ice_breaker_list:
            st.markdown(f"💬 {breaker}")

        st.header("Topics of Interest")
        for topic in topics:
            st.markdown(f"🔍 {topic}")

        st.subheader("Twitter Alert")
        st.markdown(f"🚨 {twitter_alert}")

        st.markdown("**Note:**")
        st.markdown(f"📢 {final_message}")

    def display_input_form(self):
        col1, col2, col3 = st.columns(3)
        with col1:
            name = st.text_input('Enter the person\'s name', placeholder='e.g., Bill Gates')
        with col2:
            company = st.text_input('Enter the company where the person works', placeholder='e.g., Microsoft')
        with col3:
            position = st.text_input('Enter the current position', placeholder='e.g., CEO')
        return name, company, position

    def run(self):
        self.configure_header()
        name, company, position = self.display_input_form()

        st.write("")  # Add some space

        button_clicked = st.button('Search Info')
        if button_clicked:
            if name and company:
                progress_bar = st.progress(0)

                progress_bar.progress(3)
                summary_and_facts, topic_of_interest, ice_breakers = st.session_state.ice_breaker.generate_ice_breakers(name, company, position, progress_bar)

                progress_bar.progress(100)
                self.configure_body(summary_and_facts, topic_of_interest, ice_breakers)
            else:
                st.warning("Please fill in both fields to receive suggestions.")
