from flask import Flask, request, render_template, jsonify
from langdetect import detect
from transformers import MBartForConditionalGeneration, MBart50TokenizerFast, MarianMTModel, MarianTokenizer
import re

app = Flask(__name__)

# Summarization model initialization
summarization_model_name = "facebook/mbart-large-50"
summarization_tokenizer = MBart50TokenizerFast.from_pretrained(summarization_model_name)
summarization_model = MBartForConditionalGeneration.from_pretrained(summarization_model_name)

# Translation model cache
translation_models = {}

# Language Detection
def detect_language(text):
    try:
        return detect(text)
    except Exception as e:
        return "unknown"

# Text Cleaning
def clean_text(text):
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    return text.strip()

# Summarization
def summarize_text(text, source_language="en"):
    try:
        summarization_tokenizer.src_lang = source_language
        inputs = summarization_tokenizer(text, return_tensors="pt", max_length=1024, truncation=True)
        summary_ids = summarization_model.generate(inputs["input_ids"], max_length=100, min_length=20, length_penalty=2.0, num_beams=4)
        summary = summarization_tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return summary
    except Exception as e:
        return f"Error in summarization: {str(e)}"

# Translation
def translate_text(text, source_language="en", target_language="hi"):
    try:
        model_name = f"Helsinki-NLP/opus-mt-{source_language}-{target_language}"
        if model_name not in translation_models:
            translation_tokenizer = MarianTokenizer.from_pretrained(model_name)
            translation_model = MarianMTModel.from_pretrained(model_name)
            translation_models[model_name] = (translation_tokenizer, translation_model)
        else:
            translation_tokenizer, translation_model = translation_models[model_name]

        inputs = translation_tokenizer(text, return_tensors="pt", padding=True, truncation=True)
        translated_ids = translation_model.generate(**inputs)
        translation = translation_tokenizer.decode(translated_ids[0], skip_special_tokens=True)
        return translation
    except Exception as e:
        return f"Error in translation: {str(e)}"

# Formatting
def format_output(text):
    return text.strip().capitalize()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_text():
    try:
        text = request.form.get('text')
        target_language = request.form.get('target_language')

        if not text.strip():
            return jsonify({"error": "No text provided"}), 400

        # Step 1: Preprocessing
        detected_language = detect_language(text)
        if detected_language == "unknown":
            return jsonify({"error": "Language detection failed"}), 400
        cleaned_text = clean_text(text)

        # Step 2: Summarization
        summarized_text = summarize_text(cleaned_text, source_language=detected_language)

        # Step 3: Translation
        translated_text = translate_text(summarized_text, source_language=detected_language, target_language=target_language)

        # Step 4: Postprocessing
        final_output = format_output(translated_text)

        return jsonify({
            "original_text": text,
            "detected_language": detected_language,
            "summarized_text": summarized_text,
            "translated_text": final_output
        })
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
