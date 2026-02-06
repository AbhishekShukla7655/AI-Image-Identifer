from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch

# Global loader to prevent reloading on every request
print("Initializing AI Model (BLIP)...")
try:
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")
    print("AI Model Loaded Successfully.")
except Exception as e:
    print(f"Warning: AI Model could not load. Ensure internet connection. Error: {e}")
    processor = None
    model = None

def generate_caption(image_path):
    if not model or not processor:
        return "Error: AI Model not loaded."
        
    try:
        image = Image.open(image_path).convert('RGB')
        inputs = processor(images=image, return_tensors="pt")
        
        output_ids = model.generate(**inputs, max_length=80, num_beams=5, no_repeat_ngram_size=3)
        caption = processor.decode(output_ids[0], skip_special_tokens=True)
        return caption.capitalize()
    except Exception as e:
        return f"Error processing image: {str(e)}"
