from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="phi")

for i in llm.stream("Explain sun  briefly."):
    print(i)
