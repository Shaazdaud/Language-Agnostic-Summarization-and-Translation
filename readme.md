### **README.md**

```markdown
# Language-Agnostic Summarization and Translation Tool

This project is an open-source NLP application that summarizes text and translates it into a target language, maintaining the original context. It is ideal for multilingual platforms and applications requiring cross-language accessibility.

## Features
- **Automatic Language Detection**: Automatically detects the language of the input text.
- **Summarization**: Generates concise summaries of input text using transformer-based models.
- **Translation**: Translates summarized text into a target language of choice.
- **User-Friendly Web Interface**: Provides a simple and intuitive web interface for text input and result display.

## Tech Stack
- **Python**: Core programming language.
- **Flask**: Web framework for hosting the application.
- **Hugging Face Transformers**: Pretrained summarization and translation models.
- **LangDetect**: For automatic language detection.
- **HTML, CSS, JavaScript**: For building the web interface.

## How It Works
1. The user inputs text and specifies a target language.
2. The system detects the language of the input text.
3. The input text is cleaned and processed.
4. A summary of the input text is generated using a transformer-based summarization model.
5. The summarized text is translated into the target language using a transformer-based translation model.
6. The results (original text, detected language, summary, and translation) are displayed on the web interface.

## Installation

### Prerequisites
- Python 3.8 or later
- pip (Python package manager)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/summarization-translation-tool.git
   cd summarization-translation-tool
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Flask application:
   ```bash
   python app.py
   ```
4. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

## Usage
1. Enter the text you want to summarize in the provided text box.
2. Specify the target language (e.g., `hi` for Hindi, `fr` for French).
3. Submit the form to view:
   - Detected language
   - Generated summary
   - Translated text

## Models Used
- **Summarization**: `facebook/mbart-large-50`
- **Translation**: `Helsinki-NLP/opus-mt-{source_language}-{target_language}`

## Example
### Input
- **Text**: "This is a long text that needs summarization and translation."
- **Target Language**: `hi` (Hindi)

### Output
- **Detected Language**: `en` (English)
- **Summarized Text**: "Summarization and translation are required."
- **Translated Text**: "सारांश और अनुवाद की आवश्यकता है।"

## Project Structure
```
summarization-translation-tool/
│
├── app.py                 # Flask application
├── templates/
│   └── index.html         # Web interface template          
├── README.md              # Project documentation
```

## Limitations
- **Performance**: Dependent on pretrained models; fine-tuning can improve results.
- **Languages**: Translation is limited to supported language pairs by Helsinki-NLP models.
- **Summarization**: May miss critical details if the input is too long.

## Future Improvements
- Add support for additional summarization models.
- Include batch processing for multiple inputs.
- Enhance the web interface for better user experience.

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit your changes and push the branch:
   ```bash
   git push origin feature/your-feature
   ```
4. Open a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For questions or feedback, please reach out to:
- **GitHub**: [Shaazdaud](https://github.com/Shaazdaud)