import pickle
import logging

import streamlit as st   

from assistant import PersonalAssistant
import config


logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)


def answer(question: str) -> str:
    """Answer any question relative to me.

    Args:
        question (str): Question asked by the user

    Returns:
        str: The answer based on the infomation provided about me.
    """
    with open(config.DOCSEARCH_PATH, 'rb') as f:
        docsearch = pickle.load(f)
    personal_assistant = PersonalAssistant(docsearch=docsearch)
    answer = personal_assistant.answer(question=question)
    LOGGER.info(f"The question is '{question}' and the answer is '{answer}'")
    st.session_state.answer = answer


if __name__ == "__main__":

    st.text_input(
        "What do you want to know about me?", 
        key="question",
        on_change=answer
    )

    if "answer" in st.session_state:
        st.write(st.session_state.answer)

    
