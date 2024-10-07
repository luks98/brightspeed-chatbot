from langchain.agents import ConversationalChatAgent,AgentExecutor
from vectordb_tool import get_vectordb_tool
from greet_user_tool import get_greet_user_tool
from general_tool import get_general_tool
from stc.model import model 
from chat_memory import get_memory
from prompts.general_agent_prompt import general_agent_prompt
from langchain_community.agent_toolkits.load_tools import load_tools

def get_tools():
    tools=load_tools([],llm=model)
    tools.append(get_vectordb_tool())
    tools.append(get_greet_user_tool())
    tools.append(get_general_tool())
    return tools

system_message=general_agent_prompt

agent_definition=ConversationalChatAgent.from_llm_and_tools(
    llm=model,
    tools=get_tools(),
    system_message=system_message
)

agent_execution=AgentExecutor.from_agent_and_tools(
    agent=agent_definition,
    llm=model,
    tools=get_tools(),
    handle_parsing_errors=True,
    verbose=True,
    max_iterations=3,
    memory=get_memory(),
    
)
