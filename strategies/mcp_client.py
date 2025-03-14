import asyncio
from typing import Optional
from contextlib import AsyncExitStack
import time

from mcp import ClientSession, StdioServerParameters
from mcp.client.sse import sse_client
import logging


class MCPClient:
    def __init__(self, server_url: str):
        self.session: Optional[ClientSession] = None
        self.exit_stack = AsyncExitStack()
        self.server_url = server_url

    async def _connect_to_server(self):
        """Connect to an MCP server via SSE"""
        sse_transport = await self.exit_stack.enter_async_context(sse_client(self.server_url))
        self.stdio, self.write = sse_transport
        self.session = await self.exit_stack.enter_async_context(ClientSession(self.stdio, self.write))
        await self.session.initialize()

    async def get_tools(self):
        try:
            await self._connect_to_server()
            response = await self.session.list_tools()
            tools = response.tools
            return tools
        finally:
            await self.exit_stack.aclose()

    async def call_tool(self, tool_name: str, tool_args: dict):
        try:
            await self._connect_to_server()
            response = await self.session.call_tool(tool_name, tool_args)
            return response
        finally:
            await self.exit_stack.aclose()


def main():
    """同步入口函数"""
    client = MCPClient("http://localhost:8000/sse")
    tools = asyncio.run(client.get_tools())
    print(tools)
    res = asyncio.run(client.call_tool("get_alerts", {"state": "CA"}))
    print(res)

if __name__ == "__main__":
    main()
