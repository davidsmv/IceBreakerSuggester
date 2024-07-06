import os
from dotenv import load_dotenv, find_dotenv

from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

from services.langchain.third_parties.linkedin_scraper import LinkedinScraper
from services.langchain.third_parties.twitter_scrapper import TwitterScraper
from services.langchain.agents.linkedin_lookup_agent import LinkedInLookAgent
from services.langchain.agents.twitter_lookup_agent import TwitterLookAgent
from services.langchain.output.output_parsers import summary_parser, topic_of_interest_parser, ice_breaker_parser
from services.langchain.templates.templates import summary_template, topics_template, ice_breakers_template

from services.langchain.chains.chain_factory import ChainFactory

class IceBreaker:

    def __init__(self) -> None:
        """Class to generate ice breakers using LinkedIn and Twitter data."""
        self.llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
        self.linkedin_scraper = LinkedinScraper()
        self.twitter_scraper = TwitterScraper()
        self.linkedin_agent = LinkedInLookAgent(llm=self.llm)
        self.twitter_agent = TwitterLookAgent(llm=self.llm)
        self.chain_factory = ChainFactory(self.llm)

    def get_social_media_data(self, name: str, company: str):
        """Fetches LinkedIn and Twitter data for a given person."""
        linkedin_profile_url = self.linkedin_agent.lookup(name, company)
        linkedin_data = self.linkedin_scraper.linkedin_profile(linkedin_profile_url)

        twitter_username = self.twitter_agent.lookup(name, company)
        twitter_data = self.twitter_scraper.fetch_tweets(twitter_username)

        return linkedin_data, twitter_data


    def generate_ice_breakers(self, name: str, company: str):
        """Generates ice breakers, topics of interest, and summaries for a given person."""
        linkedin_data, twitter_data = self.get_social_media_data(name, company)


        summary_and_facts = self.chain_factory.get_prompt_dict(summary_template, summary_parser, linkedin_data, twitter_data)
        topic_of_interest = self.chain_factory.get_prompt_dict(topics_template, topic_of_interest_parser, linkedin_data, twitter_data)
        ice_breakers = self.chain_factory.get_prompt_dict(ice_breakers_template, ice_breaker_parser, linkedin_data, twitter_data)

        return summary_and_facts, topic_of_interest, ice_breakers
