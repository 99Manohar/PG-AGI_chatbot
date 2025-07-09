import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from datetime import datetime
from textblob import TextBlob
from deep_translator import GoogleTranslator


# Load the API key from a text file
with open("google_api_key.txt", "r") as f:
    api_key = f.read().strip()

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash-latest",
    google_api_key=api_key,
    temperature=0.7,
    convert_system_message_to_human=True
)

# --- Streamlit Setup ---
st.set_page_config(page_title="PG-AGI AI", layout="centered")
st.markdown("""
    <style>
    .main {background-color: #f4f6fa; font-family: 'Segoe UI', sans-serif;}
    .stButton>button {border-radius: 8px; background-color: #0e76a8; color: white;}
    </style>
""", unsafe_allow_html=True)

st.title("🤖 PG-AGI - Hiring Assistant")
st.caption("Empowering Recruiters with AI-Powered Conversations 🧠")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        AIMessage(content="Hi! 👋 I'm your PG-AGI Hiring Assistant. I’ll collect your details and ask a few technical questions based on your skills.")
    ]
if "conversation_ended" not in st.session_state:
    st.session_state.conversation_ended = False
if "saved" not in st.session_state:
    st.session_state.saved = False
if "user_profile" not in st.session_state:
    st.session_state.user_profile = {}

system_template = """
You are TalentScout, a professional hiring assistant for a tech recruitment agency.
Your job is to:
1. Collect basic candidate details:
   - Full Name
   - Email Address
   - Phone Number
   - Years of Experience
   - Desired Position(s)
   - Current Location
   - Tech Stack
2. Based on tech stack, ask 3–5 relevant technical questions.
3. Respond clearly and concisely.
4. End if user says "exit".
"""

prompt = ChatPromptTemplate.from_messages([
    ("system", system_template),
    *[(msg.type, msg.content) for msg in st.session_state.chat_history],
    ("human", "{input}")
])

# --- Chat interaction ---
if not st.session_state.conversation_ended:
    user_input = st.chat_input("Your message...")
    if user_input:
        # Sentiment Analysis
        sentiment = TextBlob(user_input).sentiment.polarity
        tone = "🙂 Positive" if sentiment > 0 else ("😐 Neutral" if sentiment == 0 else "🙁 Negative")

        # Optional Translation (to English for backend if needed)
        try:
            detected_lang = GoogleTranslator(source='auto', target='en').detect(user_input)
            if detected_lang != "en":
                user_input = GoogleTranslator(source='auto', target='en').translate(user_input)
                st.info(f"🌐 Translated to English from {detected_lang.upper()}")
        except:
            pass

        st.session_state.chat_history.append(HumanMessage(content=user_input))

        if user_input.strip().lower() in ["exit", "quit", "bye", "goodbye", "see you"]:
            st.session_state.chat_history.append(AIMessage(content="Thanks! We’ll get back to you soon. 👋"))
            st.session_state.conversation_ended = True
        else:
            with st.spinner("Thinking..."):
                full_prompt = prompt.invoke({"input": user_input})
                response = llm.invoke(full_prompt)
                st.session_state.chat_history.append(AIMessage(content=response.content))

        st.toast(f"Sentiment Detected: {tone}", icon="💬")

# --- Display messages ---
for msg in st.session_state.chat_history:
    with st.chat_message("user" if isinstance(msg, HumanMessage) else "assistant"):
        st.markdown(msg.content)

# --- Save chat history to file ---
if st.session_state.conversation_ended and not st.session_state.saved:
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"chat_history_{timestamp}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        for msg in st.session_state.chat_history:
            speaker = "User" if isinstance(msg, HumanMessage) else "Assistant"
            f.write(f"{speaker}: {msg.content}\n")

    st.success(f"✅ Chat history saved as `{filename}`")
    st.session_state.saved = True
