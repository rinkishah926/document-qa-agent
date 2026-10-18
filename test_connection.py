from dotenv import load_dotenv
from openai import OpenAI

# Load the API key from our private settings file.
load_dotenv(".env")

# The client reads OPENAI_API_KEY automatically.
client = OpenAI()

# Send a short request to test the connection.
response = client.responses.create(
    model="gpt-4.1-mini",
    input="Reply with exactly: Connection successful",
    max_output_tokens=30,
)

print(response.output_text)