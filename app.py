import streamlit as st
from langgraph_flow.flow_builder import build_flow
from utils.apify_scraper import scrape_linkedin
from utils.role_predictor import suggest_job_role  
from utils.openrouter_chat import call_openrouter
from utils.memory_store import save_memory, load_memory

st.set_page_config(page_title="ProfileCopilot - LinkedIn AI Bot", layout="centered")
st.title("🚀 LinkedIn Profile Analyzer by RohanRVC")

# Session state
if "analyzed" not in st.session_state:
    st.session_state.analyzed = False
if "user_id" not in st.session_state:
    st.session_state.user_id = None

st.markdown("""
    <style>
    body {
        background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #4CAF50;
        color: white;
        padding: 0.6em 1.2em;
        font-size: 16px;
        border-radius: 8px;
        border: none;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
    html, body, [class*="css"]  {
        font-family: 'Segoe UI', sans-serif;
    }
    </style>
""", unsafe_allow_html=True)


# --- Inputs ---
linkedin_url = st.text_input("🔗 Enter your LinkedIn profile URL:")
target_job = st.text_input("🎯 Enter your Target Job Role (e.g., AI Engineer) (optional):")

# --- Analyze ---
if st.button("✨ Analyze Profile"):
    if not linkedin_url:
        st.warning("Please enter a valid LinkedIn URL.")
    else:
        with st.spinner("🔄 Scraping and analyzing your profile..."):
            scraped_data = scrape_linkedin(linkedin_url)
            cleaned_profile = scraped_data
            user_id = cleaned_profile.get("publicIdentifier") or "default_user"
            st.session_state.user_id = user_id

            memory = load_memory(user_id)
            memory.update({"profile": cleaned_profile, "job": target_job})

            if not target_job:
                target_job = suggest_job_role(cleaned_profile)
                memory["job"] = target_job
                st.info(f"🧭 Suggested Role: **{target_job}**")

            save_memory(user_id, memory)

            state = {"profile": cleaned_profile, "job": target_job, "jd": None}
            graph = build_flow()
            result = graph.invoke(state)

            memory["analysis"] = result.get("analysis", "")
            memory["match"] = result.get("match", "")
            memory["rewrite"] = result.get("rewrite", "")
            save_memory(user_id, memory)
            st.session_state.analyzed = True

# --- Results & Chat ---
if st.session_state.analyzed and st.session_state.user_id:
    user_id = st.session_state.user_id
    memory = load_memory(user_id)

    st.subheader("🧠 Profile Feedback")
    st.markdown(memory.get("analysis", "❌ No analysis returned."))

    st.subheader("📊 Job Match & Suggestions")
    st.markdown(memory.get("match", "❌ No match result returned."))

    st.subheader("✍️ Rewritten Content + Learning Path")
    st.markdown(memory.get("rewrite", "❌ No rewritten content returned."))

    # --- Chatbot ---
    st.subheader("💬 Continue the Conversation")
    chat_box = st.empty()
    chat_history = memory.get("chat_history", [])

    # Show past chat
    with chat_box.container():
        for chat in chat_history:
            st.markdown(f"**You:** {chat['user']}")
            st.markdown(f"**Bot:** {chat['bot']}")

    # Form input
    with st.form("chat_form", clear_on_submit=True):
        user_input = st.text_input("Ask your career assistant anything:", key="chat_input")
        submitted = st.form_submit_button("Send")

    if submitted and user_input.strip():
        with st.spinner("Thinking..."):
            history_str = "\n".join([f"You: {c['user']}\nBot: {c['bot']}" for c in chat_history])
            profile_summary = f"{memory['profile'].get('headline', '')}, {memory['profile'].get('about', '')}"
            user_name = memory['profile'].get('firstName', 'there')

            prompt = f"""
You are a career mentor AI.
User's Name: {user_name}
LinkedIn Summary: {profile_summary}

Conversation so far:
{history_str}

New Message:
{user_input}

Reply as a friendly, helpful mentor.
            """

            bot_reply = call_openrouter(prompt)

            chat_history.append({"user": user_input, "bot": bot_reply})
            memory["chat_history"] = chat_history
            save_memory(user_id, memory)

            # Re-render full chat
            with chat_box.container():
                for chat in chat_history:
                    st.markdown(f"**You:** {chat['user']}")
                    st.markdown(f"**Bot:** {chat['bot']}")

# --- Reset ---
if st.button("🔄 Reset Session"):
    st.session_state.analyzed = False
    st.session_state.user_id = None
