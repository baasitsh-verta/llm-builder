# Document Summarization Bot
The quickstart example is a document summarization bot that can take a file, URL or text as input and summarize the content. It uses Open AI APIs. It also includes a LLM builder tool to help youu manage and iterate on prompts and input datasets. A set of sample prompts and datasets are already available and you can bring your own data and refine on prompts.

## Setup steps
* Python 3 in your machine
* Setup and activate python virtual environment
   - brew install pyenv-virtualenv 
   - python3 -m venv yourownenv
   - source yourownenv/bin/activate
* Install streamlit
   - Pip install streamlit
* Download or git-clone the quickstart project
* Go to main folder of the project and run pip install -r requirements.txt
* Go to src folder and run streamlit run LLM_Builder.py
* The  quickstart app will open in localhost

## Setup steps
* Sign-up in Verta and get your DevKey - https://app.verta.ai/sign-up
   - Run export VERTA_EMAIL= your verta email
   - Run export VERTA_DEV_KEY=your verta devkey
* You can either use your own Open AI DevKey or Verta will provide a temporary key
Run export OPENAI_API_KEY=openAI key
