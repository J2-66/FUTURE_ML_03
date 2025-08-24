# FUTURE_ML_03
I create a chatbot—a virtual assistant that answers questions, helps customers, and even responds automatically 24/7. This is the kind of tool used on websites like Amazon, Flipkart, and Zomato to support users instantly.

# 🛍️ Foodmart – Customer Support Chatbot

An AI-powered **customer support chatbot** built with **Dialogflow Messenger** and **Streamlit**.  

The chatbot helps customers with **orders, deliveries, refunds, returns, and more** — directly from a web app.
---
# 🚀 Features
- 🤖 **Dialogflow Messenger Integration** – conversational AI powered by Google Dialogflow ES.
  
- 🎨 **Custom Dark Mode UI** with Streamlit styling.
  
- 💬 **Customer Queries** about orders, refunds, returns, and general support. 

- ⚡ Lightweight – no backend required, runs fully in Streamlit.
  
---
# 📂 Project Structure

├── app.py # Main Streamlit app

├── requirements.txt # Project dependencies

├── devcontainer.json # Devcontainer setup for Codespaces/VSCode

└── README.md # Documentation


# 🛠️ Installation & Setup

# 1. Clone Repository

git clone https://github.com/your-username/Foodmart-chatbot.git

cd Foodmart-chatbot

# 2. Create Virtual Environment (Recommended) 
•	python -m venv venv 
•	venv\Scripts\activate # On Windows source 
•	venv/bin/activate # On Mac/Linux

# 3.Install Dependencies

•	pip install -r requirements.txt

3.	Run Streamlit App
•	streamlit run app.py
       or if Streamlit isn’t on PATH:
•	python -m streamlit run app.py

# ⚙️ Configuration 
•	Go to Dialogflow ES Console.

•	Enable Dialogflow Messenger under Integrations.

•	Copy your Agent ID.

•	Replace the agent-id inside app.py with your own:

# 🚀 Deployment
You can deploy the app to:

•	Streamlit Cloud (free & simple)

•	Render, Heroku, or Google Cloud Run
________________________________________
# 📌 Tech Stack
•	Streamlit – Web app framework

•	Dialogflow ES – Conversational AI platform
________________________________________
# 📖 Future Enhancements
•	📊 Logging user queries & responses for analytics.

•	🌍 Multilingual support.

•	🔗 Connect with databases (e.g., MySQL, Firebase) for real-time order tracking.




