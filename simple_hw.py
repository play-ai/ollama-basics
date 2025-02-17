import requests
import json

# Define the Ollama Chat URL
OLLAMA_API_URL = "http://localhost:11434/api/chat"

# Define the payload for the API request
payload = { 
    "model": "llama3.2",
    "messages": [
        {"role": "user", "content": "Hello, how are you?"}
    ]
}

# Send the request to the Ollama Chat API   
response = requests.post(OLLAMA_API_URL, json=payload, stream=True)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    print("Response from LLM: ")
    for line in response.iter_lines(decode_unicode=True):
        if line:
            try:
                #Parse each line as JSON object
                json_data = json.loads(line)
                if "message" in json_data and "content" in json_data["message"]:
                    print(json_data["message"]["content"], end="", flush=True)
            except json.JSONDecodeError:
                print(f"\nFailed to parse line: {line}")
else:
    print(f"Error: {response.status_code} - {response.text}")   