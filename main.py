from dotenv import load_dotenv
from langchain.agents import create_agent

load_dotenv()


def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's sunny in {city}."


def calculator(expression: str) -> str:
    """Calculate a mathematical expression."""
    return str(eval(expression))


agent = create_agent(
    model="google_genai:gemini-3.7-flash",
    tools=[get_weather, calculator],
    system_prompt="You are a helpful assistant.",
)


result = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "What is 25 * 8?"
            }
        ]
    }
)

print(result["messages"][-1].content_blocks)