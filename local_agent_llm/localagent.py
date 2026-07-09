#local agent triggering the qwe3: 8b serving on http://localhost:11434 and a local agentic architecture triggering qwen to produce output
#tokens through a decoder.

import requests

url ="http://localhost:11434/api/generate"


load = {
    "model": "qwen3:8b",
    "prompt": "What is the future of agentic AI and vibe coding",
    "stream": False
}


response = requests.post(url, json=load)

print(response.json()["response"])