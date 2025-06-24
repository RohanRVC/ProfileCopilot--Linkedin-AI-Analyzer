from apify_client import ApifyClient
import os
from dotenv import load_dotenv


load_dotenv()


# You can replace this with an environment variable if needed
API_KEY = os.getenv("OPENROUTER_API_KEY")
ACTOR_ID = "2SyF0bVxmgGr8IVCZ"

client = ApifyClient(API_KEY)

def scrape_linkedin(profile_url: str) -> dict:
    """
    Fetches LinkedIn profile data using Apify LinkedIn Scraper actor.
    
    Args:
        profile_url (str): Full URL of the LinkedIn profile
    
    Returns:
        dict: Profile data (scraped) as a dictionary
    """
    try:
        run_input = {"profileUrls": [profile_url]}
        run = client.actor(ACTOR_ID).call(run_input=run_input)

        # Expecting one profile, fetch the first result
        for item in client.dataset(run["defaultDatasetId"]).iterate_items():
            return item
        
        return {"error": "No data found"}

    except Exception as e:
        return {"error": str(e)}

# print(scrape_linkedin('https://www.linkedin.com/in/akash-khamkar?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAACXpsyMBCf-YsbR2qk8un2fwoP014LdQdO8&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_all%3BnhZDd5MuR7WkGNZuW3c%2Beg%3D%3D'))
