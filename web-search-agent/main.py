from mcp import ClientSession
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
import asyncio
from mcp.client.stdio import stdio_client
from serverParameter import server_param
from model import model
async def main():
    async with stdio_client(server_param) as (read,write):
        async with ClientSession(read,write) as session:
            await session.initialize()
            tools = await load_mcp_tools(session)
            agent = create_react_agent(model,tools)
            message = [
                {"role" : "system","content" : "You are a helpfull Asistant in finding and delivering Query of a User"}
                ]
            while True:
                user = input("-----\t")
                if user == int(1):
                    break
                message.append(
                    {"role" : "user","content" : user}
                )
                try:
                    agent_resonse = await agent.ainvoke({"messages":message})
                    message_ai = agent_resonse["messages"][-1].content
                    print("Respond: ",message_ai)
                except Exception as e:
                    print("Error is ",e)
if __name__ == "__main__":
    asyncio.run(main())