# AI-Powered PDF Summarizer | Summi Rizer

## Overview
Summi Rizer is an AI-driven PDF summarization tool designed to efficiently extract and condense textual content from PDF documents. Built using **Python, NLP, and a GUI-based interface**, this tool allows users to upload PDFs and receive concise summaries using **state-of-the-art NLP models**.

## Features
- 📄 **Extracts text** from PDFs effortlessly
- 🧠 **AI-based summarization** using `facebook/bart-large-cnn`
- ⏳ **Fast and efficient** with multi-threaded processing
- 🖥️ **User-friendly GUI** built with Tkinter
- 📝 **Saves summaries** as text files for future reference

## Installation
To run Summi Rizer on your system, follow these steps:

### Prerequisites
Make sure you have Python installed. If not, download it from [python.org](https://www.python.org/downloads/).

### Steps to Install
```bash
# Clone the repository
git clone https://github.com/Sdhrt-chauhan/AI-Chapter-summarizer.git

# Navigate to the project directory
cd AI-PDF-Summarizer

# Install required dependencies
pip install -r requirements.txt
```

## Usage
1. Run the application:
   ```bash
   python AI_chapter_summarizer.py
   ```
2. Click the **"Select PDFs & Summarize"** button.
3. Choose one or multiple PDF files.
4. Wait for the AI to process and summarize the content.
5. The summarized text will appear on the screen and be saved in `summary_output.txt`.

## Technologies Used
- **Python** 🐍
- **PyPDF2** (for extracting text from PDFs)
- **Hugging Face Transformers** (for AI summarization)
- **Tkinter** (for GUI)
- **Asyncio & Threading** (for efficient processing)

## Contributing
Want to enhance Summi Rizer? Follow these steps:
1. Fork the repository
2. Create a new branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Open a Pull Request

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author
**Siddharth Chauhan**  
Student at Galgotias University

## Support
For any issues, feel free to raise an [issue](https://github.com/Sdhrt-chauhan/AI-Chapter-summarizer/issues) or contact me.

🚀 **Happy Summarizing!**

