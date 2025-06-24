from utils.openrouter_chat import call_openrouter

def rewrite_content(profile: dict, target_job: str) -> str:
    user_name = profile.get("firstName") or profile.get("fullName") or "there"

    prompt = f"""
    Hi {user_name}, I'm here to help you rewrite your LinkedIn content for the role: **{target_job}**.

You are a LinkedIn content optimization assistant.

The user wants to apply for the role: **{target_job}**.

🔹 Profile About Section:
{profile.get('about')}

🔹 Headline:
{profile.get('headline')}

🔹 Skills:
{', '.join(
    str(skill) if isinstance(skill, str) else skill.get("name", "")
    for skill in profile.get("skills", [])
)}


Your task:
1. Rewrite the **About** section using confident and job-relevant tone (under 150 words)
2. Rewrite a better **LinkedIn Headline** for this role
3. Suggest 3 **missing or important skills**
4. Recommend 2 **free online resources** to learn those skills
    """
    return call_openrouter(prompt)
