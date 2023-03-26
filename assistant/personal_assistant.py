from langchain.llms import OpenAI
from langchain.vectorstores import Chroma

import logging

from assistant.semantic_search import SemanticSearch


LOGGER = logging.getLogger(__name__)


class PersonalAssistant():
    """Chatbot assistant.
    """
    def __init__(self, **kwargs) -> None:
        pass

    def answer(self, query: str) -> str:
        """Answer the question."""
        semanticsearch = SemanticSearch()
        results = semanticsearch.search(query=query)
        for document, score in results:
            return document.page_content
