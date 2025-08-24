from mcp import StdioServerParameters
from dotenv import load_dotenv
import os

load_dotenv()

#Firecrawl api setup
FIRECRAWL_API_KEY = os.getenv("FIRECRAWL_API_KEY")

#Setting server parameters for firecrawl mcp server
server_param = StdioServerParameters(
    command = "npx",
    firecrawl_api = FIRECRAWL_API_KEY,
    args = ["firecrawl-mcp"]
)
