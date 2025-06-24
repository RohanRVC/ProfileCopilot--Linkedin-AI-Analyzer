from utils.openrouter_chat import call_openrouter

def analyze_profile(profile: dict) -> str:
    user_name = profile.get("firstName") or profile.get("fullName") or "there"
    prompt = f"""
    You are a LinkedIn Profile Coach.

    Analyze this LinkedIn profile:
    Hi {user_name}! 👋  
I'm your AI assistant. Here's a deep analysis of your LinkedIn profile:
    Headline: {profile.get('headline')}
    About: {profile.get('about')}
    Skills: {', '.join(
    str(skill) if isinstance(skill, str) else skill.get("name", "")
    for skill in profile.get('skills', [])
)}

    Experience: {profile.get('experiences', [])}

    Give:
    1. Strengths
    2. Weaknesses
    3. Missing info
    4. Suggestions
    """

    return call_openrouter(prompt)
