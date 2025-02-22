import PyPDF2
from transformers import pipeline
from tkinter import Tk, filedialog, Text, Button, Label, Scrollbar, Frame
import os
import threading
import asyncio

# Disable Hugging Face symlink warning
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"


# Function to extract text from a PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            extracted_text = page.extract_text()
            if extracted_text:
                text += extracted_text + "\n"
    return text


# Function to split text dynamically
def split_text(text, max_length=800):
    words = text.split()
    return [" ".join(words[i:i + max_length]) for i in range(0, len(words), max_length)]


# Function to summarize text asynchronously
async def summarize_text(text, model_choice="facebook/bart-large-cnn"):
    summarizer = pipeline("summarization", model=model_choice, device=0)
    chunks = split_text(text)
    summaries = []

    async def process_chunk(chunk):
        try:
            summary = summarizer(chunk, max_length=400, min_length=200, do_sample=False)
            if summary:
                summaries.append(summary[0]['summary_text'])
        except Exception as e:
            print(f"Error processing chunk: {e}")

    await asyncio.gather(*(process_chunk(chunk) for chunk in chunks))

    full_summary = "\n".join(summaries) if summaries else "Error: No valid summary generated."
    save_summary_to_file(full_summary)
    return full_summary


# Function to save summary to a file
def save_summary_to_file(summary):
    with open("summary_output.txt", "w", encoding="utf-8") as file:
        file.write(summary)
    print("Summary saved as summary_output.txt")


# Function to select a PDF file
def select_pdf_file():
    file_paths = filedialog.askopenfilenames(title="Select PDF files", filetypes=[["PDF Files", "*.pdf"]])
    return file_paths


# Function to process selected PDFs
def process_pdf():
    pdf_paths = select_pdf_file()
    if not pdf_paths:
        return

    text_area.delete("1.0", "end")
    loading_label.config(text="Summarizing... Please wait...")
    root.update()

    def run_summarization():
        all_text = ""
        for pdf_path in pdf_paths:
            extracted_text = extract_text_from_pdf(pdf_path)
            if not extracted_text.strip():
                text_area.insert("end", f"Error: No text extracted from {pdf_path}\n")
            else:
                all_text += extracted_text + "\n"

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        summary = loop.run_until_complete(summarize_text(all_text))
        text_area.insert("end", summary)
        loading_label.config(text="")

    threading.Thread(target=run_summarization, daemon=True).start()


# GUI Setup
root = Tk()
root.title("Summi Rizer - AI PDF Summarizer")
root.geometry("900x750")
root.configure(bg="#000000")

frame = Frame(root, bg="#000000", bd=5, relief="ridge")
frame.place(relx=0.5, rely=0.6, anchor="center", width=850, height=450)

label = Label(frame, text="Select PDF files to summarize:", font=("Comic Sans MS", 14, "bold"), bg="#000000",
              fg="#ffffff")
label.pack(pady=10)

loading_label = Label(frame, text="", font=("Comic Sans MS", 12, "italic"), fg="#ffcc00", bg="#000000")
loading_label.pack()

button_select = Button(frame, text="Select PDFs & Summarize", command=process_pdf, font=("Comic Sans MS", 12, "bold"),
                       bg="#ff00ff", fg="#ffffff", padx=10, pady=5, relief="raised")
button_select.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

text_area = Text(frame, wrap="word", yscrollcommand=scrollbar.set, height=15, width=90, font=("Comic Sans MS", 12),
                 bg="#000000", fg="#ffffff", padx=10, pady=10, relief="solid")
text_area.pack()

scrollbar.config(command=text_area.yview)

root.mainloop()
