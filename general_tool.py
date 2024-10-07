from langchain.agents import Tool
from langchain.chains import LLMChain
from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage
from stc.model import model


prompt=ChatPromptTemplate.from_messages([SystemMessage(content="use this tool only for questions related to brightspeed.If the question is not related to brightspeed redirect user to brightspeed.")])

chain= prompt|model

def get_general_tool():
    tool=Tool(
        func=chain.stream,
        name='General Tool',
        description="tool to answer questions outside the Brightspeed",
        handle_parsing_errors=True
    )
    return tool