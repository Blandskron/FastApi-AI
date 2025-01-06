from transformers import AutoModelForCausalLM, AutoTokenizer
from app.config import settings

# Cargar el tokenizer y el modelo
tokenizer = AutoTokenizer.from_pretrained(settings.LLM_MODEL_PATH)

# Establecer el pad_token a eos_token si no está configurado
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

model = AutoModelForCausalLM.from_pretrained(settings.LLM_MODEL_PATH)

def reformulate_query(question: str) -> str:
    prompt = f"Reformula esta pregunta para Elasticsearch: {question}"
    
    # Tokenizar el prompt y generar la respuesta
    inputs = tokenizer(prompt, return_tensors="pt", padding=True)
    outputs = model.generate(
        **inputs, max_length=200, pad_token_id=tokenizer.eos_token_id
    )
    
    # Decodificar y devolver la respuesta
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
