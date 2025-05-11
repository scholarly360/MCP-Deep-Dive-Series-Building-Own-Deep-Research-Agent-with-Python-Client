import asyncio
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from mcp_use import MCPAgent, MCPClient


def save_results_to_file(result, filename="output.txt"):
    """ Open a file in write mode and save the result """
    with open(filename, "w",encoding="utf-8") as file:
      file.write(result)
    print("Result saved")

def read_results_from_file(filename="output.txt"):
    """ Open a file in write mode and save the result """
    with open(filename, "r") as file:
      content = file.read()
    return(content)

async def main():
    # Load environment variables
    load_dotenv()

    # Create configuration dictionary
    config = {
      "mcpServers": {
        "playwright": {
          "command": "npx",
          "args": ["@playwright/mcp@latest"],
          "env": {
            "DISPLAY": ":1"
          }
        }
      }
    }

    # Create MCPClient from configuration dictionary
    client = MCPClient.from_dict(config)

    # Create agent with the client
    agent1 = MCPAgent(llm=ChatOpenAI(model="gpt-4o"), client=client, max_steps=15)
    # agent2 = MCPAgent(llm=ChatOllama(model="llama3.2:latest"), client=client, max_steps=15)

    # Optional Run
    if(True):
      result = await agent1.run(
          "Find the news on 'Honda and nissan' using Google Search Use tool 'browser_navigate' and 'url':'https://www.google.com/' " \
          "navigate to bottom of page . NO Screenshots. Give me all 'links' in form of a list segregated with newline SKIP Youtube content and LINKS" \
          "" \
          "",

      )
      save_results_to_file(result,"links.txt")
    
    # Optional Run

    # Read the results from the file
    if(True):
      content = read_results_from_file("links.txt")

      # Run the query
      result = await agent1.run("""
        Read this content {content} and navigate to first "two" links using 'browser_navigate' 
        Read the content of the page and summarize it in 5 bullet points for each link.
      """

      )
      save_results_to_file(result,"output.txt")
    
if __name__ == "__main__":
    asyncio.run(main())