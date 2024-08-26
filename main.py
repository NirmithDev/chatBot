from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import sys
import time

template = """
Answer the question below.

Here is the conversation history: {context}

Question: {question}
Answer:
"""

model = OllamaLLM(model="phi3")
prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model

def type_out_text(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def handle_conversation():
    context = ""
    print("Welcome to the AI chatbot! Type exit to end conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        result = chain.invoke({"context": context, "question": user_input})
        
        print("Bot: ", end="")
        type_out_text(result)  # Simulate typing out the result
        
        context += f"\nUser: {user_input}\nAI: {result}"

if __name__ == "__main__":
    handle_conversation()
