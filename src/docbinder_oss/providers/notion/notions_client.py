import requests
import logging
from docbinder_oss.providers.base_class import BaseProvider
from notion_client import Client
import os

class NotionClient(BaseProvider):
    def __init__(self, config):
        super().__init__(config)
        self.client = Client(auth=os.environ.get("NOTION_API_TOKEN"))

    def get_users(self):
        """
        Retrieves the list of users from the Notion API.
        
        Returns:
            list: A list of users in Notion.
        """
        try:
            response = self.client.users.list()
            return response.get("results", [])
        except Exception as e:
            logging.error(f"Error fetching users: {e}")
            return []

    def get_user_me(self):
        """
        Retrieves the information of the authenticated user from the Notion API.
        
        Returns:
            dict: Information about the authenticated user.
        """
        try:
            response = self.client.users.me()
            return response
        except Exception as e:
            logging.error(f"Error fetching authenticated user: {e}")
            return {}

    def test_connection(self) -> bool:
        """
        Tests the connection to the Notion API by attempting to fetch the authenticated user.
        
        Returns:
            bool: True if the connection is successful, False otherwise.
        """
        try:
            self.get_user_me()
            return True
        except Exception as e:
            logging.error(f"Test connection failed: {e}")
            return False 


    # The following methods are commented out as they are not implemented, it's just a paste from the gdrive provider : It only services for basis to create provider functions.
    # def list_buckets(self) -> list[Bucket]:
    #     return self.buckets.list_buckets()

    # def list_files_in_folder(self, folder_id: Optional[str] = None) -> List[File]:
    #     return self.files.list_files_in_folder(folder_id)

    # def list_all_files(self) -> List[File]:
    #     return self.files.list_files_in_folder()

    # def get_file_metadata(self, item_id: str) -> File:
    #     return self.files.get_file_metadata(item_id)

    # def get_permissions(self, file_id: str) -> List[Permission]:
    #     return self.permissions.get_permissions(file_id)
