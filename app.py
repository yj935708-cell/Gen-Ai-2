"""
AI-Based College Enquiry Chatbot
=================================
Uses Groq API (free & fast) with Streamlit GUI.
Model: llama3-8b-8192 via Groq
"""

import streamlit as st
from groq import Groq
from knowledge_base import get_faq_answer, COLLEGE_INFO
from config import GROQ_API_KEY, COLLEGE_NAME

# ──────────────────────────────────────────────
# Page Configuration
# ──────────────────────────────────────────────
st.set_page_config(
    page_title=f"{COLLEGE_NAME} Chatbot",
    page_icon="🎓",
    layout="centered"
)

# ──────────────────────────────────────────────
# Custom CSS
# ──────────────────────────────────────────────
st.markdown("""
<style>
    .college-header {
        background: linear-gradient(135deg, #1a237e, #283593);
        color: white;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 20px;
    }
    .info-badge {
        background: #e8eaf6;
        border-left: 4px solid #3f51b5;
        padding: 10px 14px;
        border-radius: 6px;
        font-size: 13px;
        color: #283593;
        margin-bottom: 16px;
    }
</style>
""", unsafe_allow_html=True)


# ──────────────────────────────────────────────
# System prompt for the LLM
# ──────────────────────────────────────────────
SYSTEM_PROMPT = f"""You are a helpful and friendly college enquiry assistant for {COLLEGE_NAME}.
Your job is to answer student and parent queries about the college.

Here is the college knowledge base:
{COLLEGE_INFO}

Guidelines:
- Be polite, clear, and concise.
- If you don't know something specific, say so honestly and suggest contacting the admissions office.
- Stay on topic (college-related queries only).
- Use bullet points for clarity when listing multiple items.
- Always be encouraging and supportive to students.
"""


# ──────────────────────────────────────────────
# Get AI Response using Groq
# ──────────────────────────────────────────────
def get_groq_response(api_key: str, user_query: str, chat_history: list) -> str:
    """
    Generate response using Groq LLM.
    Includes chat history for context-aware replies.
    """
    try:
        client = Groq(api_key=api_key)

        # Build messages list with history
        messages = [{"role": "system", "content": SYSTEM_PROMPT}]

        # Add last 6 messages for context
        for msg in chat_history[-6:]:
            messages.append({
                "role": msg["role"],
                "content": msg["content"]
            })

        # Add current user query
        messages.append({"role": "user", "content": user_query})

        response = client.chat.completions.create(
            model="llama3-8b-8192",   # Free, fast Llama 3 model
            messages=messages,
            max_tokens=1024,
            temperature=0.7,
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"⚠️ Error: {str(e)}\n\nPlease check your Groq API key in config.py"


# ──────────────────────────────────────────────
# Get Response (FAQ first, then LLM)
# ──────────────────────────────────────────────
def get_response(api_key: str, user_query: str, chat_history: list) -> str:
    """
    1. Check FAQ knowledge base first (instant, no API needed).
    2. Fall back to Groq LLM for detailed/complex queries.
    """
    faq_response = get_faq_answer(user_query)
    if faq_response:
        return f"📋 **From our FAQ:**\n\n{faq_response}"

    return get_groq_response(api_key, user_query, chat_history)


# ──────────────────────────────────────────────
# Session State
# ──────────────────────────────────────────────
def init_session():
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "api_key" not in st.session_state:
        st.session_state.api_key = GROQ_API_KEY
    if "quick_query" not in st.session_state:
        st.session_state.quick_query = None


def clear_chat():
    st.session_state.messages = []


# ──────────────────────────────────────────────
# Sidebar
# ──────────────────────────────────────────────
def render_sidebar():
    with st.sidebar:
        st.markdown("## ⚙️ Settings")

        api_key = st.text_input(
            "Groq API Key",
            value=st.session_state.api_key,
            type="password",
            help="Get free key from https://console.groq.com"
        )
        if api_key:
            st.session_state.api_key = api_key

        if st.button("✅ Save Key", use_container_width=True):
            st.success("API Key saved!")

        st.divider()

        if st.button("🗑️ Clear Chat", use_container_width=True, on_click=clear_chat):
            st.success("Chat cleared!")

        st.divider()

        st.markdown("### 💡 Quick Questions")
        quick_questions = [
            "What courses are available?",
            "What are the fees?",
            "Tell me about hostel",
            "What is the admission process?",
            "What are the placements?",
        ]
        for q in quick_questions:
            if st.button(q, use_container_width=True, key=f"q_{q}"):
                st.session_state.quick_query = q

        st.divider()
        st.markdown("### 📞 Contact")
        st.markdown("📧 admissions@techvision.edu.in")
        st.markdown("📱 +91-98765-43210")

        st.divider()
        st.markdown("**Model:** Llama 3 (via Groq)")
        st.markdown("**Speed:** ⚡ Ultra fast")


# ──────────────────────────────────────────────
# Main App
# ──────────────────────────────────────────────
def main():
    init_session()

    # Header
    st.markdown(f"""
    <div class="college-header">
        <h1>🎓 {COLLEGE_NAME}</h1>
        <p>AI-Powered College Enquiry Assistant</p>
    </div>
    """, unsafe_allow_html=True)

    render_sidebar()

    # Show info if no API key
    if not st.session_state.api_key or st.session_state.api_key == "YOUR_GROQ_API_KEY_HERE":
        st.markdown("""
        <div class="info-badge">
            👈 Enter your <strong>Groq API Key</strong> in the sidebar.
            Get a free key at <a href="https://console.groq.com" target="_blank">console.groq.com</a>
        </div>
        """, unsafe_allow_html=True)

    # Welcome message
    if not st.session_state.messages:
        with st.chat_message("assistant"):
            st.markdown(f"""
👋 Hello! Welcome to **{COLLEGE_NAME}** Enquiry Assistant!

I can help you with:
- 📚 **Courses & Programs**
- 💰 **Fee structure** and scholarships
- 🏠 **Hostel** and campus facilities
- 📝 **Admission process** and eligibility
- 💼 **Placements** and career support

**What would you like to know?**
            """)

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Handle quick question from sidebar
    user_input = None
    if st.session_state.quick_query:
        user_input = st.session_state.quick_query
        st.session_state.quick_query = None

    # Chat input box
    chat_input = st.chat_input("Ask me anything about the college...")
    if chat_input:
        user_input = chat_input

    # Process input
    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = get_response(
                    st.session_state.api_key,
                    user_input,
                    st.session_state.messages[:-1]
                )
            st.markdown(response)

        st.session_state.messages.append({"role": "assistant", "content": response})
        st.rerun()


if __name__ == "__main__":
    main()
