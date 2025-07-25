from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from config import MODEL_NAME

class Generator:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        self.model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
        self.pipeline = pipeline("text-generation", model=self.model, tokenizer=self.tokenizer)

    def generate(self, context, user_query):
        prompt = f"Based on these job descriptions:\n{context}\nAnswer this: {user_query}"
        output = self.pipeline(prompt, max_length=256, do_sample=True)[0]['generated_text']
        return output