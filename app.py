from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools

import os
from dotenv import load_dotenv
load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

# Web search agent
agent_search = Agent(
    name="web search agent",
    role="search web for information",
    model=Groq(id="llama-3.1-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True
)

# Finance agent
agent_finance = Agent(
    name="finance agent",
    model=Groq(id="llama-3.1-70b-versatile"),
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            stock_fundamentals=True,
            company_news=True
        )
    ],
    instructions=["Use tables to display data."],
    show_tool_calls=True,
    markdown=True,
)

# Multi-agent setup
multi_ai_agent = Agent(
    team=[agent_search, agent_finance],
    model=Groq(id="llama-3.1-70b-versatile"),
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

stock_name = input("Enter the stock name or ticker symbol: ")
response = multi_ai_agent.print_response(
    f"Summarize analyst recommendations and share the latest news for {stock_name}", 
    stream=True
)
