import asyncio
import json

from fastmcp import Client
from fastmcp.client.transports import StreamableHttpTransport

# Create the transport with your MCP server URL
server_url = "https://mcp.zapier.com/api/mcp/s/OWJmYzkwYTYtMjUwZS00YWRkLThkOTItMmM1ZTVlNTMzMTM5OjMzNjA2MjQxLTZhNTAtNGEyZC1iMjdlLTUyZGY1NTI1MjFiOA==/mcp"
transport = StreamableHttpTransport(server_url)

# Initialize the client with the transport
client = Client(transport=transport)


async def main():
    # Connection is established here
    print("Connecting to MCP server...")
    async with client:
        print(f"Client connected: {client.is_connected()}")

        # Make MCP calls within the context
        print("Fetching available tools...")
        tools = await client.list_tools()

        print(f"Available tools: {json.dumps([t.name for t in tools], indent=2)}")
        # Tools returned would look like:
        # - name: "tavily_search"
        #   description: "Search the web and return answers using Tavily"
        #   params: ["query","topic","include_answer", ...]

        # Example: Call a specific tool with parameters
        print("Calling tavily_search...")
        result = await client.call_tool(
            "tavily_search",
            {
                "instructions": "Execute the Tavily: Search tool with the following parameters",
                "query": "example-string",
            },
        )

        # Parse the JSON string from the TextContent and print it nicely formatted
        json_result = json.loads(result.content[0].text)
        print(
            f"\ntavily_search result:\n{json.dumps(json_result, indent=2)}"
        )

    # Connection is closed automatically when exiting the context manager
    print("Example completed")


if __name__ == "__main__":
    asyncio.run(main())
