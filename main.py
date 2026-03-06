import os

from dotenv import load_dotenv


load_dotenv()


from crew import get_research_crew

def run(topic: str):
    result = get_research_crew().kickoff(inputs={"topic": topic})

    print("-"*50)
    print(result)
    print("-" * 50)

if __name__ == "__main__":
    topic = (
        "AI Agents"
    )

    run(topic)