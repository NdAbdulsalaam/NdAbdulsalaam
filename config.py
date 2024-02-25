"""This module extracts information from your `.env` file so that
I can use my API keys in other parts of the application.
"""

import os

# pydantic used for data validation: https://pydantic-docs.helpmanual.io/
from pydantic import BaseSettings


def return_full_path(filename: str = ".env") -> str:
    """Uses os to return the correct path of the `.env` file."""
    absolute_path = os.path.abspath(__file__)
    directory_name = os.path.dirname(absolute_path)
    full_path = os.path.join(directory_name, filename)
    return full_path


class Settings(BaseSettings):
    """Uses pydantic to define settings for project."""
    
    twitter_consumer_key: str
    twitter_consumer_secret: str
    twitter_access_token: str
    twitter_access_secret: str
    twitter_bearer_token: str
    twitter_Client_ID: str
    twitter_Client_Screte: str
    github_access_token: str

    class Config:
        env_file = return_full_path(".env")


# Create instance of `Settings` class that will be imported
# in lesson notebooks and the other modules for application.
settings = Settings()