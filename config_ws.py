# coding: utf-8
# Filename: config_ws.py
# Path: /config_ws.py

"""
This module loads environment variables from the .env file.

The .env file is not included in the repository for security reasons.
"""
import os
from dotenv import load_dotenv

load_dotenv()

AZURE_SYSTEM_PROMPT = os.getenv("AZURE_SYSTEM_PROMPT")
if AZURE_SYSTEM_PROMPT is None:
    raise ValueError("AZURE_SYSTEM_PROMPT not set")

AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
if AZURE_OPENAI_ENDPOINT is None:
    raise ValueError("AZURE_OPENAI_ENDPOINT not set")

AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")
if AZURE_OPENAI_KEY is None:
    raise ValueError("AZURE_OPENAI_KEY not set")

AZURE_API_VERSION = os.getenv("AZURE_API_VERSION")
if AZURE_API_VERSION is None:
    raise ValueError("AZURE_API_VERSION not set")

AZURE_OPENAI_MODEL = os.getenv("AZURE_OPENAI_MODEL")
if AZURE_OPENAI_MODEL is None:
    raise ValueError("AZURE_OPENAI_MODEL not set")

SPEECH_KEY = os.getenv("SPEECH_KEY")
if SPEECH_KEY is None:
    raise ValueError("SPEECH_KEY not set")

SPEECH_REGION = os.getenv("SPEECH_REGION")
if SPEECH_REGION is None:
    raise ValueError("SPEECH_REGION not set")

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
if ELEVENLABS_API_KEY is None:
    raise ValueError("ELEVENLABS_API_KEY not set")

ELEVENLABS_VOICE_ID = os.getenv("ELEVENLABS_VOICE_ID")
if ELEVENLABS_VOICE_ID is None:
    raise ValueError("ELEVENLABS_VOICE_ID not set")

CONVERSATION_MODE = os.getenv("CONVERSATION_MODE")
if CONVERSATION_MODE is None:
    raise ValueError("CONVERSATION_MODE not set")
