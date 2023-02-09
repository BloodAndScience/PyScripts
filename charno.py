import os 
import openai

openai.api_key = "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"
response = openai.Completion.create(model="text-davinci-003", prompt="Say this is a test", temperature=0, max_tokens=7)
