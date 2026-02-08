from dotenv import load_dotenv
from langchain_cerebras import ChatCerebras

load_dotenv()
llm= ChatCerebras(model="gpt-oss-120b")

print("Caramel AI - Chatbot from Sairam")
while(q := input("You: ")) not in ["exit","quit"]:
    print(f"AI: {llm.invoke(q).content}\n")