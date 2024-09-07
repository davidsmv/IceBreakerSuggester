from langchain_openai import ChatOpenAI

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

    def get_social_media_data(self, name: str, company: str, position: str, progress_bar):
        """Fetches LinkedIn and Twitter data for a given person."""
        linkedin_profile_url = self.linkedin_agent.lookup(name, company, position)
        progress_bar.progress(5)
        linkedin_data = self.linkedin_scraper.linkedin_profile(linkedin_profile_url)
        progress_bar.progress(10)

        twitter_username = self.twitter_agent.lookup(name, company)
        progress_bar.progress(15)
        twitter_data = self.twitter_scraper.fetch_tweets(twitter_username)
        progress_bar.progress(20)

        return linkedin_data, twitter_data

    def generate_ice_breakers(self, name: str, company: str, position: str, progress_bar):
        linkedin_data, twitter_data = None, None
        max_retries = 2
        for attempt in range(1, max_retries + 1):
            try:
                print(f"Attempt {attempt} to get social media data.")
                linkedin_data, twitter_data = self.get_social_media_data(name, company, position, progress_bar)
                progress_bar.progress(25)

                print(f"Attempt {attempt} to generate summary and facts.")
                summary_and_facts = self.chain_factory.get_prompt_dict(summary_template, summary_parser, linkedin_data, twitter_data)
                progress_bar.progress(50)

                print(f"Attempt {attempt} to generate topics of interest.")
                topic_of_interest = self.chain_factory.get_prompt_dict(topics_template, topic_of_interest_parser, linkedin_data, twitter_data)
                progress_bar.progress(75)

                print(f"Attempt {attempt} to generate ice breakers.")
                ice_breakers = self.chain_factory.get_prompt_dict(ice_breakers_template, ice_breaker_parser, linkedin_data, twitter_data)

                print("Successfully generated all data.")
                return summary_and_facts, topic_of_interest, ice_breakers

            except Exception as e:
                print(f"Error on attempt {attempt}: {e}")
                if attempt < max_retries:
                    print("Retrying...")
                else:
                    print("Max retries reached. Raising exception.")
                    raise e

        return None, None, None
