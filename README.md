## MCP agent Strategy

**Author:** hjlarry  
**Version:** 0.0.1  
**Type:** extension   
**Repo:** [https://github.com/hjlarry/dify-plugin-mcp_agent](https://github.com/hjlarry/dify-plugin-mcp_agent)  
**Feature Request:** [issues](https://github.com/hjlarry/dify-plugin-mcp_agent/issues)


### Description

An agent strategy with MCP tool calls and common function calls.

Same as offical function call agent strategy, but with MCP tool calls.

### Usage

![agent](./_assets/agent.png)

#### Input a mcp server url:
```shell
http://localhost:8000/sse
```

#### Input multi mcp server:
```json
{
  "server_name1": {
    "url": "http://127.0.0.1:8000/sse",
    "headers": {},
    "timeout": 5,
    "sse_read_timeout": 300
  },
  "server_name2": {
    "url": "http://127.0.0.1:8001/sse"
  }
}
```


### How to change MCP server from `stdio` to `sse` ?

#### Method 1: change the source code
```python
if __name__ == "__main__":
    mcp.run(transport='sse')
```

#### Method 2: use the [mcp-proxy](https://github.com/sparfenyuk/mcp-proxy)
```shell
uv tool install mcp-proxy
mcp-proxy --sse-host=0.0.0.0 --sse-port=8080 uvx your-server
```