import pickle
import logging

import streamlit as st   

from assistant import PersonalAssistant
import config


logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)


def answer() -> str:
    """Answer any question relative to me.

    Returns:
        str: The answer based on the infomation provided about me.
    """
    if "question" in st.session_state:
        with open(config.DOCSEARCH_PATH, 'rb') as f:
            docsearch = pickle.load(f)
        personal_assistant = PersonalAssistant(docsearch=docsearch)
        question = st.session_state.question
        answer = personal_assistant.answer(question=question)
        LOGGER.info(f"The question is '{question}' and the answer is '{answer}'")
        st.session_state.answer = answer


if __name__ == "__main__":

    st.text_input(
        "What do you want to know about me?", 
        key="question",
        on_change=answer
    )

    if st.session_state.question:
        st.write(st.session_state.answer)

    
