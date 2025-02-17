import requests
import json

# Define the Ollama Chat URL
OLLAMA_API_URL = "http://localhost:11434/api/chat"

# Function to send a message to the Ollama Chat API and print the response
def send_message(message):
    payload = { 
        "model": "llama3.2",
        "messages": [
            {"role": "user", "content": message}
        ]
    }
    response = requests.post(OLLAMA_API_URL, json=payload, stream=True)
    if response.status_code == 200:
        print("Response from LLM: ")
        for line in response.iter_lines(decode_unicode=True):
            if line:
                try:
                    json_data = json.loads(line)
                    if "message" in json_data and "content" in json_data["message"]:
                        print(json_data["message"]["content"], end="", flush=True)
                except json.JSONDecodeError:
                    print(f"\nFailed to parse line: {line}")
    else:
        print(f"Error: {response.status_code} - {response.text}")

# Main loop to interact with the user
while True:
    user_input = input("\>>> ")
    if user_input.lower() in ["bye", "exit"]:
        print("Goodbye!")
        break
    send_message(user_input)