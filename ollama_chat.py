import ollama
import json

# Initialize the Ollama client
client = ollama.Client()

# Define the model and the input prompt
model = "llama3.2" 


# Function to send a message to the Ollama Chat API and print the response
def send_message(message):
   # Send the query to the model
    response = client.generate(model=model, prompt=message)

    # Print the response
    print(response.response)
   

# Main loop to interact with the user
while True:
    user_input = input(">>> ")
    if user_input.lower() in ["bye", "exit"]:
        print("Goodbye!")
        break
    send_message(user_input)



