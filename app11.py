import streamlit as st
import streamlit.components.v1 as components

# Streamlit Page Config
st.set_page_config(page_title="🛒 ShopSmart – Chatbot", layout="wide")

# Dark Mode CSS
st.markdown("""
    <style>
        body {
            background-color: #121212;
            color: white;
        }
        .stApp {
            background-color: #121212;
        }
        h1, h2, h3, h4 {
            color: #ffffff;
        }
        .block-container {
            padding: 2rem 2rem 2rem 2rem;
        }
    </style>
""", unsafe_allow_html=True)

# Two-column layout
left_col, right_col = st.columns([1, 2])

with left_col:
    st.markdown("### 🛍️ **Welcome to Foodmart**")
    st.markdown("#### Your AI-powered Food booking assistant 🤖")
    st.markdown("Ask anything about your orders, deliveries, refunds, returns, and more! 💬")

with right_col:
    components.html("""
        <style>
            df-messenger {
              --df-messenger-bot-message: #2e2e2e;
              --df-messenger-button-titlebar-color: #1f1f1f;
              --df-messenger-chat-background-color: #2b2b2b;
              --df-messenger-font-color: white;
              --df-messenger-send-icon: #ffffff;
              --df-messenger-user-message: #4a4a4a;
            }
        </style>

        <!-- Load Dialogflow Messenger -->
        <script src="https://www.gstatic.com/dialogflow-console/fast/messenger/bootstrap.js?v=1"></script>

        <!-- Messenger widget -->
        <df-messenger
          intent="WELCOME"
          chat-title="ShopSmart Assistant"
          agent-id="7ee53394-5547-40cb-8c12-66514f5f455d"
          language-code="en">
        </df-messenger>
    """, height=600)
