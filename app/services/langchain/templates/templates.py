summary_template ="""
    Based on the provided LinkedIn profile information {linkedin_data} and recent Twitter posts {twitter_data}, please create:
    1. A concise summary of the person's professional background and recent activities, primarily based on LinkedIn data.
    2. Four notable facts about the individual, drawing on insights from both LinkedIn and Twitter data. In one of this facts always mentioning the twitter username (If the Twitter data shows little relevance to the LinkedIn information or is limited, always explicitly mention the Twitter username.)
    Alert: Importantly, always clarify at the end as a alert that the Twitter username might not accurate if you take any information from twitter or its twitter user
    Finnal message: At the end it also leaves a message saying that this info-statement was taken from linkedin and twitter.
    \n{format_instructions}
    """

topics_template = """
    given the information about a person from linkedin {linkedin_data}, and twitter posts {twitter_data} I want you to create:
    3 topics that might interest them but take into account the Linkedin information more than the twitter information as the twitter information may not be as accurate.
    \n{format_instructions}
"""

ice_breakers_template = """
    given the information about a person from linkedin {linkedin_data}, and twitter posts {twitter_data} I want you to create:
    2 creative Ice breakers with them that are derived from their activity on Linkedin and twitter, but take into account the Linkedin information more than the twitter information as the twitter information may not be as accurate.
    \n{format_instructions}
"""