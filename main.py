import os
from uagents_core.utils.registration import (
    register_chat_agent,
    RegistrationRequestCredentials,
)

if __name__ == "__main__":
    print("Registering BudgetAssistantAgent with Agentverse...")
    
    register_chat_agent(
        "BudgetAssistantAgent",
        "https://priyanshusingh404.github.io/budget-forecast-agent/",
        active=True,
        credentials=RegistrationRequestCredentials(
            agentverse_api_key=os.environ["AGENTVERSE_KEY"],
            agent_seed_phrase=os.environ["AGENT_SEED_PHRASE"],
        ),
    )
    
    print("Agent successfully registered and connected to Agentverse!")