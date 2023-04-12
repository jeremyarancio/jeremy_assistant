from assistant.personal_assistant import SemanticSearch

def test_search():
    query = "Where did Jeremy study?"
    semantic_search = SemanticSearch()
    results = semantic_search.search(query=query)
    context = results[0].page_content
    assert isinstance(context, str)
    assert "education" in context



