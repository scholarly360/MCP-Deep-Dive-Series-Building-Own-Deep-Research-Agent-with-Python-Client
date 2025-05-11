# MCP Deep Dive Series : Building Own Deep Research Agent using mcp-use

The Research Agent utilizes a search engine to gather all links related to a specific topic. It saves all links and summarizes content from each link using LLM.

## Set '.venv'

OPENAI_API_KEY=



## Install Libraries

>> python -m venv .venv

>> .venv/Scripts/activate

>> pip install -r req.txt

## url 

>> https://github.com/mcp-use/mcp-use



# OPTIONAL NEXT STEPS (TRY OLLMA MODELS)

## Install ollama

Visit https://ollama.com/ (See instructions specific to OS)

https://github.com/ollama/ollama/blob/main/docs/faq.md

>> ollama run phi4:14b-q4_K_M

## Set ".env"

>> ollama rm phi4:14b-q4_K_M
