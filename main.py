import asyncio
import json
import os
from fastapi import FastAPI
from fastapi_mcp import FastApiMCP
import redis.asyncio as redis

# Initialize FastAPI app
app = FastAPI()

# Configure Redis for session storage
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

# Initialize FastApiMCP
mcp = FastApiMCP(
    app,
    name="Zapier MCP API",
    description="API for interacting with Zapier MCP tools",
    base_url=os.getenv("BASE_URL", "http://localhost:8000"),
    redis_client=redis_client
)

# Mount the MCP server to the FastAPI app
mcp.mount()

@app.get("/")
async def read_root():
    return {"message": "FastAPI MCP server is running!"}

# You can add more FastAPI endpoints here to expose specific Zapier MCP tools
# For example, an endpoint to trigger a specific Zapier action:
# @app.post("/zapier/action")
# async def trigger_zapier_action(payload: dict):
#     # Logic to interact with Zapier MCP using the mcp client
#     # This would involve using the tools discovered by the MCP client
#     return {"status": "action triggered", "payload": payload}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
