import ollama

# Configure your server URL here
SERVER_HOST = 'http://ollama.cs.wallawalla.edu:11434'
client = ollama.Client(host=SERVER_HOST)

def call_ollama(prompt, model="cs450", **options):
    """
    Send a prompt to the Ollama API.
    
    Args:
        prompt (str): The prompt to send
        model (str): Model name to use
        **options: Additional model parameters (temperature, top_k, etc.)
    
    Returns:
        str: The model's response
    """
    try:
        response = client.generate(
            model=model,
            prompt=prompt,
            options=options
        )
        return response['response']
    
    except Exception as e:
        return f"Error: {e}"

def chat_ollama(messages, model="cs450", **options):
    """
    Send a chat conversation to the Ollama API.
    
    Args:
        messages (list): List of message dicts with 'role' and 'content'
        model (str): Model name to use
        **options: Additional model parameters
    
    Returns:
        str: The model's response
    """
    try:
        response = client.chat(
            model=model,
            messages=messages,
            options=options
        )
        return response['message']['content']
    
    except Exception as e:
        return f"Error: {e}"

def stream_ollama(prompt, model="cs450", **options):
    """
    Stream a response from Ollama (for real-time output).
    
    Args:
        prompt (str): The prompt to send
        model (str): Model name to use
        **options: Additional model parameters
    
    Yields:
        str: Chunks of the response as they arrive
    """
    try:
        stream = client.generate(
            model=model,
            prompt=prompt,
            stream=True,
            options=options
        )
        for chunk in stream:
            yield chunk['response']
    
    except Exception as e:
        yield f"Error: {e}"

def analyze_image(image_path, prompt, model="gemma3", temperature=0.3):
    """
    Analyze an image with a text prompt.
    
    Args:
        image_path: Path to image file
        prompt: Question or instruction about the image
        model: Vision model to use
        temperature: Randomness (0.0-1.0)
    """
    response = ollama.chat(
        model=model,
        messages=[{
            'role': 'user',
            'content': prompt,
            'images': [image_path]
        }],
        options={'temperature': temperature}
    )
    return response['message']['content']

# Test the function
if __name__ == "__main__":
    test_prompt = "Say 'Hello, World!' and nothing else."
    print("Testing API call...")
    result = call_ollama(test_prompt, temperature=0.1)
    print(f"Response: {result}")
    
    print("\n" + "="*50)
    print("Testing streaming:")
    for chunk in stream_ollama("Count to 5 slowly.", temperature=0.1):
        print(chunk, end='', flush=True)
    print()