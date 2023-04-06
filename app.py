import logging

import streamlit as st
from memory_profiler import profile

from assistant.personal_assistant import PersonalAssistant


LOGGER = logging.getLogger(__name__)
__version__ = "0.0.1"

@profile
def answer() -> str:
    """Answer the question.

    Returns:
        str: The answer based on the infomation provided.
    """
    if "query" in st.session_state:
        personal_assistant = PersonalAssistant()
        query = st.session_state.query
        answer = personal_assistant.answer(query=query)
        LOGGER.info(f"The question is '{query}' and the answer is '{answer}'")
        st.session_state.answer = answer


if __name__ == "__main__":

    st.text_input(
        "What do you want to know about me?", 
        key="query",
        on_change=answer
    )
    if st.session_state.query:
        st.write(st.session_state.answer)

    
