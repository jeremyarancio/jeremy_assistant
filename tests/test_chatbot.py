from assistant.personal_assistant import PersonalAssistant

def test_is_openai_ok():
    query = "Are you ok?"
    assistant = PersonalAssistant()
    answer = assistant.answer(query=query)
    assert isinstance(answer, str)


