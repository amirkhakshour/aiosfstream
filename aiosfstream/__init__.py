"""Salesforce Streaming API client for asyncio"""
import logging

from ._metadata import VERSION as __version__  # noqa: F401
from .client import Client  # noqa: F401
from .auth import PasswordAuthenticator  # noqa: F401
from .auth import RefreshTokenAuthenticator  # noqa: F401

# Create a default handler to avoid warnings in applications without logging
# configuration
logging.getLogger(__name__).addHandler(logging.NullHandler())
