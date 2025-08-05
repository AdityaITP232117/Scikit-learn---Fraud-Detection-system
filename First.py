import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("API key not found. Please set it in .env as GOOGLE_API_KEY")

# Configure Gemini
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-pro")

# Translation Function
def translate(text, language):
    prompt = f"Translate the following English text into {language}:\n\n{text}"
    response = model.generate_content(prompt)
    return response.text

# Main
if __name__ == "__main__":
    eng = input("Enter English text: ")
    lang = input("Translate into (e.g. Hindi, Spanish, Marathi): ")
    result = translate(eng, lang)
    print(f"\nTranslated text in {lang}: {result}")
