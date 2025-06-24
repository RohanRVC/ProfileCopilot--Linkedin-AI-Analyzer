from utils.openrouter_chat import call_openrouter

def suggest_job_role(profile: dict) -> str:
    prompt = f"""
You are a career recommendation assistant.

Based on the following LinkedIn profile data, suggest the **most suitable job title** this person should apply for:

🔹 Headline: {profile.get('headline')}
🔹 About: {profile.get('about')}
🔹 Skills: {', '.join(str(skill) if isinstance(skill, str) else skill.get("name", "") for skill in profile.get('skills', []))}

🔹 Experience: {profile.get('experiences', [])}

Just return the job title in 5 words or less.
"""
    return call_openrouter(prompt).strip()
