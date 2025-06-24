# 🚀 ProfileCopilot – LinkedIn AI Career Bot by RohanRVC

## live link-: https://profilecopilot-linkedin-ai-analyzer.onrender.com/

An intelligent AI assistant that analyzes LinkedIn profiles, suggests ideal career roles, matches job titles, rewrites weak sections, recommends learning paths, and continues personalized conversations with memory support. All in one smart Streamlit app.

![image](https://github.com/user-attachments/assets/e3a34bd9-75e0-47d4-b53b-1822d5e063ce)
![image](https://github.com/user-attachments/assets/97bd8d3d-4c50-4960-902f-10db52421d75)
![image](https://github.com/user-attachments/assets/a413389c-02dc-4563-821b-d25e7d6625f6)

---

## 🧠 What It Does

This app turns any LinkedIn profile into a career advantage. It can:

- 🔍 Scrape and analyze your LinkedIn profile
- 🎯 Suggest the most suitable job role if not provided
- 📊 Score your profile match with a job title
- ✍️ Rewrite key sections to improve your personal branding
- 🧭 Recommend relevant learning paths
- 💬 Continue chatting with a memory-aware career bot

---

## 🛠️ Features

| Feature                              | Description |
|--------------------------------------|-------------|
| 🕵️‍♂️ LinkedIn Scraper                 | Uses Apify Actor to scrape full profile |
| 🤖 Multi-Agent LangGraph System       | Each agent handles a different task (analysis, match, rewrite) |
| 🧠 Persistent Memory                  | Stores profile, target job, and chat history per user |
| 💬 AI Chat Assistant                  | Remembers you, your goal, and gives tailored advice |
| 🪄 Auto Role Prediction               | If no job is given, it guesses from profile |
| 🔄 Reset Button                      | Clears memory and starts a fresh session |

---

## 📂 Project Structure

linkedin-ai-bot/
│
├── app.py # Streamlit main app
├── requirements.txt # All dependencies
├── README.md # This file
│
├── utils/
│ ├── apify_scraper.py # LinkedIn scraper via Apify
│ ├── role_predictor.py # Infers role from scraped profile
│ ├── openrouter_chat.py # Sends prompts to OpenRouter LLMs
│ ├── memory_store.py # Save/load persistent memory
│
├── agents/
│ ├── profile_analyzer.py # Agent for profile feedback
│ ├── job_matcher.py # Agent for match scoring
│ ├── content_rewriter.py # Agent to rewrite + suggest skills
│
├── langgraph_flow/
│ └── flow_builder.py # LangGraph nodes and pipeline
│
└── .streamlit/
└── config.toml # UI tweaks (optional)


---

## 📦 Requirements

Create a `requirements.txt` file with:

```txt
streamlit
apify-client
openai
langgraph
tiktoken
Optional:

txt
Copy
Edit
streamlit_chat
python-dotenv
⚙️ Setup Instructions
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/linkedin-ai-bot.git
cd linkedin-ai-bot
2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Add Your API Keys
Edit these files:

In openrouter_chat.py:

python
Copy
Edit
api_key = "your-openrouter-api-key"
In apify_scraper.py:

python
Copy
Edit
client = ApifyClient("your-apify-token")
You can also store them in .env and read with os.getenv().

4. Run the App
bash
Copy
Edit
streamlit run app.py
🧪 How to Test It
Here are ways to test the memory + analysis:

Action	What to Observe
Enter LinkedIn URL only	Bot should guess your best-fit job role
Enter URL + Job	Bot should give feedback + score
Chat: "What’s my goal?"	Bot should remember your job
Chat: "Rewrite my summary again"	Bot recalls and reuses your profile
Click Reset	All memory should clear

📸 Screenshots
Add these if you're pushing to GitHub:

Scraped profile output

Suggested job result

AI match score

Chat memory replies

💡 Built With
Streamlit

LangGraph

OpenRouter (for LLM prompts)

Apify (LinkedIn scraping)

Python 🐍

🔐 License
This project is licensed under the MIT License. You are free to use, modify, and deploy it as your own.

🙌 Credits
👨‍💻 Built by Rohan Vinay Chaudhary

🌐 APIs used: OpenRouter, Apify

💬 LangGraph orchestration for agents


