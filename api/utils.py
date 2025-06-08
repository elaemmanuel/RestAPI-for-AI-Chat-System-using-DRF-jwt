from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv() # Load the .env file

def send_code_to_api(user_query):
    """
    Sends a user's query to the Groq API for chatbot interaction.

    Args:
        user_query (str): The user's query.

    Returns:
        str: The chatbot's response, or None if an error occurs.
    """
    try:
        # Initialize the ChatGroq model with specified parameters
        llm = ChatGroq(
            model="llama-3.3-70b-versatile", 
            temperature=0.0, 
            max_retries=2,
        )
        # Define the messages to send to the Groq API, including system and human messages
        messages = [
            ("system", "You are a helpful assistant that can answer users' queries concisely.."), 
            ("human", user_query), 
        ]
        # Invoke the ChatGroq model with the defined messages and get the response
        result = llm.invoke(messages)
        return result.content
    except Exception as e:
        print(f"Error during API call: {e}") 
        return None 
