from dotenv import load_dotenv
from langchain.agents import create_agent

# Load environment variables from the .env file
load_dotenv()


# Define a custom tool that the agent can use
def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's sunny in {city}."


# Define a calculator tool that the agent can use
def calculator(expression: str) -> str:
    """Calculate a mathematical expression."""
    return str(eval(expression))


# Create the AI agent
# The agent uses Gemini as its model and has access to our custom tools
agent = create_agent(
    model="google_genai:gemini-3.7-flash",
    tools=[get_weather, calculator],
    system_prompt="You are a helpful assistant.",
)


# Send a user request to the agent
# The agent decides which tool to use based on the user's request
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


# Display the agent's final response
print(result["messages"][-1].content_blocks)