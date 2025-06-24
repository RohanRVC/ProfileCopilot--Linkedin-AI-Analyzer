from utils.openrouter_chat import call_openrouter

def generate_jd_for_role(role: str) -> str:
    
    """
    Generates a job description using LLM for a given role.
    """
    prompt = f"""
You are a job market expert.

Please write a detailed, professional job description for the role of **{role}** at a modern tech company.

Include:
1. Key responsibilities
2. Required skills
3. Tools and technologies commonly used
4. Educational or experience requirements
"""
    return call_openrouter(prompt)

def match_job(profile: dict, target_job: str, job_description: str = None) -> str:
    user_name = profile.get("firstName") or profile.get("fullName") or "there"
    """
    Matches the LinkedIn profile with a job description and provides feedback.

    If no job_description is provided, it generates one using LLM.
    """
    if not job_description:
        job_description = generate_jd_for_role(target_job)

    prompt = f"""
You are a hiring manager.

Compare the following LinkedIn profile to the job title: **{target_job}**
Hi {user_name}, here's how well your LinkedIn profile matches the role of **{target_job}**.

🔹 Profile Details:
- Headline: {profile.get('headline')}
- About: {profile.get('about')}
-  Skills: {', '.join(
    str(skill) if isinstance(skill, str) else skill.get("name", "")
    for skill in profile.get('skills', [])
)}

-  Experience: {', '.join(
    f"{exp.get('title', '')} at {exp.get('companyName', '')}"
    for exp in profile.get("experiences", [])
)}


🔹 Job Description:
{job_description}

✅ Please respond in this format:
1. **Job Match Score** (out of 100)
2. **Key strengths matched**
3. **Missing or weak areas**
4. **Suggestions to improve the profile for this role**
"""
    return call_openrouter(prompt)
