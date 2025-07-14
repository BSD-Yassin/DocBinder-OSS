import logging

from rich.logging import RichHandler

from .notions_client import NotionClient
from .notion_service_config import NotionServiceConfig

if not logging.getLogger().handlers:
    FORMAT = "%(message)s"
    logging.basicConfig(level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()])

logging.getLogger("notionapiprovider").setLevel(logging.WARNING)


def register() -> dict:
    """
    Register the Notion service provider.
    """

    # Register the Google Drive client
    return {
        "display_name": "notion",
        "config_class": NotionServiceConfig,
        "client_class": NotionClient,
    }


def get_service_name() -> str:
    """
    Returns the name of the service.
    This is used for logging and identification purposes.
    """
    return "Notion"


def get_service_display_name() -> str:
    """
    Returns the display name of the service.
    This is used for user-friendly identification.
    """
    return "Notion API Service"
