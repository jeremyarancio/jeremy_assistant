from langchain.llms import OpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores.faiss import FAISS
from langchain.vectorstores import VectorStore
from langchain.text_splitter import CharacterTextSplitter
from langchain import OpenAI, VectorDBQA
from langchain.callbacks import get_openai_callback

from typing import Optional, Union, Any, List
from pathlib import Path
import logging
import pickle

import config


LOGGER = logging.getLogger(__name__)


class PersonalAssistant():
    """Personal assistant able to answer any question relative to me.
    """

    open_ai_key: Optional[str]
    llm: OpenAI

    def __init__(
        self,
        open_ai_key: Optional[str] = None,
        docsearch: Optional[VectorStore] = None,
        **kwargs
    ) -> None:

        self.open_ai_key = open_ai_key
        self.llm = OpenAI(
            openai_api_key=open_ai_key,
            model_name=config.text_model,
            temperature=config.temperature,
            max_tokens=config.max_tokens,
            **kwargs
        )
        self.embeddings = OpenAIEmbeddings(
            openai_api_key=open_ai_key,
            query_model_name=config.embedding_model
        )
        self.docsearch: VectorStore = docsearch

    def process_document(self, file: Path) -> None:
        """Process the document to allow the AI to search any particular information in it.
        The docsearch object is then saved.

        Args:
            file (Union[Path, Any]): file to process
        """
        with open(file, "r") as f:
            text = f.read()
        texts = text.split(config.separator)
        LOGGER.info(f'Number of chunks: {len(texts)}')
        with get_openai_callback() as cb:
            embeddings = OpenAIEmbeddings(openai_api_key=self.open_ai_key)
            LOGGER.info(f"Number of tokens used for embeddings: {cb.total_tokens}")
            docsearch = FAISS.from_texts(
                texts=texts, 
                embedding=embeddings
            )
        with open(config.DOCSEARCH_PATH, "wb") as f:
            pickle.dump(docsearch, f)

    def answer(self, question: str) -> str:
        """From a question relative to a document, generate the answer.

        Args:
            question (str): Question asked by the user.

        Returns:
            str: Answer generated with the LLM
        """
        with get_openai_callback() as cb:
            chain = VectorDBQA.from_chain_type(
                llm=self.llm,
                chain_type=config.chain_type, 
                vectorstore=self.docsearch,
                verbose=config.verbose
            )
            self.sources = self.get_sources(query=question) #  TODO: Already considered in VectorDBQAWithSourcesChain but impossible to retrieve
            answer = chain.run(question)
            LOGGER.info(f"Number of tokens used for answering: {cb.total_tokens}")
        return answer
