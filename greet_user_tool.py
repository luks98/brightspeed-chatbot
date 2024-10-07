from langchain.agents import Tool

def greet_user_tool(user_name):
  
    greeting_message=f"send greet message to {user_name}"

    return greeting_message

def get_greet_user_tool():
    tool=Tool(
        func=greet_user_tool,
        name="Greet User",
        description="Tool to greet users whe they interact with the chatbot.",
        input_params=["user_name"],
        output_params=["greeting_message"]
    )

    return tool
