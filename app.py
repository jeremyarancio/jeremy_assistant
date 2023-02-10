from pathlib import Path
import os
import logging

from assistant import PersonalAssistant
import config


logging.basicConfig(level=logging.INFO)


personal_assistant = PersonalAssistant()
if not personal_assistant.docsearch:
    personal_assistant.process_document(file=config.PERSONAL_INFO_PATH)
