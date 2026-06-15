from fastapi import FastAPI
from server import mcp

# Create MCP HTTP application
mcp_app = mcp.http_app(path="/")

# Create FastAPI app
app = FastAPI(
    title="My First MCP + FastAPI",
    lifespan=mcp_app.lifespan
)

# Mount the MCP server
app.mount("/mcp", mcp_app)


@app.get("/")
def home():
    return {
        "message": "FastAPI is running successfully!"
    }