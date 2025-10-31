import asyncio
import json
import os
from fastapi import FastAPI
from fastapi_mcp import FastApiMCP
import redis.asyncio as redis

# Initialize FastAPI app
app = FastAPI()

# Configure Redis for session storage
REDIS_URL = os.getenv("REDIS_URL")
if REDIS_URL:
    redis_client = redis.from_url(REDIS_URL, decode_responses=True)
else:
    REDIS_HOST = os.getenv("REDISHOST")
    REDIS_PORT = os.getenv("REDISPORT")
    if REDIS_HOST and REDIS_PORT:
        redis_client = redis.Redis(host=REDIS_HOST, port=int(REDIS_PORT), decode_responses=True)
    else:
        redis_client = None

# Initialize FastApiMCP
mcp = FastApiMCP(
    name="MCP-Tavily",
    description="MCP-Tavily: Utilizes the `fastapi_mcp` library to interact with the Zapier MCP server.",
)

# Mount the MCP server to the FastAPI app
mcp.mount()

@app.get("/")
async def read_root():
    return {"message": "FastAPI MCP server is running!"}

@app.get("/health")
async def health_check():
    redis_status = "disconnected"
    try:
        await redis_client.ping()
        redis_status = "connected"
    except Exception:
        pass # We don't want to fail the health check just because Redis isn't ready yet

    return {"status": "ok", "redis": redis_status}

# You can add more FastAPI endpoints here to expose specific Zapier MCP tools
# For example, an endpoint to trigger a specific Zapier action:
# @app.post("/zapier/action")
# async def trigger_zapier_action(payload: dict):
#     # Logic to interact with Zapier MCP using the mcp client
#     # This would involve using the tools discovered by the MCP client
#     return {"status": "action triggered", "payload": payload}

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
