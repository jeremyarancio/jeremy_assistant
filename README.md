# jeremy_assistant
This AI can ask any questions you would have about me! 👋

The application is deployed with Streamlit: [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://jeremyarancio-jeremy-assistant-app-5k6qkn.streamlit.app/)

## How does it work?
Informations about me are divided into chunks

Each chunk of text is then embedded into a vector representation. 

When you ask a question, this one is embedded in a similar way and the most similar chunk to the question in term of spatial representation is chosen. 

The question with the chunk, we call *context* are then implemented into a GPT-3 model. An answer to your question is provided.

(The explanation is highly simplified. For more information about the algorithm, go check the article below!)

## Article
*Soon*

## Futur work
* Improve the quality of anwers and the interaction with the Chatbot
* Modify the embedding model from OpenAI (*ada-002*) to an open-source one more efficient.
* Update the informations about me
* Modify the LLM from OpenAI (Da-Vinci-002) to an open-source one (like T5)
* Improve the Front-End of the application by transforming it into a real ChatBot

## Aknowledgement 
* Langchain is an amazing open-source project that makes easier the exploitation of Large Language Models, like GPT-3, via Prompt engineering. Go check their [Github](https://github.com/hwchase17/langchain)
