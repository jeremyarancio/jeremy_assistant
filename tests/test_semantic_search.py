import pytest

from assistant.personal_assistant import PersonalAssistant

@pytest.mark.parametrize(
        "test_input, expected",
        [
            (
                "Where did Jérémy do his education?",
                """Concerning my education, I have done all my studies in France. After succeeding preparatory classes for the French "Grandes Ecoles", I got an engineer degree at ENSEM (Ecole Nationale Supérieure d'Electricité et de Mécanique) in 2016. I also got a PhD in physics (heat transfers & fluid mechanics) in 2021, in partnership with EDF, TOTAL and the LTEN in Nantes. """
            ),
        ]
)
def test_find_element(test_input, expected):
    query = test_input
    assistant = PersonalAssistant()
    answer = assistant.answer(query=query)
    assert answer == expected



