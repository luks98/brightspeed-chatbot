import streamlit as st
import base64
from PIL import Image
from general_agent import agent_execution as general_agent
from sales_agent import agent_execution as sales_agent
from service_agent import agent_execution as service_agent
from classifier import classify_text

# Path to the logo and background image
logo_path = r"C:\Users\DebadattaNayak\Desktop\chatbot\data\Brightspeed_Logo_Full.png"
background_image_path = r"C:\Users\DebadattaNayak\Desktop\chatbot\data\white-blank-background-texture-design-element.jpg"  

# Function to encode the background image in base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Encode the background image
background_image_base64 = get_base64_image(background_image_path)

# Set up the page configuration
st.set_page_config(
    page_title="Brightspeed AI Assistant",
    page_icon="🤖",  # Robot-themed icon
    layout="wide",  # Set layout to wide
    initial_sidebar_state="auto"
)

# Apply custom CSS for improved UI and interactivity with a background image
st.markdown(f"""
    <style>
    /* Set the background image */
    .stApp {{
        background: url("data:image/jpg;base64,{background_image_base64}") no-repeat center center fixed;
        background-size: cover;
    }}

    /* Header styling */
    .stTitle {{
        color: #4B0080;
        font-weight: bold;
        text-align: center;
        font-size: 2.5em;
        padding: 10px 0;
    }}

    /* Chat messages styling */
    .user_message {{
        background-color: #daf1da;
        padding: 10px;
        border-radius: 15px;
        margin: 10px 0;
        font-size: 1.1em;
        max-width: 80%;
    }}

    .ai_message {{
        background-color: #f0f0f5;
        padding: 10px;
        border-radius: 15px;
        margin: 10px 0;
        font-size: 1.1em;
        max-width: 80%;
    }}

    /* Style input box */
    .stTextInput > div {{
        background-color: #fff;
        border: 2px solid #a6a6a6;
        border-radius: 12px;
        padding: 10px;
        font-size: 1.1em;
    }}

    /* Button styling */
    .stButton > button {{
        background-color: #4B0082;
        color: white;
        padding: 10px;
        border-radius: 12px;
        border: none;
        font-size: 1.1em;
    }}

    /* Footer styling */
    footer {{
        font-size: 1em;
        text-align: center;
        padding: 10px;
        background-color: rgba(255, 255, 255, 0.7);
        color: #4B0082;
    }}
    </style>
""", unsafe_allow_html=True)

# Load and display the company logo
logo = Image.open(logo_path)
st.image(logo, width=300)

# Chatbot Title
st.markdown('<div class="stTitle">Brightspeed AI Assistant</div>', unsafe_allow_html=True)
st.sidebar.link_button(label="🏠 Home",url="https://www.brightspeedsavings.com/")
st.sidebar.link_button(label="🛒 Data Plans",url="https://www.brightspeedplans.com/internet")
st.sidebar.link_button(label="☎️ Customer Service",url="https://www.brightspeedplans.com/customer-service")
st.sidebar.link_button(label="📰 Newsroom",url="https://www.brightspeed.com/brightspeed-news/")
st.sidebar.link_button(label="📝 FAQs",url="https://www.brightspeedplans.com/faq")
st.sidebar.image(r"C:\Users\DebadattaNayak\Desktop\chatbot\data\logo.jpg",caption="Let's Connect")

# Initial chat message from Brightspeed's AI Assistant
if 'chat' not in st.session_state:
    st.session_state['chat'] = [
        {
            "content": "Hi, I'm Brightspeed's AI Assistant. How can I help you today?",
            "role": "ai"
        }
    ]

# User input field
user_input = st.chat_input('Ask Brightspeed AI anything...', key="user_input")

# Processing user input
if user_input:
    message = user_input.strip()
    if message:
        st.session_state['chat'].append({
            "content": message,
            "role": "user"
        })

        # Classify the message and invoke the correct agent
        category = classify_text(message)
        agent_response = None
        if category == "sales":
            agent = sales_agent
            agent_response = agent.invoke({'input': message})
            st.session_state['chat'].append({
                "content": agent_response['output'],
                "role": "ai"
            })
        elif category == "service":
            agent = service_agent
            agent_response = agent.invoke({'input': message})
            st.session_state['chat'].append({
                "content": agent_response['output'],
                "role": "ai"
            })
        else:
            agent = general_agent
            agent_response = agent.invoke({'input': message})
            st.session_state['chat'].append({
                "content": agent_response['output'],
                "role": "ai"
            })

# Display chat history with better message presentation
if st.session_state['chat']:
    for i in range(len(st.session_state['chat'])):
        message_data = st.session_state['chat'][i]
        if message_data['role'] == 'user':
            st.markdown(f"<div class='user_message'><strong>You:</strong> {message_data['content']}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='ai_message'><strong>Brightspeed AI Assistant:</strong> {message_data['content']}</div>", unsafe_allow_html=True)

# Add a footer for branding and a friendly touch
st.markdown("""
    <footer>💬 Powered by Brightspeed | Your digital companion</footer>
""", unsafe_allow_html=True)
