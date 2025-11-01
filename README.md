# MCP-Tavily: A FastAPI Application for Zapier MCP

This project provides a simple Python client to connect and interact with the Zapier MCP (Multi-tool Co-pilot) server, specifically demonstrating how to fetch available tools, such as the Tavily search tool. This client is designed to be a straightforward example of integrating with the MCP platform for programmatic access to its functionalities.

## Features

-   **FastAPI Integration**: Leverages the FastAPI framework for building robust and scalable APIs.
-   **MCP-Tavily**: Utilizes the `fastapi_mcp` library to interact with the Zapier MCP server.
-   Connects to a specified Zapier MCP server URL.
-   Fetches and lists all available tools from the MCP server.
-   Provides a foundation for making further MCP calls.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have the following installed:

-   Python 3.8+
-   `fastapi-mcp` library

You can install `fastmcp` using pip:

```bash
pip install fastapi-mcp
```

### Installation

1.  Clone this repository (or create the `main.py` file with the provided content).
2.  Navigate to the project directory:

    ```bash
    cd c:\Users\relay\Downloads\hmm
    ```

### Usage

To run the client and connect to the Zapier MCP server:

```bash
python main.py
```

Upon successful execution, the script will:
1.  Connect to the MCP server.
2.  Print whether the client is connected.
3.  Fetch and display a JSON list of all available tools on the server.
4.  Close the connection.

Example Output:

```
Connecting to MCP server...
Client connected: True
Fetching available tools...
Available tools: [
  "tool_name_1",
  "tool_name_2"
]
Example completed
```

*(Note: The actual tool names will depend on what is configured on your Zapier MCP server.)*

## Open Source

This project is open source and welcomes contributions. Feel free to fork the repository, make improvements, and submit pull requests.

## Author

Digital hustlers

## License

This project is licensed under the MIT License - see the LICENSE.md file for details (if applicable, otherwise consider adding one).