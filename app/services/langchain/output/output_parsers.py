from typing import List, Dict, Any
from langchain.output_parsers import PydanticOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field

class Summary(BaseModel):
    summary: str = Field(description="Consolidated profile summary from LinkedIn.")
    facts: List[str] = Field(description="List of interesting facts about the individual.")
    twitter_alert: str = Field(description="Warning related to the accuracy of Twitter username.")
    final_message: str = Field(description="Final compiled statement regarding the profile.")

    def to_dict(self) -> Dict[str, Any]:
        return {
            "summary": self.summary,
            "facts": self.facts,
            "twitter_alert": self.twitter_alert,
            "final_message": self.final_message
        }
    

class TopicOfInterest(BaseModel):
    topics_of_interest: List[str] = Field(
        description="topic that might interest the person"
    )

    def to_dict(self) -> Dict[str, Any]:
        return {"topics_of_interest": self.topics_of_interest}
    

class IceBreaker(BaseModel):
    ice_breakers: List[str] = Field(description="ice breaker list")

    def to_dict(self) -> Dict[str, Any]:
        return {"ice_breakers": self.ice_breakers}
    
  
summary_parser = PydanticOutputParser(pydantic_object=Summary)
topic_of_interest_parser = PydanticOutputParser(pydantic_object=TopicOfInterest)
ice_breaker_parser = PydanticOutputParser(pydantic_object=IceBreaker)
