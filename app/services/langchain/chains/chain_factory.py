from langchain_core.runnables import RunnableSequence
from langchain_openai import ChatOpenAI
from langchain.prompts.prompt import PromptTemplate
from langchain.chains import LLMChain


class ChainFactory:
    def __init__(self, llm) -> None:
        self.llm = llm

    def get_prompt_dict(self, template, parser, linkedin_data, twitter_data) -> dict:
        prompt_template = PromptTemplate(
            input_variables=["linkedin_data", "twitter_data"],
            template=template,
            partial_variables={
                "format_instructions": parser.get_format_instructions()
            },
        )

        chain = LLMChain(llm=self.llm, prompt=prompt_template, output_parser=parser)
        res = chain.invoke(input={"linkedin_data": linkedin_data, "twitter_data": twitter_data})

        return res
