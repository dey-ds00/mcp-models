# mcp-models

This repository contains **MCP-integrated tools and agents**.  
Each folder inside the repo represents an independent agent or tool built using the **Model Context Protocol (MCP)**.

---

## 🔹 What is MCP?

The **Model Context Protocol (MCP)** is an open standard that allows AI models and agents to connect with external tools, APIs, and data sources.  
Think of it as a universal interface for extending model capabilities.



- Each folder = **one MCP-integrated agent/tool**.  
- Every agent/tool comes with its own `README.md` for usage instructions.  

---

## 🚀 Getting Started

1. **Clone the repository**  
   - git clone https://github.com/dey-ds00/mcp-models.git
   > *cd mcp-models*
   
2. **Navigate to an agent/tool folder**
   cd web-searched-agent
   
3. **Activate venv and Install dependencies**
   source .venv/bin/activate
   uv sync
   
5. **Run the agent/tool**
   uv run agent.py


***See each agent’s README for specifics on usage, configuration, inputs, and behavior.***


