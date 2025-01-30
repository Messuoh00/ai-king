import sys
import ollama

sys.stdout.reconfigure(encoding='utf-8')  # Force UTF-8 encoding

model = "narrator"
prompt = "who am i"

response = ollama.generate(model=model, prompt=prompt)
print(response["response"])
