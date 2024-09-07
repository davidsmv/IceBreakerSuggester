# IceBreakerSuggester

IceBreaker Suggester is a Streamlit-based application that uses LangChain to generate icebreaker questions. Given a person's name and workplace, the application scrapes relevant information to suggest engaging questions to break the ice. It utilizes the LangChain framework and OpenAI's GPT-3.5-turbo model.


## Features

- **LinkedIn and Twitter Integration:** Fetches data from LinkedIn and Twitter based on the provided details.
- **Ice Breaker Suggestions:** Generates ice breakers, topics of interest, and summaries to help with conversations.
- **Progress Tracking:** Displays a progress bar while fetching and processing data.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/davidsmv/IceBreakerSuggester.git
   cd IceBreakerSuggester
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the necessary API keys for LinkedIn and Twitter by adding them to an `.streamlit/secrets.toml` file:
   ```
   LINKEDIN_USERNAME="your_linkedin_username"
   LINKEDIN_PASSWORD="your_linkedin_password"
   OPENAI_API_KEY="your_openai_api_key"
   ```

## Usage

To start the Streamlit application, run:

```bash
streamlit run app/main.py
```

After running the command, open your browser and navigate to `http://localhost:8501` to use the application.

## How It Works

1. **Input Details:** Enter the person's name, company, and position in the Streamlit interface.
2. **Data Fetching:** The application fetches data from LinkedIn and Twitter.
3. **Ice Breaker Generation:** Using the LangChain framework and GPT-3.5-turbo, it generates ice breakers, topics of interest, and summaries.
4. **Output:** The generated content is displayed on the screen.

## Demo

Check out the video below for a demonstration of how the application works.

[![Watch the demo on YouTube](https://img.youtube.com/vi/dZgkv6ZCZDM/0.jpg)](https://www.youtube.com/watch?v=dZgkv6ZCZDM)

