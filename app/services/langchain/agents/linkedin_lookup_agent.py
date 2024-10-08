from langchain import hub
from langchain.agents import (
    create_react_agent,
    AgentExecutor,
)
from langchain_core.tools import Tool
from langchain.prompts.prompt import PromptTemplate
from services.langchain.tools.profile_url_fetcher import ProfileUrlFetcher


class LinkedInLookAgent:

    TEMPLATE = """
        Given the full name {name_of_person} and the company where they work, {company_name},
        and his current position {position}
        please provide the URL to their LinkedIn profile page.
        Your answer should contain only the URL.
    """

    def __init__(self, llm) -> None:
        self.llm = llm
        self.react_prompt = hub.pull("hwchase17/react")
        self.profile_url_fetcher = ProfileUrlFetcher()

    def lookup(self, name: str, company: str, position: str) -> str:
        tools_for_agent = [
            Tool(
                name="Crawl Google 4 linkedin profile page",
                func=self.profile_url_fetcher.get_profile_url,
                description="useful for when you need get the Linkedin Page URL",  # Mandatory
            )
        ]

        agent = create_react_agent(llm=self.llm, tools=tools_for_agent, prompt=self.react_prompt)
        agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)
        prompt_template = PromptTemplate(
            template=self.TEMPLATE, input_variables=["name_of_person", "company_name", "position"]
        )
        result = agent_executor.invoke(
            input={"input": prompt_template.format_prompt(name_of_person=name, company_name=company, position=position)}
        )
        linked_profile_url = result["output"]

        return linked_profile_url
