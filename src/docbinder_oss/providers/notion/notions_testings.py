import requests
import logging
from notion_client import Client
import os

logger = logging.getLogger(__name__)
default_notion_api_url = "https://api.notion.com"

notion = Client(auth=os.environ["NOTION_API_TOKEN"])
def get_notion_api_headers(api_key: str) -> dict:
    """
    Returns the headers required for Notion API requests.
    
    Args:
        api_key (str): The Notion API key.
        
    Returns:
        dict: Headers for the Notion API request.
    """
    return {
        "Authorization": f"Bearer {api_key}",
        "Notion-Version": "2022-06-28"
    }

def get_notion_users(api_key: str, api_url: str = default_notion_api_url) -> dict:
    """
    Retrieves the list of users from the Notion API.
    
    Args:
        api_key (str): The Notion API key.
        api_url (str): The base URL for the Notion API. Defaults to the official Notion API URL.
        
    Returns:
        dict: The response from the Notion API containing user information.
    """
    headers = get_notion_api_headers(api_key)
    url = f"{api_url}/v1/users"
    
    logger.info(f"Fetching users from Notion API at {url}")
    
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        logger.error(f"Failed to fetch users: {response.status_code} - {response.text}")
        response.raise_for_status()
    
    return response.json()

def get_notion_user_me(api_key: str, api_url: str = default_notion_api_url) -> dict:
    """
    Retrieves the information of the authenticated user from the Notion API.
    
    Args:
        api_key (str): The Notion API key.
        api_url (str): The base URL for the Notion API. Defaults to the official Notion API URL.

    Returns:
        dict: The response from the Notion API containing the authenticated user's information.
    """

    headers = get_notion_api_headers(api_key)
    url = f"{api_url}/v1/users/me"
    
    logger.info(f"Fetching authenticated user from Notion API at {url}")
    
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        logger.error(f"Failed to fetch user: {response.status_code} - {response.text}")
        response.raise_for_status()
    
    return response.json()

if __name__ == "__main__":
    api_key = os.getenv("NOTION_API_TOKEN")
    if not api_key:
        raise ValueError("NOTION_API_TOKEN environment variable is not set.")

    try:
        users = get_notion_users(api_key)
        print("Users:", users)
        
        user_me = get_notion_user_me(api_key)
        print("Authenticated User:", user_me)
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        print(f"An error occurred: {e}")

