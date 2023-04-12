from pathlib import Path
import os


# [Chunking]
separator = "\n\n\n"
k = 2 # Number of chunks to consider for the answer

# [PATHS]
DATA = Path(os.path.realpath(os.path.dirname(__file__))).parent / "data"
PERSONAL_INFO_PATH = DATA / "me.txt"
DOCSEARCH_PATH = DATA / "docsearch.pkl"
VECTORDB_DIR = DATA / "vectordb"

# [Semantic Search]
sbert_model_name = "sentence-transformers/all-mpnet-base-v2" # https://www.sbert.net/docs/pretrained_models.html

# [OpenAI]
temperature = 0
model_name = "text-davinci-002"
max_tokens = 256
openai_organization = "Personal"