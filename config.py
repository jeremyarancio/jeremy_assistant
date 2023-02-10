from pathlib import Path
import os


# [Chain]
chunk_size = 1000
chunk_overlap = 0
separator = "\n\n\n"
chain_type = "stuff"

# [OpenAI]
embedding_model = "text-embedding-ada-002"
text_model = "text-davinci-002"
temperature = 0.1
max_tokens = 120
top_p = 1
frequency_penalty = 0
presence_penalty = 0
n = 1
stream = False
logprobs = None
verbose = True

# [Sources]
k = 2

# [PATHS]
DATA = Path(os.path.realpath(os.path.dirname(__file__))) / "data"
PERSONAL_INFO_PATH = DATA / "me.txt"
DOCSEARCH_PATH = DATA / "docsearch.pkl"