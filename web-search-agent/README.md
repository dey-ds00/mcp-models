🔎 AI Web Search Agent (Firecrawl MCP + Gemini)

This project is an AI-powered web search agent that leverages Firecrawl MCP for searching and retrieving web content, and Google’s Gemini 2.0 Flash API for intelligent summarization.


- Built using:

  - ⚡ LangChain – for orchestration & tool management

  - 🔗 LangGraph – for building flexible agent workflows

  - 🔥 Firecrawl MCP Tools – to fetch and process web content

  - 🤖 Gemini-2.0-Flash – for reasoning, summarizing, and answering queries


- 🚀 Features

  - 🌍 Perform web searches via Firecrawl MCP

  - 📑 Retrieve and summarize webpage content using Gemini-2.0-Flash

  - 🧩 Modular design with LangChain + LangGraph agents

  - ⚡ Lightweight and extensible
 

🔑 API Keys

You need two API keys:Update the .env file:
> GOOGLE_API_KEY=your_google_api_key_here
> FIRECRAWL_API_KEY=your_firecrawl_api_key_here

    

🛠️ Installation

1. Clone the repo
   > git clone https://github.com/your-username/ai-web-search-agent.git
   > cd ai-web-search-agent

2. Setup virtual environment (using uv)
   > uv venv
   > source .venv/bin/activate
   
3. Install Dependencies
   > uv sync


⚙️ On System: Node.js v24.x or higher (required for running Firecrawl MCP via npx)


▶️ Run the agent
      > uv run main.py
***Then, you can start querying:***
**---  "What are the latest headlines on Hindustan Times."**


🧠 How It Works

1. LangGraph builds a ReAct-style agent loop.

2. Firecrawl MCP tools (via npx) handle web search + scraping.

3. Gemini LLM API processes results → provides summaries/answers.

4. Results are returned in a clean, structured format.


