
## Simple Llama2 Chatbot

This is a simple chatbot made with the help of opensource LLM model Llama2 powered by meta.



## Installation
- Download Ollama for your windows/mac whichever is suitable
- Install Ollama
- Open command prompt
- Here I am downloading the Llama2 model to my local system as we are running this model locally

```bash
ollama run llama2
```
After downloading, follow the steps listed below:
- Clone the repository

- Create an .env file inside the repository and make the following changes

```bash
LANGCHAIN_API_KEY="<your_api_key>"
```
```bash
LANGCHAIN_PROJECT="<your_project_name>"
```
    
- Open command prompt and change the location to current working directory

- Install the required libraries

```bash
pip install -r requirements.txt
```
- Start the application by calling the streamlit service

```bash
streamlit run localama.py
```

### Incase of Model change
If you are interested in a different open source LLM model, you can install that particular model by opening the command prompt and by using the command

```bash
ollama run <your_model_name>
```
and change the model name in localama.py file on `26th` line.

```bash
llm = Ollama(model='<your_model_name>')
```

## Screenshots

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

